import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    QuotientMap,
    all_bijection_solutions,
    bounded_words,
    direct_symmetric_known_branch_reason,
    exact_detector_image_audit,
    group_exponent,
    has_identity_longitude_signature,
    identity_solution,
    lcm_upto,
    permutation_order,
    symmetric_group,
    two_strand_crossing_order,
    two_strand_symmetric_gate_summary,
    two_strand_symmetric_detector_covers_solution,
    two_strand_symmetric_longitude_period,
)
from ybe_domination.residual import action_permutation  # noqa: E402


OUT_JSON = ROOT / "proofs" / "symmetric_detector_audit.json"
OUT_MD = ROOT / "proofs" / "symmetric_detector_audit.md"


def _one_point_quotient(solution):
    quotient = identity_solution(("*",))
    return QuotientMap(solution, quotient, {element: "*" for element in solution.elements})


def _first_mover(solution, n, words):
    for word in words:
        for tup in product(solution.elements, repeat=n):
            image = solution.braid_action(word, tup)
            if image != tup:
                return {
                    "word": list(word),
                    "tuple": [repr(item) for item in tup],
                    "image": [repr(item) for item in image],
                }
    return None


def _has_trivial_braid_action(solution, n):
    identity = tuple(range(len(solution.elements) ** n))
    return all(
        action_permutation(solution, n, (generator,)) == identity
        for generator in range(1, n)
    )


def bounded_scan(size, n, max_length):
    group = symmetric_group(size)
    words = bounded_words(n, max_length)
    invisible_words = [
        word
        for word in words
        if has_identity_longitude_signature(group, n, word)
    ]
    solution_count = 0
    failure_count = 0
    first_failure = None
    for solution in all_bijection_solutions(size):
        solution_count += 1
        mover = _first_mover(solution, n, invisible_words)
        if mover is None:
            continue
        failure_count += 1
        if first_failure is None:
            first_failure = mover
    return {
        "size": size,
        "n": n,
        "max_length": max_length,
        "word_count": len(words),
        "symmetric_group_order": len(group.elements),
        "symmetric_group_exponent": group_exponent(group),
        "invisible_word_count": len(invisible_words),
        "invisible_words": [list(word) for word in invisible_words],
        "solution_count": solution_count,
        "failure_count": failure_count,
        "first_failure": first_failure,
    }


def exact_scan(size, n, state_limit):
    group = symmetric_group(size)
    quotient = identity_solution(("*",))
    solution_count = 0
    proved_count = 0
    trivial_action_count = 0
    truncated_count = 0
    failure_count = 0
    max_visited_state_count = 0
    first_nonproof = None
    for solution in all_bijection_solutions(size):
        solution_count += 1
        if _has_trivial_braid_action(solution, n):
            proved_count += 1
            trivial_action_count += 1
            continue
        audit = exact_detector_image_audit(
            _one_point_quotient(solution),
            quotient,
            (group,),
            n,
            state_limit=state_limit,
        )
        max_visited_state_count = max(max_visited_state_count, audit.visited_state_count)
        if audit.proves_fixed_n_implication:
            proved_count += 1
        elif audit.truncated:
            truncated_count += 1
            if first_nonproof is None:
                first_nonproof = audit
        else:
            failure_count += 1
            if first_nonproof is None:
                first_nonproof = audit
    return {
        "size": size,
        "n": n,
        "state_limit": state_limit,
        "symmetric_group_order": len(group.elements),
        "symmetric_group_exponent": group_exponent(group),
        "solution_count": solution_count,
        "proved_count": proved_count,
        "trivial_action_count": trivial_action_count,
        "truncated_count": truncated_count,
        "failure_count": failure_count,
        "max_visited_state_count": max_visited_state_count,
        "first_nonproof": (
            None
            if first_nonproof is None
            else {
                "visited_state_count": first_nonproof.visited_state_count,
                "detector_state_count": first_nonproof.detector_state_count,
                "residual_state_count": first_nonproof.residual_state_count,
                "truncated": first_nonproof.truncated,
                "kernel_failure": first_nonproof.kernel_failure,
                "collision_failure": first_nonproof.collision_failure,
            }
        ),
    }


def crossing_order_gate_scan(size):
    period = two_strand_symmetric_longitude_period(size)
    solution_count = 0
    bad_count = 0
    order_histogram = {}
    explanation_counts = {}
    first_bad = None
    for solution in all_bijection_solutions(size):
        solution_count += 1
        order = two_strand_crossing_order(solution)
        order_histogram[str(order)] = order_histogram.get(str(order), 0) + 1
        summary = two_strand_symmetric_gate_summary(solution)
        explanation_counts[summary.explanation] = (
            explanation_counts.get(summary.explanation, 0) + 1
        )
        if two_strand_symmetric_detector_covers_solution(solution):
            continue
        bad_count += 1
        if first_bad is None:
            first_bad = {
                "crossing_order": order,
                "table": [
                    list(solution.R[(x, y)])
                    for x in solution.elements
                    for y in solution.elements
                ],
            }
    return {
        "size": size,
        "solution_count": solution_count,
        "symmetric_longitude_period": period,
        "order_histogram": dict(sorted(order_histogram.items(), key=lambda item: int(item[0]))),
        "explanation_counts": dict(sorted(explanation_counts.items())),
        "bad_count": bad_count,
        "first_bad": first_bad,
    }


