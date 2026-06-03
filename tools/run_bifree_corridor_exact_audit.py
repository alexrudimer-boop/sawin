import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    LocalInterval,
    bifree_corridor_detector_groups,
    bifree_corridor_detector_target,
    bifree_corridor_exact_image_audit,
    bifree_corridor_product_subgroup_audit,
    bifree_corridor_word_certificate,
    commutator,
    cyclic_group,
    free_word_power,
    law_word_on_last_strand,
)


OUT_JSON = ROOT / "proofs" / "bifree_corridor_exact_audit.json"
OUT_MD = ROOT / "proofs" / "bifree_corridor_exact_audit.md"


def interval_from_solution(solution):
    colors = ("*",)
    fibres = {"*": tuple(solution.elements)}
    base_R = {("*", "*"): ("*", "*")}
    table = {
        ("*", "*", x, y): solution.R[(x, y)]
        for x, y in product(solution.elements, repeat=2)
    }
    return LocalInterval(colors, fibres, base_R, table)


def size_three_affine_candidate():
    pairs = [(x, y) for x in range(3) for y in range(3)]
    values = [
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
    return FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, values)))


def _audit_json(audit):
    return {
        "n": audit.n,
        "visited_state_count": audit.visited_state_count,
        "detector_state_count": audit.detector_state_count,
        "residual_state_count": audit.residual_state_count,
        "base_kernel_detector_state_count": audit.base_kernel_detector_state_count,
        "base_kernel_residual_state_count": audit.base_kernel_residual_state_count,
        "truncated": audit.truncated,
        "kernel_failure": None if audit.kernel_failure is None else list(audit.kernel_failure),
        "collision_failure": None
        if audit.collision_failure is None
        else [list(word) for word in audit.collision_failure],
        "proves_fixed_n_implication": audit.proves_fixed_n_implication,
    }


def _product_audit_json(audit):
    return {
        "n": audit.n,
        "braid_word": list(audit.braid_word),
        "factor_names": list(audit.factor_names),
        "factor_orders": list(audit.factor_orders),
        "factor_identity_signatures": list(audit.factor_identity_signatures),
        "all_factor_identity_signatures": audit.all_factor_identity_signatures,
        "product_group_order": audit.product_group_order,
        "truncated": audit.truncated,
        "product_subgroup_size": audit.product_subgroup_size,
        "expected_product_subgroup_size": audit.expected_product_subgroup_size,
        "product_subgroup_equals_factor_product": (
            audit.product_subgroup_equals_factor_product
        ),
        "product_identity_signature": audit.product_identity_signature,
        "product_identity_signature_equivalent": (
            audit.product_identity_signature_equivalent
        ),
    }


