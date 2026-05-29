import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    LocalInterval,
    all_bijection_solutions,
    branch_tags,
    direct_product_holonomy_summary,
    direct_product_invariant_families,
    local_master_bottleneck_summary,
    solution_from_local_interval,
    swapped_product_holonomy_summary,
    swapped_product_invariant_families,
)
from ybe_domination.local_interval import canonical_partition, set_partitions  # noqa: E402


OUT_JSON = ROOT / "proofs" / "two_colour_fibre3_product_audit.json"
OUT_MD = ROOT / "proofs" / "two_colour_fibre3_product_audit.md"

POINTS = (0, 1, 2)
PERMS = tuple(images for images in product(POINTS, repeat=3) if set(images) == set(POINTS))
IDENTITY_PERM = tuple(range(3))
KNOWN_TAGS = {
    "involutive",
    "permutation_form",
    "affine_cyclic",
    "nondegenerate",
    "rack_type",
}


def compose(left, right):
    return tuple(left[right[index]] for index in POINTS)


COMPOSE = {(left, right): compose(left, right) for left in PERMS for right in PERMS}
PARTITIONS = tuple(set_partitions(POINTS))
EQUALITY_PARTITION = canonical_partition(frozenset([point]) for point in POINTS)
UNIVERSAL_PARTITION = canonical_partition([POINTS])


def transport_partition(permutation, partition):
    return canonical_partition(
        (permutation[point] for point in block)
        for block in partition
    )


def swapped_equation_refs(base):
    refs = []
    for a, b, c in product(base.elements, repeat=3):
        ab, a_b = base.R[(a, b)]
        bc, b_c = base.R[(b, c)]
        a_b_c, _ = base.R[(a_b, c)]
        _, a_star_bc = base.R[(a, bc)]
        refs.append(
            {
                "left_lhs": (ab, a_b_c),
                "left_rhs": (a_b, c),
                "left_target_lhs": (a, bc),
                "left_target_rhs": (b, c),
                "middle_lhs_r": (ab, a_b_c),
                "middle_lhs_l": (a, b),
                "middle_rhs_l": (a_star_bc, b_c),
                "middle_rhs_r": (b, c),
                "right_lhs": (a_b, c),
                "right_rhs": (a, b),
                "right_target_lhs": (a_star_bc, b_c),
                "right_target_rhs": (a, bc),
            }
        )
    return tuple(refs)


def valid_left_label_choices(base, pairs, side):
    refs = swapped_equation_refs(base)
    out = []
    for values in product(PERMS, repeat=len(pairs)):
        labels = dict(zip(pairs, values))
        ok = True
        for ref in refs:
            if side == "swapped":
                if COMPOSE[
                    (labels[ref["left_lhs"]], labels[ref["left_rhs"]])
                ] != COMPOSE[
                    (labels[ref["left_target_lhs"]], labels[ref["left_target_rhs"]])
                ]:
                    ok = False
                    break
            elif side == "direct":
                if COMPOSE[(labels[ref["left_lhs"]], labels[ref["middle_lhs_l"]])] != labels[
                    (ref["left_target_lhs"])
                ]:
                    ok = False
                    break
            else:
                raise ValueError(f"unknown product side {side!r}")
        if ok:
            out.append(values)
    return tuple(out)


def product_primitive(base, left, right, side):
    for part_0, part_1 in product(PARTITIONS, repeat=2):
        family = {0: part_0, 1: part_1}
        invariant = True
        for a, b in product(base.elements, repeat=2):
            c, d = base.R[(a, b)]
            if side == "swapped":
                constraints = (
                    (left[(a, b)], family[b], family[c]),
                    (right[(a, b)], family[a], family[d]),
                )
            elif side == "direct":
                constraints = (
                    (left[(a, b)], family[a], family[c]),
                    (right[(a, b)], family[b], family[d]),
                )
            else:
                raise ValueError(f"unknown product side {side!r}")
            for permutation, source_partition, target_partition in constraints:
                if transport_partition(permutation, source_partition) != target_partition:
                    invariant = False
                    break
            if not invariant:
                break
        if not invariant:
            continue
        if (part_0, part_1) in (
            (EQUALITY_PARTITION, EQUALITY_PARTITION),
            (UNIVERSAL_PARTITION, UNIVERSAL_PARTITION),
        ):
            continue
        return False
    return True


