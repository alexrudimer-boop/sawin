import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    adjacent_two_body_realization_audit,
    braid_locality_shadow_audit,
    cyclic_group,
    labeled_permutation_braid_audit,
    rees_rectangle_cocycle,
    rees_rectangle_cocycle_audit,
)


OUT_JSON = ROOT / "proofs" / "rees_braid_cocycle_obstruction_audit.json"
OUT_MD = ROOT / "proofs" / "rees_braid_cocycle_obstruction_audit.md"


def _pattern_data():
    group = cyclic_group(2)
    rows = ("lambda0", "lambda1")
    columns = ("i0", "i1")
    sandwich = {
        ("lambda0", "i0"): 0,
        ("lambda0", "i1"): 0,
        ("lambda1", "i0"): 0,
        ("lambda1", "i1"): 1,
    }
    states = ("q00", "q01", "q10", "q11")
    row1 = {
        "q00": "q10",
        "q01": "q11",
        "q10": "q01",
        "q11": "q00",
    }
    row2 = {
        "q00": "q01",
        "q01": "q10",
        "q10": "q11",
        "q11": "q00",
    }
    labels1 = {"q00": 0, "q01": 0, "q10": 0, "q11": 1}
    labels2 = {"q00": 0, "q01": 0, "q10": 1, "q11": 0}
    return group, rows, columns, sandwich, states, row1, labels1, row2, labels2