def build_report():
    interval = interval_from_solution(size_three_affine_candidate())
    target = bifree_corridor_detector_target(interval)
    groups = bifree_corridor_detector_groups(interval)
    exact_n2 = bifree_corridor_exact_image_audit(interval, n=2, state_limit=1000)
    exact_n2_with_extra_c5 = bifree_corridor_exact_image_audit(
        interval,
        n=2,
        state_limit=1000,
        extra_groups=(cyclic_group(5),),
    )
    product_audit = bifree_corridor_product_subgroup_audit(interval, 2, (1, 1))
    law = commutator(free_word_power(0, 1), free_word_power(1, 1))
    n, braid = law_word_on_last_strand(law, arity=2)
    certificate = bifree_corridor_word_certificate(interval, n, braid)
    report = {
        "scenario": "size_three_affine_commutator_stress_row",
        "target_applies": target.applies,
        "target_verdict": target.summary.verdict,
        "factor_orders": sorted(target.factor_orders),
        "detector_order": target.detector_order,
        "named_factor_orders": {
            name: len(group.elements)
            for name, group in groups.items()
        },
        "exact_n2": _audit_json(exact_n2),
        "exact_n2_with_extra_c5": _audit_json(exact_n2_with_extra_c5),
        "product_subgroup_n2": _product_audit_json(product_audit),
        "commutator_certificate": {
            "n": certificate.n,
            "braid_word": list(certificate.braid_word),
            "quotient_fixed": certificate.quotient_fixed,
            "moves_residual_tuple": certificate.moved_residual_tuple is not None,
            "moved_residual_tuple": None
            if certificate.moved_residual_tuple is None
            else [
                [repr(item) for item in part]
                for part in certificate.moved_residual_tuple
            ],
            "all_listed_factors_invisible": certificate.all_listed_factors_invisible,
            "visible_factor_names": list(certificate.visible_factor_names),
            "is_b_failure_against_listed_factors": certificate.is_b_failure_against_listed_factors,
            "subgroup_profile": [
                {
                    "name": row.name,
                    "group_order": row.group_order,
                    "permutation": list(row.permutation),
                    "generator_count": row.generator_count,
                    "subgroup_size": row.subgroup_size,
                    "identity_longitude_signature": row.identity_longitude_signature,
                }
                for row in certificate.subgroup_profile
            ],
        },
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    exact = report["exact_n2"]
    exact_extra = report["exact_n2_with_extra_c5"]
    product_audit = report["product_subgroup_n2"]
    cert = report["commutator_certificate"]
    lines = [
        "# Bi-free corridor exact audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit records the exact fixed-index image closure for",
        "the bi-free/corridor detector factor list on the standard size-three",
        "affine commutator stress row.  The row is not itself a remaining",
        "corridor target: the local router sends it to an already known branch.",
        "Its role is to test the corridor certificate layer against a row where",
        "actual kernel-image groups are too small but full symmetric",
        "kernel-block factors see the mover.",
        "",
        "## Detector Target",
        "",
        f"Target applies: `{report['target_applies']}`.",
        f"Router verdict: `{report['target_verdict']}`.",
        f"Factor orders: `{report['factor_orders']}`.",
        f"Detector product order: `{report['detector_order']}`.",
        f"Named factor orders: `{report['named_factor_orders']}`.",
        "",
        "## Exact n=2 Closure",
        "",
        f"Visited states: `{exact['visited_state_count']}`.",
        f"Detector states: `{exact['detector_state_count']}`.",
        f"Residual states: `{exact['residual_state_count']}`.",
        f"Base-kernel detector states: `{exact['base_kernel_detector_state_count']}`.",
        f"Base-kernel residual states: `{exact['base_kernel_residual_state_count']}`.",
        f"Truncated: `{exact['truncated']}`.",
        f"Kernel failure: `{exact['kernel_failure']}`.",
        f"Collision failure: `{exact['collision_failure']}`.",
        f"Proves fixed-n implication: `{exact['proves_fixed_n_implication']}`.",
        "",
        "## Exact n=2 Closure With Fixed Extra C5 Factor",
        "",
        "This row appends one fixed extra detector factor `C5`, representing",
        "the quotient/known/unit detector slot in the corridor target.",
        f"Visited states: `{exact_extra['visited_state_count']}`.",
        f"Detector states: `{exact_extra['detector_state_count']}`.",
        (
            "Base-kernel detector states: "
            f"`{exact_extra['base_kernel_detector_state_count']}`."
        ),
        f"Truncated: `{exact_extra['truncated']}`.",
        f"Kernel failure: `{exact_extra['kernel_failure']}`.",
        f"Collision failure: `{exact_extra['collision_failure']}`.",
        (
            "Proves fixed-n implication: "
            f"`{exact_extra['proves_fixed_n_implication']}`."
        ),
        "",
        "## Direct Product Subgroup Check",
        "",
        f"Braid degree: `{product_audit['n']}`.",
        f"Braid word: `{product_audit['braid_word']}`.",
        f"Factor orders: `{product_audit['factor_orders']}`.",
        f"Product group order: `{product_audit['product_group_order']}`.",
        f"Truncated: `{product_audit['truncated']}`.",
        f"Product subgroup size: `{product_audit['product_subgroup_size']}`.",
        (
            "Expected factor-product subgroup size: "
            f"`{product_audit['expected_product_subgroup_size']}`."
        ),
        (
            "Product subgroup equals factor product: "
            f"`{product_audit['product_subgroup_equals_factor_product']}`."
        ),
        (
            "Product identity signature equivalent to all factor identity "
            "signatures: "
            f"`{product_audit['product_identity_signature_equivalent']}`."
        ),
        "",
        "## Commutator Certificate",
        "",
        f"Braid degree: `{cert['n']}`.",
        f"Braid word: `{cert['braid_word']}`.",
        f"Quotient fixed: `{cert['quotient_fixed']}`.",
        f"Moves residual tuple: `{cert['moves_residual_tuple']}`.",
        f"Visible factors: `{cert['visible_factor_names']}`.",
        f"All listed factors invisible: `{cert['all_listed_factors_invisible']}`.",
        (
            "B-shaped failure against listed factors: "
            f"`{cert['is_b_failure_against_listed_factors']}`."
        ),
        "",
        "Subgroup profile:",
        "",
    ]
    for row in cert["subgroup_profile"]:
        lines.append(
            "- "
            f"`{row['name']}` order `{row['group_order']}`, "
            f"subgroup size `{row['subgroup_size']}`, "
            f"identity signature `{row['identity_longitude_signature']}`."
        )
    lines.extend(
        [
            "",
            "## Consequence",
            "",
            "This exact audit does not prove the corridor theorem.  It does make",
            "the fixed-index certificate reusable at the corridor layer: the",
            "same factor list named by `bifree_corridor_detector_target()` can",
            "be fed into exact finite-image closure.  For the affine stress row,",
            "that exact closure proves the `n=2` implication, while the",
            "commutator mover is seen by the order-`6` symmetric factor and is",
            "therefore not a B-shaped failure against the listed detector",
            "factors.  The extra-`C5` row confirms that fixed quotient, known,",
            "or endpoint/unit factors are part of the exact detector state, not",
            "only part of the separate longitude-subgroup profile.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps(report["exact_n2"], sort_keys=True))


if __name__ == "__main__":
    main()