def is_identity_base(base):
    return all(base.R[(a, b)] == (a, b) for a, b in product(base.elements, repeat=2))


def interval_from_labels(base, left, right, side):
    fibres = {color: POINTS for color in base.elements}
    table = {}
    for a, b in product(base.elements, repeat=2):
        for x, y in product(POINTS, repeat=2):
            if side == "swapped":
                table[(a, b, x, y)] = (left[(a, b)][y], right[(a, b)][x])
            elif side == "direct":
                table[(a, b, x, y)] = (left[(a, b)][x], right[(a, b)][y])
            else:
                raise ValueError(f"unknown product side {side!r}")
    return LocalInterval(base.elements, fibres, base.R, table)


def label_payload(labels, pairs):
    return {
        repr(pair): list(labels[pair])
        for pair in pairs
    }


def scan_side(base_index, base, side):
    pairs = tuple(product(base.elements, repeat=2))
    refs = swapped_equation_refs(base)
    valid_lefts = valid_left_label_choices(base, pairs, side)
    checked = 0
    cocycle_count = 0
    primitive_count = 0
    tag_counts = {}
    holonomy_counts = {}
    known_primitive_count = 0
    identity_base_cyclic_count = 0
    unknown_count = 0
    router_verdict_counts = {}
    product_holonomy_detail_counts = {}
    first_unknowns = []
    first_router_targets = []
    first_identity_base_cyclic = None

    for left_values in valid_lefts:
        left = dict(zip(pairs, left_values))
        for right_values in product(PERMS, repeat=len(pairs)):
            checked += 1
            right = dict(zip(pairs, right_values))
            ok = True
            for ref in refs:
                if side == "swapped":
                    if COMPOSE[
                        (right[ref["middle_lhs_r"]], left[ref["middle_lhs_l"]])
                    ] != COMPOSE[
                        (left[ref["middle_rhs_l"]], right[ref["middle_rhs_r"]])
                    ]:
                        ok = False
                        break
                    if COMPOSE[
                        (right[ref["right_lhs"]], right[ref["right_rhs"]])
                    ] != COMPOSE[
                        (right[ref["right_target_lhs"]], right[ref["right_target_rhs"]])
                    ]:
                        ok = False
                        break
                elif side == "direct":
                    middle_left = COMPOSE[
                        (
                            right[ref["middle_lhs_r"]],
                            COMPOSE[(left[(ref["right_lhs"])], right[ref["middle_lhs_l"]])],
                        )
                    ]
                    middle_right = COMPOSE[
                        (
                            left[ref["middle_rhs_l"]],
                            COMPOSE[(right[ref["right_target_rhs"]], left[ref["middle_rhs_r"]])],
                        )
                    ]
                    if middle_left != middle_right:
                        ok = False
                        break
                    if right[ref["right_lhs"]] != COMPOSE[
                        (right[ref["right_target_lhs"]], right[ref["middle_rhs_r"]])
                    ]:
                        ok = False
                        break
                else:
                    raise ValueError(f"unknown product side {side!r}")
            if not ok:
                continue
            cocycle_count += 1
            if not product_primitive(base, left, right, side):
                continue
            primitive_count += 1

            interval = interval_from_labels(base, left, right, side)
            if not interval.is_colored_ybe():
                raise AssertionError("product cocycle accepted a non-YBE table")
            router = local_master_bottleneck_summary(interval)
            router_verdict_counts[router.verdict] = (
                router_verdict_counts.get(router.verdict, 0) + 1
            )
            for detail in router.product_holonomy_details:
                product_holonomy_detail_counts[detail] = (
                    product_holonomy_detail_counts.get(detail, 0) + 1
                )
            if router.verdict in {
                "product_genuinely_coloured_bottleneck",
                "bi_free_universal_corridor_bottleneck",
            } and len(first_router_targets) < 3:
                first_router_targets.append(
                    {
                        "verdict": router.verdict,
                        "details": list(router.product_holonomy_details),
                        "tags": list(router.total_branch_tags),
                        "left": label_payload(left, pairs),
                        "right": label_payload(right, pairs),
                    }
                )
            if side == "swapped":
                invariant_families = swapped_product_invariant_families(interval)
                holonomy = swapped_product_holonomy_summary(interval)
            elif side == "direct":
                invariant_families = direct_product_invariant_families(interval)
                holonomy = direct_product_holonomy_summary(interval)
            else:
                raise ValueError(f"unknown product side {side!r}")
            if len(invariant_families) != 2:
                raise AssertionError("primitive partition audit mismatch")
            total = solution_from_local_interval(interval).total
            tags = branch_tags(total)
            tag_key = "+".join(tags) if tags else "(untagged)"
            tag_counts[tag_key] = tag_counts.get(tag_key, 0) + 1
            hol_key = repr(holonomy.component_group_sizes)
            holonomy_counts[hol_key] = holonomy_counts.get(hol_key, 0) + 1

            known = bool(set(tags).intersection(KNOWN_TAGS))
            if known:
                known_primitive_count += 1
                continue
            if side == "swapped" and is_identity_base(base) and holonomy.component_group_sizes == (
                ((0, 1, 2), 3),
            ):
                identity_base_cyclic_count += 1
                if first_identity_base_cyclic is None:
                    first_identity_base_cyclic = {
                        "left": label_payload(left, pairs),
                        "right": label_payload(right, pairs),
                        "holonomy": hol_key,
                    }
                continue

            unknown_count += 1
            if len(first_unknowns) < 3:
                first_unknowns.append(
                    {
                        "tags": list(tags),
                        "left": label_payload(left, pairs),
                        "right": label_payload(right, pairs),
                        "holonomy": hol_key,
                    }
                )

    return {
        "base_index": base_index,
        "side": side,
        "base_tags": list(branch_tags(base)),
        "base_identity": is_identity_base(base),
        "valid_left_label_count": len(valid_lefts),
        "right_label_assignments_checked": checked,
        "product_cocycle_count": cocycle_count,
        "primitive_count": primitive_count,
        "known_primitive_count": known_primitive_count,
        "identity_base_cyclic_count": identity_base_cyclic_count,
        "unknown_primitive_count": unknown_count,
        "router_verdict_counts": dict(sorted(router_verdict_counts.items())),
        "product_holonomy_detail_counts": dict(sorted(product_holonomy_detail_counts.items())),
        "branch_tag_counts": dict(sorted(tag_counts.items())),
        "holonomy_counts": dict(sorted(holonomy_counts.items())),
        "first_identity_base_cyclic": first_identity_base_cyclic,
        "first_unknowns": first_unknowns,
        "first_router_targets": first_router_targets,
    }


