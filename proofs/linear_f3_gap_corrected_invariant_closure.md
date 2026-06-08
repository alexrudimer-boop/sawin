# Linear F3 Collision Rows: Gap-Corrected Quotient Closure

Date: 2026-06-08

This note records the corrected all-arity closure for all `32` formal
monolith-`J`-collision rows in the six-point linear skew-over-flip family

```text
X={0,1} x F_3,
R((a,i),(b,j))=((b,I),(a,J)),
(I,J)^T=M_ab(i,j)^T.
```

The generated audit is

```text
proofs/linear_f3_gap_corrected_invariant_audit.md
```

It verifies the local identities below for all `32` rows and directly checks
the resulting tagged-strand invariant through arity `5` for positive and
negative local crossings.

This does not solve Sawin's problem in full.  It removes the formal
monolith-collision half of the structured six-point linear `F_3`
skew-over-flip residual branch.

## Setup

For each of the `32` rows, the monolith has one three-point block and three
singleton blocks.  After possibly swapping the two base fibres, write

```text
X=E union F,
E={e_a : a in F_3},
F={f_i : i in F_3}.
```

The monolith collapses `F` and keeps `E` separate.  The dual cases are the
same with `E` and `F` interchanged.

Collapse the monolith fibre:

```text
pi(e_a)=e_a,
pi(f_i)=F.
```

The quotient `Z={e_0,e_1,e_2,F}` is a finite nondegenerate braided set in all
`32` rows, so `Z` is dominated by its derived rack.

The lift has local form

```text
R(F_i,F_j)=(F_i,F_j),
R(z,F_i)=(F_{S_z(i)}, alpha(z)),
R(F_i,z)=(beta(z), F_{T_z(i)}),
```

for visible singleton labels `z in Z\{F}`.  Here `S_z` and `T_z` are affine
permutations of `F_3`, and `alpha,beta` are permutations of the three visible
labels.

The audit verifies:

```text
beta = alpha^{-1},
S_{beta(z)} T_z = id,
R(F_i,F_j)=(F_i,F_j),
```

and, for every visible-visible quotient crossing

```text
R_Z(z,w)=(u,v),
```

and every power `alpha^g`,

```text
S_{alpha^g(z)} S_{alpha^g(w)}
  =
S_{alpha^g(u)} S_{alpha^g(v)}.
```

These are exactly the local identities needed below.

## Gap-Corrected Invariant

In a quotient word, enumerate the `F`-letters from left to right.  Because

```text
R(F_i,F_j)=(F_i,F_j),
```

two hidden `F`-strands never exchange order.

Track the `s`-th `F`-strand.  Suppose it is currently lifted to `F_i`.  For
each visible singleton label `z` to its left, let

```text
gap_s(z) = number of F-strands strictly between z and the tracked strand.
```

Read the visible labels to the left of the tracked strand from left to right:

```text
z_1, z_2, ..., z_k.
```

Define

```text
H_s =
S_{alpha^{gap_s(z_1)}(z_1)}
S_{alpha^{gap_s(z_2)}(z_2)}
...
S_{alpha^{gap_s(z_k)}(z_k)}(i).
```

The older one-strand invariant used `S_z` directly.  That failed when a
visible label crossed a different `F`-strand to the left of the tracked
strand.  The corrected invariant uses the number of intervening `F`-strands
to normalize that visible label.

## Local Invariance

Only local braid moves need to be checked.

First, if the tracked strand crosses leftward past a visible label,

```text
z F_i -> F_{S_z(i)} alpha(z),
```

then `z` was immediately to the left of the tracked strand, so its gap was
`0`.  The factor `S_z` is removed from the left-list product, and the hidden
fibre changes from `i` to `S_z(i)`.  Thus `H_s` is unchanged.

Second, if the tracked strand crosses rightward past a visible label,

```text
F_i z -> beta(z) F_{T_z(i)},
```

then `beta(z)` is added immediately to the left of the tracked strand, again
with gap `0`.  The audited identity

```text
S_{beta(z)} T_z = id
```

preserves `H_s`.

Third, if two visible labels cross to the left of the tracked strand,

```text
z w -> u v,
```

then the two adjacent visible labels have the same gap `g` from the tracked
strand.  The audited identity

```text
S_{alpha^g(z)} S_{alpha^g(w)}
  =
S_{alpha^g(u)} S_{alpha^g(v)}
```

preserves their contribution to `H_s`.

Fourth, suppose a visible label crosses a different `F`-strand to the left of
the tracked strand.  In a move

```text
z F_j -> F_j alpha(z),
```

the visible label moves one `F`-strand closer to the tracked strand, so its
gap decreases by `1`, while its label changes from `z` to `alpha(z)`.  The
effective label is unchanged:

```text
alpha^{g-1}(alpha(z)) = alpha^g(z).
```

In the reverse mixed move

```text
F_j z -> beta(z) F_j,
```

the visible label moves one `F`-strand farther from the tracked strand, so
its gap increases by `1`, while its label changes from `z` to `beta(z)`.
Since `beta=alpha^{-1}`,

```text
alpha^{g+1}(beta(z)) = alpha^g(z).
```

So passive visible-label transport also preserves `H_s`.

All remaining crossings occur to the right of the tracked strand or are
`F`-`F` identity crossings.  Therefore every positive and negative braid
generator preserves every `H_s`.

## Kernel Inclusion

Let

```text
beta_braid in ker rho^Z_n.
```

For any `x in X^n`, put

```text
x' = rho^X_n(beta_braid)(x).
```

Since `pi:X -> Z` is braided and `beta_braid` fixes the quotient word,

```text
pi^n(x')=pi^n(x).
```

Thus each tracked `F`-strand returns to the same quotient position, with the
same visible labels and the same gap values to its left.  The invariant `H_s`
is unchanged, and the product of affine permutations defining `H_s` is
bijective.  Hence the hidden fibre coordinate `i` of the tracked strand is
unchanged.

All non-`F` quotient fibres are singletons.  Therefore

```text
rho^X_n(beta_braid)(x)=x
```

for every `x in X^n`, and hence

```text
ker rho^Z_n <= ker rho^X_n
```

for all arities `n`.

## Domination

Let `Y_Z` be the finite derived rack of the nondegenerate quotient `Z`.  Then

```text
ker rho^{Y_Z}_n <= ker rho^Z_n <= ker rho^X_n
```

for every `n`.  Therefore all `32` formal monolith-collision rows in this
six-point linear `F_3` family are finite-rack dominated.

The remaining rows in this family were already on the monolith
`J`-separating side of the relative contextual criterion or outside the
subdirect collision branch.  The next counterexample search should therefore
leave this formal-collision residual pattern.
