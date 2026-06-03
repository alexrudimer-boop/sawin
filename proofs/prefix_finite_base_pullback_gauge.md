# Prefix finite-base pullback and gauge checkpoint

Date: 2026-06-03

After the Peiffer cube-transport audit, the remaining point-pushing pressure
is not a commutator or exponent question.  It is the fixed-base pullback and
section-gauge quotient:

```text
deletion 2-cocycle class in vertical fibre bisections
modulo section-change coboundary
and modulo pullback from one fixed finite operator-label Hurwitz base.
```

The generated audit

```text
proofs/prefix_finite_base_pullback_gauge_audit.md
```

tests the natural translation-pair finite label base

```text
x |-> (lambda_x, rho_x)
```

through point-pushing arities `3,4,5`.  It checks that the crossing descends
to this finite label base, that the marked point-pushing image has a
well-defined quotient to the label action, and that the observed deletion
defect, Peiffer square, and Peiffer cube data have no low-dimensional
2-cocycle obstruction on the checked prefix surface.

For the nondegenerate prefix witness, this base collapses to one label.  Thus
the entire checked point-pushing image is vertical over the candidate base,
with vertical exponent `2`.  The canonical section has nonzero generator
displacement, so the section itself is not fixed.  The Peiffer and cube
ledgers nevertheless show that the deletion 2-cocycle obstruction is trivial
on this prefix.

For the degenerate identity row, the label tuple is injective and the
point-pushing image is trivial.

This checkpoint still does not prove the finite augmented Artin-envelope
lemma.  The open theorem step is to promote a finite label-action base like
this to one fixed finite group-Hurwitz operator-label tower, uniformly in all
arities, or to find a finite low-arity certificate proving that no such fixed
base can pull back the tower.

The external theoretical checkpoint after this audit sharpened the remaining
criterion.  A fixed-base pullback claim needs:

- a comparison from the YBE tower to one finite base tower;
- a vertical coefficient system over that base;
- a section-change cochain whose coboundary carries the observed deletion
  `2`-cocycle into the pullback image.

For a fixed proposed base, a finite obstruction certificate is emptiness of
this finite gauge/pullback system at some arity.  However, replacing the
all-arity requirement by one universal bounded arity needs an additional
pullback-coskeletal lemma.  Without that lemma, the prefix audit is only a
low-dimensional pressure test, not a complete obstruction or realization
theorem.
