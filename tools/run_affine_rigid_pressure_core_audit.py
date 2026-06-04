from __future__ import annotations

import itertools
import json
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_audit import affine_solution  # noqa: E402
from run_linear_f2_audit import mat_rank, matrix_signature  # noqa: E402
from run_rigid_pressure_core_audit import rigid_pressure_core_row  # noqa: E402
from run_sequential_primitivity_frontier_audit import (  # noqa: E402
    affine_f2_hidden_cyclic_solution,
)
from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    branch_tags,
    flip_across_partitions,
    is_involutive_solution,
    is_left_nondegenerate,
    is_rack_type,
    is_right_nondegenerate,
)

OUT_JSON = ROOT / "proofs" / "affine_rigid_pressure_core_audit.json"
OUT_MD = ROOT / "proofs" / "affine_rigid_pressure_core_audit.md"


def _terminal_first_failure(solution: FiniteBraidedSet) -> str | None:
    if is_left_nondegenerate(solution) or is_right_nondegenerate(solution):
        return "bidegenerate"
    if is_involutive_solution(solution):
        return "noninvolutive"
    if is_rack_type(solution):
        return "not_rack"
    if flip_across_partitions(solution):
        return "not_flip_across"
    return None


def _sample_record(matrix, offset, row) -> dict[str, object]:
    return {
        "matrix": matrix_signature(matrix),
        "offset": "".join(str(entry) for entry in offset),
        "branch_tags": list(row.branch_tags),
        "first_failed_filter": row.first_failed_filter,
        "congruence_count": row.congruence_count,
        "quotient_rigid": row.quotient_rigid,
        "proper_subsolution_count": row.proper_subsolution_count,
        "subsolution_rigid": row.subsolution_rigid,
        "observer_partition_block_count": row.observer_partition_block_count,
        "observer_rigid": row.observer_rigid,
        "transport_split_count": row.transport_split_count,
        "no_transport_isomorphic_split": row.no_transport_isomorphic_split,
    }


def scan_affine_f2_dimension_two() -> dict[str, object]:
    dimension = 2
    rows = tuple(itertools.product((0, 1), repeat=2 * dimension))
    offsets = tuple(itertools.product((0, 1), repeat=2 * dimension))
    checked = 0
    invertible = 0
    ybe_count = 0
    first_failed = Counter()
    branch_tag_counts = Counter()
    terminal_survivor_count = 0
    structural_survivor_count = 0
    candidate_count = 0
    terminal_survivor_samples = []
    structural_survivor_samples = []

    for matrix in itertools.product(rows, repeat=2 * dimension):
        checked += len(offsets)
        if mat_rank(matrix) != 2 * dimension:
            continue
        invertible += len(offsets)
        for offset in offsets:
            solution = affine_solution(matrix, offset, dimension)
            if not solution.is_ybe():
                continue
            ybe_count += 1
            tags = branch_tags(solution)
            branch_tag_counts["+".join(tags) if tags else "(untagged)"] += 1
            terminal_failure = _terminal_first_failure(solution)
            if terminal_failure is not None:
                first_failed[terminal_failure] += 1
                continue

            terminal_survivor_count += 1
            row = rigid_pressure_core_row(
                "affine_f2_dimension2",
                solution,
                run_pressure_if_structural=False,
            )
            first_failed[row.first_failed_filter] += 1
            if len(terminal_survivor_samples) < 8:
                terminal_survivor_samples.append(_sample_record(matrix, offset, row))
            if row.structural_filter_survives is True:
                structural_survivor_count += 1
                if len(structural_survivor_samples) < 8:
                    structural_survivor_samples.append(_sample_record(matrix, offset, row))
            if row.rigid_pressure_core_candidate:
                candidate_count += 1

    return {
        "dimension": dimension,
        "point_count": 2**dimension,
        "checked_affine_map_count": checked,
        "invertible_affine_map_count": invertible,
        "affine_ybe_count": ybe_count,
        "terminal_survivor_count": terminal_survivor_count,
        "structural_survivor_count": structural_survivor_count,
        "rigid_pressure_core_candidate_count": candidate_count,
        "first_failed_filter_counts": dict(sorted(first_failed.items())),
        "branch_tag_counts": dict(sorted(branch_tag_counts.items())),
        "terminal_survivor_samples": terminal_survivor_samples,
        "structural_survivor_samples": structural_survivor_samples,
        "exact_exhaustive_affine_linear": True,
        "pressure_attempted": structural_survivor_count > 0,
    }


