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
    local_master_bottleneck_summary,
    solution_from_local_interval,
)


OUT_JSON = ROOT / "proofs" / "three_colour_fibre2_product_audit.json"
OUT_MD = ROOT / "proofs" / "three_colour_fibre2_product_audit.md"

POINTS = (0, 1)
PERMS = {
    0: (0, 1),
    1: (1, 0),
}
KNOWN_TAGS = {
    "involutive",
    "permutation_form",
    "nondegenerate",
    "rack_type",
}


def _xor_equation(indices):
    mask = 0
    for index in indices:
        mask ^= 1 << index
    return mask


def _triangular_basis(equations, nvars):
    basis = [0] * nvars
    for row in equations:
        current = row
        while current:
            pivot = current.bit_length() - 1
            if basis[pivot]:
                current ^= basis[pivot]
            else:
                basis[pivot] = current
                break
    return tuple(basis)


def _homogeneous_solutions(equations, nvars):
    basis = _triangular_basis(equations, nvars)
    pivots = {index for index, row in enumerate(basis) if row}
    free = tuple(index for index in range(nvars) if index not in pivots)
    for choice in range(1 << len(free)):
        value = 0
        for index, free_index in enumerate(free):
            if choice & (1 << index):
                value |= 1 << free_index
        for pivot, row in enumerate(basis):
            if row and (row & value).bit_count() % 2:
                value |= 1 << pivot
        yield value


def _equations(base, side):
    pairs = tuple(product(base.elements, repeat=2))
    pair_index = {pair: index for index, pair in enumerate(pairs)}
    offset = len(pairs)

    def left(pair):
        return pair_index[pair]

    def right(pair):
        return offset + pair_index[pair]

    equations = []
    for a, b, c in product(base.elements, repeat=3):
        ab, a_b = base.R[(a, b)]
        bc, b_c = base.R[(b, c)]
        a_b_c, _ = base.R[(a_b, c)]
        _, a_star_bc = base.R[(a, bc)]
        if side == "swapped":
            equations.append(
                _xor_equation(
                    (
                        left((ab, a_b_c)),
                        left((a_b, c)),
                        left((a, bc)),
                        left((b, c)),
                    )
                )
            )
            equations.append(
                _xor_equation(
                    (
                        right((ab, a_b_c)),
                        left((a, b)),
                        left((a_star_bc, b_c)),
                        right((b, c)),
                    )
                )
            )
            equations.append(
                _xor_equation(
                    (
                        right((a_b, c)),
                        right((a, b)),
                        right((a_star_bc, b_c)),
                        right((a, bc)),
                    )
                )
            )
        elif side == "direct":
            equations.append(
                _xor_equation(
                    (
                        left((ab, a_b_c)),
                        left((a, b)),
                        left((a, bc)),
                    )
                )
            )
            equations.append(
                _xor_equation(
                    (
                        right((ab, a_b_c)),
                        left((a_b, c)),
                        right((a, b)),
                        left((a_star_bc, b_c)),
                        right((a, bc)),
                        left((b, c)),
                    )
                )
            )
            equations.append(
                _xor_equation(
                    (
                        right((a_b, c)),
                        right((a_star_bc, b_c)),
                        right((b, c)),
                    )
                )
            )
        else:
            raise ValueError(f"unknown side {side!r}")
    return tuple(mask for mask in equations if mask), pairs, 2 * len(pairs)


def _rank(equations, nvars):
    return sum(1 for row in _triangular_basis(equations, nvars) if row)


def _label_maps(mask, pairs):
    offset = len(pairs)
    left = {}
    right = {}
    for index, pair in enumerate(pairs):
        left[pair] = PERMS[(mask >> index) & 1]
        right[pair] = PERMS[(mask >> (offset + index)) & 1]
    return left, right