def build_report():
    (
        group,
        rows,
        columns,
        sandwich,
        states,
        row1,
        labels1,
        row2,
        labels2,
    ) = _pattern_data()
    omega = rees_rectangle_cocycle(
        group, sandwich, "lambda0", "lambda1", "i0", "i1"
    )
    rectangle_audit = rees_rectangle_cocycle_audit(group, rows, columns, sandwich)
    braid_audit = labeled_permutation_braid_audit(
        group,
        states,
        row1,
        labels1,
        row2,
        labels2,
    )
    locality_audit = braid_locality_shadow_audit(states, row1, row2)
    direct_states = ("00", "01", "10", "11")
    direct_row1 = {"00": "10", "10": "00", "01": "11", "11": "01"}
    direct_row2 = {"00": "01", "01": "00", "10": "11", "11": "10"}
    direct_locality_audit = braid_locality_shadow_audit(
        direct_states,
        direct_row1,
        direct_row2,
    )
    adjacent_audit = adjacent_two_body_realization_audit(
        states,
        row1,
        row2,
        basis_size=2,
        require_ybe=False,
    )
    adjacent_ybe_audit = adjacent_two_body_realization_audit(
        states,
        row1,
        row2,
        basis_size=2,
    )
    report = {
        "description": (
            "Small C2 Rees braid-cocycle obstruction pattern: nonflat "
            "sandwich rectangle plus braid-compatible labeled quotient rows."
        ),
        "group": "C2_additive_0_identity_1_nonidentity",
        "states": states,
        "row1": row1,
        "row1_labels": labels1,
        "row2": row2,
        "row2_labels": labels2,
        "distinguished_rectangle_omega": omega,
        "rectangle_audit": {
            **asdict(rectangle_audit),
            "is_flat": rectangle_audit.is_flat,
            "rectangle_cocycles_are_trivial": (
                rectangle_audit.rectangle_cocycles_are_trivial
            ),
            "sandwich_is_row_column_coboundary": (
                rectangle_audit.sandwich_is_row_column_coboundary
            ),
        },
        "braid_audit": {
            **asdict(braid_audit),
            "beta_has_constant_label": braid_audit.beta_has_constant_label,
            "beta_constant_label": braid_audit.beta_constant_label,
            "beta_constant_label_is_nontrivial": (
                braid_audit.beta_constant_label_is_nontrivial
            ),
            "verifies_closed_nontrivial_braid_holonomy": (
                braid_audit.verifies_closed_nontrivial_braid_holonomy
            ),
        },
        "locality_shadow_audit": {
            **asdict(locality_audit),
            "direct_coordinate_shadow_possible": (
                locality_audit.direct_coordinate_shadow_possible
            ),
        },
        "direct_coordinate_control_audit": {
            **asdict(direct_locality_audit),
            "direct_coordinate_shadow_possible": (
                direct_locality_audit.direct_coordinate_shadow_possible
            ),
        },
        "adjacent_two_body_audit": asdict(adjacent_audit),
        "adjacent_two_body_ybe_audit": asdict(adjacent_ybe_audit),
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    rectangle = report["rectangle_audit"]
    braid = report["braid_audit"]
    locality = report["locality_shadow_audit"]
    direct_locality = report["direct_coordinate_control_audit"]
    adjacent = report["adjacent_two_body_audit"]
    adjacent_ybe = report["adjacent_two_body_ybe_audit"]
    lines = [
        "# Rees braid-cocycle obstruction audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the smallest finite pattern currently",
        "suggested by the Rees-flatness pressure test.  It is not claimed to",
        "be an actual finite bijective YBE solution.  It is a finite local",
        "quotient-row pattern that satisfies the braid relation while keeping",
        "a nontrivial Rees rectangle cocycle.",
        "",
        "The group is `C2`, written additively as `0` for the identity and",
        "`1` for the nonidentity element.",
        "",
        "## Rees Rectangle",
        "",
        "The sandwich matrix is",
        "",
        "```text",
        "          i0  i1",
        "lambda0   0   0",
        "lambda1   0   1",
        "```",
        "",
        f"- distinguished rectangle omega: `{report['distinguished_rectangle_omega']}`;",
        f"- rectangle failure count: `{rectangle['rectangle_failure_count']}`;",
        f"- coboundary failure count: `{rectangle['coboundary_failure_count']}`;",
        f"- rectangle cocycles are trivial: `{rectangle['rectangle_cocycles_are_trivial']}`;",
        f"- sandwich is row-column coboundary: `{rectangle['sandwich_is_row_column_coboundary']}`;",
        f"- is flat: `{rectangle['is_flat']}`.",
        "",
        "## Labeled Braid Rows",
        "",
        "States are `q00, q01, q10, q11`.  The two quotient rows are",
        "",
        "```text",
        "q        q00  q01  q10  q11",
        "s1(q)    q10  q11  q01  q00",
        "ell1(q)  0    0    0    1",
        "s2(q)    q01  q10  q11  q00",
        "ell2(q)  0    0    1    0",
        "```",
        "",
        "A row `(s, ell)` acts on `Omega x C2` by",
        "",
        "```text",
        "(q,g) |-> (s(q), g + ell(q)).",
        "```",
        "",
        f"- quotient braid relation holds: `{braid['quotient_braid_relation_holds']}`;",
        f"- labeled braid relation holds: `{braid['braid_relation_holds']}`;",
        f"- beta word: `{tuple(braid['beta_word'])}`;",
        f"- beta is quotient-closed: `{braid['beta_is_quotient_closed']}`;",
        f"- beta distinct labels: `{tuple(braid['beta_distinct_labels'])}`;",
        f"- beta constant label: `{braid['beta_constant_label']}`;",
        (
            "- verifies closed nontrivial braid holonomy: "
            f"`{braid['verifies_closed_nontrivial_braid_holonomy']}`."
        ),
        "",
        "The beta state images are:",
        "",
        "```text",
    ]
    for source, target, label in braid["beta_state_images"]:
        lines.append(f"{source} -> ({target}, {label})")
    lines.extend(
        [
            "```",
            "",
            "## Consequence",
            "",
            "The local braid/YBE relation only checks a braid cocycle identity",
            "for the labels.  This audit shows that such an identity can hold",
            "while the Rees rectangle cocycle is still nontrivial.  Therefore",
            "a positive finite-rack-domination route needs an additional",
            "realization or flatness lemma: actual finite bijective YBE local",
            "quotient-fibre intervals must either avoid this pattern or force",
            "it into a bounded vertical coboundary.",
            "",
            "## Direct Locality Shadow",
            "",
            "A literal three-strand set-theoretic action has coordinate-local",
            "partitions: `sigma1` preserves the third-coordinate fibres, and",
            "`sigma2` preserves the first-coordinate fibres.  The locality",
            "shadow audit asks whether the two quotient rows have nontrivial",
            "fixed partitions which jointly separate the four states.",
            "",
            "For a direct `2 x 2` coordinate model, the control audit records:",
            "",
            (
                "- direct coordinate shadow possible: "
                f"`{direct_locality['direct_coordinate_shadow_possible']}`;"
            ),
            (
                "- jointly separating fixed pair count: "
                f"`{direct_locality['jointly_separating_fixed_pair_count']}`."
            ),
            "",
            "For the nonflat obstruction rows, the locality audit records:",
            "",
            f"- row 1 cycle lengths: `{tuple(locality['row1_cycle_lengths'])}`;",
            f"- row 2 cycle lengths: `{tuple(locality['row2_cycle_lengths'])}`;",
            (
                "- row 1 has a nontrivial fixed partition: "
                f"`{locality['row1_has_nontrivial_fixed_partition']}`;"
            ),
            (
                "- row 2 has a nontrivial fixed partition: "
                f"`{locality['row2_has_nontrivial_fixed_partition']}`;"
            ),
            (
                "- direct coordinate shadow possible: "
                f"`{locality['direct_coordinate_shadow_possible']}`."
            ),
            "",
            "Thus this four-state obstruction cannot be used as a literal",
            "visible coordinate-local quotient for a three-strand YBE action.",
            "A genuine realization would have to occur deeper inside a",
            "quotient-fibre interval where the outside-coordinate partitions",
            "have already been collapsed or transported.",
            "",
            "## Adjacent Two-Body Search",
            "",
            "A still stronger direct-realization check asks whether there is a",
            "single bijection `R: A^2 -> A^2`, with `|A|=2`, and an embedding",
            "of the four quotient states into `A^3`, such that `R` on adjacent",
            "coordinates induces both rows.  This search is exhaustive for",
            "two-element `A`.",
            "",
            (
                "- without requiring global YBE for `R`, realization found: "
                f"`{adjacent['realization_found']}`;"
            ),
            (
                "- pair bijections checked: "
                f"`{adjacent['checked_pair_bijection_count']}` of "
                f"`{adjacent['pair_bijection_count']}`;"
            ),
            (
                "- embeddings checked: "
                f"`{adjacent['checked_embedding_count']}` total "
                f"(`{adjacent['candidate_embedding_count']}` candidates per pair map);"
            ),
            (
                "- requiring `R` to satisfy YBE on all of `A^3`, realization found: "
                f"`{adjacent_ybe['realization_found']}`."
            ),
            "",
            "Thus the four-state pattern is not directly induced by any",
            "two-element adjacent binary bijection, even before imposing YBE",
            "on that binary map.  This again pushes any possible realization",
            "into a more hidden quotient-fibre interval.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps(report["braid_audit"], sort_keys=True))


if __name__ == "__main__":
    main()
