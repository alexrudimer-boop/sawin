import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    LocalInterval,
    branch_tags,
    context_retraction_audit,
    product_permutation_witness,
    solution_from_local_interval,
)


OUT = ROOT / "proofs" / "two_colour_fibre2_audit.json"


def _family_signature(interval, family):
    return {
        repr(color): [
            sorted(repr(item) for item in block)
            for block in family[color]
        ]
        for color in interval.colors
    }


def _table_signature(interval):
    return [
        {
            "colors": [repr(a), repr(b)],
            "input": [repr(x), repr(y)],
            "output": [repr(u), repr(v)],
        }
        for a in interval.colors
        for b in interval.colors
        for x in interval.fibres[a]
        for y in interval.fibres[b]
        for u, v in [interval.T[(a, b, x, y)]]
    ]


def scan(base_name, base_R):
    colors = (0, 1)
    fibres = {0: (0, 1), 1: (0, 1)}
    source_pairs = {
        (a, b): [(x, y) for x in fibres[a] for y in fibres[b]]
        for a in colors
        for b in colors
    }
    target_permutations = {
        key: list(
            itertools.permutations(
                [
                    (x, y)
                    for x in fibres[base_R[key][0]]
                    for y in fibres[base_R[key][1]]
                ]
            )
        )
        for key in source_pairs
    }
    keys = tuple(source_pairs)
    checked = 0
    ybe_count = 0
    local_minimal_count = 0
    retraction_kind_counts = {}
    branch_tag_counts = {}
    product_permutation_count = 0
    unknown_examples = []
    first_examples_by_kind = {}

    for choices in itertools.product(*(target_permutations[key] for key in keys)):
        checked += 1
        table = {}
        for key, images in zip(keys, choices):
            for source, image in zip(source_pairs[key], images):
                table[(key[0], key[1], source[0], source[1])] = image
        interval = LocalInterval(colors, fibres, base_R, table)
        if not interval.is_colored_ybe():
            continue
        ybe_count += 1
        if not interval.is_local_minimal(max_fibre_size=2):
            continue
        local_minimal_count += 1
        audit = context_retraction_audit(interval)
        retraction_kind_counts[audit.kind] = retraction_kind_counts.get(audit.kind, 0) + 1
        total = solution_from_local_interval(interval).total
        tags = branch_tags(total)
        tag_key = " + ".join(tags) if tags else "(untagged)"
        branch_tag_counts[tag_key] = branch_tag_counts.get(tag_key, 0) + 1
        has_product_witness = product_permutation_witness(interval) is not None
        if has_product_witness:
            product_permutation_count += 1
        known = bool(
            set(tags)
            & {
                "involutive",
                "permutation_form",
                "affine_cyclic",
                "nondegenerate",
                "rack_type",
            }
        ) or has_product_witness
        if audit.kind not in first_examples_by_kind:
            first_examples_by_kind[audit.kind] = {
                "branch_tags": list(tags),
                "product_permutation_witness": has_product_witness,
                "retraction_family": _family_signature(interval, audit.stable_family),
                "table": _table_signature(interval),
            }
        if not known and len(unknown_examples) < 5:
            unknown_examples.append(first_examples_by_kind[audit.kind])

    return {
        "base": base_name,
        "checked_table_count": checked,
        "colored_ybe_count": ybe_count,
        "local_minimal_count": local_minimal_count,
        "retraction_kind_counts": dict(sorted(retraction_kind_counts.items())),
        "branch_tag_counts": dict(sorted(branch_tag_counts.items())),
        "product_permutation_witness_count": product_permutation_count,
        "unknown_example_count": len(unknown_examples),
        "unknown_examples": unknown_examples,
        "first_examples_by_kind": first_examples_by_kind,
    }


def main():
    colors = (0, 1)
    report = {
        "identity_base": scan(
            "identity",
            {(a, b): (a, b) for a in colors for b in colors},
        ),
        "flip_base": scan(
            "flip",
            {(a, b): (b, a) for a in colors for b in colors},
        ),
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
