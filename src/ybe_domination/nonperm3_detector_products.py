from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Any, Iterable

from .finite_braided_set import FiniteBraidedSet, rack_solution
from .finite_rack_sat import is_rack_table
from .small_search import all_bijection_solutions, is_permutation_solution_form

FlatYbeTable = tuple[int, ...]
RackTable = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class DetectorSchemaRecord:
    """One schema-like detector record extracted from a certificate JSON."""

    ybe_table: FlatYbeTable
    rack_table: RackTable


def flat_table_from_solution(solution: FiniteBraidedSet) -> FlatYbeTable:
    """Return the flat ``3*x+y`` table convention used by the certificates."""

    size = len(solution.elements)
    return tuple(
        size * solution.R[(x, y)][0] + solution.R[(x, y)][1]
        for x in solution.elements
        for y in solution.elements
    )


def solution_from_flat_table(table: Iterable[int]) -> FiniteBraidedSet:
    """Build a zero-based finite braided set from a flat pair table."""

    flat = tuple(int(entry) for entry in table)
    size_squared = len(flat)
    size = int(size_squared**0.5)
    if size * size != size_squared:
        raise ValueError("flat YBE table length must be a square")
    elements = tuple(range(size))
    pairs = tuple(product(elements, repeat=2))
    values = tuple(divmod(value, size) for value in flat)
    return FiniteBraidedSet(elements, dict(zip(pairs, values)))


def nonpermutation_size3_flat_tables() -> tuple[FlatYbeTable, ...]:
    """Return all non-permutation-form size-three bijective YBE tables."""

    return tuple(
        flat_table_from_solution(solution)
        for solution in all_bijection_solutions(3)
        if not is_permutation_solution_form(solution)
    )


def rack_from_table(table: RackTable) -> FiniteBraidedSet:
    """Build a rack solution from a normalized rack table."""

    if not is_rack_table(table):
        raise ValueError(f"invalid rack table: {table!r}")
    return rack_solution(
        tuple(range(len(table))),
        lambda left, right: table[left][right],
    )


def _parse_int_row(value: Any) -> tuple[int, ...]:
    if isinstance(value, str):
        text = value.replace(",", " ").strip()
        if not text:
            return tuple()
        return tuple(int(part) for part in text.split())
    if isinstance(value, (list, tuple)):
        return tuple(int(entry) for entry in value)
    raise TypeError(f"cannot parse integer row from {value!r}")


def normalize_flat_ybe_table(value: Any) -> FlatYbeTable:
    return _parse_int_row(value)


def normalize_rack_table(value: Any) -> RackTable:
    """Normalize rack table rows from compact JSON-friendly forms."""

    if isinstance(value, dict):
        if "table" not in value:
            raise ValueError("rack table dictionary must contain a table field")
        value = value["table"]
    if not isinstance(value, (list, tuple)):
        raise TypeError(f"cannot parse rack table from {value!r}")
    if value and all(isinstance(entry, int) for entry in value):
        size_squared = len(value)
        size = int(size_squared**0.5)
        if size * size != size_squared:
            raise ValueError("flat rack table length must be a square")
        rows = tuple(
            tuple(int(value[row * size + col]) for col in range(size))
            for row in range(size)
        )
    else:
        rows = tuple(_parse_int_row(row) for row in value)
    size = len(rows)
    if size == 0 or any(len(row) != size for row in rows):
        raise ValueError(f"rack table must be nonempty and square: {rows!r}")
    return rows


def _rack_table_from_detector_record(record: dict[str, Any]) -> RackTable | None:
    if "rack" in record:
        rack = record["rack"]
        if isinstance(rack, dict) and "table" in rack:
            return normalize_rack_table(rack["table"])
        if isinstance(rack, (list, tuple)):
            return normalize_rack_table(rack)
    if "rack_table" in record:
        return normalize_rack_table(record["rack_table"])
    return None


def extract_detector_schema_records(payload: Any) -> tuple[DetectorSchemaRecord, ...]:
    """Extract schema-like records containing both a YBE table and rack table.

    The q=5 certificate is not yet present in the workspace, so this parser is
    intentionally shape-tolerant.  It walks nested JSON and accepts records
    with a ``ybe_table`` plus either ``rack.table``, ``rack`` as a table, or
    ``rack_table``.  It extracts only the target rack tables needed for the
    componentwise detector-product audit.
    """

    records: list[DetectorSchemaRecord] = []

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            if "ybe_table" in value:
                rack_table = _rack_table_from_detector_record(value)
                if rack_table is not None:
                    records.append(
                        DetectorSchemaRecord(
                            ybe_table=normalize_flat_ybe_table(value["ybe_table"]),
                            rack_table=rack_table,
                        )
                    )
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(payload)
    return tuple(records)


def detector_components_by_ybe_table(
    payloads: Iterable[Any],
) -> dict[FlatYbeTable, tuple[RackTable, ...]]:
    """Return distinct target rack components grouped by YBE table."""

    grouped: dict[FlatYbeTable, list[RackTable]] = {}
    seen: dict[FlatYbeTable, set[RackTable]] = {}
    for payload in payloads:
        for record in extract_detector_schema_records(payload):
            table_seen = seen.setdefault(record.ybe_table, set())
            if record.rack_table in table_seen:
                continue
            table_seen.add(record.rack_table)
            grouped.setdefault(record.ybe_table, []).append(record.rack_table)
    return {table: tuple(racks) for table, racks in grouped.items()}
