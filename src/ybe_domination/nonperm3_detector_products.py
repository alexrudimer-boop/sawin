from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Any, Iterable

from .finite_braided_set import FiniteBraidedSet, rack_solution
from .finite_rack_sat import is_rack_table
from .small_search import all_bijection_solutions, is_permutation_solution_form

FlatYbeTable = tuple[int, ...]
RackTable = tuple[tuple[int, ...], ...]
WIDTH3_AUDIT_KIND = "nonperm3_width3_componentwise_cross_effect_audit_v1"
WIDTH3_AUDIT_BRANCH = "nonpermutation_size3"
WIDTH3_AUDIT_ROW_FIELDS = (
    "ybe_table",
    "detector_component_count",
    "detector_component_sizes",
    "bound",
    "arity",
    "joint_image_size",
    "kernel_image_size",
    "parabolic_image_size",
    "quotient_size",
    "quotient_nontrivial",
    "seed_count",
    "first_witness_word",
    "first_moved_tuple",
    "first_moved_tuple_image",
    "truncated",
)


@dataclass(frozen=True)
class DetectorSchemaRecord:
    """One schema-like detector record extracted from a certificate JSON."""

    ybe_table: FlatYbeTable
    rack_table: RackTable
    source_schema_ids: tuple[str, ...] = tuple()


@dataclass(frozen=True)
class DetectorComponentRecord:
    """One distinct detector rack component for a fixed YBE table."""

    rack_table: RackTable
    source_schema_ids: tuple[str, ...]


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


def _schema_ids_from_detector_record(record: dict[str, Any]) -> tuple[str, ...]:
    ids = []
    for key in ("source_schema_ids", "schema_ids"):
        value = record.get(key)
        if isinstance(value, (list, tuple)):
            ids.extend(str(entry) for entry in value)
        elif value is not None:
            ids.append(str(value))
    for key in ("id", "schema_id", "detector_id", "name"):
        if key in record:
            ids.append(str(record[key]))
    deduped = []
    seen = set()
    for schema_id in ids:
        if schema_id in seen:
            continue
        seen.add(schema_id)
        deduped.append(schema_id)
    return tuple(deduped)


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
                            source_schema_ids=_schema_ids_from_detector_record(value),
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

    return {
        table: tuple(component.rack_table for component in components)
        for table, components in detector_index_by_ybe_table(payloads).items()
    }


def detector_index_by_ybe_table(
    payloads: Iterable[Any],
) -> dict[FlatYbeTable, tuple[DetectorComponentRecord, ...]]:
    """Return distinct detector rack components plus source schema IDs."""

    grouped: dict[FlatYbeTable, dict[RackTable, list[str]]] = {}
    for payload in payloads:
        for record in extract_detector_schema_records(payload):
            table_group = grouped.setdefault(record.ybe_table, {})
            source_ids = table_group.setdefault(record.rack_table, [])
            for schema_id in record.source_schema_ids:
                if schema_id not in source_ids:
                    source_ids.append(schema_id)
    return {
        table: tuple(
            DetectorComponentRecord(
                rack_table=rack_table,
                source_schema_ids=tuple(source_ids),
            )
            for rack_table, source_ids in components.items()
        )
        for table, components in grouped.items()
    }


def _require(condition: bool, failures: list[str], message: str) -> None:
    if not condition:
        failures.append(message)


def _payload_int(payload: dict[str, Any], key: str, failures: list[str]) -> int | None:
    value = payload.get(key)
    if isinstance(value, bool) or not isinstance(value, int):
        failures.append(f"{key} must be an integer")
        return None
    return value


def _normalize_ybe_table_for_audit(
    value: Any,
    failures: list[str],
    context: str,
    *,
    require_nonpermutation: bool = True,
) -> FlatYbeTable | None:
    try:
        table = normalize_flat_ybe_table(value)
    except (TypeError, ValueError) as exc:
        failures.append(f"{context}: invalid ybe_table: {exc}")
        return None
    if len(table) != 9:
        failures.append(f"{context}: expected a size-three flat table with 9 entries")
        return None
    solution = solution_from_flat_table(table)
    if not solution.is_ybe():
        failures.append(f"{context}: ybe_table is not a YBE solution")
    if require_nonpermutation and is_permutation_solution_form(solution):
        failures.append(f"{context}: ybe_table is permutation-form, not non-permutation")
    return table