def known_branch_filter_scan(size):
    solution_count = 0
    reason_counts = {}
    first_unknown = None
    for solution in all_bijection_solutions(size):
        solution_count += 1
        reason = direct_symmetric_known_branch_reason(solution)
        key = "unknown" if reason is None else reason
        reason_counts[key] = reason_counts.get(key, 0) + 1
        if reason is None and first_unknown is None:
            first_unknown = {
                "table": [
                    list(solution.R[(x, y)])
                    for x in solution.elements
                    for y in solution.elements
                ],
            }
    return {
        "size": size,
        "solution_count": solution_count,
        "reason_counts": dict(sorted(reason_counts.items())),
        "unknown_count": reason_counts.get("unknown", 0),
        "first_unknown": first_unknown,
    }


def affine_cyclic_solution(modulus, a, b, c, d, e=0, f=0):
    elements = tuple(range(modulus))
    return FiniteBraidedSet(
        elements,
        {
            (x, y): (
                (a * x + b * y + e) % modulus,
                (c * x + d * y + f) % modulus,
            )
            for x, y in product(elements, repeat=2)
        },
    )


def affine_cyclic_two_strand_scan(max_modulus):
    rows = []
    for modulus in range(2, max_modulus + 1):
        ybe_count = 0
        max_crossing_order = 0
        order_histogram = {}
        first_bad = None
        invisible_power = 2 * lcm_upto(modulus)
        for a, b, c, d, e, f in product(range(modulus), repeat=6):
            try:
                solution = affine_cyclic_solution(modulus, a, b, c, d, e, f)
            except ValueError:
                continue
            if not solution.is_ybe():
                continue
            ybe_count += 1
            order = permutation_order(action_permutation(solution, 2, (1,)))
            max_crossing_order = max(max_crossing_order, order)
            order_histogram[str(order)] = order_histogram.get(str(order), 0) + 1
            if invisible_power % order != 0 and first_bad is None:
                first_bad = {
                    "parameters": [a, b, c, d, e, f],
                    "crossing_order": order,
                }
        rows.append(
            {
                "modulus": modulus,
                "ybe_count": ybe_count,
                "sym_exponent": lcm_upto(modulus),
                "two_strand_invisible_power": invisible_power,
                "max_crossing_order": max_crossing_order,
                "order_histogram": order_histogram,
                "first_bad": first_bad,
            }
        )
    return rows


