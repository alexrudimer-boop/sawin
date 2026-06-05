from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "proofs" / "size5_6_everywhere_singular_search_plan.json"
OUT_MD = ROOT / "proofs" / "size5_6_everywhere_singular_search_plan.md"


def build_report() -> dict[str, object]:
    return {
        "title": "Size 5/6 everywhere-singular rigid-core search plan",
        "status": (
            "search plan only; no exhaustive size 5 or 6 enumeration has "
            "been run"
        ),
        "target": (
            "Search for or rule out finite bijective YBE tables on 5 and 6 "
            "points that are everywhere singular and survive the current "
            "rigid-core filters before rack-prefix pressure is attempted."
        ),
        "coordinate_model": {
            "labels": "X={0,...,d-1}, with d in {5,6}",
            "arrays": "U[x,y]=L_x(y) and V[x,y]=R_y(x)",
            "table": "r(x,y)=(U[x,y],V[x,y])",
            "bijectivity": (
                "the d^2 output pairs (U[x,y],V[x,y]) are all distinct"
            ),
            "balanced_counts": (
                "bijectivity forces every symbol to occur exactly d times in "
                "U and exactly d times in V"
            ),
            "everywhere_singularity": (
                "every U-row y -> U[x,y] is non-bijective and every V-column "
                "x -> V[x,y] is non-bijective"
            ),
            "pair_orthogonality": (
                "for every u,v, exactly one cell in U^{-1}(u) receives V=v"
            ),
        },
        "ybe_identities": [
            {
                "name": "Y1",
                "identity": (
                    "U[U[x,y], U[V[x,y],z]] = U[x, U[y,z]]"
                ),
                "use": (
                    "before V is assigned, this yields A_xy feasibility via "
                    "L_{U[x,y]} L_v = L_x L_y"
                ),
            },
            {
                "name": "Y2",
                "identity": (
                    "V[U[x,y], U[V[x,y],z]] = "
                    "U[V[x,U[y,z]], V[y,z]]"
                ),
                "use": "propagate during the V exact-cover search",
            },
            {
                "name": "Y3",
                "identity": (
                    "V[V[x,y], z] = V[V[x,U[y,z]], V[y,z]]"
                ),
                "use": "propagate during the V exact-cover search",
            },
        ],
        "stage_a_u_enumeration": {
            "goal": "enumerate canonical U arrays before searching V",
            "preferred_implementation": (
                "enumerate singular row transformations L_x rather than "
                "individual cells; maintain global symbol counts and apply "
                "MF at completed row families"
            ),
            "constraints": [
                "each symbol occurs exactly d times globally in U",
                "each U-row is singular",
                "for each cell (x,y), A_xy is nonempty",
                "the multiset-factorization law holds for every output u",
                "U is canonical under simultaneous relabeling",
            ],
            "feasibility_set": (
                "A_xy={v in X : L_{U[x,y]} o L_v = L_x o L_y}"
            ),
            "multiset_factorization": (
                "for every u, multiset{L_x L_y : L_x(y)=u} equals "
                "multiset{L_u L_v : v in X}"
            ),
            "bucket_checkpoint": (
                "for every (u,P), store cells C(u,P)={(x,y):L_x(y)=u, "
                "L_x L_y=P} and values V(u,P)={v:L_u L_v=P}"
            ),
            "canonicalization": (
                "U^pi[x,y]=pi(U[pi^{-1}x,pi^{-1}y]); keep the "
                "lexicographically minimal word over all d! relabelings"
            ),
            "next_decisive_prompt": (
                "ask whether Stage A already rules out d=5, or request a "
                "certifiable canonical enumeration scheme/count"
            ),
        },
        "stage_b_v_exact_cover": {
            "goal": "assign V after U passes Stage A",
            "variables": "V[x,y] in bucket domain V(U[x,y], L_x L_y)",
            "bucket_variables": (
                "V choices are bucket permutations C(u,P)->V(u,P), not "
                "arbitrary choices from A_xy"
            ),
            "constraints": [
                "(U[x,y],V[x,y]) are all distinct",
                "each V-column is singular",
                "Y2 and Y3 hold",
                "r^2 is not the identity",
            ],
            "branching": (
                "choose a cell minimizing remaining allowed unused values in "
                "its U-fibre"
            ),
        },
        "complete_table_filters": [
            {
                "name": "canonical full table",
                "rule": (
                    "canonicalize r under all simultaneous relabelings before "
                    "expensive filters"
                ),
            },
            {
                "name": "congruence rigidity",
                "rule": (
                    "every congruence generated by a nontrivial pair must be "
                    "universal"
                ),
            },
            {
                "name": "subsolution rigidity",
                "rule": (
                    "reject if any nonempty proper S satisfies "
                    "U[S,S],V[S,S] subset S"
                ),
            },
            {
                "name": "observer rigidity",
                "rule": (
                    "the graph generated by x~U[x,y] and y~V[x,y] must be "
                    "connected"
                ),
            },
            {
                "name": "flip-across exclusion",
                "rule": (
                    "reject partitions A sqcup B with crossing-closed blocks "
                    "and mixed rows equal to flip-across"
                ),
            },
        ],
        "everywhere_singular_filters": [
            {
                "name": "minimal-image filter",
                "rule": (
                    "form S_L and S_R from minimal-size generator images; "
                    "reject if either is nonempty proper crossing-closed"
                ),
            },
            {
                "name": "semigroup-minimal image filter",
                "rule": (
                    "close the transformation semigroups <L_x> and <R_y>; "
                    "test unions of minimal semigroup images for proper "
                    "crossing-closed subsets"
                ),
                "bounds": (
                    "at most d^d transformations: 3125 for d=5 and 46656 "
                    "for d=6"
                ),
            },
            {
                "name": "fibre-pair congruence filter",
                "rule": (
                    "kernel pairs of any singular L_x or R_y must generate "
                    "universal YBE congruences"
                ),
            },
            {
                "name": "kernel-hypergraph connectedness",
                "rule": (
                    "nontrivial fibres of all L_x and R_y form a connected "
                    "hypergraph; disconnected component partitions seed "
                    "observer and congruence checks"
                ),
            },
        ],
        "positive_certificate_search": {
            "position": "run before rack-prefix pressure",
            "certificates": [
                "periodic observer-rack factorization",
                "transport/monodromy rackification",
                "proper active-factor certificates into racks or smaller dominated YBE factors",
            ],
            "suggested_bounds": [
                "periods in {1,2,3,4,6}",
                "output racks of size <=4",
                "observer alphabets of size <=d",
                "state sets of size <=6",
            ],
            "checks": "local two-letter equations plus pair-automaton injectivity",
        },
        "rack_prefix_pressure": {
            "warning": "do not build the product rack P_{<=4} as a set",
            "compression": (
                "represent the detector on the disjoint union "
                "Omega_{<=k,n}=coprod_R R^n over racks R of size <=k"
            ),
            "criterion": (
                "a braid is trivial on the product rack iff it is trivial on "
                "every factor, equivalently on the disjoint-union detector"
            ),
            "joint_group": (
                "Gamma_{<=k,n}(X)=< (D_i^(n), X_i^(n)) : 1<=i<n >"
            ),
            "kernel_test": (
                "N_{<=k,n}(X) is the X-block projection of the kernel of "
                "Gamma_{<=k,n}(X)-><D_i^(n)>"
            ),
            "priority": [
                "P_{<=3}, n<=8",
                "P_{<=4}, n<=5",
                "P_{<=4}, n=6,7 only for structural survivors",
            ],
        },
        "pipeline": [
            "enumerate canonical U arrays",
            "solve V as exact cover with Y2/Y3 propagation",
            "canonicalize completed tables",
            "run rigid-core and everywhere-singular filters",
            "search cheap positive certificates",
            "run compressed rack-prefix pressure only on survivors",
        ],
        "stopping_criteria": [
            "no table survives filters: no everywhere-singular rigid core of that size",
            "all survivors have positive certificates: size-d frontier is handled",
            "survivors without pressure: likely hidden rackification or larger detector needed",
            "survivor with pressure: first serious asymptotic rack-invisibility candidate",
        ],
        "next_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-stage-a-u-array-enumeration_ask_now.md"
        ),
    }


