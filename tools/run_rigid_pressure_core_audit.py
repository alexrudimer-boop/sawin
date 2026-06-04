from __future__ import annotations

import json
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from tools.run_sequential_primitivity_frontier_audit import (  # noqa: E402
    affine_f2_hidden_cyclic_solution,
    affine_f2_type_a_solution,
    permutation_solution_with_toggle,
)
from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    all_bijection_solutions,
    branch_tags,
    congruences,
    equality_congruence,
    flip_across_partitions,
    flip_disjoint_union_solution,
    identity_solution,
    is_involutive_solution,
    is_left_nondegenerate,
    is_rack_type,
    is_right_nondegenerate,
    one_state_invariant_observer_partition,
    proper_subsolution_subsets,
    small_rack_prefix_obstruction_rows,
    subsolution_fibre_congruences,
    subsolution_fibre_transport_isomorphism_audit,
    universal_congruence,
)

OUT_JSON = ROOT / "proofs" / "rigid_pressure_core_audit.json"
OUT_MD = ROOT / "proofs" / "rigid_pressure_core_audit.md"


@dataclass(frozen=True)
class RigidPressureCoreRow:
    name: str
    size: int
    ybe: bool
    branch_tags: tuple[str, ...]
    left_degenerate: bool
    right_degenerate: bool
    bidegenerate: bool
    left_bijective_coordinate_count: int
    right_bijective_coordinate_count: int
    everywhere_left_singular: bool
    everywhere_right_singular: bool
    everywhere_bisingular: bool
    noninvolutive: bool
    not_rack: bool
    flip_across_partition_count: int | None
    not_flip_across: bool | None
    congruence_count: int | None
    quotient_rigid: bool | None
    proper_subsolution_count: int | None
    subsolution_rigid: bool | None
    observer_partition_block_count: int
    observer_rigid: bool
    transport_split_count: int | None
    no_transport_isomorphic_split: bool | None
    terminal_filter_survives: bool | None
    structural_filter_survives: bool | None
    rack_prefix_pressure_attempted: bool
    rack_prefix_pressure_found: bool | None
    rack_prefix_pressure_truncated: bool | None
    first_pressure_witness: str | None
    rigid_pressure_core_candidate: bool
    first_failed_filter: str | None


def _safe_count(fn, disabled_value=None):
    try:
        return len(fn())
    except ValueError:
        return disabled_value


def _first_failed_filter(row_data: dict) -> str | None:
    checks = (
        ("ybe", row_data["ybe"]),
        ("bidegenerate", row_data["bidegenerate"]),
        ("noninvolutive", row_data["noninvolutive"]),
        ("not_rack", row_data["not_rack"]),
        ("not_flip_across", row_data["not_flip_across"]),
        ("everywhere_bisingular", row_data["everywhere_bisingular"]),
        ("quotient_rigid", row_data["quotient_rigid"]),
        ("subsolution_rigid", row_data["subsolution_rigid"]),
        ("observer_rigid", row_data["observer_rigid"]),
        (
            "no_transport_isomorphic_split",
            row_data["no_transport_isomorphic_split"],
        ),
        ("rack_prefix_pressure_found", row_data["rack_prefix_pressure_found"]),
    )
    for name, value in checks:
        if value is not True:
            return name
    return None


def _coordinate_bijective_counts(solution: FiniteBraidedSet) -> tuple[int, int]:
    left_count = 0
    right_count = 0
    for left in solution.elements:
        images = [solution.R[(left, right)][0] for right in solution.elements]
        if len(set(images)) == len(solution.elements):
            left_count += 1
    for right in solution.elements:
        images = [solution.R[(left, right)][1] for left in solution.elements]
        if len(set(images)) == len(solution.elements):
            right_count += 1
    return left_count, right_count


def _transport_split_count(solution: FiniteBraidedSet) -> int | None:
    try:
        partitions = subsolution_fibre_congruences(solution)
    except ValueError:
        return None
    count = 0
    for partition in partitions:
        audit = subsolution_fibre_transport_isomorphism_audit(solution, partition)
        if (
            audit.all_mixed_rows_product_like
            and audit.all_product_like_rows_have_transport_isomorphisms
        ):
            count += 1
    return count