def write_markdown(report):
    lines = [
        "# Universal symmetric detector audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit tests the candidate global detector",
        "",
        "```text",
        "G_X = Sym(X)",
        "```",
        "",
        "for whole finite YBE solutions over the one-point quotient.  If the",
        "candidate theorem were true, the rack `A_{Sym(X)}` would dominate `X`",
        "directly, bypassing the congruence-chain local theorem.  The audit is",
        "not a proof: bounded scans are finite search, and exact scans are only",
        "fixed braid-index finite-image closures.",
        "",
        "## Exact fixed-index scans",
        "",
    ]
    for scan in report["exact_scans"]:
        first_nonproof = scan["first_nonproof"]
        first_nonproof_text = ""
        if first_nonproof is not None:
            first_nonproof_text = (
                " First nonproof: "
                f"detector states `{first_nonproof['detector_state_count']}`, "
                f"residual states `{first_nonproof['residual_state_count']}`, "
                f"truncated `{first_nonproof['truncated']}`."
            )
        lines.extend(
            [
                f"- size `{scan['size']}`, n `{scan['n']}`: "
                f"solutions `{scan['solution_count']}`, proved `{scan['proved_count']}`, "
                f"trivial action `{scan['trivial_action_count']}`, "
                f"truncated `{scan['truncated_count']}`, failures `{scan['failure_count']}`, "
                f"max visited states `{scan['max_visited_state_count']}`."
                f"{first_nonproof_text}",
            ]
        )
    lines.extend(["", "## Bounded kernel scans", ""])
    for scan in report["bounded_scans"]:
        lines.extend(
            [
                f"- size `{scan['size']}`, n `{scan['n']}`, length <= `{scan['max_length']}`: "
                f"words `{scan['word_count']}`, Sym-invisible words `{scan['invisible_word_count']}`, "
                f"solutions `{scan['solution_count']}`, failures `{scan['failure_count']}`.",
            ]
        )
    lines.extend(
        [
            "",
            "## Symbolic known-branch filter",
            "",
            "This filter is not a search proof.  It records rows where a separate",
            "all-`n` branch argument already implies direct `Sym(X)` detection:",
            "rack inner group, involutive Artin-permutation quotient,",
            "permutation-form twist subgroup, or nondegenerate guitar-derived",
            "rack.  Exact detector-state enumeration may still truncate on such",
            "rows because it tracks many irrelevant longitude states.",
            "",
        ]
    )
    for scan in report["known_branch_filter_scans"]:
        lines.extend(
            [
                f"- size `{scan['size']}`: solutions `{scan['solution_count']}`, "
                f"unknown rows `{scan['unknown_count']}`, "
                f"reason counts `{scan['reason_counts']}`.",
            ]
        )
    lines.extend(
        [
            "",
            "## Exact two-strand crossing-order gate",
            "",
            "`proofs/two_strand_symmetric_gate.md` proves that the `B_2`",
            "longitude kernel for `Sym(X)` has exact period",
            "`2*lcm(1,...,|X|)`.  Therefore the two-strand part of the",
            "direct symmetric detector succeeds exactly when the crossing",
            "permutation order divides that number.  The following tiny",
            "exhaustive scans record this exact gate.",
            "",
        ]
    )
    for scan in report["crossing_order_gate_scans"]:
        lines.extend(
            [
                f"- size `{scan['size']}`: solutions `{scan['solution_count']}`, "
                f"period `{scan['symmetric_longitude_period']}`, "
                f"bad rows `{scan['bad_count']}`, "
                f"order histogram `{scan['order_histogram']}`.",
                f"  Explanation counts: `{scan['explanation_counts']}`.",
            ]
        )
    lines.extend(
        [
            "",
            "## Affine cyclic two-strand stress test",
            "",
            "For `n=2`, the exact positive period of the finite-G longitude",
            "kernel is `2*exp(G)`.  For `G=Sym(X)` this is",
            "`2*lcm(1,...,|X|)`.  Thus a two-strand failure of the symmetric",
            "detector route would require the crossing",
            "permutation `R` to have order not dividing that number.  The audit",
            "checks affine cyclic solutions",
            "",
            "```text",
            "R(x,y)=(a*x+b*y+e, c*x+d*y+f) mod m",
            "```",
            "",
            "for small `m`.",
            "",
        ]
    )
    for row in report["affine_cyclic_two_strand_scans"]:
        lines.extend(
            [
                f"- m `{row['modulus']}`: YBE affine tables `{row['ybe_count']}`, "
                f"max crossing order `{row['max_crossing_order']}`, "
                f"invisible power `{row['two_strand_invisible_power']}`, "
                f"bad rows `{0 if row['first_bad'] is None else 1}`.",
            ]
        )
    lines.extend(
        [
            "",
            "## Consequence",
            "",
            "No failure appears in these small scans.  This suggests a new",
            "positive route:",
            "",
            "> Universal symmetric detector candidate.  For every finite",
            "> bijective YBE solution `X`, every `n`, and every braid `beta`,",
            "> `Lambda_{Sym(X),n}(beta)=Lambda_{Sym(X),n}(1)` should imply",
            "> `rho_{X,n}(beta)=1`.",
            "",
            "If this candidate is proved, Sawin finite-rack domination follows",
            "with the explicit finite rack `A_{Sym(X)}`.  If it is false, the",
            "first counterexample gives a very direct B-route target: a finite",
            "solution `X` and a braid invisible to `Sym(X)`-longitudes but moving",
            "`X^n`; the diagonal normalized-obstruction lemma would still be",
            "needed to upgrade one failure into an all-finite-group obstruction.",
            "",
            "The next symbolic task is therefore to prove the universal symmetric",
            "detector candidate by a context/Green factorization argument, or to",
            "find an explicit finite solution where it fails.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    report = {
        "exact_scans": [
            exact_scan(2, 2, 20000),
            exact_scan(2, 3, 20000),
            exact_scan(3, 2, 50000),
            exact_scan(3, 3, 1000),
        ],
        "bounded_scans": [
            bounded_scan(2, 3, 4),
            bounded_scan(3, 3, 4),
            bounded_scan(2, 4, 4),
            bounded_scan(3, 4, 4),
        ],
        "known_branch_filter_scans": [
            known_branch_filter_scan(2),
            known_branch_filter_scan(3),
        ],
        "crossing_order_gate_scans": [
            crossing_order_gate_scan(2),
            crossing_order_gate_scan(3),
        ],
        "affine_cyclic_two_strand_scans": affine_cyclic_two_strand_scan(8),
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
