from __future__ import annotations

import json
import sys
from collections import Counter
from itertools import product
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    InvariantTransducer,
    MealyTransducer,
    active_factor_certificate_audit,
    all_bijection_solutions,
    branch_tags,
    cyclic_group,
    direct_symmetric_known_branch_reason,
    flip_disjoint_union_solution,
    identity_solution,
    is_involutive_solution,
    known_branch_detector_certificate,
    multi_active_factor_certificate_audit,
    rack_solution,
    terminal_branch_triage_audit,
    transducer_rackification_audit,
)

OUT_JSON = ROOT / "proofs" / "sequential_primitivity_frontier_audit.json"
OUT_MD = ROOT / "proofs" / "sequential_primitivity_frontier_audit.md"


def affine_f2_type_a_solution() -> FiniteBraidedSet:
    elements = tuple(product((0, 1), repeat=2))
    table = {}
    for a, b in elements:
        for c, d in elements:
            table[((a, b), (c, d))] = (
                (d, (a + b + d) % 2),
                ((a + c + d + 1) % 2, (a + 1) % 2),
            )
    return FiniteBraidedSet(elements, table)


def affine_type_a_transducers(solution: FiniteBraidedSet) -> tuple[
    MealyTransducer,
    InvariantTransducer,
]:
    states = (("start", 0), ("seen", 0), ("seen", 1))
    rack_delta = {}
    rack_omega = {}
    inv_delta = {}
    inv_nu = {}
    for state in states:
        for letter in solution.elements:
            a, b = letter
            parity = (a + b) % 2
            kind, offset = state
            if kind == "start":
                current_offset = 0
                next_state = ("seen", 0)
            else:
                current_offset = (offset + parity + 1) % 2
                next_state = ("seen", current_offset)
            rack_delta[(state, letter)] = next_state
            rack_omega[(state, letter)] = (a + current_offset) % 2
            inv_delta[(state, letter)] = state
            inv_nu[(state, letter)] = parity
    return (
        MealyTransducer(states, ("start", 0), rack_delta, rack_omega),
        InvariantTransducer(states, ("start", 0), inv_delta, inv_nu),
    )


def permutation_solution_with_toggle() -> FiniteBraidedSet:
    elements = (0, 1)
    return FiniteBraidedSet(
        elements,
        {(left, right): (right, 1 - left) for left in elements for right in elements},
    )


def one_state_transducer(solution: FiniteBraidedSet, output_map) -> MealyTransducer:
    state = "q"
    delta = {}
    omega = {}
    for letter in solution.elements:
        delta[(state, letter)] = state
        omega[(state, letter)] = output_map[letter]
    return MealyTransducer((state,), state, delta, omega)


def affine_f2_hidden_cyclic_solution() -> FiniteBraidedSet:
    elements = tuple(product((0, 1), repeat=3))
    table = {}
    for a, z1, z2 in elements:
        for b, w1, w2 in elements:
            table[((a, z1, z2), (b, w1, w2))] = (
                (a, w2, w1),
                (b, (z2 + 1) % 2, (z1 + 1) % 2),
            )
    return FiniteBraidedSet(elements, table)


def affine_f2_hidden_cyclic_transducers(solution: FiniteBraidedSet) -> tuple[
    MealyTransducer,
    InvariantTransducer,
]:
    states = (0, 1)
    rack_delta = {}
    rack_omega = {}
    inv_delta = {}
    inv_nu = {}
    for state in states:
        for letter in solution.elements:
            a, z1, z2 = letter
            rack_delta[(state, letter)] = 1 - state
            if state == 0:
                rack_omega[(state, letter)] = (z1, z2)
            else:
                rack_omega[(state, letter)] = ((z2 + 1) % 2, (z1 + 1) % 2)
            inv_delta[(state, letter)] = state
            inv_nu[(state, letter)] = a
    return (
        MealyTransducer(states, 0, rack_delta, rack_omega),
        InvariantTransducer(states, 0, inv_delta, inv_nu),
    )


