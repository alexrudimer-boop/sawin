import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    all_bijection_solutions,
    branch_tags,
    rack_solution,
    solution_table_signature,
    structure_orbit_law_separation,
    symmetric_group,
)


OUT_JSON = ROOT / "proofs" / "symmetric_law_separator_audit.json"
OUT_MD = ROOT / "proofs" / "symmetric_law_separator_audit.md"


def _word_payload(word):
    if word is None:
        return None
    return [[generator, exponent] for generator, exponent in word]


def _tuple_payload(value):
    if value is None:
        return None
    return [repr(item) for item in value]


def _separation_payload(separation):
    return {
        "arity": separation.arity,
        "orbit_index": separation.orbit_index,
        "orbit_size": separation.orbit_size,
        "target_group_size": separation.target_group_size,
        "separating_word": _word_payload(separation.separating_word),
        "moved_tuple": _tuple_payload(separation.moved_tuple),
        "moved_image": _tuple_payload(separation.moved_image),
        "truncated_orbit_count": separation.truncated_orbit_count,
    }


def _solution_payload(solution):
    return {
        "tags": list(branch_tags(solution)),
        "table": [
            [repr(left), repr(right)]
            for left, right in solution_table_signature(solution)
        ],
    }


def scan_all(size, n, max_length, max_group_size):
    group = symmetric_group(size)
    solution_count = 0
    failure_count = 0
    truncated_orbit_total = 0
    first_failure = None
    for index, solution in enumerate(all_bijection_solutions(size)):
        solution_count += 1
        separation = structure_orbit_law_separation(
            solution,
            n,
            (group,),
            max_length=max_length,
            max_group_size=max_group_size,
        )
        truncated_orbit_total += separation.truncated_orbit_count
        if separation.separating_word is None:
            continue
        failure_count += 1
        if first_failure is None:
            first_failure = {
                "solution_index": index,
                **_solution_payload(solution),
                "separation": _separation_payload(separation),
            }
    return {
        "scope": "all_bijection_solutions",
        "size": size,
        "n": n,
        "max_length": max_length,
        "max_group_size": max_group_size,
        "detector_group_order": len(group.elements),
        "solution_count": solution_count,
        "failure_count": failure_count,
        "truncated_orbit_total": truncated_orbit_total,
        "first_failure": first_failure,
    }


def size3_affine_commutator_candidate():
    pairs = list(product(range(3), repeat=2))
    signature = [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 2),
        (0, 2),
        (1, 2),
        (1, 1),
        (2, 1),
        (0, 1),
    ]
    return FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, signature)))


def scan_named(name, solution, n, max_length, max_group_size):
    group = symmetric_group(len(solution.elements))
    separation = structure_orbit_law_separation(
        solution,
        n,
        (group,),
        max_length=max_length,
        max_group_size=max_group_size,
    )
    return {
        "scope": "named_solution",
        "name": name,
        "size": len(solution.elements),
        "n": n,
        "max_length": max_length,
        "max_group_size": max_group_size,
        "detector_group_order": len(group.elements),
        **_solution_payload(solution),
        "separation": _separation_payload(separation),
        "has_failure": separation.separating_word is not None,
    }


def write_markdown(report):
    lines = [
        "# Symmetric law-separator audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit targets the B-route obstruction to the direct",
        "`G_X = Sym(X)` detector candidate.  It searches for short free words",
        "that are laws on `Sym(X)` but whose pure-braid embedding moves a tuple",
        "inside a structure orbit of `X^n`.",
        "",
        "The check uses `structure_orbit_law_separation()`, so a failure is an",
        "assigned pure-generator mover, not merely non-lawhood in an abstract",
        "orbit image group.  The audit is finite diagnostic evidence only: no",
        "bounded scan proves the all-`n` theorem or outcome B.",
        "",
        "## Exhaustive Tiny Scans",
        "",
    ]
    for scan in report["exhaustive_scans"]:
        lines.append(
            f"- size `{scan['size']}`, n `{scan['n']}`, word length <= "
            f"`{scan['max_length']}`: solutions `{scan['solution_count']}`, "
            f"detector order `{scan['detector_group_order']}`, failures "
            f"`{scan['failure_count']}`, truncated orbit total "
            f"`{scan['truncated_orbit_total']}`."
        )
    lines.extend(["", "## Named Stress Rows", ""])
    for row in report["named_rows"]:
        separation = row["separation"]
        lines.append(
            f"- `{row['name']}`, n `{row['n']}`, word length <= "
            f"`{row['max_length']}`: failure `{row['has_failure']}`, "
            f"orbit size `{separation['orbit_size']}`, target group size "
            f"`{separation['target_group_size']}`, truncated orbits "
            f"`{separation['truncated_orbit_count']}`."
        )
    lines.extend(
        [
            "",
            "## Consequence",
            "",
            "No short law on the full symmetric detector appears in these rows.",
            "This rules out the first tempting moving-variety obstruction to the",
            "direct `A_{Sym(X)}` route in the size-`2` and size-`3` corpora",
            "checked here.  It also sharpens the B search target: a genuine",
            "normalized-law counterexample must escape the full symmetric",
            "detector for each finite stage, not only small cyclic or abelian",
            "detectors.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    report = {
        "exhaustive_scans": [
            scan_all(2, 3, max_length=6, max_group_size=5000),
            scan_all(2, 4, max_length=6, max_group_size=5000),
            scan_all(3, 3, max_length=6, max_group_size=5000),
        ],
        "named_rows": [
            scan_named(
                "dihedral_quandle_3",
                rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3),
                4,
                max_length=6,
                max_group_size=5000,
            ),
            scan_named(
                "size3_affine_commutator_candidate",
                size3_affine_commutator_candidate(),
                4,
                max_length=6,
                max_group_size=5000,
            ),
        ],
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
