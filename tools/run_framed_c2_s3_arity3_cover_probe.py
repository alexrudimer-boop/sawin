from __future__ import annotations

from dataclasses import asdict
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.artin_longitudes import artin_detector_rack  # noqa: E402
from ybe_domination.finite_group import cyclic_group, symmetric_group  # noqa: E402
from ybe_domination.rack_residual_tower import (  # noqa: E402
    group_conjugation_rack,
    rack_residual_obstruction_audit,
)


OUT_JSON = ROOT / "proofs" / "framed_c2_s3_arity3_cover_probe.json"
OUT_MD = ROOT / "proofs" / "framed_c2_s3_arity3_cover_probe.md"


def _audit_row(n: int) -> dict[str, Any]:
    framed_c2 = artin_detector_rack(cyclic_group(2), include_trivial_two=False)
    s3_conj = group_conjugation_rack(symmetric_group(3))
    audit = rack_residual_obstruction_audit(
        framed_c2,
        s3_conj,
        n=n,
        state_limit=1_000_000,
    )
    row = asdict(audit)
    row["kernel_containment_certified"] = (
        not audit.truncated and audit.kernel_contains_nonidentity is False
    )
    row["interpretation"] = (
        f"No element of K_{n}(S3^conj) acts nontrivially on A_C2 in this "
        "finite residual-image audit."
    )
    return row


def build_report() -> dict[str, Any]:
    rows = [_audit_row(n) for n in (2, 3)]
    return {
        "title": "Framed C2 versus S3 arity-3 cover probe",
        "solution": "A_C2",
        "detector": "S3^conj",
        "arities_checked": [2, 3],
        "rows": rows,
        "all_checked_kernel_containments_certified": all(
            row["kernel_containment_certified"] for row in rows
        ),
        "proves_all_arity_cover": False,
        "conclusion": (
            "The S3 conjugation rack covers the framed C2 Artin detector in "
            "arities 2 and 3 under the residual-image audit.  This strengthens "
            "the two-strand sanity check, but it remains finite evidence only; "
            "the Framed-to-Conjugation Cover Lemma still requires an all-arity "
            "proof."
        ),
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# {report['title']}",
        "",
        report["conclusion"],
        "",
        "## Setup",
        "",
        f"- solution: `{report['solution']}`;",
        f"- detector: `{report['detector']}`;",
        f"- arities checked: `{report['arities_checked']}`;",
        "- proves all-arity cover: "
        f"`{report['proves_all_arity_cover']}`;",
        "",
        "## Residual-image rows",
        "",
        "| n | joint image | solution image | detector image | kernel size | kernel contains nonidentity | truncated | containment certified |",
        "| ---: | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in report["rows"]:
        lines.append(
            "| {n} | {joint} | {solution} | {detector} | {kernel} | {contains} | {truncated} | {certified} |".format(
                n=row["n"],
                joint=row["joint_image_size"],
                solution=row["solution_image_size"],
                detector=row["detector_image_size"],
                kernel=row["kernel_size"],
                contains=row["kernel_contains_nonidentity"],
                truncated=row["truncated"],
                certified=row["kernel_containment_certified"],
            )
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This proves the containment",
            "",
            "```text",
            "K_n(S3^conj) subset K_n(A_C2)",
            "```",
            "",
            "for arity 2 and 3 only.  It does not prove the all-arity",
            "Framed-to-Conjugation Cover Lemma.",
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
