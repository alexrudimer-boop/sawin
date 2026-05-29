# Readout-kernel admissibility criterion

Date: 2026-05-29

This note follows `proofs/continuation_readout_propagation.md`.  It does not
prove descent separation and does not prove Sawin finite-rack domination.  It
records the finite local criterion needed to use the propagation lemma with an
actual detector readout.

The previous note says: if a fixed readout relation is admissible and contains
a representative continuation seed, then it contains that seed's whole least
admissible closure.  This note explains how to certify the admissibility part
from finite readout labels.

## Setup

Let

```text
pi : X -> Z
```

be a local interval with fibres `A_a` over colours `a`.  A fixed detector
readout gives, for each colour, a finite label map

```text
r_a : A_a -> E_a.
```

In the intended bottleneck application, the labels are tuples of fixed
Green-kernel, Schutzenberger, atom, known-branch, and endpoint/unit readout
coordinates.  The label sets `E_a` are finite and attached to the interval,
not to the braid index.

Define the readout-kernel relation

```text
x equiv_r y  iff  r_a(x)=r_a(y),       x,y in A_a.
```

Let `Phi^r=(equiv_r)_a` be the resulting fibrewise partition family.

## Criterion

The readout kernel `Phi^r` is an admissible local congruence family if and
only if, for every coloured row

```text
T_{a,b}: A_a x A_b -> A_c x A_d,
```

where `R_Z(a,b)=(c,d)`, the table transports the source product kernel exactly
onto the target product kernel:

```text
T_{a,b}(Phi^r_a x Phi^r_b) = Phi^r_c x Phi^r_d.
```

Equivalently, the local row descends to a bijective row on readout blocks:

```text
([x]_r,[y]_r) |-> ([u]_r,[v]_r),
    T_{a,b}(x,y)=(u,v),
```

and the inverse local table also descends.

Proof.  This is the definition of an admissible local congruence family
specialized to relations that are kernels of finite label maps.  Exact
transport of the product relation is precisely the statement that equivalent
source pairs map to equivalent target pairs and, conversely, that every target
equivalence pair is the image of a source equivalence pair.  Since every
`T_{a,b}` is a bijection, this is the same as saying the quotient row on
readout blocks is well-defined and bijective.  QED.

## Code certificate

The helper

```text
readout_kernel_family(interval, labels)
```

turns finite fibrewise labels into the kernel partition family.

The helper

```text
readout_kernel_audit(interval, labels)
```

records:

- the readout-kernel partition family;
- the relation kind: equality, universal, semisplit/mixed, or proper mixed;
- the number of distinct labels/blocks per colour;
- whether the kernel is admissible;
- the first transport failure, if the kernel is not admissible.

The property

```text
proves_readout_kernel_admissible
```

is true exactly when the readout kernel passes the same exact transport test
used for semisplit, local-minimality, and generated-congruence audits.

## Consequence for the bottleneck

Combining this note with `proofs/continuation_readout_propagation.md`, the
remaining descent-separation theorem can now be stated as a two-part finite
local readout target.

For every local-minimal bottleneck interval and every chart-conjugacy orbit of
nontrivial continuation seeds, construct fixed interval-level readout labels
`r_a` such that:

1. `readout_kernel_audit(interval,r)` is admissible;
2. one representative seed `x~v` satisfies `r_a(x)=r_a(v)`.

Then the readout kernel contains the whole generated seed closure.  If that
closure is universal, the readout kernel is universal.  Thus the fixed readout
collapses all lower continuation motion forced by the seed, and the remaining
residue is strand-continuing transport-rack gauge.

This does not finish outcome A.  It converts the current descent-separation
burden into a concrete readout construction problem:

```text
Find fixed interval-level labels from the Green/Schutzenberger/atom/unit
detector factors whose kernel is admissible and contains each representative
continuation seed.
```

## B-route meaning

A failed proposed readout can fail in only two ways at this stage:

1. its kernel is not admissible, with an explicit local transport-failure row;
2. its kernel is admissible but does not contain the representative seed.

Neither is yet outcome B.  To prove B, such a finite failure must still be
upgraded to a normalized-law sequence invisible to every finite group while
moving a residual tuple.  The audit only identifies the finite local row where
that upgrade would have to start.
