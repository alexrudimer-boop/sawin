# Linear F3 Collision Rows: Passive-Fibre Quotient Closure

Date: 2026-06-08

This note records the corrected all-arity closure for the passive-fibre
subfamily of the formal monolith-collision rows in the six-point linear
skew-over-flip family

```text
X={0,1} x F_3,
R((a,i),(b,j))=((b,I),(a,J)),
(I,J)^T=M_ab(i,j)^T.
```

It does not prove Sawin domination for all finite YBE solutions.  It removes
the passive-certified part of the first serious residual branch found in this
structured six-point family.

The generated audit is

```text
proofs/linear_f3_collision_quotient_invariant_audit.md
```

and verifies that the certificate below applies to `16` of the `32` formal
monolith-`J`-collision rows.  The other `16` rows fail the passive transport
condition in the audit and are not closed by this one-strand invariant.

## Normal Form

For every certified collision row, the monolith has one three-point block and
three singleton blocks.  After possibly swapping the two base fibres, write

```text
X=E union F,
E={e_a : a in F_3},
F={f_i : i in F_3},
```

where the monolith collapses `F` and keeps `E` separate.  The dual cases are
identical with `E` and `F` interchanged.

The local rules have the form

```text
R(f_i,f_j)=(f_i,f_j),
R(e_a,e_b)=(e_{I(a,b)},e_{J(a,b)}),
R(e_a,f_i)=(f_{S_a(i)},e_{\gamma(a)}),
R(f_i,e_a)=(e_{\sigma(a)},f_{T_a(i)}),
```

where each `S_a` and `T_a` is an affine permutation of `F_3`.

The audit checks the two identities needed for the invariant:

```text
S_a S_b = S_{I(a,b)} S_{J(a,b)},
S_{\sigma(a)} T_a = id.
```

The first identity is the singleton-singleton crossing compatibility; the
second is the mixed crossing compatibility.

There is also a necessary passive transport condition.  If a visible
singleton crosses a different collapsed-fibre strand to the left of the
tracked strand, the tracked hidden fibre does not move, but the visible label
in its left list changes.  Therefore the invariant below also requires

```text
S_{\alpha(a)} = S_a,
S_{\sigma(a)} = S_a.
```

The audit verifies this passive condition for exactly `16` formal collision
rows and records the `16` passive-failure rows separately.

## Quotient

For a certified row, collapse the monolith fibre:

```text
pi(e_a)=e_a,
pi(f_i)=F.
```

The quotient `Z={e_0,e_1,e_2,F}` is a braided quotient, and the audit verifies
that it is left- and right-nondegenerate for each of the `32` formal collision
rows.  For the `16` rows satisfying passive transport, the kernel inclusion
below follows.  By the known nondegenerate theorem, `Z` is dominated by its
finite derived rack.

It remains to prove

```text
ker rho^Z_n <= ker rho^X_n
```

for every arity `n`.

## Hidden-Fibre Invariant

In a quotient word, enumerate the `F`-letters from left to right.  Since

```text
R(f_i,f_j)=(f_i,f_j),
```

two `F`-strands never exchange hidden fibre coordinates.

Track the `s`-th `F`-strand.  Suppose at some moment it is lifted to `f_i` in
`X`, and the singleton quotient letters to its left are

```text
e_{a_1}, e_{a_2}, ..., e_{a_k}.
```

Define

```text
H_s = S_{a_1} S_{a_2} ... S_{a_k}(i) in F_3.
```

Because each `S_a` is a bijection, `H_s` determines `i` once the left singleton
list is known.

## Invariance

Only local crossings need to be checked.

First, crossing a singleton leftward across the tracked fibre strand gives

```text
e_a f_i -> f_{S_a(i)} e_{\gamma(a)}.
```

The left list loses its last `e_a`, while the hidden fibre changes from `i`
to `S_a(i)`.  Therefore `H_s` is unchanged.

Second, crossing the tracked fibre strand rightward across a singleton gives

```text
f_i e_a -> e_{\sigma(a)} f_{T_a(i)}.
```

The left list gains `e_{\sigma(a)}`, and the hidden fibre becomes `T_a(i)`.
The audited identity

```text
S_{\sigma(a)} T_a = id
```

shows that `H_s` is unchanged.

Third, crossing two singleton letters to the left of the tracked strand gives

```text
e_a e_b -> e_{I(a,b)} e_{J(a,b)}.
```

The audited identity

```text
S_a S_b = S_{I(a,b)} S_{J(a,b)}
```

shows that their contribution to the left-context action is unchanged.

Fourth, a singleton can cross a different `F`-strand to the left of the
tracked strand.  In a move

```text
e_a F -> F e_{\alpha(a)}
```

or

```text
F e_a -> e_{\sigma(a)} F,
```

the tracked hidden fibre does not change, but the visible left-list label
changes from `a` to `alpha(a)` or `sigma(a)`.  The passive transport
condition

```text
S_{\alpha(a)}=S_a,
S_{\sigma(a)}=S_a
```

keeps `H_s` unchanged.

Crossings to the right of the tracked strand do not affect its left list, and
crossings of two `F`-strands are the identity.  Thus every braid generator and
inverse generator preserves `H_s` in the certified rows.

## Kernel Inclusion

Let `beta in ker rho^Z_n`, and let `x in X^n`.  Put

```text
x' = rho^X_n(beta)(x).
```

Since `pi` is braided and `beta` fixes the quotient word,

```text
pi^n(x')=pi^n(x).
```

Therefore every singleton coordinate returns as the same singleton quotient
letter, and each tracked `F`-strand returns to the same quotient position with
the same singleton list to its left.

For each tracked `F`-strand, `H_s` is unchanged.  Since the final left list is
the initial left list and the corresponding affine map is bijective, its
hidden fibre coordinate is unchanged.  The singleton letters have no hidden
coordinate beyond the quotient.  Hence

```text
rho^X_n(beta)(x)=x.
```

Since `x` was arbitrary,

```text
ker rho^Z_n <= ker rho^X_n
```

for every `n`.

## Domination

Let `Y_Z` be the finite derived rack of the nondegenerate quotient `Z`.  Then

```text
ker rho^{Y_Z}_n <= ker rho^Z_n <= ker rho^X_n
```

for every `n`.  Thus each passive-certified collision row is finite-rack
dominated.

The passive-failure rows are not closed by this invariant.  In those rows the
visible label seen by a later tracked fibre changes when it crosses another
collapsed-fibre strand, and the corresponding `S`-map changes as well.  They
therefore require either a stronger multi-fibre invariant or an actual
quotient-kernel braid witness.
