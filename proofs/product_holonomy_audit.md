# Product holonomy audit

Date: 2026-05-28

This generated audit runs the product-permutation holonomy summaries
through the small local-minimal congruence-cover corpus.  It is not a
proof of the master theorem; it checks where the product-branch
holonomy obstruction first appears.

## Results

### size_2_exhaustive

- YBE tables: `5`;
- congruence covers: `5`;
- local-minimal covers: `5`;
- product rows audited: `5`.

swapped product branches:

- coboundary: `1`;
- one-colour pairwise: `3`;
- genuinely coloured holonomy: `0`.
- genuinely coloured holonomy in known branches: `0`;
- genuinely coloured holonomy outside known tags: `0`.
- nonprimitive invariant-family rows: `0`.

direct product branches:

- coboundary: `1`;
- one-colour pairwise: `0`;
- genuinely coloured holonomy: `0`.
- genuinely coloured holonomy in known branches: `0`;
- genuinely coloured holonomy outside known tags: `0`.
- nonprimitive invariant-family rows: `0`.

### size_3_exhaustive

- YBE tables: `73`;
- congruence covers: `134`;
- local-minimal covers: `134`;
- product rows audited: `116`.

swapped product branches:

- coboundary: `57`;
- one-colour pairwise: `8`;
- genuinely coloured holonomy: `45`.
- genuinely coloured holonomy in known branches: `45`;
- genuinely coloured holonomy outside known tags: `0`.
- nonprimitive invariant-family rows: `0`.

direct product branches:

- coboundary: `6`;
- one-colour pairwise: `0`;
- genuinely coloured holonomy: `0`.
- genuinely coloured holonomy in known branches: `0`;
- genuinely coloured holonomy outside known tags: `0`.
- nonprimitive invariant-family rows: `0`.

## Consequence

In the audited size range, product holonomy does appear: the
size-3 swapped product rows include one-colour pairwise holonomy
and genuinely coloured holonomy.  However, every genuinely
coloured holonomy row lies in a known branch tag such as
`nondegenerate`, `involutive`, `rack_type`, or `permutation_form`.
This is finite audit evidence only.  The symbolic obligation remains
to prove that local-minimality forces unknown product holonomy into
the coboundary/pairwise-linking/known measurable cases, or to
construct an explicit interval with genuinely coloured holonomy
outside those tags.