def verify_width3_audit_payload(payload: dict[str, Any]) -> tuple[str, ...]:
    """Return structural verification failures for a width-3 audit payload.

    This verifier checks the certificate shape and finite consistency of the
    detector index and rows.  It deliberately does not rerun the expensive
    componentwise closure computation; the audit rows remain the source of the
    reported finite cross-effect data.
    """

    failures: list[str] = []
    if not isinstance(payload, dict):
        return ("payload must be a JSON object",)
    _require(
        payload.get("kind") == WIDTH3_AUDIT_KIND,
        failures,
        f"kind must be {WIDTH3_AUDIT_KIND!r}",
    )
    _require(
        payload.get("branch") == WIDTH3_AUDIT_BRANCH,
        failures,
        f"branch must be {WIDTH3_AUDIT_BRANCH!r}",
    )
    bound = _payload_int(payload, "bound", failures)
    arity = _payload_int(payload, "arity", failures)
    if bound is not None:
        _require(bound >= 1, failures, "bound must be positive")
    if arity is not None:
        _require(arity >= 1, failures, "arity must be positive")

    expected_tables = set(nonpermutation_size3_flat_tables())
    nonperm_count = payload.get("nonpermutation_ybe_tables")
    if nonperm_count is not None:
        _require(nonperm_count == 55, failures, "nonpermutation_ybe_tables must be 55")

    detector_index = payload.get("detector_index")
    if not isinstance(detector_index, list):
        failures.append("detector_index must be a list")
        detector_index = []
    index_tables: dict[FlatYbeTable, list[dict[str, Any]]] = {}
    for index, entry in enumerate(detector_index):
        context = f"detector_index[{index}]"
        if not isinstance(entry, dict):
            failures.append(f"{context}: entry must be an object")
            continue
        table = _normalize_ybe_table_for_audit(entry.get("ybe_table"), failures, context)
        detectors = entry.get("detectors")
        if not isinstance(detectors, list) or not detectors:
            failures.append(f"{context}: detectors must be a nonempty list")
            detectors = []
        if table is not None:
            if table in index_tables:
                failures.append(f"{context}: duplicate detector_index ybe_table")
            index_tables[table] = detectors
        seen_racks = set()
        for detector_index_in_entry, detector in enumerate(detectors):
            detector_context = f"{context}.detectors[{detector_index_in_entry}]"
            if not isinstance(detector, dict):
                failures.append(f"{detector_context}: detector must be an object")
                continue
            try:
                rack_table = normalize_rack_table(detector.get("rack_table"))
            except (TypeError, ValueError) as exc:
                failures.append(f"{detector_context}: invalid rack_table: {exc}")
                continue
            if not is_rack_table(rack_table):
                failures.append(f"{detector_context}: rack_table is not a rack")
            if rack_table in seen_racks:
                failures.append(f"{detector_context}: duplicate rack_table for this ybe_table")
            seen_racks.add(rack_table)
            source_ids = detector.get("source_schema_ids")
            if source_ids is not None:
                if not isinstance(source_ids, list) or any(
                    not isinstance(schema_id, str) for schema_id in source_ids
                ):
                    failures.append(
                        f"{detector_context}: source_schema_ids must be a list of strings"
                    )

    imported_tables = set(index_tables)
    missing_tables = expected_tables - imported_tables
    extra_tables = imported_tables - expected_tables
    _require(
        payload.get("tables_with_detector_components") == len(imported_tables),
        failures,
        "tables_with_detector_components does not match detector_index",
    )
    _require(
        payload.get("missing_table_count") == len(missing_tables),
        failures,
        "missing_table_count does not match detector_index complement",
    )
    _require(
        payload.get("extra_imported_table_count") == len(extra_tables),
        failures,
        "extra_imported_table_count does not match detector_index",
    )
    _require(
        payload.get("incomplete_detector_basis") == bool(missing_tables),
        failures,
        "incomplete_detector_basis does not match missing tables",
    )
    if "missing_ybe_tables" in payload:
        supplied_missing = {
            table
            for table in (
                _normalize_ybe_table_for_audit(item, failures, "missing_ybe_tables")
                for item in payload["missing_ybe_tables"]
            )
            if table is not None
        }
        _require(
            supplied_missing == missing_tables,
            failures,
            "missing_ybe_tables does not match detector_index complement",
        )
    if "extra_imported_ybe_tables" in payload:
        supplied_extra = {
            table
            for table in (
                _normalize_ybe_table_for_audit(
                    item,
                    failures,
                    "extra_imported_ybe_tables",
                    require_nonpermutation=False,
                )
                for item in payload["extra_imported_ybe_tables"]
            )
            if table is not None
        }
        _require(
            supplied_extra == extra_tables,
            failures,
            "extra_imported_ybe_tables does not match detector_index extras",
        )

    rows = payload.get("rows")
    if not isinstance(rows, list):
        failures.append("rows must be a list")
        rows = []
    if "row_count" in payload:
        _require(payload.get("row_count") == len(rows), failures, "row_count mismatch")
    for row_index, row in enumerate(rows):
        context = f"rows[{row_index}]"
        if not isinstance(row, dict):
            failures.append(f"{context}: row must be an object")
            continue
        for field in WIDTH3_AUDIT_ROW_FIELDS:
            if field not in row:
                failures.append(f"{context}: missing field {field}")
        table = _normalize_ybe_table_for_audit(row.get("ybe_table"), failures, context)
        if table is None:
            continue
        detectors = index_tables.get(table)
        if detectors is None:
            failures.append(f"{context}: row ybe_table is absent from detector_index")
            detectors = []
        detector_sizes = []
        for detector in detectors:
            if not isinstance(detector, dict) or "rack_table" not in detector:
                continue
            try:
                detector_sizes.append(len(normalize_rack_table(detector["rack_table"])))
            except (TypeError, ValueError):
                pass
        _require(
            row.get("detector_component_count") == len(detectors),
            failures,
            f"{context}: detector_component_count mismatch",
        )
        _require(
            row.get("detector_component_sizes") == detector_sizes,
            failures,
            f"{context}: detector_component_sizes mismatch",
        )
        if bound is not None:
            _require(row.get("bound") == bound, failures, f"{context}: bound mismatch")
        if arity is not None:
            _require(row.get("arity") == arity, failures, f"{context}: arity mismatch")
        truncated = row.get("truncated")
        if not isinstance(truncated, bool):
            failures.append(f"{context}: truncated must be boolean")
            continue
        seed_count = row.get("seed_count")
        if isinstance(seed_count, bool) or not isinstance(seed_count, int) or seed_count < 0:
            failures.append(f"{context}: seed_count must be a nonnegative integer")
        if not truncated:
            for field in (
                "joint_image_size",
                "kernel_image_size",
                "parabolic_image_size",
                "quotient_size",
            ):
                value = row.get(field)
                if isinstance(value, bool) or not isinstance(value, int) or value < 1:
                    failures.append(f"{context}: {field} must be a positive integer")
            if isinstance(row.get("kernel_image_size"), int) and isinstance(
                row.get("parabolic_image_size"), int
            ) and isinstance(row.get("quotient_size"), int):
                kernel_size = row["kernel_image_size"]
                parabolic_size = row["parabolic_image_size"]
                quotient_size = row["quotient_size"]
                if parabolic_size and kernel_size % parabolic_size:
                    failures.append(
                        f"{context}: parabolic_image_size does not divide kernel_image_size"
                    )
                elif parabolic_size and kernel_size // parabolic_size != quotient_size:
                    failures.append(f"{context}: quotient_size arithmetic mismatch")
            quotient_nontrivial = row.get("quotient_nontrivial")
            if not isinstance(quotient_nontrivial, bool):
                failures.append(f"{context}: quotient_nontrivial must be boolean")
            elif isinstance(row.get("quotient_size"), int):
                _require(
                    quotient_nontrivial == (row["quotient_size"] != 1),
                    failures,
                    f"{context}: quotient_nontrivial disagrees with quotient_size",
                )
    return tuple(failures)
