# Left-nondegenerate guitar branch

Date: 2026-05-30

This note records the already-known one-sided nondegenerate branch in the
detector language used by the rest of the repository.  It is not the Master
Local-Minimal Residual Theorem; it removes a known case before the fully
degenerate local theorem is invoked.

## Setup

Let `X` be a finite bijective set-theoretic Yang-Baxter solution and write

```text
R(x,y) = (sigma_x(y), rho_y(x)).
```

Assume `X` is left nondegenerate: every map

```text
sigma_x : X -> X
```

is a bijection.

The standard guitar-map theorem for left-nondegenerate braided sets constructs
a derived rack `D_X` on the same finite set.  In the convention used by the
workspace, the rack operation is

```text
a triangleright b =
  sigma_a(rho_{sigma_b^{-1}(a)}(b)).
```

Equivalently, if `R(b,t)=(a,v)`, then

```text
a triangleright b = sigma_a(v).
```

The executable constructor

```text
derived_rack_solution(X)
```

implements this operation and verifies that it is a finite rack.

## Guitar conjugacy

The guitar theorem gives bijections

```text
J_n : X^n -> X^n
```

for all braid indices `n`, natural in braid words, such that

```text
J_n rho_{X,n}(beta) = rho_{D_X,n}(beta) J_n
```

for every `beta in B_n`.

For `n=2`, this conjugacy has the visible form

```text
J_2(x,y) = (sigma_x(y), x),
```

and the equality

```text
J_2 R_X = R_{D_X} J_2
```

is exactly the derived-rack formula above.  The all-`n` theorem is the known
guitar-map extension of this two-strand identity.

## Detector consequence

Let

```text
G = Inn(D_X) <= Sym(X).
```

If

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1),
```

then the usual rack longitude factorization gives

```text
rho_{D_X,n}(beta)=1.
```

By guitar conjugacy,

```text
rho_{X,n}(beta)
  = J_n^{-1} rho_{D_X,n}(beta) J_n
  = 1.
```

Thus `G=Inn(D_X)` is a finite detector group for the left-nondegenerate
branch, independent of `n`.  Since `Inn(D_X)` acts faithfully on the finite set
`X`, it embeds in `Sym(X)`.  Therefore identity `Sym(X)` longitude data also
kills the left-nondegenerate branch.

## Role in the reduction ledger

The helper

```text
direct_symmetric_known_branch_reason(X)
```

now records this case as

```text
left_nondegenerate_guitar_derived_rack
```

whenever the table is left nondegenerate and the derived rack constructor
succeeds.  This is a closed known branch, not finite-search evidence.

The remaining master local theorem is therefore only needed after the
left-nondegenerate/guitar branch and the other known finite-`G` branches have
failed.
