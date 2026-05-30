# Terminal gauge abelianization barrier

Date: 2026-05-30

This note corrects the strongest possible reading of
`proofs/terminal_gauge_artin_defect_target.md`.  It does not prove Sawin
finite-rack domination and it does not construct a counterexample.

The target stated there is useful only after the abelian part of the terminal
gauge endpoint has been handled.  A pure Artin permutation-defect display
cannot see nontrivial abelian terminal holonomy.

## Lemma: Artin-defect products are commutator-valued

Let `beta in B_n`, and let `p_beta` be the induced strand permutation.  For
every free word `w in F_n`, the Artin permutation defect

```text
beta(w) p_beta(w)^-1
```

has trivial image in the abelianization of `F_n`.

Proof.  The Artin action on `H_1(F_n)` is the permutation action induced by
`p_beta`.  Thus `beta(w)` and `p_beta(w)` have the same exponent vector, and
their quotient has exponent vector zero.  QED.

Consequently, for every homomorphism `psi:F_n -> U` into a finite group `U`,

```text
psi(beta(w) p_beta(w)^-1) in [U,U].
```

Any finite product of evaluated Artin permutation defects also lies in
`[U,U]`.

## Consequence for terminal gauge

Let `S_beta in U` be a terminal gauge/unit endpoint in one fixed
interval-level factor.  If `S_beta` has nontrivial image in

```text
U_ab = U/[U,U],
```

then `S_beta` cannot be displayed as a product of evaluated Artin permutation
defects in `U`.

This does not mean `S_beta` is outside `V_beta(U)`.  Ordinary recursive
Artin longitudes can carry abelian information.  The abelian part must be
proved by the finite abelian longitude matrix criterion from
`proofs/abelian_longitude_image_criterion.md`, not by Artin-defect displays.

## Corrected terminal gauge target

The valid final target is therefore the quotient-plus-kernel form already
prepared in `proofs/unit_continuation_abelian_kernel_lift.md`.

For every terminal gauge endpoint `S_beta in U`:

1. prove the abelianized endpoint

```text
q(S_beta) in V_beta(U_ab)
```

using the abelian longitude matrix;
2. lift that abelian witness to a witness value `v_beta in V_beta(U)`;
3. prove the commutator correction

```text
K_beta = S_beta v_beta^-1 in [U,U]
```

lies in `V_beta(U)`, for example by a full recursive-longitude witness,
Artin-defect display, detector-lift label, or further normal quotient split.

Only when `q(S_beta)=1` is the pure Artin-defect endpoint target strong
enough on its own.

## Derived-series form

Applying the same split down the finite derived series of `U` gives the
current honest route:

- finite solvable terminal gauge groups reduce to finitely many abelian
  matrix-longitude witnesses in fixed derived quotients;
- a nonsolvable terminal gauge obstruction must live in the stable perfect
  residual after all abelian quotients have been handled.

This is exactly the reduction recorded by
`proofs/unit_continuation_derived_series_reduction.md`.

## B-route consequence

A counterexample cannot be certified merely by saying that a terminal gauge
endpoint is not a product of Artin permutation defects.  If its abelian image
is nontrivial, that failure is expected and must be tested against ordinary
abelian longitude data.

A genuine B seed must instead defeat the corrected target:

```text
S_beta notin V_beta(U)
```

after all abelian quotient witnesses and commutator-kernel corrections are
allowed, and then it must still be upgraded to a normalized-law sequence
invisible to every finite group.

## Executable audit hook

The helper

```text
artin_defect_abelianization_barrier_audit(U, endpoints)
```

computes `[U,U]` and reports which supplied endpoints lie outside it.  Such
endpoints cannot have Artin-defect-only displays in `U`; they must be routed
through the abelian matrix and normal-quotient lift machinery instead.