def _interval_from_labels(base, left, right, side):
    fibres = {color: POINTS for color in base.elements}
    table = {}
    for a, b in product(base.elements, repeat=2):
        for x, y in product(POINTS, repeat=2):
            if side == "swapped":
                table[(a, b, x, y)] = (left[(a, b)][y], right[(a, b)][x])
            elif side == "direct":
                table[(a, b, x, y)] = (left[(a, b)][x], right[(a, b)][y])
            else:
                raise ValueError(f"unknown side {side!r}")
    return LocalInterval(base.elements, fibres, base.R, table)


def _semisplit_free(base, side):
    colors = tuple(base.elements)
    for mask in range(1, (1 << len(colors)) - 1):
        kind = {
            color: (mask >> index) & 1
            for index, color in enumerate(colors)
        }
        invariant = True
        for a, b in product(colors, repeat=2):
            c, d = base.R[(a, b)]
            if side == "swapped":
                checks = ((b, c), (a, d))
            elif side == "direct":
                checks = ((a, c), (b, d))
            else:
                raise ValueError(f"unknown side {side!r}")
            if any(kind[source] != kind[target] for source, target in checks):
                invariant = False
                break
        if invariant:
            return False
    return True


def _payload(mask, pairs):
    return {
        repr(pair): {
            "L": (mask >> index) & 1,
            "R": (mask >> (len(pairs) + index)) & 1,
        }
        for index, pair in enumerate(pairs)
    }


def _bump(counter, key, amount=1):
    counter[key] = counter.get(key, 0) + amount


def scan_base(base_index, base, side):
    equations, pairs, nvars = _equations(base, side)
    dimension = nvars - _rank(equations, nvars)
    semisplit_free = _semisplit_free(base, side)
    cocycle_count = 0
    primitive_count = 0
    router_verdict_counts = {}
    product_holonomy_detail_counts = {}
    tag_counts = {}
    known_primitive_count = 0
    first_router_targets = []

    for mask in _homogeneous_solutions(equations, nvars):
        cocycle_count += 1
        if not semisplit_free:
            continue
        left, right = _label_maps(mask, pairs)
        interval = _interval_from_labels(base, left, right, side)
        if not interval.is_colored_ybe():
            raise AssertionError("linear cocycle equations accepted a non-YBE table")
        if not interval.is_local_minimal():
            raise AssertionError("semisplit-free two-point product interval is not local-minimal")
        primitive_count += 1
        router = local_master_bottleneck_summary(interval)
        _bump(router_verdict_counts, router.verdict)
        for detail in router.product_holonomy_details:
            _bump(product_holonomy_detail_counts, detail)
        total = solution_from_local_interval(interval).total
        tags = branch_tags(total)
        _bump(tag_counts, "+".join(tags) if tags else "(untagged)")
        if set(tags) & KNOWN_TAGS:
            known_primitive_count += 1
        if router.verdict in {
            "product_genuinely_coloured_bottleneck",
            "bi_free_universal_corridor_bottleneck",
        } and len(first_router_targets) < 5:
            first_router_targets.append(
                {
                    "verdict": router.verdict,
                    "details": list(router.product_holonomy_details),
                    "tags": list(router.total_branch_tags),
                    "labels": _payload(mask, pairs),
                }
            )

    return {
        "base_index": base_index,
        "base_tags": list(branch_tags(base)),
        "side": side,
        "linear_dimension": dimension,
        "cocycle_count": cocycle_count,
        "semisplit_free": semisplit_free,
        "primitive_count": primitive_count,
        "known_primitive_count": known_primitive_count,
        "router_verdict_counts": router_verdict_counts,
        "product_holonomy_detail_counts": product_holonomy_detail_counts,
        "tag_counts": tag_counts,
        "first_router_targets": first_router_targets,
    }


def _merge_counts(rows, key):
    out = {}
    for row in rows:
        for name, count in row[key].items():
            _bump(out, name, count)
    return dict(sorted(out.items()))