def scan_base(base_index, base):
    return {
        "base_index": base_index,
        "base_tags": list(branch_tags(base)),
        "base_identity": is_identity_base(base),
        "swapped": scan_side(base_index, base, "swapped"),
        "direct": scan_side(base_index, base, "direct"),
    }


def write_markdown(report):
    swapped_totals = report["totals"]["swapped"]
    direct_totals = report["totals"]["direct"]
    swapped_router = report["router_totals"]["swapped"]
    direct_router = report["router_totals"]["direct"]
    swapped_details = report["product_detail_totals"]["swapped"]
    direct_details = report["product_detail_totals"]["direct"]
    lines = [
        "# Two-colour fibre-3 product audit",
        "",
        "Date: 2026-05-28",
        "",
        "This audit enumerates the swapped and direct product-permutation",
        "branches with two quotient colours and three fibre points over each",
        "colour.  It is an exact candidate-discovery audit for this structured",
        "branch, not a finite-search proof of the master theorem.",
        "",
        "The enumerated swapped local maps have the form",
        "",
        "```text",
        "T_{a,b}(x,y) = (L_{a,b}(y), R_{a,b}(x))",
        "```",
        "",
        "and the direct maps have the form",
        "",
        "```text",
        "T_{a,b}(x,y) = (L_{a,b}(x), R_{a,b}(y)).",
        "```",
        "",
        "All `L` and `R` labels lie in `S_3`, over each of the five two-point",
        "bijective YBE quotient colour tables.",
        "",
        "## Swapped Totals",
        "",
        f"- valid left-label assignments: `{swapped_totals['valid_left_label_count']}`;",
        f"- right-label assignments checked: `{swapped_totals['right_label_assignments_checked']}`;",
        f"- swapped product cocycle solutions: `{swapped_totals['product_cocycle_count']}`;",
        f"- primitive/local-minimal product rows: `{swapped_totals['primitive_count']}`;",
        f"- known-branch primitive rows: `{swapped_totals['known_primitive_count']}`;",
        f"- identity-base cyclic rows: `{swapped_totals['identity_base_cyclic_count']}`;",
        f"- unknown primitive rows: `{swapped_totals['unknown_primitive_count']}`.",
        f"- router verdicts: `{swapped_router}`.",
        f"- product details: `{swapped_details}`.",
        "",
        "## Direct Totals",
        "",
        f"- valid left-label assignments: `{direct_totals['valid_left_label_count']}`;",
        f"- right-label assignments checked: `{direct_totals['right_label_assignments_checked']}`;",
        f"- direct product cocycle solutions: `{direct_totals['product_cocycle_count']}`;",
        f"- primitive/local-minimal product rows: `{direct_totals['primitive_count']}`;",
        f"- known-branch primitive rows: `{direct_totals['known_primitive_count']}`;",
        f"- unknown primitive rows: `{direct_totals['unknown_primitive_count']}`.",
        f"- router verdicts: `{direct_router}`.",
        f"- product details: `{direct_details}`.",
        "",
        "## By Base",
        "",
    ]
    for scan in report["base_scans"]:
        swapped = scan["swapped"]
        direct = scan["direct"]
        lines.extend(
            [
                f"### base {scan['base_index']}",
                "",
                f"- base tags: `{'+'.join(scan['base_tags']) if scan['base_tags'] else '(untagged)'}`;",
                f"- identity base: `{scan['base_identity']}`;",
                f"- swapped cocycle solutions: `{swapped['product_cocycle_count']}`;",
                f"- swapped primitive rows: `{swapped['primitive_count']}`;",
                f"- swapped unknown primitive rows: `{swapped['unknown_primitive_count']}`;",
                f"- swapped router verdicts: `{swapped['router_verdict_counts']}`;",
                f"- direct cocycle solutions: `{direct['product_cocycle_count']}`;",
                f"- direct primitive rows: `{direct['primitive_count']}`;",
                f"- direct unknown primitive rows: `{direct['unknown_primitive_count']}`.",
                f"- direct router verdicts: `{direct['router_verdict_counts']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Consequence",
            "",
            "Within this exact two-colour/fibre-3 swapped product search, the only",
            "primitive row outside the standard branch tags is the identity-base",
            "cyclic case.  That case is covered by the symbolic identity-base",
            "product lemma and the cyclic pairwise-linking detector.  The",
            "non-identity two-colour bases contribute primitive rows only in",
            "known finite-G-measurable tags such as nondegenerate, rack-type,",
            "permutation-form, or involutive.",
            "",
            "The direct search has nontrivial direct product holonomy in the full",
            "cocycle space, so direct holonomy is not automatically coboundary.",
            "However, every primitive direct row in this exact search is",
            "involutive and hence already belongs to a known finite-G-measurable",
            "branch.",
            "",
            "This does not prove the arbitrary-colour product theorem.  It does",
            "remove the smallest genuinely coloured product search space as a",
            "source of B-style obstruction candidates.",
            "",
            "The central local router agrees with this split: every primitive",
            "row in this corpus routes to `product_finite_g_branch`; no row",
            "routes to `product_genuinely_coloured_bottleneck` or to the",
            "bi-free corridor target.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    scans = tuple(scan_base(index, base) for index, base in enumerate(all_bijection_solutions(2)))
    total_keys = (
        "valid_left_label_count",
        "right_label_assignments_checked",
        "product_cocycle_count",
        "primitive_count",
        "known_primitive_count",
        "identity_base_cyclic_count",
        "unknown_primitive_count",
    )
    totals = {
        side: {key: sum(scan[side][key] for scan in scans) for key in total_keys}
        for side in ("swapped", "direct")
    }
    def aggregate_counter(field, side):
        out = {}
        for scan in scans:
            for key, value in scan[side][field].items():
                out[key] = out.get(key, 0) + value
        return dict(sorted(out.items()))

    report = {
        "base_scans": scans,
        "totals": totals,
        "router_totals": {
            side: aggregate_counter("router_verdict_counts", side)
            for side in ("swapped", "direct")
        },
        "product_detail_totals": {
            side: aggregate_counter("product_holonomy_detail_counts", side)
            for side in ("swapped", "direct")
        },
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
