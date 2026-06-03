import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import pullback_coskeletal_criterion_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "pullback_coskeletal_criterion_audit.json"
OUT_MD = ROOT / "proofs" / "pullback_coskeletal_criterion_audit.md"


def build_report():
    audit = pullback_coskeletal_criterion_audit()
    report = asdict(audit)
    report["case_keys"] = audit.case_keys
    report["records_pullback_coskeletal_route_boundary"] = (
        audit.records_pullback_coskeletal_route_boundary
    )
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Pullback-coskeletal criterion audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the logical boundary between two",
        "different statements in the finite-base pullback route.",
        "",
        "For one fixed proposed finite operator-label base, the finite",
        "gauge/pullback solution sets in arities `<=N` form an inverse",
        "system when restriction maps are part of the data.  Nonemptiness",
        "at every finite `N` gives an all-arity branch by compactness.",
        "",
        "That is not the same as a uniform bounded-arity cutoff.  A cutoff",
        "requires an additional coskeletality or finite-type lemma saying",
        "that higher deletion cocycles, coefficient transports, and",
        "section-gauge relations are forced by a bounded skeleton.",
        "",
        "## Flags",
        "",
        (
            "- fixed-base inverse-limit compactness recorded: "
            f"`{report['fixed_base_inverse_limit_compactness_recorded']}`;"
        ),
        (
            "- bounded-arity cutoff rejected without extra hypothesis: "
            f"`{report['uniform_bounded_arity_cutoff_rejected_without_extra_hypothesis']}`;"
        ),
        (
            "- pullback-coskeletal hypothesis identified: "
            f"`{report['pullback_coskeletal_hypothesis_identified']}`;"
        ),
        (
            "- finite obstruction certificate identified: "
            f"`{report['finite_obstruction_certificate_identified']}`;"
        ),
        (
            "- records route boundary: "
            f"`{report['records_pullback_coskeletal_route_boundary']}`."
        ),
        "",
        "Missing lemma:",
        "",
        "```text",
        report["missing_pullback_coskeletal_lemma"],
        "```",
        "",
        "## Cases",
        "",
    ]
    for case in report["cases"]:
        lines.extend(
            [
                f"### {case['key']}",
                "",
                f"- role: `{case['role']}`;",
                f"- finite data: {case['finite_data']};",
                f"- criterion: {case['criterion']};",
                f"- consequence: {case['consequence']};",
                f"- failure mode: {case['failure_mode']}.",
                "",
            ]
        )
    lines.extend(
        [
            "## Meaning",
            "",
            "A finite negative certificate for a fixed proposed base is honest:",
            "if the gauge/pullback system is empty at arity `N`, no all-arity",
            "pullback to that base can exist.",
            "",
            "A finite positive prefix is weaker.  It proves only that no",
            "obstruction has appeared yet.  To upgrade a bounded prefix to an",
            "all-arity theorem, one must prove the missing pullback-coskeletal",
            "lemma or another noetherian finite-type replacement.",
            "",
            "Thus the next all-arity work is not another small prefix audit.",
            "It is either a proof of coskeletality for finite YBE point-pushing",
            "deletion towers, or a countermechanism where independent",
            "gauge/pullback constraints first appear in arbitrarily high",
            "arity.",
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
            {
                "case_keys": report["case_keys"],
                "records": report[
                    "records_pullback_coskeletal_route_boundary"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
