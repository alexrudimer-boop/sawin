# Affine cyclic audit-tag guardrail

Date: 2026-05-28

The tag `affine_cyclic` is an audit and classification tag, not by itself a
closed all-`n` finite-G detector branch in the local bottleneck router.

The local router is allowed to treat a whole-solution tag as closed only when a
symbolic detector proof is already available for all braid indices.  The
current closed total tags are:

```text
involutive, permutation_form, rack_type, nondegenerate
```

The affine scans are useful evidence and have eliminated several small hiding
places, but an affine-looking table must still be routed through one of the
proved detector mechanisms:

- involutive or permutation-form detector;
- rack-type detector;
- nondegenerate/guitar detector;
- a product-specific coboundary, pairwise-linking, identity-base cyclic, or
  semidirect/finite-label detector proof;
- or the remaining genuinely coloured product or bi-free corridor target.

Consequently, a local-minimal interval whose only total tag were
`affine_cyclic`, and which did not fall into a closed product subbranch, would
remain in the open master-local target.  It cannot be counted as
`known_total_branch` merely because the affine formula was detected.

The regression test

```text
test_affine_cyclic_tag_alone_is_not_a_known_total_detector
```

locks this convention: `affine_cyclic` is excluded from
`KNOWN_TOTAL_DETECTOR_TAGS`, and a universal-kernel interval with only that tag
still routes to `bi_free_universal_corridor_bottleneck` when no product branch
has already closed it.
