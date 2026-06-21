from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.artin_longitudes import artin_detector_rack  # noqa: E402
from ybe_domination.finite_group import cyclic_group, symmetric_group  # noqa: E402
from ybe_domination.rack_residual_tower import group_conjugation_rack  # noqa: E402
from ybe_domination.residual import action_permutation  # noqa: E402
from ybe_domination.semigroup_shadows import permutation_order  # noqa: E402


OUT_JSON = ROOT / "proofs" / "framed_to_conjugation_b2_probe.json"
OUT_MD = ROOT / "proofs" / "framed_to_conjugation_b2_probe.md"


def _two_strand_orders(solution) -> dict[str, int]:
    sigma = action_permutation(solution, 2, (1,))
    sigma_squared = action_permutation(solution, 2, (1, 1))
    return {
        "sigma_order": permutation_order(sigma),
        "sigma_squared_order": permutation_order(sigma_squared),
    }


def _conjugation_row(name: str, group) -> dict[str, Any]:
    rack = group_conjugation_rack(group)
    return {
        "name": name,
        "rack_size": len(rack.elements),
        **_two_strand_orders(rack),
    }


def build_report() -> dict[str, Any]:
    framed_c2 = artin_detector_rack(cyclic_group(2), include_trivial_two=False)
    framed_c2_with_trivial = artin_detector_rack(
        cyclic_group(2),
        include_trivial_two=True,
    )
    framed_rows = [
        {
            "name": "A_C2",
            "include_trivial_two": False,
            "rack_size": len(framed_c2.elements),
            **_two_strand_orders(framed_c2),
        },
        {
            "name": "T2 x A_C2",
            "include_trivial_two": True,
            "rack_size": len(framed_c2_with_trivial.elements),
            **_two_strand_orders(framed_c2_with_trivial),
        },
    ]
    conjugation_rows = [
        _conjugation_row("C2^conj", cyclic_group(2)),
        _conjugation_row("S3^conj", symmetric_group(3)),
        _conjugation_row("S4^conj", symmetric_group(4)),
    ]
    framed_order = framed_rows[0]["sigma_order"]
    for row in conjugation_rows:
        row["b2_kernel_subset_framed_c2_kernel"] = (
            row["sigma_order"] % framed_order == 0
        )

    return {
        "title": "Framed-to-conjugation two-strand probe",
        "framed_rows": framed_rows,
        "conjugation_rows": conjugation_rows,
        "s3_b2_kernel_covers_framed_c2": next(
            row["b2_kernel_subset_framed_c2_kernel"]
            for row in conjugation_rows
            if row["name"] == "S3^conj"
        ),
        "proves_higher_arity_conjugation_cover": False,
        "proof_summary": (
            "For B_2, a rack action is determined by the order of sigma_1. "
            "The framed C2 detector A_C2 has sigma_1 order 4.  S3^conj has "
            "sigma_1 order 12, so K_2(S3^conj) is contained in K_2(A_C2). "
            "This is only a two-strand compatibility check; it does not prove "
            "that framed detector racks are dominated by finite conjugation "
            "racks in all arities."
        ),
        "conclusion": (
            "The framed route is compatible with the familiar S3 bridge in "
            "the smallest arity, but a separate framed-to-conjugation cover "
            "lemma is still needed for the finite-group detector route."
        ),
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# {report['title']}",
        "",
        report["conclusion"],
        "",
        "## Summary",
        "",
        report["proof_summary"],
        "",
        "## Framed rows",
        "",
        "| name | size | sigma order | sigma^2 order |",
        "| --- | ---: | ---: | ---: |",
    ]
    for row in report["framed_rows"]:
        lines.append(
            f"| {row['name']} | {row['rack_size']} | {row['sigma_order']} | {row['sigma_squared_order']} |"
        )
    lines.extend(
        [
            "",
            "## Conjugation rows",
            "",
            "| name | size | sigma order | sigma^2 order | B2 kernel subset framed C2 kernel |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
    )
    for row in report["conjugation_rows"]:
        lines.append(
            "| {name} | {size} | {sigma} | {sigma2} | {subset} |".format(
                name=row["name"],
                size=row["rack_size"],
                sigma=row["sigma_order"],
                sigma2=row["sigma_squared_order"],
                subset=row["b2_kernel_subset_framed_c2_kernel"],
            )
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            f"- S3 B2 kernel covers framed C2: `{report['s3_b2_kernel_covers_framed_c2']}`;",
            "- proves higher-arity conjugation cover: "
            f"`{report['proves_higher_arity_conjugation_cover']}`;",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    report = build_report()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")


if __name__ == "__main__":
    main()
