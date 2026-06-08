"""Derive low-arity pure-kernel consequences from linear F3 audits.

This verifier does not redo the heavy orbit search.  It cross-checks the
existing generated completion, orbit, monolith, and pure-kernel audit
artifacts and records the logical consequence used in the current prompt:
contextual orbit-injectivity through a fixed arity excludes contextual-rack
kernel X-motion through that arity.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMPLETION_JSON = ROOT / "proofs" / "linear_f3_skew_flip_completion_audit.json"
ORBIT_JSON = ROOT / "proofs" / "linear_f3_skew_flip_orbit_audit.json"
MONOLITH_JSON = ROOT / "proofs" / "linear_f3_skew_flip_monolith_audit.json"
PURE_JSON = ROOT / "proofs" / "linear_f3_skew_flip_pure_kernel_monodromy_audit.json"

OUT_JSON = ROOT / "proofs" / "linear_f3_skew_flip_contextual_kernel_consequence.json"
OUT_MD = ROOT / "proofs" / "linear_f3_skew_flip_contextual_kernel_consequence.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def arities_without_collision(row: dict) -> list[int]:
    out = []
    for check in row["arity_checks"]:
        if check.get("collision") is None:
            out.append(int(check["arity"]))
    return out


def run_report() -> dict:
    completion = load_json(COMPLETION_JSON)
    orbit = load_json(ORBIT_JSON)
    monolith = load_json(MONOLITH_JSON)
    pure = load_json(PURE_JSON)

    subdirect_rows = [
        row
        for row in monolith["rows"]
        if row["monolith_is_nontrivial"]
        and row["monolith"] is not None
        and row["monolith"]["quotient_class_count"] > 1
    ]
    subdirect_indices = {row["row_index"] for row in subdirect_rows}
    orbit_by_index = {
        row["row_index"]: row
        for row in orbit["all_case_summaries"]
    }
    missing_orbit_rows = sorted(subdirect_indices.difference(orbit_by_index))

    arity_bound = int(orbit["all_case_max_arity"])
    expected_arities = set(range(1, arity_bound + 1))
    subdirect_orbit_failures = []
    for row in subdirect_rows:
        orbit_row = orbit_by_index.get(row["row_index"])
        if orbit_row is None:
            continue
        good_arities = set(arities_without_collision(orbit_row))
        if expected_arities.difference(good_arities):
            subdirect_orbit_failures.append(
                {
                    "row_index": row["row_index"],
                    "missing_good_arities": sorted(expected_arities.difference(good_arities)),
                    "matrix_indices": row["matrix_indices"],
                }
            )

    report = {
        "family": "linear_f3_skew_over_flip_degenerate_noninvolutive",
        "source_artifacts": [
            str(COMPLETION_JSON.relative_to(ROOT)),
            str(ORBIT_JSON.relative_to(ROOT)),
            str(MONOLITH_JSON.relative_to(ROOT)),
            str(PURE_JSON.relative_to(ROOT)),
        ],
        "completion_audit_passed": bool(completion["all_claimed_checks_passed"]),
        "orbit_audit_passed": bool(orbit["all_claimed_checks_passed"]),
        "monolith_audit_passed": bool(monolith["all_claimed_checks_passed"]),
        "pure_kernel_audit_passed": bool(pure["all_claimed_checks_passed"]),
        "degenerate_noninvolutive_rows": int(orbit["degenerate_noninvolutive_rows"]),
        "subdirect_row_count": len(subdirect_rows),
        "contextual_orbit_injectivity_all_rows_through_arity": arity_bound,
        "subdirect_rows_missing_from_orbit_audit": missing_orbit_rows,
        "subdirect_orbit_injectivity_failures": subdirect_orbit_failures,
        "explicit_pure_kernel_two_strand_nontrivial_count": int(
            pure["two_strand"]["detector_kernel_x_nontrivial_count"]
        ),
        "explicit_pure_kernel_three_strand_checked_rows": int(
            pure["three_strand"]["audited_rows"]
        ),
        "explicit_pure_kernel_three_strand_nontrivial_count": int(
            pure["three_strand"]["detector_kernel_x_nontrivial_count"]
        ),
    }
    report["derived_contextual_kernel_x_motion_excluded_through_arity"] = (
        arity_bound
        if (
            report["completion_audit_passed"]
            and report["orbit_audit_passed"]
            and report["monolith_audit_passed"]
            and report["pure_kernel_audit_passed"]
            and report["degenerate_noninvolutive_rows"] == 144
            and report["subdirect_row_count"] == 64
            and not missing_orbit_rows
            and not subdirect_orbit_failures
        )
        else None
    )
    report["all_claimed_checks_passed"] = (
        report["derived_contextual_kernel_x_motion_excluded_through_arity"] == 5
        and report["explicit_pure_kernel_two_strand_nontrivial_count"] == 0
        and report["explicit_pure_kernel_three_strand_checked_rows"] == 4
        and report["explicit_pure_kernel_three_strand_nontrivial_count"] == 0
    )
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Contextual Kernel Consequence",
        "",
        "This generated verifier cross-checks the linear F3 completion,",
        "orbit-injectivity, monolith, and pure-kernel monodromy audit artifacts.",
        "It records the low-arity consequence used by the current theoretical",
        "prompt.",
        "",
        "## Source Artifacts",
        "",
    ]
    for artifact in report["source_artifacts"]:
        lines.append(f"- `{artifact}`")
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- completion audit passed: `{report['completion_audit_passed']}`;",
            f"- orbit audit passed: `{report['orbit_audit_passed']}`;",
            f"- monolith audit passed: `{report['monolith_audit_passed']}`;",
            f"- pure-kernel audit passed: `{report['pure_kernel_audit_passed']}`;",
            "- degenerate non-involutive rows: "
            f"`{report['degenerate_noninvolutive_rows']}`;",
            f"- subdirect rows: `{report['subdirect_row_count']}`;",
            "- contextual orbit-injectivity all rows through arity: "
            f"`{report['contextual_orbit_injectivity_all_rows_through_arity']}`;",
            "- derived contextual-kernel X-motion exclusion through arity: "
            f"`{report['derived_contextual_kernel_x_motion_excluded_through_arity']}`;",
            "- explicit two-strand pure-kernel X-motion count: "
            f"`{report['explicit_pure_kernel_two_strand_nontrivial_count']}`;",
            "- explicit three-strand pure-kernel checked rows: "
            f"`{report['explicit_pure_kernel_three_strand_checked_rows']}`;",
            "- explicit three-strand pure-kernel X-motion count: "
            f"`{report['explicit_pure_kernel_three_strand_nontrivial_count']}`;",
            f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
            "",
            "## Consequence",
            "",
            "For the 64 subdirectly irreducible rows in this family, the existing",
            "contextual rack completion and orbit-injectivity audit imply that",
            "any braid in the contextual-rack kernel acts trivially on `X^n` for",
            "`n <= 5`.  Therefore the pure detector-kernel monodromy obstruction",
            "is excluded through arity 5 for these rows, independently of the",
            "monolith quotient detector.",
            "",
            "This remains finite evidence.  It does not prove all-arity",
            "contextual pure-loop faithfulness and does not resolve A or B.",
        ]
    )
    if report["subdirect_rows_missing_from_orbit_audit"]:
        lines.extend(["", "## Missing Orbit Rows", "", "```json"])
        lines.append(json.dumps(report["subdirect_rows_missing_from_orbit_audit"], indent=2))
        lines.append("```")
    if report["subdirect_orbit_injectivity_failures"]:
        lines.extend(["", "## Subdirect Orbit Failures", "", "```json"])
        lines.append(json.dumps(report["subdirect_orbit_injectivity_failures"], indent=2))
        lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_report()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 contextual-kernel consequence check failed")
    print("OK linear F3 contextual-kernel consequence")
    print(
        "derived exclusion through arity "
        f"{report['derived_contextual_kernel_x_motion_excluded_through_arity']}"
    )


if __name__ == "__main__":
    main()