def _totals(rows):
    return {
        "cocycle_count": sum(row["cocycle_count"] for row in rows),
        "primitive_count": sum(row["primitive_count"] for row in rows),
        "known_primitive_count": sum(row["known_primitive_count"] for row in rows),
        "router_verdict_counts": _merge_counts(rows, "router_verdict_counts"),
        "product_holonomy_detail_counts": _merge_counts(rows, "product_holonomy_detail_counts"),
        "tag_counts": _merge_counts(rows, "tag_counts"),
    }


def build_report():
    rows = []
    for base_index, base in enumerate(all_bijection_solutions(3)):
        for side in ("swapped", "direct"):
            rows.append(scan_base(base_index, base, side))
    by_side = {
        side: _totals([row for row in rows if row["side"] == side])
        for side in ("swapped", "direct")
    }
    payload = {
        "description": "three quotient colours, two-point fibres, product labels in S2",
        "rows": rows,
        "totals": _totals(rows),
        "by_side": by_side,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")
    return payload


def render_markdown(payload):
    lines = [
        "# Three-colour fibre-2 product audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit enumerates product-permutation local intervals with",
        "three quotient colours and two-point fibres.  Since every fibre label is",
        "either the identity or the transposition, the product cocycle equations",
        "are solved exactly as homogeneous linear equations over `F_2`; this is",
        "not a timeout or word-length search.",
        "",
        "The audit is still finite candidate evidence only.  Its role is to look",
        "for explicit local-minimal rows that route to",
        "`product_genuinely_coloured_bottleneck`, not to prove the arbitrary-fibre",
        "product theorem.",
        "",
        "## Totals",
        "",
    ]
    totals = payload["totals"]
    lines.extend(
        [
            f"- product cocycle rows: `{totals['cocycle_count']}`.",
            f"- primitive/local-minimal rows: `{totals['primitive_count']}`.",
            f"- primitive rows with standard known total tags: `{totals['known_primitive_count']}`.",
            f"- router verdicts: `{totals['router_verdict_counts']}`.",
            f"- product details: `{totals['product_holonomy_detail_counts']}`.",
            "",
        ]
    )
    for side, side_totals in payload["by_side"].items():
        lines.extend(
            [
                f"## {side.title()} branch",
                "",
                f"- product cocycle rows: `{side_totals['cocycle_count']}`.",
                f"- primitive/local-minimal rows: `{side_totals['primitive_count']}`.",
                f"- primitive rows with standard known total tags: `{side_totals['known_primitive_count']}`.",
                f"- router verdicts: `{side_totals['router_verdict_counts']}`.",
                f"- product details: `{side_totals['product_holonomy_detail_counts']}`.",
                "",
            ]
        )
    targets = [
        (row["base_index"], row["side"], target)
        for row in payload["rows"]
        for target in row["first_router_targets"]
    ]
    if targets:
        lines.extend(["## First open router targets", ""])
        for base_index, side, target in targets[:10]:
            lines.append(
                f"- base `{base_index}`, side `{side}`, verdict `{target['verdict']}`, "
                f"details `{target['details']}`, tags `{target['tags']}`."
            )
        lines.append("")
    else:
        lines.extend(
            [
                "## Router outcome",
                "",
                "No primitive row in this exact product-label corpus routes to",
                "`product_genuinely_coloured_bottleneck` or",
                "`bi_free_universal_corridor_bottleneck`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Interpretation",
            "",
            "This extends the product search surface in the complementary direction",
            "from the two-colour/fibre-3 audit: more quotient colours, but the",
            "smallest nontrivial fibres.  The result is consistent with the",
            "fibre-size-two affine/semidirect branch being finite-G measurable,",
            "while keeping the global all-`n` product theorem open for arbitrary",
            "fibre sizes and quotient colour sets.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    payload = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps(payload["totals"], sort_keys=True))


if __name__ == "__main__":
    main()