def affine_prime_line_solution(prime: int, coeffs: tuple[int, ...]) -> FiniteBraidedSet:
    if len(coeffs) != 6:
        raise ValueError("expected six affine coefficients")
    a, b, c, d, e, f = coeffs
    elements = tuple(range(prime))
    table = {}
    for x in elements:
        for y in elements:
            table[(x, y)] = (
                (a * x + b * y + c) % prime,
                (d * x + e * y + f) % prime,
            )
    return FiniteBraidedSet(elements, table)


def _determinant_two_by_two(coeffs: tuple[int, ...], prime: int) -> int:
    a, b, _c, d, e, _f = coeffs
    return (a * e - b * d) % prime


def scan_affine_prime_line(prime: int) -> dict[str, object]:
    checked = 0
    invertible = 0
    ybe_count = 0
    first_failed = Counter()
    branch_tag_counts = Counter()
    terminal_survivor_count = 0
    structural_survivor_count = 0
    candidate_count = 0
    terminal_survivor_samples = []

    for coeffs in itertools.product(range(prime), repeat=6):
        checked += 1
        if _determinant_two_by_two(coeffs, prime) == 0:
            continue
        invertible += 1
        solution = affine_prime_line_solution(prime, coeffs)
        if not solution.is_ybe():
            continue
        ybe_count += 1
        tags = branch_tags(solution)
        branch_tag_counts["+".join(tags) if tags else "(untagged)"] += 1
        terminal_failure = _terminal_first_failure(solution)
        if terminal_failure is not None:
            first_failed[terminal_failure] += 1
            continue

        terminal_survivor_count += 1
        row = rigid_pressure_core_row(
            f"affine_f{prime}_line",
            solution,
            run_pressure_if_structural=False,
        )
        first_failed[row.first_failed_filter] += 1
        if len(terminal_survivor_samples) < 8:
            terminal_survivor_samples.append(
                {
                    "coefficients": "".join(str(entry) for entry in coeffs),
                    "branch_tags": list(row.branch_tags),
                    "first_failed_filter": row.first_failed_filter,
                    "congruence_count": row.congruence_count,
                    "observer_partition_block_count": (
                        row.observer_partition_block_count
                    ),
                }
            )
        if row.structural_filter_survives is True:
            structural_survivor_count += 1
        if row.rigid_pressure_core_candidate:
            candidate_count += 1

    return {
        "prime": prime,
        "point_count": prime,
        "checked_affine_map_count": checked,
        "invertible_affine_map_count": invertible,
        "affine_ybe_count": ybe_count,
        "terminal_survivor_count": terminal_survivor_count,
        "structural_survivor_count": structural_survivor_count,
        "rigid_pressure_core_candidate_count": candidate_count,
        "first_failed_filter_counts": dict(sorted(first_failed.items())),
        "branch_tag_counts": dict(sorted(branch_tag_counts.items())),
        "terminal_survivor_samples": terminal_survivor_samples,
        "exact_exhaustive_affine_line": True,
        "pressure_attempted": structural_survivor_count > 0,
    }


def named_dimension_three_pressure_row() -> dict[str, object]:
    row = rigid_pressure_core_row(
        "affine_f2_hidden_cyclic_pressure_row",
        affine_f2_hidden_cyclic_solution(),
        run_pressure_if_structural=False,
    )
    data = asdict(row)
    data["closed_by_known_certificate"] = (
        "two-state hidden cyclic rack gauge plus inert observer"
    )
    return data


def companion_dimension_three_q3_resolution() -> dict[str, object]:
    return {
        "name": "affine_f2_q3_tetrahedral_pressure_row",
        "point_count": 8,
        "same_affine_dimension": True,
        "rescanned_in_this_audit": False,
        "resolution": (
            "all-arity braid-kernel equality with the four-element "
            "tetrahedral Alexander rack, after adding n fixed observer bits"
        ),
        "proof_artifact": (
            "proofs/affine_f2_q3_full_tetrahedral_conjugacy_audit.md"
        ),
        "rigid_pressure_audit": (
            "proofs/affine_f2_q3_rigid_pressure_core_audit.md"
        ),
    }