def _rack_prefix_pressure(
    solution: FiniteBraidedSet,
    *,
    max_rack_size: int = 3,
    max_arity: int = 4,
    max_detector_size: int = 64,
    state_limit: int = 50_000,
) -> tuple[bool, bool, str | None]:
    rows = small_rack_prefix_obstruction_rows(
        solution,
        max_rack_size=max_rack_size,
        max_arity=max_arity,
        max_detector_size=max_detector_size,
        state_limit=state_limit,
    )
    truncated = any(row.audit.truncated for row in rows)
    for row in rows:
        if row.obstruction_found:
            return (
                True,
                truncated,
                (
                    f"prefix={row.detector_prefix_length}, "
                    f"detector_size={row.detector_size}, arity={row.arity}, "
                    f"word={row.audit.first_witness_word}"
                ),
            )
    return (False, truncated, None)


def rigid_pressure_core_row(
    name: str,
    solution: FiniteBraidedSet,
    *,
    run_pressure_if_structural: bool = True,
) -> RigidPressureCoreRow:
    ybe = solution.is_ybe()
    left_degenerate = not is_left_nondegenerate(solution)
    right_degenerate = not is_right_nondegenerate(solution)
    bidegenerate = left_degenerate and right_degenerate
    left_bijective_count, right_bijective_count = _coordinate_bijective_counts(solution)
    everywhere_left_singular = left_bijective_count == 0
    everywhere_right_singular = right_bijective_count == 0
    everywhere_bisingular = everywhere_left_singular and everywhere_right_singular
    noninvolutive = not is_involutive_solution(solution)
    not_rack = not is_rack_type(solution)

    flip_count = _safe_count(lambda: flip_across_partitions(solution))
    not_flip_across = None if flip_count is None else flip_count == 0

    try:
        all_congruences = congruences(solution)
        congruence_count = len(all_congruences)
        quotient_rigid = set(all_congruences) == {
            equality_congruence(solution.elements),
            universal_congruence(solution.elements),
        }
    except ValueError:
        congruence_count = None
        quotient_rigid = None

    sub_count = _safe_count(lambda: proper_subsolution_subsets(solution))
    subsolution_rigid = None if sub_count is None else sub_count == 0

    observer_blocks = len(one_state_invariant_observer_partition(solution))
    observer_rigid = observer_blocks == 1

    transport_count = _transport_split_count(solution)
    no_transport_split = None if transport_count is None else transport_count == 0

    terminal_values = (
        ybe,
        bidegenerate,
        noninvolutive,
        not_rack,
        not_flip_across,
    )
    terminal_survives = (
        None if any(value is None for value in terminal_values) else all(terminal_values)
    )
    structural_values = (
        terminal_survives,
        everywhere_bisingular,
        quotient_rigid,
        subsolution_rigid,
        observer_rigid,
        no_transport_split,
    )
    structural_survives = (
        None
        if any(value is None for value in structural_values)
        else all(structural_values)
    )

    pressure_attempted = False
    pressure_found = None
    pressure_truncated = None
    witness = None
    if run_pressure_if_structural and structural_survives is True:
        pressure_attempted = True
        pressure_found, pressure_truncated, witness = _rack_prefix_pressure(solution)

    row_data = {
        "ybe": ybe,
        "bidegenerate": bidegenerate,
        "noninvolutive": noninvolutive,
        "not_rack": not_rack,
        "not_flip_across": not_flip_across,
        "everywhere_bisingular": everywhere_bisingular,
        "quotient_rigid": quotient_rigid,
        "subsolution_rigid": subsolution_rigid,
        "observer_rigid": observer_rigid,
        "no_transport_isomorphic_split": no_transport_split,
        "rack_prefix_pressure_found": pressure_found,
    }
    candidate = all(value is True for value in row_data.values())
    first_failed = _first_failed_filter(row_data)
    return RigidPressureCoreRow(
        name=name,
        size=len(solution.elements),
        ybe=ybe,
        branch_tags=branch_tags(solution),
        left_degenerate=left_degenerate,
        right_degenerate=right_degenerate,
        bidegenerate=bidegenerate,
        left_bijective_coordinate_count=left_bijective_count,
        right_bijective_coordinate_count=right_bijective_count,
        everywhere_left_singular=everywhere_left_singular,
        everywhere_right_singular=everywhere_right_singular,
        everywhere_bisingular=everywhere_bisingular,
        noninvolutive=noninvolutive,
        not_rack=not_rack,
        flip_across_partition_count=flip_count,
        not_flip_across=not_flip_across,
        congruence_count=congruence_count,
        quotient_rigid=quotient_rigid,
        proper_subsolution_count=sub_count,
        subsolution_rigid=subsolution_rigid,
        observer_partition_block_count=observer_blocks,
        observer_rigid=observer_rigid,
        transport_split_count=transport_count,
        no_transport_isomorphic_split=no_transport_split,
        terminal_filter_survives=terminal_survives,
        structural_filter_survives=structural_survives,
        rack_prefix_pressure_attempted=pressure_attempted,
        rack_prefix_pressure_found=pressure_found,
        rack_prefix_pressure_truncated=pressure_truncated,
        first_pressure_witness=witness,
        rigid_pressure_core_candidate=candidate,
        first_failed_filter=first_failed,
    )


