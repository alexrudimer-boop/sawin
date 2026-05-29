# Product readout-kernel assembly

Date: 2026-05-29

This note follows `proofs/readout_kernel_quotient_interval.md`.  It does not
prove the Master Local-Minimal Residual Theorem.  It records the local
readout-kernel analogue of the fixed product detector construction: finitely
many fixed readout factors may be bundled into one tuple-valued readout, and
the resulting kernel is the meet of the factor kernels.

## Setup

Let `pi:X->Z` be a local interval with fibres `A_a`.  Suppose we have finitely
many interval-level readout label systems

```text
r^j_a : A_a -> E^j_a,      j=1,...,m.
```

For each factor let `Phi^j` be its kernel relation:

```text
x Phi^j_a y  iff  r^j_a(x)=r^j_a(y).
```

Define the product readout

```text
r_a(x) = (r^1_a(x),...,r^m_a(x)).
```

Let `Phi` be the kernel of `r`.

## Lemma 1: the product kernel is the meet

For every colour `a`,

```text
Phi_a = meet_j Phi^j_a.
```

Proof.  Two points have the same tuple-valued product label exactly when they
have the same label in every factor.  This is precisely membership in the
intersection of the factor equivalence relations, i.e. the meet of the
partitions.  QED.

## Lemma 2: admissibility is stable under finite product assembly

If every factor kernel `Phi^j` is an admissible local congruence family, then
the product kernel `Phi` is admissible.

Proof.  Fix one coloured local bijection

```text
T_{a,b}: A_a x A_b -> A_c x A_d.
```

For each factor `j`,

```text
T_{a,b}(Phi^j_a x Phi^j_b) = Phi^j_c x Phi^j_d.
```

Since `T_{a,b}` is a bijection, it preserves finite intersections of relations:

```text
T_{a,b}(intersection_j R_j) = intersection_j T_{a,b}(R_j).
```

Apply this to the source product relations `R_j=Phi^j_a x Phi^j_b`.  The
intersection of these source product relations is `Phi_a x Phi_b`, and the
intersection of the target product relations is `Phi_c x Phi_d`.  Therefore

```text
T_{a,b}(Phi_a x Phi_b) = Phi_c x Phi_d.
```

This holds for every coloured row, so `Phi` is admissible.  QED.

## Code certificate

The helper

```text
product_readout_labels(interval,*label_families)
```

returns tuple-valued labels.

The helper

```text
product_readout_kernel_audit(interval,*label_families)
```

records:

- the factor readout-kernel audits;
- the tuple-valued product labels;
- the product readout-kernel audit;
- the fibrewise meet of the factor kernels;
- whether the product kernel equals that meet;
- whether all factors are admissible.

The property

```text
proves_product_readout_kernel_admissible
```

is true exactly when there is at least one factor, every factor kernel is
admissible, the product kernel is the factor meet, and the product kernel is
admissible.

## Consequence for descent separation

The current A-route asks for fixed Green, Schutzenberger, atom, known-branch,
and endpoint/unit labels whose readout-kernel quotient passes the
descent-separation audit.  This note justifies assembling those named factor
labels into one tuple-valued label system attached to the interval.

Thus a proof may work factor by factor:

1. construct finite labels for each fixed detector factor;
2. prove each factor kernel is admissible;
3. assemble the product readout;
4. check that the product kernel kills the representative continuation seeds;
5. use `readout_descent_separation_audit` and the quotient interval
   construction.

No braid-index parameter is introduced: the product is finite and fixed once
the interval and quotient detector are fixed.

## Guardrail

The product label kernel can be admissible accidentally even if a proposed
factor kernel is not.  That is not a factorwise proof.  The audit therefore
keeps the factor audits and only certifies the product assembly lemma when
all factor kernels are admissible.

As usual, a finite failure of this audit is not outcome B.  It is only a seed
for a possible normalized-law obstruction sequence.