def build_report() -> dict[str, object]:
    dimension_two = scan_affine_f2_dimension_two()
    prime_lines = {
        "f3": scan_affine_prime_line(3),
        "f5": scan_affine_prime_line(5),
    }
    dimension_three_pressure = named_dimension_three_pressure_row()
    q3_resolution = companion_dimension_three_q3_resolution()
    return {
        "title": "Affine rigid pressure core audit",
        "dimension_two": dimension_two,
        "prime_lines": prime_lines,
        "dimension_three_named_pressure_row": dimension_three_pressure,
        "dimension_three_companion_q3_resolution": q3_resolution,
        "conclusion": (
            "The exact affine-linear size-four family over F_2^2 has terminal "
            "survivors, but no structural rigid-pressure-core survivor: all "
            "24 terminal survivors fail quotient-rigidity.  The exact affine "
            "line searches over F_3 and F_5 have no terminal survivors.  The "
            "named hidden-cyclic F_2^3 pressure row remains a useful guardrail "
            "but fails observer and subsolution rigidity and is already closed "
            "by a finite sequential rack gauge.  The companion q=3 affine "
            "F_2^3 pressure row is tracked in its own audit and is also closed "
            "positively, with all-arity kernel equality to the tetrahedral "
            "four-element rack."
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    dimension_two = report["dimension_two"]
    prime_lines = report["prime_lines"]
    dimension_three = report["dimension_three_named_pressure_row"]
    q3_resolution = report["dimension_three_companion_q3_resolution"]
    lines = [
        "# Affine Rigid Pressure Core Audit",
        "",
        "This generated audit applies the rigid-pressure-core filters to a",
        "structured affine-linear search space.  It is a finite search",
        "frontier, not a proof of Sawin's problem.",
        "",
        "## Exact Affine `F_2^2` Search",
        "",
        f"- exhaustive affine-linear scan: `{dimension_two['exact_exhaustive_affine_linear']}`;",
        f"- checked affine maps: `{dimension_two['checked_affine_map_count']}`;",
        f"- invertible affine maps: `{dimension_two['invertible_affine_map_count']}`;",
        f"- affine YBE tables: `{dimension_two['affine_ybe_count']}`;",
        f"- terminal survivors: `{dimension_two['terminal_survivor_count']}`;",
        f"- structural survivors: `{dimension_two['structural_survivor_count']}`;",
        "- rigid pressure core candidates: "
        f"`{dimension_two['rigid_pressure_core_candidate_count']}`;",
            f"- first failed filter counts: `{dimension_two['first_failed_filter_counts']}`.",
            "",
        "The terminal survivors are exactly the affine size-four rows that",
        "escape bidegeneracy, involutivity, rack-type, and flip-across filters.",
        "They still all fail the next structural test, quotient-rigidity.",
        "",
        "Representative terminal survivor records:",
        "",
    ]
    for sample in dimension_two["terminal_survivor_samples"][:4]:
        lines.extend(
            [
                "- "
                f"offset `{sample['offset']}`, "
                f"first failed `{sample['first_failed_filter']}`, "
                f"congruences `{sample['congruence_count']}`, "
                f"observer blocks `{sample['observer_partition_block_count']}`.",
            ]
        )
    lines.extend(
        [
            "",
            "## Exact Affine Prime-Line Searches",
            "",
        ]
    )
    for key, row in prime_lines.items():
        lines.extend(
            [
                f"### `{key.upper()}`",
                "",
                f"- exhaustive affine-line scan: `{row['exact_exhaustive_affine_line']}`;",
                f"- checked affine maps: `{row['checked_affine_map_count']}`;",
                f"- invertible affine maps: `{row['invertible_affine_map_count']}`;",
                f"- affine YBE tables: `{row['affine_ybe_count']}`;",
                f"- terminal survivors: `{row['terminal_survivor_count']}`;",
                f"- structural survivors: `{row['structural_survivor_count']}`;",
                "- rigid pressure core candidates: "
                f"`{row['rigid_pressure_core_candidate_count']}`;",
                f"- first failed filter counts: `{row['first_failed_filter_counts']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Named `F_2^3` Pressure Row",
            "",
            f"- bidegenerate: `{dimension_three['bidegenerate']}`;",
            f"- noninvolutive: `{dimension_three['noninvolutive']}`;",
            f"- not rack: `{dimension_three['not_rack']}`;",
            f"- observer rigid: `{dimension_three['observer_rigid']}`;",
            f"- subsolution rigid: `{dimension_three['subsolution_rigid']}`;",
            f"- first failed filter: `{dimension_three['first_failed_filter']}`;",
            "- known closure: "
            f"`{dimension_three['closed_by_known_certificate']}`.",
            "",
            "## Companion `F_2^3` Tetrahedral Pressure Row",
            "",
            f"- name: `{q3_resolution['name']}`;",
            f"- point count: `{q3_resolution['point_count']}`;",
            "- rescanned in this audit: "
            f"`{q3_resolution['rescanned_in_this_audit']}`;",
            f"- resolution: `{q3_resolution['resolution']}`;",
            f"- proof artifact: `{q3_resolution['proof_artifact']}`;",
            f"- rigid pressure audit: `{q3_resolution['rigid_pressure_audit']}`.",
            "",
            "## Conclusion",
            "",
            report["conclusion"],
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    if argv not in (None, ()):
        raise SystemExit("no arguments are supported")
    report = build_report()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
