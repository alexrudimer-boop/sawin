"""Audit contextual completion data for all size-three bijective YBE tables."""

from __future__ import annotations

import json
import sys
import argparse
from collections import Counter
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    branch_tags,
    contextual_completion_data,
    contextual_readout_equivariance_failure,
    identity_extension_summary,
    is_involutive_solution,
    is_nondegenerate,
    solution_table_signature,
)
from ybe_domination.small_search import all_bijection_solutions  # noqa: E402

OUT_JSON = ROOT / "proofs" / "size3_contextual_completion_audit.json"
OUT_MD = ROOT / "proofs" / "size3_contextual_completion_audit.md"


def _classification(solution) -> str:
    if is_nondegenerate(solution):
        return "nondegenerate"
    if is_involutive_solution(solution):
        return "degenerate_involutive"
    return "degenerate_noninvolutive"


def run_audit(max_equivariance_arity: int) -> dict:
    classification_counts = Counter()
    profile_counts = Counter()
    failure_rows = []
    equivariance_failures = []
    sample_rows = []
    solution_count = 0
    max_contextual_class_count = 0

    for solution_index, solution in enumerate(all_bijection_solutions(3)):
        solution_count += 1
        classification = _classification(solution)
        classification_counts[classification] += 1
        data = contextual_completion_data(solution)
        summary = identity_extension_summary(data)
        max_contextual_class_count = max(
            max_contextual_class_count,
            summary.class_count,
        )
        profile_key = (
            classification,
            summary.left_monoid_size,
            summary.right_monoid_size,
            summary.class_count,
            summary.forced_product_count,
            summary.domain_sizes,
            summary.conflict_count,
            summary.partial_translations_injective,
            summary.balanced_domains,
            summary.identity_extension_total_permutations,
            summary.identity_extension_conjugacy_covariance,
            summary.full_forced_graph_local_covariance_failures,
            summary.nontrivial_left_translation_count,
        )
        profile_counts[profile_key] += 1
        row = {
            "solution_index": solution_index,
            "classification": classification,
            "branch_tags": list(branch_tags(solution)),
            "summary": asdict(summary),
            "table_signature": [list(pair) for pair in solution_table_signature(solution)],
        }
        if len(sample_rows) < 10:
            sample_rows.append(row)
        if not (
            summary.conflict_count == 0
            and summary.partial_translations_injective
            and summary.balanced_domains
            and summary.identity_extension_total_permutations
            and summary.identity_extension_conjugacy_covariance
            and summary.full_forced_graph_local_covariance_failures == 0
        ):
            failure_rows.append(row)
        else:
            equivariance_checks = []
            for arity in range(1, max_equivariance_arity + 1):
                result = contextual_readout_equivariance_failure(solution, data, arity)
                equivariance_checks.append(result)
                if result.get("failure") is not None:
                    equivariance_failures.append(
                        {
                            "row": row,
                            "result": result,
                        }
                    )
                    break
            row["equivariance_checks"] = equivariance_checks

    profiles = [
        {
            "case_count": count,
            "classification": key[0],
            "left_monoid_size": key[1],
            "right_monoid_size": key[2],
            "contextual_class_count": key[3],
            "forced_product_count": key[4],
            "domain_sizes": list(key[5]),
            "conflict_count": key[6],
            "partial_translations_injective": key[7],
            "balanced_domains": key[8],
            "identity_extension_total_permutations": key[9],
            "identity_extension_conjugacy_covariance": key[10],
            "full_forced_graph_local_covariance_failures": key[11],
            "nontrivial_left_translation_count": key[12],
        }
        for key, count in sorted(
            profile_counts.items(),
            key=lambda item: (-item[1], item[0]),
        )
    ]
    report = {
        "corpus": "all_size3_bijective_ybe_tables",
        "solution_count": solution_count,
        "expected_solution_count": 73,
        "classification_counts": dict(sorted(classification_counts.items())),
        "profile_count": len(profiles),
        "profiles": profiles,
        "max_contextual_class_count": max_contextual_class_count,
        "max_equivariance_arity": max_equivariance_arity,
        "failure_count": len(failure_rows),
        "failures": failure_rows[:8],
        "equivariance_failure_count": len(equivariance_failures),
        "equivariance_failures": equivariance_failures[:8],
        "sample_rows": sample_rows,
        "all_claimed_checks_passed": (
            solution_count == 73
            and classification_counts["nondegenerate"] == 66
            and classification_counts["degenerate_involutive"] == 7
            and classification_counts["degenerate_noninvolutive"] == 0
            and not failure_rows
            and not equivariance_failures
        ),
    }
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Size-3 Contextual Completion Audit",
        "",
        "This generated audit enumerates every bijective YBE table on a",
        "three-point set and applies the generic two-sided contextual",
        "completion helper.",
        "",
        "## Summary",
        "",
        f"- YBE solutions: `{report['solution_count']}`;",
        f"- classification counts: `{report['classification_counts']}`;",
        "- maximum contextual quotient size: "
        f"`{report['max_contextual_class_count']}`;",
        "- identity-extension equivariance checked through arity: "
        f"`{report['max_equivariance_arity']}`;",
        f"- contextual profile count: `{report['profile_count']}`;",
        f"- failure count: `{report['failure_count']}`;",
        f"- equivariance failure count: `{report['equivariance_failure_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "The corpus has no degenerate non-involutive rows.  It is therefore not",
        "a hard-case corpus, but it verifies that the generic contextual code",
        "agrees with the expected smallest complete classification and finds no",
        "active-lift or identity-extension obstruction.",
        "",
        "## Checked Conditions",
        "",
        "For every size-three YBE table the audit checks:",
        "",
        "```text",
        "forced products have no representative-independence conflicts;",
        "forced partial translations are injective;",
        "lambda_p(D_p)=D_p for every contextual class p;",
        "identity-outside extensions are total permutations;",
        "L_{L_p(q)}=L_p L_q L_p^{-1} for every p,q;",
        "the full forced graph has no local covariance failures;",
        "J_n rho^X = rho^P J_n in every checked arity.",
        "```",
        "",
        "## Profiles",
        "",
        "| cases | class | M_L | M_R | P | forced | domains | nontriv L |",
        "|---:|---|---:|---:|---:|---:|---|---:|",
    ]
    for row in report["profiles"]:
        lines.append(
            "| {case_count} | {classification} | {left_monoid_size} | "
            "{right_monoid_size} | {contextual_class_count} | "
            "{forced_product_count} | {domain_sizes} | "
            "{nontrivial_left_translation_count} |".format(**row)
        )
    if report["failures"] or report["equivariance_failures"]:
        lines.extend(["", "## Failures", "", "```json"])
        lines.append(
            json.dumps(
                {
                    "contextual": report["failures"],
                    "equivariance": report["equivariance_failures"],
                },
                indent=2,
            )
        )
        lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-equivariance-arity", type=int, default=5)
    args = parser.parse_args()
    report = run_audit(args.max_equivariance_arity)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("size-three contextual completion audit failed")
    print("OK size-three contextual completion audit")
    print(f"YBE solutions {report['solution_count']}")
    print(f"classification {report['classification_counts']}")
    print(f"max contextual quotient {report['max_contextual_class_count']}")
    print(f"equivariance through arity {report['max_equivariance_arity']}")


if __name__ == "__main__":
    main()
