from __future__ import annotations

from dataclasses import asdict
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.artin_longitudes import artin_detector_rack  # noqa: E402
from ybe_domination.finite_group import build_group, cyclic_group  # noqa: E402
from ybe_domination.rack_residual_tower import (  # noqa: E402
    group_conjugation_rack,
    rack_residual_obstruction_audit,
)
from ybe_domination.residual import action_permutation  # noqa: E402
from ybe_domination.semigroup_shadows import permutation_order  # noqa: E402


OUT_JSON = ROOT / "proofs" / "framed_abelian_dihedral_cover_probe.json"
OUT_MD = ROOT / "proofs" / "framed_abelian_dihedral_cover_probe.md"


def dihedral_cyclic(rotation_order: int):
    elements = tuple(
        (rotation, reflection)
        for rotation in range(rotation_order)
        for reflection in range(2)
    )

    def multiply(left, right):
        left_rotation, left_reflection = left
        right_rotation, right_reflection = right
        signed_right = right_rotation if left_reflection == 0 else -right_rotation
        return (
            (left_rotation + signed_right) % rotation_order,
            (left_reflection + right_reflection) % 2,
        )

    return build_group(elements, (0, 0), multiply)


def _sigma_order(solution) -> int:
    return permutation_order(action_permutation(solution, 2, (1,)))


def _row(exponent: int, rotation_order: int, label: str) -> dict[str, Any]:
    solution = artin_detector_rack(cyclic_group(exponent), include_trivial_two=False)
    detector = group_conjugation_rack(dihedral_cyclic(rotation_order))
    audit = rack_residual_obstruction_audit(
        solution,
        detector,
        n=2,
        state_limit=200_000,
    )
    audit_row = asdict(audit)
    audit_row["kernel_containment_certified"] = (
        not audit.truncated and audit.kernel_contains_nonidentity is False
    )
    return {
        "exponent": exponent,
        "detector_label": label,
        "rotation_order": rotation_order,
        "detector_group_order": 2 * rotation_order,
        "solution_sigma_order": _sigma_order(solution),
        "detector_sigma_order": _sigma_order(detector),
        "audit": audit_row,
    }


def build_report() -> dict[str, Any]:
    rows = []
    for exponent in range(2, 9):
        rows.append(_row(exponent, exponent, "naive_Dih_Ce"))
        rows.append(_row(exponent, 2 * exponent, "doubled_Dih_C2e"))
    doubled_rows = [
        row for row in rows if row["detector_label"] == "doubled_Dih_C2e"
    ]
    naive_failures = [
        row
        for row in rows
        if row["detector_label"] == "naive_Dih_Ce"
        and not row["audit"]["kernel_containment_certified"]
    ]
    return {
        "title": "Framed abelian dihedral cover probe",
        "arity": 2,
        "exponents_checked": list(range(2, 9)),
        "rows": rows,
        "all_doubled_rows_certified": all(
            row["audit"]["kernel_containment_certified"] for row in doubled_rows
        ),
        "naive_failure_exponents": [
            row["exponent"] for row in naive_failures
        ],
        "proves_all_arity_theorem": False,
        "theorem_artifact": "proofs/framed_abelian_dihedral_cover_theorem.md",
        "conclusion": (
            "In arity 2, the doubled generalized dihedral detector "
            "Dih(C_{2e}) covers A_Ce for exponents 2 through 8.  The naive "
            "Dih(C_e) detector can fail at even exponents, which is the parity "
            "issue addressed in the theorem."
        ),
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# {report['title']}",
        "",
        report["conclusion"],
        "",
        "## Scope",
        "",
        f"- arity: `{report['arity']}`;",
        f"- exponents checked: `{report['exponents_checked']}`;",
        "- proves all-arity theorem: "
        f"`{report['proves_all_arity_theorem']}`;",
        f"- theorem artifact: `{report['theorem_artifact']}`;",
        "",
        "## Rows",
        "",
        "| e | detector | rotation order | group order | A_Ce sigma order | detector sigma order | kernel contains nonidentity | certified | witness |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in report["rows"]:
        audit = row["audit"]
        lines.append(
            "| {e} | {label} | {rot} | {order} | {asol} | {adet} | {contains} | {certified} | {witness} |".format(
                e=row["exponent"],
                label=row["detector_label"],
                rot=row["rotation_order"],
                order=row["detector_group_order"],
                asol=row["solution_sigma_order"],
                adet=row["detector_sigma_order"],
                contains=audit["kernel_contains_nonidentity"],
                certified=audit["kernel_containment_certified"],
                witness=audit["first_witness_word"],
            )
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is a small arity-2 parity probe.  The all-arity proof is the",
            "separate theorem artifact; this probe is only a guardrail against",
            "choosing the naive even-exponent dihedral detector.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    report = build_report()
    OUT_JSON.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
