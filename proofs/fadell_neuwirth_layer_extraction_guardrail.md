# Fadell-Neuwirth layer extraction guardrail

Date: 2026-05-30

This note supports `proofs/sawin_last_strand_law_reduction.md` and
`proofs/point_pushing_fixed_variety_domination.md`.  It does not prove
outcome A or B.  Its role is to make explicit the convention-sensitive step
used there: a moving braid in a finite-longitude kernel has a moving
last-strand point-pushing layer.

The statement is deliberately tied to the standard right-strand
Fadell-Neuwirth splitting.  It should not be read as permission to replace the
layers by arbitrary conjugated point-pushing subgroups without a separate
action-triviality check.

## Setup

For a finite group `G`, let

```text
K_G(n) =
{ beta in B_n :
  p_beta=id and phi(L_i(beta))=1
  for every phi:F_n->G and every i }.
```

For `n>=2`, let

```text
partial_n:P_n -> P_{n-1}
```

delete the last strand, and let

```text
s_n:P_{n-1}->P_n
```

be the splitting which adds one unused straight strand on the right.  The
kernel of `partial_n` is the free point-pushing subgroup

```text
F_{n-1}^{(n)}=<A_{1,n},...,A_{n-1,n}>.
```

Write `s_{r,n}:P_r->P_n` for repeated right stabilization, with
`s_{n,n}=id`:

```text
s_{r,n}=s_n s_{n-1} ... s_{r+1}.
```

## Kernel Preservation

Deletion and right splitting preserve finite-longitude kernels:

```text
partial_n(K_G(n)) subset K_G(n-1),
s_n(K_G(n-1)) subset K_G(n).
```

For deletion, quotient the free group by killing the deleted meridian:

```text
d_n:F_n->F_{n-1},    d_n(x_n)=1,    d_n(x_i)=x_i for i<n.
```

The recursive longitudes of `partial_n(beta)` are the images
`d_n(L_i(beta))` for `i<n`.  Any assignment `psi:F_{n-1}->G` extends to an
assignment `phi:F_n->G` by `phi(x_n)=1`, so identity of all `phi(L_i(beta))`
implies identity of all `psi(d_n(L_i(beta)))`.

For right splitting, the old longitudes are the same words in the old
variables and the new last longitude is trivial.  Thus every assignment
`F_n->G` restricts to one on `F_{n-1}`, and identity longitude data in degree
`n-1` gives identity longitude data after adding the unused last strand.

## Recursive Layer Decomposition

Let `beta_n in K_G(n)`.  Define recursively

```text
beta_{r-1}=partial_r(beta_r),
lambda_r=beta_r s_r(beta_{r-1})^{-1}
```

for `r=n,n-1,...,2`.  By kernel preservation, each `beta_r` lies in
`K_G(r)`.  Since `K_G(r)` is a subgroup and `s_r(beta_{r-1}) in K_G(r)`,

```text
lambda_r in K_G(r).
```

Also `partial_r(lambda_r)=1`, hence

```text
lambda_r in F_{r-1}^{(r)} cap K_G(r).
```

Thus there is a unique word `w_r in F_{r-1}` with

```text
lambda_r=iota_r(w_r),
```

where `iota_r(x_i)=A_{i,r}` is the standard last-strand point-pushing
embedding.

Iterating the recursion gives a product of right-stabilized layers:

```text
beta_n =
lambda_n *
s_n(lambda_{n-1}) *
s_{n-2,n}(lambda_{n-2}) *
...
```

with multiplication understood in the group order supplied by the recursion.
Equivalently, `beta_n` is a product of the factors

```text
s_{r,n}(lambda_r),    2<=r<=n.
```

The precise order is irrelevant for the extraction argument below; what
matters is that only these standard right-stabilized layers occur.

## Action Guardrail

Let `X` be any finite bijective YBE solution.  If

```text
rho_{X,r}(lambda_r)=1 on X^r,
```

then

```text
rho_{X,n}(s_{r,n}(lambda_r))=1 on X^n.
```

Indeed `s_{r,n}(lambda_r)` is represented by the same braid on the first `r`
strands and no crossings involving the added right-hand strands.  Its action
on `X^n` is therefore the action of `lambda_r` on the first `r` coordinates
and the identity on coordinates `r+1,...,n`.

Consequently, if every layer `lambda_r` acts trivially on its own `X^r`, then
every right-stabilized factor `s_{r,n}(lambda_r)` acts trivially on `X^n`.
Their product `beta_n` also acts trivially on `X^n`.

Taking the contrapositive:

```text
rho_{X,n}(beta_n) != 1
```

forces at least one layer `lambda_r=iota_r(w_r)` to satisfy

```text
rho_{X,r}(iota_r(w_r)) != 1.
```

Since `lambda_r in K_G(r)`, the point-pushing exactness lemma in
`proofs/sawin_last_strand_law_reduction.md` gives

```text
w_r in Law_{r-1}(G).
```

This is the exact moving-layer extraction used in the fixed-variety
criterion.

## Guardrail

The extraction is valid because the factors are right-stabilized ordinary
last-strand point-pushing layers.  If a future argument replaces them by
conjugated point-pushing layers, moved local corridors, or non-right
stabilizations, it must separately prove that triviality in the smaller
degree implies triviality after embedding in the larger braid action.
