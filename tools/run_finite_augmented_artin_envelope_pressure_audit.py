import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import finite_augmented_artin_envelope_pressure_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "finite_augmented_artin_envelope_pressure_audit.json"
OUT_MD = ROOT / "proofs" / "finite_augmented_artin_envelope_pressure_audit.md"


def _audit_dict(audit):
    row = asdict(audit)
    row["case_count"] = audit.case_count
    row["positive_obligation_count"] = audit.positive_obligation_count
    row["failure_mechanism_count"] = audit.failure_mechanism_count
    row["case_keys"] = audit.case_keys
    row["records_true_or_false_mechanisms"] = (
        audit.records_true_or_false_mechanisms
    )
    return row


def build_report():
    audit = finite_augmented_artin_envelope_pressure_audit()
    report = {
        "description": (
            "Pressure-test ledger for the finite augmented Artin-envelope "
            "point-pushing lemma."
        ),
        "audit": _audit_dict(audit),
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    audit = report["audit"]
    lines = [
        "# Finite augmented Artin-envelope pressure audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit lists the mechanisms that can make the",
        "finite augmented Artin-envelope point-pushing lemma true or false.",
        "It excludes whole point-pushing exponent growth, since finite racks",
        "already allow that growth in the group-Hurwitz quotient.",
        "",
        "## Summary",
        "",
        f"- case count: `{audit['case_count']}`;",
        f"- positive obligation count: `{audit['positive_obligation_count']}`;",
        f"- failure mechanism count: `{audit['failure_mechanism_count']}`;",
        (
            "- records true-or-false mechanisms: "
            f"`{audit['records_true_or_false_mechanisms']}`."
        ),
        "",
        "## Cases",
        "",
    ]
    for case in audit["cases"]:
        lines.extend(
            [
                f"### {case['key']}",
                "",
                f"- role: `{case['role']}`;",
                f"- label object: `{case['label_object']}`;",
                (
                    "- required identity or failure: "
                    f"`{case['required_identity_or_failure']}`;"
                ),
                f"- first probe: `{case['first_probe']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Consequence",
            "",
            "A positive proof must build one of the finite label objects and",
            "prove its coordinatewise vertical action and point-forgetting",
            "compatibility uniformly in `n`.  A negative proof must realize",
            "one of the listed failure mechanisms in a genuine finite",
            "bijective YBE solution and promote the `n=3,4` probe to an",
            "all-`n` obstruction against every fixed `(H,C,e)`.",
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