def size_three_terminal_corpus_report() -> dict:
    reason_counter: Counter[str] = Counter()
    tag_counter: Counter[str] = Counter()
    candidate_signatures = []
    solution_count = 0
    for solution in all_bijection_solutions(3):
        solution_count += 1
        certificate = known_branch_detector_certificate(solution)
        reason = None if certificate is None else certificate.reason
        reason_counter[str(reason)] += 1
        tag_counter["+".join(branch_tags(solution)) or "(untagged)"] += 1
        if certificate is None:
            candidate_signatures.append(repr(tuple(solution.R.items())))
    return {
        "name": "exhaustive_size_3_corpus",
        "solution_count": solution_count,
        "known_branch_count": solution_count - len(candidate_signatures),
        "candidate_count": len(candidate_signatures),
        "known_branch_reasons": dict(sorted(reason_counter.items())),
        "branch_tag_counts": dict(sorted(tag_counter.items())),
        "candidate_signatures": candidate_signatures[:5],
        "exact_exhaustive": True,
        "conclusion": "no size-3 sequential-primitivity candidate",
    }


def type_a_certificate_report() -> dict:
    solution = affine_f2_type_a_solution()
    quotient = identity_solution(("z",))
    quotient_map = {element: "z" for element in solution.elements}
    cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)
    rack_transducer, invariant_transducer = affine_type_a_transducers(solution)
    audit = transducer_rackification_audit(
        solution,
        quotient,
        quotient_map,
        cyclic,
        rack_transducer,
        invariant_transducer,
    )
    triage = terminal_branch_triage_audit(solution)
    return {
        "name": "size4_affine_type_a",
        "solution_size": len(solution.elements),
        "ybe": solution.is_ybe(),
        "involutive": is_involutive_solution(solution),
        "has_point_separating_proper_quotients": (
            triage.has_point_separating_proper_quotients
        ),
        "has_nontrivial_one_state_observer": triage.has_nontrivial_one_state_observer,
        "has_subsolution_fibre_congruence": triage.has_subsolution_fibre_congruence,
        "certificate_kind": "sequential cyclic rack gauge plus parity observer",
        "finite_conditions_hold": audit.finite_conditions_hold,
        "injectivity_witness": None
        if audit.injectivity_witness is None
        else repr(audit.injectivity_witness),
        "candidate": not audit.finite_conditions_hold,
    }


def type_b_certificate_report() -> dict:
    trivial = identity_solution((0, 1))
    toggle = permutation_solution_with_toggle()
    target = flip_disjoint_union_solution(trivial, toggle, "T", "P")
    dummy = identity_solution(("dummy",))
    trivial_factor = flip_disjoint_union_solution(trivial, dummy, "T", "D")
    toggle_factor = flip_disjoint_union_solution(dummy, toggle, "D", "P")
    trivial_map = {}
    toggle_map = {}
    for tag, value in target.elements:
        if tag == "T":
            trivial_map[(tag, value)] = ("T", value)
            toggle_map[(tag, value)] = ("D", "dummy")
        else:
            trivial_map[(tag, value)] = ("D", "dummy")
            toggle_map[(tag, value)] = ("P", value)
    audit = multi_active_factor_certificate_audit(
        target,
        (
            (trivial_factor, one_state_transducer(target, trivial_map)),
            (toggle_factor, one_state_transducer(target, toggle_map)),
        ),
    )
    triage = terminal_branch_triage_audit(target)
    return {
        "name": "size4_type_b_flip_across",
        "solution_size": len(target.elements),
        "ybe": target.is_ybe(),
        "involutive": is_involutive_solution(target),
        "has_point_separating_proper_quotients": (
            triage.has_point_separating_proper_quotients
        ),
        "has_flip_across_decomposition": triage.has_flip_across_decomposition,
        "certificate_kind": "two proper active quotient factors",
        "proper_factor_sizes": (len(trivial_factor.elements), len(toggle_factor.elements)),
        "finite_conditions_hold": audit.finite_conditions_hold,
        "injectivity_witness": None
        if audit.injectivity_witness is None
        else repr(audit.injectivity_witness),
        "candidate": not audit.finite_conditions_hold,
    }


