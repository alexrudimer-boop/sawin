# Green balanced defect-gauge decomposition

Date: 2026-05-29

This note follows `proofs/green_first_output_defect_criterion.md` and refines
`proofs/green_defect_potential_coboundary.md`.  It does not prove the Master
Local-Minimal Residual Theorem.  It shows that the non-rack part of a
Green/Schutzenberger first-output row defect is not an independent
obstruction: it is an Artin-visible commutator times a terminal
second-output gauge boundary.

The remaining Green/Schutzenberger burden is therefore pushed into the
endpoint/unit gauge holonomy already isolated elsewhere in the corridor
reduction.

## Setup

Fix one finite Green observer factor

```text
U
```

coming from either a Schutzenberger action group or a Green kernel-block
permutation group.  For one completed retained row

```text
(a,q) -> (q^a,a^q),
```

write the four observer labels as

```text
A = g(a),      Q = g(q),
B = g(q^a),    C = g(a^q)
```

inside `U`.

The Green coordinate-product relation gives

```text
A Q = B C.                                      (1)
```

Define the first-output defect and second-output gauge by

```text
d(a,q) = B Q^-1,
s(a,q) = C A^-1.
```

## Balanced Decomposition

For every completed row:

```text
d(a,q) = [A,Q] * Q s(a,q)^-1 Q^-1,
```

where

```text
[A,Q] = A Q A^-1 Q^-1.
```

Proof.  Since `s=C A^-1`, we have `C=sA`.  From `(1)`:

```text
B = A Q C^-1
  = A Q (s A)^-1
  = A Q A^-1 s^-1.
```

Therefore

```text
B Q^-1
  = A Q A^-1 s^-1 Q^-1
  = A Q A^-1 Q^-1 * Q s^-1 Q^-1.
```

This is exactly the claimed decomposition.  QED.

## The commutator factor is Artin-visible

For the positive Artin generator `sigma_i`,

```text
sigma_i(x_i) = x_i x_{i+1} x_i^-1,
p_{sigma_i}(x_i) = x_{i+1}.
```

Thus the local Artin permutation defect is

```text
sigma_i(x_i) p_{sigma_i}(x_i)^-1
  = x_i x_{i+1} x_i^-1 x_{i+1}^-1.
```

Under the assignment

```text
x_i     |-> A,
x_{i+1} |-> Q,
```

this evaluates to `[A,Q]`.  The Artin-defect sieve already proves that every
Artin permutation defect value lies in `V_beta(U)` for any finite target
group `U`.  Hence the commutator part of a transported row defect is already
longitude-visible.

The remaining factor is the conjugate

```text
Q s(a,q)^-1 Q^-1.
```

Since `V_beta(U)` is normal in `U`, conjugation by `Q` does not matter for
membership.  Normality follows because conjugating an assignment
`phi:F_n -> U` by any fixed `h in U` conjugates every longitude value
`phi(L_i(beta))` by `h`.

## Consequence

The earlier target

```text
D_C(beta) in V_beta(Def_C)
```

is stronger than the genuinely Green-specific obstruction.  Row by row, the
first-output defect endpoint decomposes into:

1. a product of Artin-visible commutators; and
2. a transported product of second-output gauge increments.

Therefore a raw Green/Schutzenberger first-output defect is not a final
obstruction.  After stripping the Artin-visible commutators, the remaining
target is terminal gauge longitudinalization:

```text
S_beta in V_beta(U_gauge),
```

where `S_beta` is the transported endpoint product of the gauge increments

```text
s(a,q)=g(a^q) g(a)^-1.
```

This is exactly lower endpoint/unit chart-change holonomy.  Along a fixed
physical strand, the unconjugated product telescopes as

```text
s_t ... s_1 = g(a_terminal) g(a_initial)^-1,
```

with the usual transported form when read in moving Green or Schutzenberger
charts.

The follow-up note
`proofs/terminal_gauge_longitudinalization_criterion.md` records this
telescope as the executable certificate target: after computing the terminal
gauge endpoint, prove that endpoint lies in `V_beta` of fixed gauge factors
by a longitude expression, literal subgroup witness, Artin-defect display, or
abelian matrix witness.
The principal-gauge subcase is then closed by
`proofs/principal_gauge_extension_detector.md`: if the lower gauge row is a
principal rack-extension cocycle, the finite rack `A x U` and its inner group
detect the remaining endpoint/unit holonomy.
The transport-state refinement
`proofs/transport_state_rackification_detector.md` removes the principal
restriction for strand-continuing rows by treating `(a,r)` as the rack state.
Thus only descent-separation failures remain as Green/lower-row obstructions.

## Updated local target

The Green/Schutzenberger row list should no longer be counted as:

```text
Green kernel-block rows
+ Schutzenberger rows
+ lower endpoint/unit rows.
```

After this decomposition, the Green/Schutzenberger row mismatch reduces to:

```text
lower endpoint/unit gauge holonomy rows,
```

plus the already separate atom descent/totality issue.  Atom-inner detector
rows themselves are closed by the rack-inner detector-lift theorem once the
atom quotient is rack-like.

## Counterexample consequence

A B-route cannot use a bounded raw Green or Schutzenberger row defect as a
final obstruction.  Such a defect is an Artin commutator times terminal gauge
boundary.  A genuine counterexample must produce a normalized-law sequence
whose movement survives in that terminal gauge-boundary holonomy while every
finite group has identity recursive-longitude data.

## Executable audit hooks

The row-level code records this decomposition in
`GreenFirstOutputDefectRowAudit` through:

```text
second_output_gauge
artin_commutator_part
terminal_gauge_boundary_part
balanced_reconstructed_defect
balanced_decomposition_holds
```

and `GreenFirstOutputDefectAudit` now records whether all observed row defects
split into commutator and gauge pieces.  The affine stress-row regression also
checks that the local commutator part is the value of an Artin permutation
defect, via `artin_permutation_defect_witness_audit(...)`.