def size_three_report() -> dict:
    rows = [
        rigid_pressure_core_row(f"size3_{index}", solution)
        for index, solution in enumerate(all_bijection_solutions(3))
    ]
    first_failed = Counter(row.first_failed_filter for row in rows)
    return {
        "solution_count": len(rows),
        "candidate_count": sum(row.rigid_pressure_core_candidate for row in rows),
        "terminal_survivor_count": sum(row.terminal_filter_survives is True for row in rows),
        "structural_survivor_count": sum(
            row.structural_filter_survives is True for row in rows
        ),
        "first_failed_filter_counts": dict(sorted(first_failed.items(), key=repr)),
        "exact_exhaustive": True,
    }


def representative_rows() -> tuple[RigidPressureCoreRow, ...]:
    type_b = flip_disjoint_union_solution(
        identity_solution((0, 1)),
        permutation_solution_with_toggle(),
        "T",
        "P",
    )
    return (
        rigid_pressure_core_row("size4_affine_type_a", affine_f2_type_a_solution()),
        rigid_pressure_core_row("size4_type_b_flip_across", type_b),
        rigid_pressure_core_row(
            "affine_f2_hidden_cyclic_pressure_row",
            affine_f2_hidden_cyclic_solution(),
        ),
    )


def closed_pressure_representatives() -> tuple[dict[str, object], ...]:
    return (
        {
            "name": "affine_f2_q3_tetrahedral_pressure_row",
            "size": 8,
            "family": "affine-linear F_2^3",
            "structural_audit": (
                "proofs/affine_f2_q3_rigid_pressure_core_audit.md"
            ),
            "proof_artifact": (
                "proofs/affine_f2_q3_full_tetrahedral_conjugacy_audit.md"
            ),
            "closure_kind": (
                "all-arity braid-kernel equality with the four-element "
                "tetrahedral Alexander rack, plus n fixed observer bits"
            ),
            "rigid_core_consequence": (
                "not a rigid core, because it is braid-kernel equivalent to a "
                "finite rack in every arity"
            ),
        },
    )