def _bullet_lines(items: list[str]) -> list[str]:
    return [f"- {item};" for item in items]


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Size 5/6 Everywhere-Singular Rigid-Core Search Plan",
        "",
        str(report["target"]),
        "",
        "## Coordinate Model",
        "",
    ]
    for key, value in report["coordinate_model"].items():
        lines.append(f"- {key}: `{value}`;")

    lines.extend(["", "## YBE Identities", ""])
    for row in report["ybe_identities"]:
        lines.extend(
            [
                f"- `{row['name']}`: `{row['identity']}`;",
                f"  use: {row['use']};",
            ]
        )

    stage_a = report["stage_a_u_enumeration"]
    lines.extend(
        [
            "",
            "## Stage A: U Enumeration",
            "",
            f"- goal: `{stage_a['goal']}`;",
            f"- preferred implementation: `{stage_a['preferred_implementation']}`;",
            f"- feasibility set: `{stage_a['feasibility_set']}`;",
            f"- multiset factorization: `{stage_a['multiset_factorization']}`;",
            f"- bucket checkpoint: `{stage_a['bucket_checkpoint']}`;",
            f"- canonicalization: `{stage_a['canonicalization']}`;",
            "",
            "Constraints:",
            "",
        ]
    )
    lines.extend(_bullet_lines(stage_a["constraints"]))
    lines.extend(
        [
            "",
            f"Next decisive prompt: `{stage_a['next_decisive_prompt']}`.",
            "",
            "## Stage B: V Exact Cover",
            "",
        ]
    )
    stage_b = report["stage_b_v_exact_cover"]
    lines.extend(
        [
            f"- goal: `{stage_b['goal']}`;",
            f"- variables: `{stage_b['variables']}`;",
            f"- bucket variables: `{stage_b['bucket_variables']}`;",
            f"- branching: `{stage_b['branching']}`;",
            "",
            "Constraints:",
            "",
        ]
    )
    lines.extend(_bullet_lines(stage_b["constraints"]))

    lines.extend(["", "## Complete Table Filters", ""])
    for row in report["complete_table_filters"]:
        lines.append(f"- `{row['name']}`: {row['rule']};")

    lines.extend(["", "## Everywhere-Singular Filters", ""])
    for row in report["everywhere_singular_filters"]:
        lines.append(f"- `{row['name']}`: {row['rule']};")
        if "bounds" in row:
            lines.append(f"  bounds: {row['bounds']};")

    cert = report["positive_certificate_search"]
    lines.extend(
        [
            "",
            "## Positive Certificate Search",
            "",
            f"- position: `{cert['position']}`;",
            f"- checks: `{cert['checks']}`;",
            "",
            "Certificates:",
            "",
        ]
    )
    lines.extend(_bullet_lines(cert["certificates"]))
    lines.extend(["", "Suggested bounds:", ""])
    lines.extend(_bullet_lines(cert["suggested_bounds"]))

    pressure = report["rack_prefix_pressure"]
    lines.extend(
        [
            "",
            "## Rack-Prefix Pressure",
            "",
            f"- warning: `{pressure['warning']}`;",
            f"- compression: `{pressure['compression']}`;",
            f"- criterion: `{pressure['criterion']}`;",
            f"- joint group: `{pressure['joint_group']}`;",
            f"- kernel test: `{pressure['kernel_test']}`;",
            "",
            "Priority:",
            "",
        ]
    )
    lines.extend(_bullet_lines(pressure["priority"]))

    lines.extend(["", "## Pipeline", ""])
    lines.extend(_bullet_lines(report["pipeline"]))
    lines.extend(["", "## Stopping Criteria", ""])
    lines.extend(_bullet_lines(report["stopping_criteria"]))
    lines.extend(
        [
            "",
            "## Status",
            "",
            str(report["status"]),
            "",
            "## Next Prompt",
            "",
            f"`{report['next_prompt']}`.",
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