def affine_f2_hidden_cyclic_report() -> dict:
    solution = affine_f2_hidden_cyclic_solution()
    fibre = tuple(product((0, 1), repeat=2))
    constant_action = rack_solution(
        fibre,
        lambda _left, right: ((right[0] + 1) % 2, (right[1] + 1) % 2),
    )
    rack_transducer, invariant_transducer = affine_f2_hidden_cyclic_transducers(
        solution
    )
    audit = active_factor_certificate_audit(
        solution,
        constant_action,
        rack_transducer,
        invariant_transducer,
    )
    return {
        "name": "affine_f2_hidden_cyclic_pressure_row",
        "solution_size": len(solution.elements),
        "ybe": solution.is_ybe(),
        "known_branch_reason": direct_symmetric_known_branch_reason(solution),
        "certificate_kind": "two-state hidden cyclic rack gauge plus inert observer",
        "active_factor_size": len(constant_action.elements),
        "detector_group_order": len(cyclic_group(2).elements),
        "finite_conditions_hold": audit.finite_conditions_hold,
        "injectivity_witness": None
        if audit.injectivity_witness is None
        else repr(audit.injectivity_witness),
        "candidate": not audit.finite_conditions_hold,
    }


def build_report() -> dict:
    representatives = (
        type_a_certificate_report(),
        type_b_certificate_report(),
        affine_f2_hidden_cyclic_report(),
    )
    candidate_rows = [row for row in representatives if row["candidate"]]
    return {
        "title": "Sequential-primitivity frontier audit",
        "size_3": size_three_terminal_corpus_report(),
        "representatives": representatives,
        "representative_candidate_count": len(candidate_rows),
        "candidate_names": [row["name"] for row in candidate_rows],
        "conclusion": (
            "The exhaustive size-3 corpus has no sequential-primitivity "
            "candidate, and the current size-4/affine pressure representatives "
            "are closed by explicit active-factor or sequential rack "
            "certificates. The next falsifiable search frontier starts at "
            "larger nonterminal tables, for example size 5 or structured "
            "affine-linear families beyond the hidden cyclic gauge."
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Sequential-Primitivity Frontier Audit",
        "",
        "This generated audit packages the current finite evidence around the",
        "sequential-primitivity obstruction.  It is exact for the size-three",
        "whole-table corpus and certificate-based for the named pressure",
        "representatives.  It is not a proof of Sawin's problem.",
        "",
        "## Size 3 Corpus",
        "",
    ]
    size3 = report["size_3"]
    lines.extend(
        [
            f"- exhaustive: `{size3['exact_exhaustive']}`;",
            f"- YBE solution count: `{size3['solution_count']}`;",
            f"- known branch count: `{size3['known_branch_count']}`;",
            f"- candidate count: `{size3['candidate_count']}`;",
            f"- known branch reasons: `{size3['known_branch_reasons']}`;",
            f"- conclusion: `{size3['conclusion']}`.",
            "",
            "## Pressure Representatives",
            "",
        ]
    )
    for row in report["representatives"]:
        lines.extend(
            [
                f"### {row['name']}",
                "",
                f"- solution size: `{row['solution_size']}`;",
                f"- YBE: `{row['ybe']}`;",
                f"- certificate kind: `{row['certificate_kind']}`;",
                f"- finite conditions hold: `{row['finite_conditions_hold']}`;",
                f"- injectivity witness: `{row['injectivity_witness']}`;",
                f"- remains candidate: `{row['candidate']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Conclusion",
            "",
            f"- representative candidate count: `{report['representative_candidate_count']}`;",
            f"- candidate names: `{report['candidate_names']}`;",
            "",
            report["conclusion"],
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    if argv not in (None, ()):
        raise SystemExit("no arguments are supported")
    report = build_report()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
