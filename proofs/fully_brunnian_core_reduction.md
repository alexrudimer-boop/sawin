# Fully Brunnian Core Reduction

Date: 2026-06-06

This note strengthens the transparent deletion-core criterion.  It proves that
any failure of a transparent rack detector can be witnessed by a minimal-arity
pure braid whose every proper deletion is already `X`-invisible.

It is still a C-type reduction: it does not prove Sawin's statement and does
not construct a counterexample.

## Setup

Let `X` be a finite bijective YBE solution.  Let `Y` be a finite rack and let

```text
Q = Y^0 x T_2,
```

where `Y^0` is the transparent extension from
`proofs/transparent_deletion_core_criterion.md` and `T_2` is the two-element
trivial rack.  The `T_2` factor forces every `Q`-invisible braid to be pure.

For `n>=2`, define the fully deletion-minimal `X`-Brunnian `Q`-invisible core

```text
B_{X,Y}(n) =
{
  beta in ker rho^Q_n :
  rho^X_|I|(partial_I beta)=1
  for every proper I subsetneq {1,...,n}
}.
```

Here `partial_I beta` denotes deletion of all strands outside `I`.

## Exact Transparent Support Formula

Let `iota_I:Y^I -> (Y^0)^n` color the strands in `I` by elements of `Y` and
all other strands by the transparent color `0`.  For every braid `beta in B_n`
with underlying permutation `pi_beta`,

```text
rho^{Y^0}_n(beta) iota_I(c)
 =
iota_{pi_beta(I)}(rho^Y_|I|(partial_I beta)c).
```

Proof.  Check this on braid generators and inverse generators.  If both
crossing strands are `Y`-colored, the old `Y` rack crossing is applied.  If
both are transparent, the crossing is trivial on colors.  If exactly one is
transparent, then

```text
R_{Y^0}(0,a)=(a,0),   R_{Y^0}(a,0)=(0,a),
```

and the same equalities hold for inverse crossings, so the nontransparent
color simply passes through the transparent strand.  Thus a crossing
contributes to the retained color action exactly when both crossing strands
belong to `I`; otherwise it only updates the support positions.  Iterating
over a word for `beta` gives the formula.

Consequently, for pure `beta`,

```text
beta in ker rho^{Y^0}_n
  <=>
partial_I beta in ker rho^Y_|I| for every I.
```

One direction was enough for the bounded-deletion criterion.  The reverse
direction follows because every tuple in `(Y^0)^n` has some support `I` of
nontransparent coordinates, and the support is unchanged for pure `beta`.

## Fully Brunnian Core Theorem

The finite rack `Q=Y^0 x T_2` dominates `X` if and only if

```text
rho^X_n(beta)=1
```

for every `n>=2` and every `beta in B_{X,Y}(n)`.

Proof.  If `Q` dominates `X`, this is immediate because
`B_{X,Y}(n) subset ker rho^Q_n`.

Conversely, suppose `Q` does not dominate `X`.  Choose `n` minimal such that
there exists

```text
beta in ker rho^Q_n
```

with `rho^X_n(beta) != 1`.  Since `Q` contains `T_2`, `beta` is pure.  For
every proper subset `I`, the exact support formula gives

```text
partial_I beta in ker rho^Q_|I|.
```

If `rho^X_|I|(partial_I beta) != 1` for some proper `I`, then
`partial_I beta` would be a lower-arity `Q`-invisible, `X`-visible witness,
contradicting minimality of `n`.  Hence every proper deletion is
`X`-invisible, so `beta in B_{X,Y}(n)` while `rho^X_n(beta) != 1`.  This is
the contrapositive.

## Cofinal Prefix Consequence

Let `R_1,R_2,...` enumerate finite rack isomorphism classes, set

```text
P_m = R_1 x ... x R_m,
Q_m = P_m^0 x T_2.
```

If no finite rack dominates `X`, then for every `m` there exist `n_m` and
`beta_m in B_{n_m}` such that

```text
beta_m in ker rho^{Q_m}_{n_m},
rho^X_{n_m}(beta_m) != 1,
rho^X_|I|(partial_I beta_m)=1
  for every proper I subsetneq {1,...,n_m}.
```

Moreover `n_m -> infinity`.  If the witness arities were bounded by `N`, then
fixed-arity rack cofinality would give finitely many racks `Z_k`, `2<=k<=N`,
with

```text
ker rho^{Z_k}_k <= ker rho^X_k.
```

Once the prefix `P_m` contains all of these `Z_k`, no `Q_m`-invisible,
`X`-visible witness can occur in arity at most `N`, contradicting the
existence of the chosen witness.

Thus a genuine counterexample must supply an unbounded cofinal sequence of
rack-prefix-invisible, `X`-visible, fully deletion-minimal pure braids.

## Exact Remaining Implication

For a fixed finite `X`, Sawin-positive domination is equivalent to the
existence of a finite rack `Y_0` such that every fully deletion-minimal
`X`-Brunnian element in

```text
ker rho^{Y_0^0 x T_2}_n
```

is `X`-trivial in every arity.

If such `Y_0` exists, the theorem above says `Y_0^0 x T_2` dominates `X`.
Conversely, if a finite rack dominates `X`, adjoining a transparent color and
the `T_2` factor preserves domination and gives such a `Y_0`.

The remaining theoretical obligation is therefore Brunnian-core annihilation
for degenerate finite YBE solutions, or an explicit finite solution with a
cofinal prefix sequence of fully deletion-minimal witnesses.
