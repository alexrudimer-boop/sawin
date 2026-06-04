# Monodromy-Augmented Transport Gluing Certificate

Date: 2026-06-04

This note records the repaired form of the transport-isomorphic gluing route.
It is a certificate theorem, not a universal existence theorem.

## Boundary

The naive transport-isomorphic gluing proof tries to gauge every mixed
transport to the identity.  That is false without a flatness condition:
`proofs/transport_isomorphic_gluing_boundary_audit.md` gives a six-point
solution whose mixed rows are product-like and transport-isomorphic, but whose
transport loop groups have order `3`.

The same audit also records the correct repair in that example.  The local
router closes the row as

```text
product_finite_g_branch
```

with product holonomy detail

```text
swapped_identity_base_cyclic
```

and fixed detector group order `3`.  Thus nontrivial transport monodromy is
not itself a Sawin obstruction.  It is a residual finite motion that must be
included in the detector.

## Certificate Data

Let `pi:X -> Z` be a finite YBE quotient with crossing-closed fibres.  Suppose
the mixed fibre rows are product-like and their one-coordinate transport maps
are isomorphisms of the internal block solutions.  These transports generate
a finite groupoid `M` of block-solution isomorphisms.  For each block `a`, let

```text
M_a <= Aut(F_a)
```

be the loop monodromy group at that block after choosing a spanning transport
gauge.

A monodromy-augmented transport certificate consists of:

1. finite racks dominating the quotient `Z` and the internal block solutions;
2. one or more fixed finite detector groups `G_j`, independent of braid
   degree;
3. for every quotient-colour tuple and every residual braid in the quotient
   detector kernel, a readout of the induced closed transport word and
   internal block action from the fixed detector action on `A_{G_j}^n`;
4. an all-arity injective total equivariant reconstruction map combining the
   quotient, internal block, and monodromy readouts.

The detector groups may be product-label groups, cyclic pairwise-linking
groups, identity-base cyclic groups, known-total branch groups, endpoint
observer groups, or any other fixed finite groups that satisfy the
fixed-detector-action factorization criterion.

## Theorem

If the above certificate data exist, then `X` is rack-dominated.

Proof.  Let

```text
G = product_j G_j.
```

By `proofs/detector_action_products.md`, the sharp detector action for
`A_G` projects to all factor detector actions.  Hence the separate quotient,
internal, and monodromy readouts combine into one fixed marked factor.

By the fixed-detector-action criterion in
`proofs/fixed_detector_action_factorization.md`, identity of the `A_G`
detector action on a residual braid forces the residual fibre action read
from those factors to be trivial.  The quotient and internal block rack
factors kill the visible quotient and same-block components.  The all-arity
injective reconstruction map then satisfies the safe gluing theorem in
`proofs/ybe_equivariant_reconstruction_closure.md`: any braid invisible to
the product rack is invisible to every marked factor, hence fixes the
reconstruction code, hence fixes the original `X^n` tuple.

The final rack is the product of the quotient/block rack detectors with the
sharp detector racks `A_{G_j}`.  Equivalently, one may first combine the
finite groups into `G` and use the single sharp factor `A_G`.

## Congruence-Chain Form

In the local-minimal congruence-chain reduction, this certificate is already
encoded by the local summary interface.  A local row is usable only when its
summary exposes

```text
closed_detector_product_group != None
closed_detector_gaps == ()
```

and its verdict is one of the closed verdicts accepted by

```text
closed_local_detector_chain(...)
```

Then `assemble_closed_local_detector_chain_rack(Q_m,summaries)` constructs
the finite rack

```text
Q_i = Q_{i+1} x A_{G_i}
```

for each local row.  Rows with open product holonomy, delegated affine gaps,
or missing endpoint-observer groups are rejected rather than silently treated
as solved.

## Consequence

The repaired transport gluing route is:

```text
transport-isomorphic mixed rows
  + finite monodromy/readout detector groups
  + all-arity equivariant reconstruction
  => finite rack domination.
```

The unresolved theorem is the existence statement: prove that every
transport-isomorphic product-like gluing row supplies such fixed detector
groups and reconstruction data, or find a finite table where the residual
monodromy action defeats every fixed finite detector in the normalized-law
sense.
