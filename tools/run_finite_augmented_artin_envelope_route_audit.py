import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import finite_augmented_artin_envelope_route_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "finite_augmented_artin_envelope_route_audit.json"
OUT_MD = ROOT / "proofs" / "finite_augmented_artin_envelope_route_audit.md"


def _audit_dict(audit):
    row = asdict(audit)
    row["rack_side_invariant_is_ready"] = audit.rack_side_invariant_is_ready
    row["remaining_theorem_lemmas"] = audit.remaining_theorem_lemmas
    row["has_first_obstruction_prefix"] = audit.has_first_obstruction_prefix
    row["records_route_one_pressure_test"] = audit.records_route_one_pressure_test
    return row


def build_report():
    audit = finite_augmented_artin_envelope_route_audit()
    report = {
        "description": (
            "Symbolic route-(1) ledger for the finite augmented Artin-envelope "
            "point-pushing strategy."
        ),
        "audit": _audit_dict(audit),
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    audit = report["audit"]
    lines = [
        "# Finite augmented Artin-envelope route audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the corrected point-pushing route.",
        "It is a symbolic checklist, not a proof of the missing lemma.",
        "The finite rack side supplies an operator-label Hurwitz quotient",
        "with bounded-exponent vertical kernel; the route now asks whether",
        "every finite bijective YBE point-pushing tower has the same form.",
        "",
        "## Route flags",
        "",
        (
            "- rack operator-label exact sequence recorded: "
            f"`{audit['rack_operator_label_exact_sequence_recorded']}`;"
        ),
        (
            "- rack vertical-kernel bound recorded: "
            f"`{audit['rack_vertical_kernel_bound_recorded']}`;"
        ),
        (
            "- whole point-pushing exponent bound rejected: "
            f"`{audit['whole_point_pushing_exponent_bound_rejected']}`;"
        ),
        (
            "- domination transfers marked point-pushing quotients: "
            f"`{audit['domination_transfers_marked_point_pushing_quotients']}`;"
        ),
        (
            "- obstruction must defeat every fixed group-Hurwitz base: "
            f"`{audit['obstruction_requires_all_fixed_group_hurwitz_bases']}`;"
        ),
        (
            "- bounded vertical extension is the live invariant: "
            f"`{audit['bounded_vertical_extension_is_live_invariant']}`;"
        ),
        (
            "- records route-(1) pressure test: "
            f"`{audit['records_route_one_pressure_test']}`."
        ),
        "",
        "## Remaining lemmas",
        "",
        f"- `{audit['missing_augmented_envelope_lemma']}`;",
        f"- `{audit['missing_realization_lemma']}`.",
        "",
        "## First obstruction-prefix generators",
        "",
        "The first finite pressure test is at point-pushing arities `3` and `4`.",
        "The standard generator rows are:",
        "",
    ]
    for row in audit["generator_rows"]:
        lines.append(
            "- "
            f"`alpha_{{{row['generator_index']},{row['braid_index']}}}` "
            f"in `K_{row['point_pushing_arity']}`: `{tuple(row['braid_word'])}`."
        )
    lines.extend(
        [
            "",
            "## Meaning",
            "",
            "A counterexample to the finite augmented Artin-envelope lemma",
            "cannot be just unbounded order in `Q_X(n)`.  It must show that",
            "no fixed finite pair `(H,C)` and no fixed exponent bound `e`",
            "can produce compatible normal subgroups `V_X(n)` with",
            "`exp V_X(n) | e` and `Q_X(n)/V_X(n)` a marked quotient of",
            "the corresponding group-Hurwitz point-pushing tower.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps(report["audit"], sort_keys=True))


if __name__ == "__main__":
    main()
