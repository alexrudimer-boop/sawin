"""Certificate that the context-signature quotient need not be braided."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    context_signature_core_summary,
    context_signature_quotient_summary,
    contextual_completion_data,
    is_left_nondegenerate,
    is_nondegenerate,
    is_right_nondegenerate,
)

OUT_JSON = ROOT / "proofs" / "context_signature_quotient_failure_certificate.json"
OUT_MD = ROOT / "proofs" / "context_signature_quotient_failure_certificate.md"


def matrix_solution() -> FiniteBraidedSet:
    elements = tuple((base, fibre) for base in (0, 1) for fibre in range(3))
    matrices = {
        (0, 0): ((0, 1), (2, 2)),
        (0, 1): ((0, 1), (2, 0)),
        (1, 0): ((0, 2), (1, 0)),
        (1, 1): ((0, 2), (1, 2)),
    }
    table = {}
    for a, i in elements:
        for b, j in elements:
            matrix = matrices[(a, b)]
            output_first_fibre = (
                matrix[0][0] * i + matrix[0][1] * j
            ) % 3
            output_second_fibre = (
                matrix[1][0] * i + matrix[1][1] * j
            ) % 3
            table[((a, i), (b, j))] = (
                (b, output_first_fibre),
                (a, output_second_fibre),
            )
    return FiniteBraidedSet(elements, table)


def _label(element) -> str:
    base, fibre = element
    return f"{'e' if base == 0 else 'f'}_{fibre}"


def run_certificate() -> dict:
    solution = matrix_solution()
    data = contextual_completion_data(solution)
    summary = context_signature_quotient_summary(solution, data)
    core_summary = context_signature_core_summary(solution, data)
    element_index = data.element_index
    e0 = element_index[(0, 0)]
    f0 = element_index[(1, 0)]
    e1 = element_index[(0, 1)]
    e2 = element_index[(0, 2)]
    signatures_equal = (
        data.m_maps[e0] == data.m_maps[f0]
        and data.r_maps[e0] == data.r_maps[f0]
    )
    e1_e2_signatures_equal = (
        data.m_maps[e1] == data.m_maps[e2]
        and data.r_maps[e1] == data.r_maps[e2]
    )
    r_e0_e1 = solution.R[((0, 0), (0, 1))]
    r_f0_e1 = solution.R[((1, 0), (0, 1))]
    report = {
        "corpus": "six_point_linear_skew_over_flip_context_signature_failure",
        "elements": [_label(element) for element in solution.elements],
        "is_ybe": solution.is_ybe(),
        "left_nondegenerate": is_left_nondegenerate(solution),
        "right_nondegenerate": is_right_nondegenerate(solution),
        "nondegenerate": is_nondegenerate(solution),
        "context_signature_summary": {
            "element_count": summary.element_count,
            "quotient_class_count": summary.quotient_class_count,
            "block_sizes": list(summary.block_sizes),
            "is_braided_congruence": summary.is_braided_congruence,
            "failure": summary.failure,
        },
        "context_signature_core_summary": {
            "element_count": core_summary.element_count,
            "raw_quotient_class_count": core_summary.raw_quotient_class_count,
            "core_class_count": core_summary.core_class_count,
            "raw_block_sizes": list(core_summary.raw_block_sizes),
            "core_block_sizes": list(core_summary.core_block_sizes),
            "refinement_iterations": core_summary.refinement_iterations,
            "is_braided_congruence": core_summary.is_braided_congruence,
            "verification_failure": core_summary.verification_failure,
            "core_is_equality": core_summary.core_is_equality,
            "core_equals_raw_context_quotient": (
                core_summary.core_equals_raw_context_quotient
            ),
        },
        "claimed_equal_signature_pair": ["e_0", "f_0"],
        "claimed_equal_signature_pair_verified": signatures_equal,
        "distinguished_input": ["e_0", "e_1"],
        "comparison_input": ["f_0", "e_1"],
        "R_e0_e1": [_label(element) for element in r_e0_e1],
        "R_f0_e1": [_label(element) for element in r_f0_e1],
        "e1_e2_context_signatures_equal": e1_e2_signatures_equal,
        "all_claimed_checks_passed": (
            solution.is_ybe()
            and is_nondegenerate(solution)
            and signatures_equal
            and not e1_e2_signatures_equal
            and r_e0_e1 == ((0, 1), (0, 2))
            and r_f0_e1 == ((0, 2), (1, 0))
            and not summary.is_braided_congruence
            and core_summary.is_braided_congruence
        ),
    }
    return report


def write_markdown(report: dict) -> str:
    failure = report["context_signature_summary"]["failure"]
    lines = [
        "# Context-Signature Quotient Failure Certificate",
        "",
        "This generated certificate records a six-point linear skew-over-flip",
        "YBE solution for which the relation",
        "",
        "```text",
        "x ~ x' iff (m_x,r_x)=(m_x',r_x')",
        "```",
        "",
        "is not a braided congruence.",
        "",
        "## Checks",
        "",
        f"- YBE: `{report['is_ybe']}`;",
        f"- nondegenerate: `{report['nondegenerate']}`;",
        "- context-signature quotient classes: "
        f"`{report['context_signature_summary']['quotient_class_count']}`;",
        "- context-signature braided congruence: "
        f"`{report['context_signature_summary']['is_braided_congruence']}`;",
        "- context-signature core braided congruence: "
        f"`{report['context_signature_core_summary']['is_braided_congruence']}`;",
        "- context-signature core classes: "
        f"`{report['context_signature_core_summary']['core_class_count']}`;",
        "- `e_0` and `f_0` have equal context signatures: "
        f"`{report['claimed_equal_signature_pair_verified']}`;",
        "- `e_1` and `e_2` have equal context signatures: "
        f"`{report['e1_e2_context_signatures_equal']}`;",
        f"- `R(e_0,e_1)`: `{report['R_e0_e1']}`;",
        f"- `R(f_0,e_1)`: `{report['R_f0_e1']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "## First Congruence Failure",
        "",
        "```json",
        json.dumps(failure, indent=2),
        "```",
        "",
        "## Consequence",
        "",
        "The quotient by equal two-sided context signatures cannot be used as a",
        "universal induction quotient.  This example is nondegenerate, so it is",
        "not a Sawin counterexample, but it kills the proposed canonical",
        "`x -> (m_x,r_x)` quotient route.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_certificate()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("context-signature quotient failure certificate failed")
    print("OK context-signature quotient failure certificate")
    print(f"YBE {report['is_ybe']}")
    print(f"nondegenerate {report['nondegenerate']}")
    print(
        "context-signature congruence "
        f"{report['context_signature_summary']['is_braided_congruence']}"
    )


if __name__ == "__main__":
    main()
