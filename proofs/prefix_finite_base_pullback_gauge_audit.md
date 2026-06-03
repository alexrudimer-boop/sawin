# Prefix finite-base pullback and gauge audit

Date: 2026-06-03

This generated audit records the first finite-base pullback and
section-gauge pressure surface after the vertical Peiffer cube
transport check.  The tested finite base is the translation-pair
label of an element:

```text
x |-> (lambda_x, rho_x)
```

where `lambda_x(y)` is the first output of `R(x,y)` and `rho_x(y)`
is the second output of `R(y,x)`.  The audit checks arities
`3,4,5`, because the point-pushing surface begins at `Q_X(3)` and
the deletion Peiffer square/cube checks live at source arity `5`.

It is not a proof that this finite label-action base is an honest
finite group-Hurwitz base.  That realization is kept as an explicit
remaining obligation.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- translation-pair label count: `1`;
- left/right translation label counts: `(1, 1)`;
- crossing descends to translation-pair labels: `True`;
- crossing label ambiguity count: `0`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- checked arities: `(3, 4, 5)`;
- all rows untruncated: `True`;
- all label actions well-defined: `True`;
- all quotient maps well-defined: `True`;
- all canonical sections gauge-trivial: `False`;
- vertical kernel exponent spectrum: `(2,)`;
- vertical defect transport mismatches: `0`;
- vertical defect order spectrum: `(2, 2)`;
- Peiffer square nontrivial boundary count: `0`;
- Peiffer cube transport mismatch count: `0`;
- Peiffer order-pair spectrum: `((1, 1),)`;
- observed deletion 2-cocycle gauge-trivial: `True`;
- group-Hurwitz realization still required: `True`;
- records finite-base pullback/gauge surface: `True`.

#### Q_X(3) in B_4

- tuple count: `16`;
- generator count: `3`;
- label tuple count: `1`;
- max label-fibre size: `16`;
- tuple action group size/exponent: `(8, 2)`;
- label action group size/exponent: `(1, 1)`;
- quotient map well-defined: `True`;
- vertical kernel size/exponent: `(8, 2)`;
- canonical section displacement count: `3`;
- canonical section gauge-trivial: `False`;
- truncated: `False`.

#### Q_X(4) in B_5

- tuple count: `32`;
- generator count: `4`;
- label tuple count: `1`;
- max label-fibre size: `32`;
- tuple action group size/exponent: `(16, 2)`;
- label action group size/exponent: `(1, 1)`;
- quotient map well-defined: `True`;
- vertical kernel size/exponent: `(16, 2)`;
- canonical section displacement count: `4`;
- canonical section gauge-trivial: `False`;
- truncated: `False`.

#### Q_X(5) in B_6

- tuple count: `64`;
- generator count: `5`;
- label tuple count: `1`;
- max label-fibre size: `64`;
- tuple action group size/exponent: `(32, 2)`;
- label action group size/exponent: `(1, 1)`;
- quotient map well-defined: `True`;
- vertical kernel size/exponent: `(32, 2)`;
- canonical section displacement count: `5`;
- canonical section gauge-trivial: `False`;
- truncated: `False`.

### degenerate_identity_finite_base_pullback

- element count: `2`;
- translation-pair label count: `2`;
- left/right translation label counts: `(2, 2)`;
- crossing descends to translation-pair labels: `True`;
- crossing label ambiguity count: `0`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- checked arities: `(3, 4, 5)`;
- all rows untruncated: `True`;
- all label actions well-defined: `True`;
- all quotient maps well-defined: `True`;
- all canonical sections gauge-trivial: `True`;
- vertical kernel exponent spectrum: `(1,)`;
- vertical defect transport mismatches: `0`;
- vertical defect order spectrum: `(1, 1)`;
- Peiffer square nontrivial boundary count: `0`;
- Peiffer cube transport mismatch count: `0`;
- Peiffer order-pair spectrum: `((1, 1),)`;
- observed deletion 2-cocycle gauge-trivial: `True`;
- group-Hurwitz realization still required: `True`;
- records finite-base pullback/gauge surface: `True`.

#### Q_X(3) in B_4

- tuple count: `16`;
- generator count: `3`;
- label tuple count: `16`;
- max label-fibre size: `1`;
- tuple action group size/exponent: `(1, 1)`;
- label action group size/exponent: `(1, 1)`;
- quotient map well-defined: `True`;
- vertical kernel size/exponent: `(1, 1)`;
- canonical section displacement count: `0`;
- canonical section gauge-trivial: `True`;
- truncated: `False`.

#### Q_X(4) in B_5

- tuple count: `32`;
- generator count: `4`;
- label tuple count: `32`;
- max label-fibre size: `1`;
- tuple action group size/exponent: `(1, 1)`;
- label action group size/exponent: `(1, 1)`;
- quotient map well-defined: `True`;
- vertical kernel size/exponent: `(1, 1)`;
- canonical section displacement count: `0`;
- canonical section gauge-trivial: `True`;
- truncated: `False`.

#### Q_X(5) in B_6

- tuple count: `64`;
- generator count: `5`;
- label tuple count: `64`;
- max label-fibre size: `1`;
- tuple action group size/exponent: `(1, 1)`;
- label action group size/exponent: `(1, 1)`;
- quotient map well-defined: `True`;
- vertical kernel size/exponent: `(1, 1)`;
- canonical section displacement count: `0`;
- canonical section gauge-trivial: `True`;
- truncated: `False`.

## Meaning

For the nondegenerate prefix witness, the translation-pair base
collapses to a one-point label base.  The checked point-pushing
image is therefore entirely vertical over this base, with
vertical exponent `2` in arities `3,4,5`.  The canonical section
is not fixed by generators, so the section itself has nonzero
1-cochain displacement.  Nevertheless the deletion-defect
transport, Peiffer square, and Peiffer cube ledgers all have zero
2-cocycle obstruction on this prefix surface.

For the degenerate identity row, the translation-pair label tuple
is injective and the point-pushing image is trivial, so all
vertical and gauge rows are trivial.

Thus this checkpoint removes the current low-dimensional
pullback/gauge obstruction for the two recorded rows.  It does
not prove the finite augmented Artin-envelope lemma: the open
step is still to realize such finite label-action bases as one
fixed finite group-Hurwitz operator-label tower, uniformly in
all arities, or to find a finite low-arity certificate proving
that no such fixed base can pull back the tower.
