# Opposite detectability closure

Date: 2026-05-28

This note upgrades the left/right dual bookkeeping from
`proofs/dual_green_symmetry.md` to a theorem-level closure property for the
sharp finite-group detector condition.

## Setup

For a finite braided set `X`, let

```text
X^op = P R_X P
```

where `P(x,y)=(y,x)`.  Thus

```text
R_{X^op}(x,y) = P R_X(y,x).
```

For braid degree `n`, let `J_n:X^n -> X^n` reverse tuple order:

```text
J_n(x_1,...,x_n) = (x_n,...,x_1).
```

Let `rev_n:B_n -> B_n` be the braid automorphism

```text
rev_n(sigma_i) = sigma_{n-i}.
```

## Braid Action Relation

For every braid `beta in B_n`,

```text
rho_{X^op,n}(beta)
  =
J_n rho_{X,n}(rev_n(beta)) J_n.
```

It is enough to check one generator.  On the `i,i+1` coordinates, reversing
the tuple swaps those two inputs and moves them to positions `n-i,n-i+1`.
Applying the original crossing and reversing back gives exactly
`P R_X P`, the opposite crossing.  The word statement follows by induction.

## Longitude Invariance

Finite-group longitude identity is invariant under `rev_n`.  The Artin
representation intertwines `rev_n` with the free-generator reversal

```text
x_i -> x_{n+1-i}.
```

Therefore the recursive Artin permutation is merely conjugated by index
reversal, and the longitudes are obtained from the original longitudes by the
same index reversal and free-generator relabelling.  Since
`Lambda_{G,n}(beta)=Lambda_{G,n}(1)` quantifies over all assignments
`F_n -> G`, relabelling the free generators does not change whether every
longitude evaluates to the identity.

Thus, for every finite group `G`,

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)
iff
Lambda_{G,n}(rev_n(beta))=Lambda_{G,n}(1).
```

## Detectability Consequence

Suppose a finite group `G` detects `X` in the sharp kernel form:

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)
  => rho_{X,n}(beta)=1
```

for every `n`.  If `Lambda_{G,n}(beta)=Lambda_{G,n}(1)`, then by longitude
invariance the reversed braid `rev_n(beta)` also has identity finite-`G`
longitude data.  Hence

```text
rho_{X,n}(rev_n(beta))=1.
```

The braid-action relation gives

```text
rho_{X^op,n}(beta)=J_n 1 J_n=1.
```

So the same finite group `G`, and therefore the same detector rack `A_G`,
detects `X^op`.  Since `(X^op)^op=X`, finite-G detectability is equivalent
for `X` and `X^op`.

## Relevance

This is stronger than the finite Green audit symmetry.  It shows that any
whole-solution finite-G proof automatically has a right-handed counterpart.
For the local program it justifies treating left and right Green/kernel
detector factors symmetrically: a final A proof may multiply both sides into
one finite detector group, and a B construction must escape both because
passing to the side-opposite solution cannot create a new undetected
mechanism.

## Executable Checks

The helper `reverse_braid_word(n,word)` implements `rev_n`.  Regression tests
verify:

- `reverse_braid_word` is involutive;
- the opposite-solution braid action is `J rho_X(rev(beta)) J`;
- identity finite-group longitude signature is invariant under strand
  reversal in representative words.
