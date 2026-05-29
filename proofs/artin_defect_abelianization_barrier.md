# Artin-defect abelianization barrier

Date: 2026-05-29

This note corrects the strongest possible reading of the
`green_defect_potential_coboundary` target.  It does not prove or disprove
Sawin finite-rack domination.  It proves that an elementary Green defect
cannot always be displayed as a product of Artin permutation defect values.

The obstruction is abelianization.  Therefore the remaining Green route must
use either full recursive-longitude membership in `V_beta(Def_C)`, endpoint
cancellation after transport, or detector-lift style longitude labels.  A
proof that demands every elementary defect itself be an Artin permutation
defect value is too strong.

## Lemma: Artin permutation defects are abelianization-trivial

Let `beta in B_n`, and let `p_beta` be its strand permutation.  For every free
word `w in F_n`,

```text
beta(w) p_beta(w)^-1
```

has trivial image in the abelianization of `F_n`.

Proof.  The Artin action on `H_1(F_n)` is exactly the permutation action
induced by `p_beta`.  Hence `beta(w)` and `p_beta(w)` have the same
abelianized exponent vector.  Their quotient has exponent vector `0`.  QED.

Consequently, for any homomorphism `phi:F_n -> K` into a finite group `K`,

```text
phi(beta(w) p_beta(w)^-1) in [K,K].
```

Any finite product of Artin permutation defect values also lies in `[K,K]`.

## Consequence for Green defect kernels

For a Green/Schutzenberger defect kernel `Def_C`, an endpoint element with
nontrivial image in the abelianization

```text
Def_C / [Def_C,Def_C]
```

cannot be displayed as a product of Artin permutation defect values inside
`Def_C`.

This applies already to the existing affine stress row in the audit suite.
For both the Schutzenberger observer and the kernel-block observer:

```text
|Def_C| = 3,
[Def_C,Def_C] = 1,
```

and `18` of the `27` completed row defects are nonidentity elements of
`Def_C`.  Thus those elementary defects have nontrivial abelianization and
cannot be Artin-defect products.

This is not outcome B.  It is a guardrail against an invalid A proof.  The
Sawin detector condition asks for the transported endpoint product

```text
D_C(beta) in V_beta(Def_C),
```

not for each elementary row defect to be an Artin permutation defect product.
The full longitude-value subgroup may contain abelian information through the
recursive longitudes themselves; Artin permutation defects do not.

## Correct remaining target

The current Green state is therefore:

1. `U_C/Def_C` is rack-detected by the defect-quotient theorem.
2. Elementary defects in `Def_C` are finite potential coboundaries
   `eta(q^a)eta(q)^-1`.
3. The Artin-defect-only display of elementary defects is blocked whenever a
   defect has nontrivial image in `Def_C/[Def_C,Def_C]`.

The remaining theorem must prove one of the following stronger but valid
statements.

- The transported endpoint product `D_C(beta)` lies in `V_beta(Def_C)` by a
  full recursive-longitude expression, not necessarily an Artin permutation
  defect expression.
- The potential transport cancels all abelianized defect contributions for
  every residual braid in `N_n`, leaving only commutator-subgroup data that
  can then be attacked by Artin-defect displays.
- A detector-lift structure exists for the potential transport itself, so the
  endpoint labels are ordinary recursive Artin-longitude values.

A counterexample route must still upgrade any remaining failure to a
normalized-law sequence invisible to every finite group while moving a
residual tuple.  A nontrivial abelian elementary defect at one row is not
enough.

## Executable audit hooks

The code records this barrier through:

```text
commutator_subgroup_elements(...)
green_defect_artin_abelianization_barrier_audit(...)
schutzenberger_defect_artin_abelianization_barrier_audits(...)
kernel_block_defect_artin_abelianization_barrier_audits(...)
```

The audit computes `[Def_C,Def_C]` inside the finite defect kernel and counts
the row defects outside it.  Such rows cannot have elementary Artin-defect
displays in `Def_C`.
