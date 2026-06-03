import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_finite_base_pullback_gauge_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_finite_base_pullback_gauge_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_finite_base_pullback_gauge_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["checked_arities"] = audit.checked_arities
    row["all_rows_untruncated"] = audit.all_rows_untruncated
    row["all_label_actions_well_defined"] = audit.all_label_actions_well_defined
    row["all_quotient_maps_well_defined"] = audit.all_quotient_maps_well_defined
    row["all_canonical_section_gauges_trivial"] = (
        audit.all_canonical_section_gauges_trivial
    )
    row["vertical_kernel_exponent_spectrum"] = (
        audit.vertical_kernel_exponent_spectrum
    )
    row["records_prefix_finite_base_pullback_gauge_surface"] = (
        audit.records_prefix_finite_base_pullback_gauge_surface
    )
    return row


def build_report():
    nondegenerate_prefix_witness = FiniteBraidedSet(
        (0, 1),
        {
            (0, 0): (1, 0),
            (0, 1): (0, 0),
            (1, 0): (1, 1),
            (1, 1): (0, 1),
        },
    )
    degenerate_identity = FiniteBraidedSet(
        (0, 1),
        {
            (0, 0): (0, 0),
            (0, 1): (0, 1),
            (1, 0): (1, 0),
            (1, 1): (1, 1),
        },
    )
    rows = []
    for name, solution in (
        ("nondegenerate_prefix_witness", nondegenerate_prefix_witness),
        ("degenerate_identity_finite_base_pullback", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_finite_base_pullback_gauge_audit(
                    solution,
                    max_subgroup_size=10000,
                ),
            )
        )
    report = {
        "description": (
            "Finite translation-pair base ledger for the fixed-base "
            "pullback and section-gauge pressure test."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Prefix finite-base pullback and gauge audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the first finite-base pullback and",
        "section-gauge pressure surface after the vertical Peiffer cube",
        "transport check.  The tested finite base is the translation-pair",
        "label of an element:",
        "",
        "```text",
        "x |-> (lambda_x, rho_x)",
        "```",
        "",
        "where `lambda_x(y)` is the first output of `R(x,y)` and `rho_x(y)`",
        "is the second output of `R(y,x)`.  The audit checks arities",
        "`3,4,5`, because the point-pushing surface begins at `Q_X(3)` and",
        "the deletion Peiffer square/cube checks live at source arity `5`.",
        "",
        "It is not a proof that this finite label-action base is an honest",
        "finite group-Hurwitz base.  That realization is kept as an explicit",
        "remaining obligation.",
        "",
        "## Rows",
        "",
    ]
    for row in report["rows"]:
        lines.extend(
            [
                f"### {row['name']}",
                "",
                f"- element count: `{row['element_count']}`;",
                (
                    "- translation-pair label count: "
                    f"`{row['translation_pair_label_count']}`;"
                ),
                (
                    "- left/right translation label counts: "
                    f"`({row['left_translation_label_count']}, "
                    f"{row['right_translation_label_count']})`;"
                ),
                (
                    "- crossing descends to translation-pair labels: "
                    f"`{row['crossing_descends_to_translation_pair_labels']}`;"
                ),
                (
                    "- crossing label ambiguity count: "
                    f"`{row['crossing_label_ambiguity_count']}`;"
                ),
                (
                    "- left-prefix monoid size: "
                    f"`{row['left_prefix_monoid_size']}`;"
                ),
                f"- nonunit prefix count: `{row['nonunit_prefix_count']}`;",
                f"- checked arities: `{tuple(row['checked_arities'])}`;",
                f"- all rows untruncated: `{row['all_rows_untruncated']}`;",
                (
                    "- all label actions well-defined: "
                    f"`{row['all_label_actions_well_defined']}`;"
                ),
                (
                    "- all quotient maps well-defined: "
                    f"`{row['all_quotient_maps_well_defined']}`;"
                ),
                (
                    "- all canonical sections gauge-trivial: "
                    f"`{row['all_canonical_section_gauges_trivial']}`;"
                ),
                (
                    "- vertical kernel exponent spectrum: "
                    f"`{tuple(row['vertical_kernel_exponent_spectrum'])}`;"
                ),
                (
                    "- vertical defect transport mismatches: "
                    f"`{row['vertical_defect_transport_mismatch_count']}`;"
                ),
                (
                    "- vertical defect order spectrum: "
                    f"`{tuple(row['vertical_defect_order_spectrum'])}`;"
                ),
                (
                    "- Peiffer square nontrivial boundary count: "
                    f"`{row['peiffer_square_nontrivial_boundary_count']}`;"
                ),
                (
                    "- Peiffer cube transport mismatch count: "
                    f"`{row['peiffer_cube_transport_mismatch_count']}`;"
                ),
                (
                    "- Peiffer order-pair spectrum: "
                    f"`{tuple(row['peiffer_order_pair_spectrum'])}`;"
                ),
                (
                    "- observed deletion 2-cocycle gauge-trivial: "
                    f"`{row['observed_deletion_two_cocycle_gauge_trivial']}`;"
                ),
                (
                    "- group-Hurwitz realization still required: "
                    f"`{row['group_hurwitz_realization_still_required']}`;"
                ),
                (
                    "- records finite-base pullback/gauge surface: "
                    f"`{row['records_prefix_finite_base_pullback_gauge_surface']}`."
                ),
                "",
            ]
        )
        for surface in row["rows"]:
            lines.extend(
                [
                    (
                        f"#### Q_X({surface['point_pushing_arity']}) "
                        f"in B_{surface['braid_index']}"
                    ),
                    "",
                    f"- tuple count: `{surface['tuple_count']}`;",
                    f"- generator count: `{surface['generator_count']}`;",
                    f"- label tuple count: `{surface['label_tuple_count']}`;",
                    (
                        "- max label-fibre size: "
                        f"`{surface['max_label_fibre_size']}`;"
                    ),
                    (
                        "- tuple action group size/exponent: "
                        f"`({surface['tuple_action_group_size']}, "
                        f"{surface['tuple_action_group_exponent']})`;"
                    ),
                    (
                        "- label action group size/exponent: "
                        f"`({surface['label_action_group_size']}, "
                        f"{surface['label_action_group_exponent']})`;"
                    ),
                    (
                        "- quotient map well-defined: "
                        f"`{surface['quotient_map_well_defined']}`;"
                    ),
                    (
                        "- vertical kernel size/exponent: "
                        f"`({surface['vertical_kernel_size']}, "
                        f"{surface['vertical_kernel_exponent']})`;"
                    ),
                    (
                        "- canonical section displacement count: "
                        f"`{surface['canonical_section_displacement_count']}`;"
                    ),
                    (
                        "- canonical section gauge-trivial: "
                        f"`{surface['canonical_section_gauge_trivial']}`;"
                    ),
                    f"- truncated: `{surface['truncated']}`.",
                    "",
                ]
            )
    lines.extend(
        [
            "## Meaning",
            "",
            "For the nondegenerate prefix witness, the translation-pair base",
            "collapses to a one-point label base.  The checked point-pushing",
            "image is therefore entirely vertical over this base, with",
            "vertical exponent `2` in arities `3,4,5`.  The canonical section",
            "is not fixed by generators, so the section itself has nonzero",
            "1-cochain displacement.  Nevertheless the deletion-defect",
            "transport, Peiffer square, and Peiffer cube ledgers all have zero",
            "2-cocycle obstruction on this prefix surface.",
            "",
            "For the degenerate identity row, the translation-pair label tuple",
            "is injective and the point-pushing image is trivial, so all",
            "vertical and gauge rows are trivial.",
            "",
            "Thus this checkpoint removes the current low-dimensional",
            "pullback/gauge obstruction for the two recorded rows.  It does",
            "not prove the finite augmented Artin-envelope lemma: the open",
            "step is still to realize such finite label-action bases as one",
            "fixed finite group-Hurwitz operator-label tower, uniformly in",
            "all arities, or to find a finite low-arity certificate proving",
            "that no such fixed base can pull back the tower.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(
        json.dumps(
            [
                {
                    "name": row["name"],
                    "checked_arities": row["checked_arities"],
                    "vertical_kernel_exponent_spectrum": row[
                        "vertical_kernel_exponent_spectrum"
                    ],
                    "observed_deletion_two_cocycle_gauge_trivial": row[
                        "observed_deletion_two_cocycle_gauge_trivial"
                    ],
                    "records": row[
                        "records_prefix_finite_base_pullback_gauge_surface"
                    ],
                }
                for row in report["rows"]
            ],
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
