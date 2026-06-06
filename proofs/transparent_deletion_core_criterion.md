# Transparent Deletion Core Criterion

Date: 2026-06-06

This note records a proof-grade conditional narrowing of Sawin's finite-rack
domination problem.  It does not prove domination for every finite bijective
YBE solution, and it does not give a counterexample.  It sharpens what a
negative example must do after the fixed-arity rack cofinality theorem.

## Transparent Rack Extension

Let `Y` be a rack with operation `*`.  Define

```text
Y^0 = Y sqcup {0}
```

by extending the operation as follows:

```text
a*b = old a*b      for a,b in Y,
0*b = b,
a*0 = 0,
0*0 = 0.
```

Then `Y^0` is a rack.  The left translation by `0` is the identity, and the
left translation by `a in Y` is the old left translation on `Y` together with
the fixed point `0`, hence every left translation is bijective.  The
self-distributivity identity follows by a direct case split on whether one of
the three variables is `0`; if all variables lie in `Y`, it is the old rack
identity, and if the right input in a product is `0`, both sides are forced to
`0`.

Equivalently, `Y^0` is the flip-across disjoint union of `Y` with the one-point
trivial rack.  The helper `transparent_rack_extension` constructs this finite
rack in the workspace.

## Deletion Lemma

Let `beta in P_n` be pure, let `I subset {1,...,n}`, and let

```text
partial_I beta in P_|I|
```

be the braid obtained by deleting all strands outside `I`.

If `Y^0` is the transparent extension above and an input in `(Y^0)^n` is
colored by arbitrary `Y`-colors on the strands in `I` and by `0` on all other
strands, then the retained `I`-coordinates after acting by `beta` are exactly
the `Y`-rack action of `partial_I beta`.

Consequently,

```text
beta in ker rho^{Y^0}_n  =>  partial_I beta in ker rho^Y_|I|.
```

The purity hypothesis is essential: it guarantees that the deleted strands
return to the deleted positions and that the retained coordinates are still
read on the same subset after the braid action.

## Relative Bounded-Deletion Core Theorem

Assume the fixed-arity rack cofinality theorem: for every finite quotient
representation of `B_k`, in particular for `rho^X_k`, there is a finite rack
`Z_k` with

```text
ker rho^{Z_k}_k <= ker rho^X_k.
```

Let `X` be a finite bijective YBE solution.  Suppose there are a finite rack
`Y_0` and an integer `N` such that for every `n` and every

```text
beta in ker rho^{Y_0^0 x T_2}_n,
```

where `T_2` is the two-element trivial rack, the implication

```text
rho^X_n(beta) != 1
  =>
there is I with 2 <= |I| <= N and rho^X_|I|(partial_I beta) != 1
```

holds.  Then `X` is dominated by one finite rack.

Proof.  For each `2 <= k <= N`, choose a finite rack `Z_k` with

```text
ker rho^{Z_k}_k <= ker rho^X_k,
```

and replace it by its transparent extension `Z_k^0`.  Since `Z_k` is a
subrack of `Z_k^0`,

```text
ker rho^{Z_k^0}_k <= ker rho^{Z_k}_k <= ker rho^X_k.
```

Now set

```text
Y = Y_0^0 x T_2 x prod_{k=2}^N Z_k^0.
```

Let `beta in ker rho^Y_n`.  The `T_2` factor forces `beta` to be pure.  If
`rho^X_n(beta) != 1`, the bounded-deletion hypothesis gives a subset `I` with
`|I|=k <= N` and `rho^X_k(partial_I beta) != 1`.  But `beta` is in the kernel
of the `Z_k^0` factor, so by the deletion lemma

```text
partial_I beta in ker rho^{Z_k^0}_k <= ker rho^X_k,
```

a contradiction.  Hence every `beta in ker rho^Y_n` is `X`-invisible in every
arity, so `Y` dominates `X`.

## Contrapositive Obstruction Target

If a finite bijective YBE solution `X` is not dominated by any finite rack,
then for every finite rack prefix `P_m` and every deletion cutoff `N`, there
must exist some arity `n` and pure braid `beta in P_n` such that

```text
rho^{P_m^0 x T_2}_n(beta) = 1,
rho^X_n(beta) != 1,
```

while every bounded deletion shadow is already `X`-invisible:

```text
rho^X_|I|(partial_I beta) = 1
for all I with 2 <= |I| <= N.
```

Thus a genuine negative answer requires more than a Brunnian braid missed by
one detector.  It requires a cofinal sequence of rack-prefix-invisible,
`X`-visible pure braids whose `X`-visibility has unbounded deletion support.

## Status

The theorem is conditional.  The remaining positive obligation is a uniform
bounded-deletion core theorem for every finite degenerate `X`.  The remaining
negative obligation is an explicit finite degenerate `X` with the cofinal
rack-prefix and unbounded deletion-support witnesses above.

The later note `proofs/fully_brunnian_core_reduction.md` strengthens this
criterion: any transparent rack detector failure can be chosen fully
deletion-minimal, with every proper `X`-deletion shadow trivial.
