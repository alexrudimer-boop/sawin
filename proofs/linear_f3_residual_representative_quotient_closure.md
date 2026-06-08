# Linear F3 Residual Representative Quotient Closure

Date: 2026-06-08

This note records an all-arity closure for one displayed six-point residual
representative in the linear skew-over-flip family.  It is not a proof of
Sawin domination for all finite YBE solutions.  It removes one serious local
candidate by showing that it is already dominated by a four-point
left-nondegenerate quotient.

## Representative

Let

```text
X={e_i,f_i : i in F_3}
```

with `e_i=(0,i)` and `f_i=(1,i)`.  The solution is

```text
R((a,i),(b,j))=((b,I),(a,J)),
(I,J)^T=M_ab (i,j)^T,
```

where

```text
M_00 = [0 1; 2 2],
M_01 = [1 2; 1 0],
M_10 = [0 1; 2 1],
M_11 = [1 0; 0 1].
```

Equivalently, using `2=-1` in `F_3`,

```text
R(e_a,e_b)=(e_b,e_{-a-b}),
R(e_a,f_i)=(f_{a-i},e_a),
R(f_i,e_a)=(e_a,f_{a-i}),
R(f_i,f_j)=(f_i,f_j).
```

The generated audit

```text
proofs/linear_f3_residual_representative_closure_audit.md
```

checks that this is degenerate, non-involutive, and YBE; it is row `20` in
the degenerate non-involutive linear F3 audit, with matrix indices
`(5,26,4,12)`.

## Quotient

Let `pi:X -> Z` collapse all `f_i` to one symbol `F` and keep the `e_a`
separate:

```text
pi(e_a)=e_a,
pi(f_i)=F.
```

Then `Z={e_0,e_1,e_2,F}` and the quotient table is

```text
R_Z(e_a,e_b)=(e_b,e_{-a-b}),
R_Z(e_a,F)=(F,e_a),
R_Z(F,e_a)=(e_a,F),
R_Z(F,F)=(F,F).
```

For each fixed first input, the first output is a permutation of `Z`; hence
`Z` is left-nondegenerate.  By the known nondegenerate theorem, `Z` is
dominated by its finite derived rack.

It remains to prove

```text
ker rho^Z_n <= ker rho^X_n
```

for every `n`.

## Alternating-Sum Invariant

Track the `s`-th `F`-strand from the left in a quotient word.  Because

```text
R_Z(F,F)=(F,F),
```

two `F`-strands never pass each other, so this strand is well-defined through
any braid trajectory.

Suppose at some moment the tracked `F`-strand is lifted to `f_i` in `X`, and
the `e`-letters to its left are

```text
e_{a_1}, e_{a_2}, ..., e_{a_k}.
```

Define

```text
H_s = (-1)^k i + sum_{r=1}^k (-1)^{r-1} a_r  in F_3.
```

This quantity is invariant under each positive braid generator, hence also
under each inverse generator.

First consider crossing `e_a` past the tracked `F`-strand:

```text
e_a f_i -> f_{a-i} e_a.
```

The strand moves left across `e_a`, so the left list loses its last entry
`e_a`, while the fibre changes from `i` to `a-i`.  Substituting in the formula
for `H_s` gives the same value.  The opposite mixed crossing

```text
f_i e_a -> e_a f_{a-i}
```

is the same calculation reversed: the left list gains `e_a`, and the same
fibre update compensates it.

Next consider a crossing of two `e`-letters to the left of the tracked
`F`-strand:

```text
e_a e_b -> e_b e_{-a-b}.
```

If these occur at positions `r,r+1` in the tracked left list, their old
contribution is

```text
(-1)^{r-1}a + (-1)^r b = (-1)^{r-1}(a-b).
```

Their new contribution is

```text
(-1)^{r-1}b + (-1)^r(-a-b)
  = (-1)^{r-1}(b+a+b)
  = (-1)^{r-1}(a-b),
```

because `2b=-b` in `F_3`.  Thus this crossing also preserves `H_s`.

Crossings of two `e`-letters to the right of the tracked `F`-strand do not
affect its left list.  Crossings of two `F`-strands are the identity in both
`X` and `Z`.  Therefore all local braid moves preserve `H_s`.

## Kernel Inclusion

Let `beta in ker rho^Z_n` and take any `x in X^n`.  Put

```text
x' = rho^X_n(beta)(x).
```

Since `pi` is a braided quotient and `beta` fixes the quotient word,

```text
pi^n(x')=pi^n(x).
```

Therefore each `e_a` coordinate returns as the same `e_a`, and each `F`
position returns to the same coordinate with the same left `e`-list.  For each
tracked `F`-strand, the invariant `H_s` is unchanged and the final left list
is the initial left list.  Hence its fibre `i` is unchanged.  Thus every
coordinate of `x` is fixed:

```text
rho^X_n(beta)(x)=x.
```

Since `x` was arbitrary,

```text
ker rho^Z_n <= ker rho^X_n
```

for every `n`.

## Domination

Let `Y_Z` be the finite derived rack of the left-nondegenerate quotient `Z`.
Then

```text
ker rho^{Y_Z}_n <= ker rho^Z_n <= ker rho^X_n
```

for every `n`.  Hence this six-point residual representative is dominated by
a finite rack.

The formal monolith `J`-collision in this row is therefore not braid-realized:
inside an all-`F` block, the braid action is trivial on the `f_i` fibres, and
mixed motion is controlled by the alternating-sum invariant above.