def build_report() -> dict:
    representatives = representative_rows()
    closed_representatives = closed_pressure_representatives()
    return {
        "title": "Rigid pressure core audit",
        "definition": (
            "A rigid pressure core is a nonterminal, quotient-rigid, "
            "everywhere-coordinate-singular, subsolution-rigid, "
            "observer-rigid, transport-split-rigid finite YBE table with "
            "actual small-rack prefix pressure."
        ),
        "singular_filter": (
            "The everywhere-coordinate-singular condition is now a theorem-level "
            "necessary filter for minimal counterexamples outside the "
            "left/right-nondegenerate branches and with no proper "
            "crossing-closed subsolution: any bijective L_x or R_x would "
            "generate a nonempty crossing-closed subsolution locus."
        ),
        "size_3": size_three_report(),
        "representatives": [asdict(row) for row in representatives],
        "closed_pressure_representatives": list(closed_representatives),
        "representative_candidate_count": sum(
            row.rigid_pressure_core_candidate for row in representatives
        ),
        "closed_pressure_representative_count": len(closed_representatives),
        "conclusion": (
            "No rigid pressure core appears in the exhaustive size-three "
            "corpus or in the current named pressure representatives.  The "
            "affine F_2^3 q=3 pressure row is now tracked as a closed "
            "representative, because the tetrahedral-rack conjugacy gives "
            "all-arity kernel equality.  The next falsifiable search target "
            "is a larger table, preferably size five or a structured "
            "affine-linear family, that survives all finite rigidity filters "
            "and then exhibits N_{m,n}(X)!=1 for a small rack prefix."
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Rigid Pressure Core Audit",
        "",
        "This generated audit records the first falsifiable negative-search",
        "target after the active-factor boundary.  It is not a proof of",
        "Sawin's problem.",
        "",
        "## Definition",
        "",
        report["definition"],
        "",
        "## Singular Coordinate Filter",
        "",
        report["singular_filter"],
        "",
        "## Exhaustive Size 3 Corpus",
        "",
    ]
    size3 = report["size_3"]
    lines.extend(
        [
            f"- exhaustive: `{size3['exact_exhaustive']}`;",
            f"- YBE solution count: `{size3['solution_count']}`;",
            f"- terminal survivor count: `{size3['terminal_survivor_count']}`;",
            f"- structural survivor count: `{size3['structural_survivor_count']}`;",
            f"- rigid pressure core candidates: `{size3['candidate_count']}`;",
            f"- first failed filter counts: `{size3['first_failed_filter_counts']}`.",
            "",
            "## Named Representatives",
            "",
        ]
    )
    for row in report["representatives"]:
        lines.extend(
            [
                f"### {row['name']}",
                "",
                f"- size: `{row['size']}`;",
                f"- tags: `{row['branch_tags']}`;",
                f"- bidegenerate: `{row['bidegenerate']}`;",
                "- left bijective coordinate maps: "
                f"`{row['left_bijective_coordinate_count']}`;",
                "- right bijective coordinate maps: "
                f"`{row['right_bijective_coordinate_count']}`;",
                f"- everywhere bisingular: `{row['everywhere_bisingular']}`;",
                f"- noninvolutive: `{row['noninvolutive']}`;",
                f"- not rack: `{row['not_rack']}`;",
                f"- not flip-across: `{row['not_flip_across']}`;",
                f"- quotient rigid: `{row['quotient_rigid']}`;",
                f"- subsolution rigid: `{row['subsolution_rigid']}`;",
                f"- observer rigid: `{row['observer_rigid']}`;",
                "- no transport-isomorphic split: "
                f"`{row['no_transport_isomorphic_split']}`;",
                "- rack-prefix pressure attempted: "
                f"`{row['rack_prefix_pressure_attempted']}`;",
                f"- rack-prefix pressure found: `{row['rack_prefix_pressure_found']}`;",
                f"- first failed filter: `{row['first_failed_filter']}`;",
                "- rigid pressure core candidate: "
                f"`{row['rigid_pressure_core_candidate']}`.",
                "",
            ]
        )
    lines.extend(["## Closed Pressure Representatives", ""])
    for row in report["closed_pressure_representatives"]:
        lines.extend(
            [
                f"### {row['name']}",
                "",
                f"- size: `{row['size']}`;",
                f"- family: `{row['family']}`;",
                f"- closure kind: `{row['closure_kind']}`;",
                f"- proof artifact: `{row['proof_artifact']}`;",
                f"- structural audit: `{row['structural_audit']}`;",
                f"- rigid-core consequence: `{row['rigid_core_consequence']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Conclusion",
            "",
            f"- representative candidate count: `{report['representative_candidate_count']}`;",
            "- closed pressure representative count: "
            f"`{report['closed_pressure_representative_count']}`;",
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
