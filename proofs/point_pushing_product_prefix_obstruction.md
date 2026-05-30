# Point-pushing product-prefix obstruction

Date: 2026-05-30

This note repairs the product-prefix B route after
`proofs/last_strand_law_gap_audit.md`.  Ordinary laws are not enough to put a
last-strand point-pushing braid in `K_G`.  Nevertheless, if finite-rack
domination fails, the normalized-law obstruction can still be chosen from
genuine point-pushing `K_G` layers.

This does not prove outcome B by itself.  It says that a B proof may search
for actual point-pushing finite-longitude kernel layers without losing
generality.

## Setup

For a finite group `G`, write

```text
K_G(n) = { beta in B_n : Lambda_{G,n}(beta)=Lambda_{G,n}(1) }.
```

Let

```text
iota_r:F_{r-1}->P_r
```

be the standard last-strand point-pushing embedding in `B_r`.

Enumerate all finite groups up to isomorphism:

```text
G_1,G_2,G_3,...
```

and set

```text
P_j=G_1 x ... x G_j.
```

## Theorem

Let `X` be a finite nonempty bijective YBE solution.  If `X` is not
finitely rack-dominated, then for every `j>=1` there are:

```text
r_j >= 2,
w_j in F_{r_j-1},
lambda_j = iota_{r_j}(w_j) in B_{r_j},
x_j in X^{r_j},
```

such that

```text
lambda_j in K_{P_j}(r_j)
```

and

```text
rho_{X,r_j}(lambda_j)(x_j) != x_j.
```

Consequently the right-stabilized braids

```text
q_j = r_j + j,
beta_j = lambda_j with j unused right strands
```

form a normalized-law obstruction sequence:

1. `q_j -> infinity`;
2. `rho_{X,q_j}(beta_j) != 1`;
3. for every fixed finite group `G`,

   ```text
   beta_j in K_G(q_j)
   ```

   for all sufficiently large `j`.

## Proof

By `proofs/normalized_law_domination_dichotomy.md`, finite-rack domination is
equivalent to the existence of one finite group `G` satisfying

```text
K_G(n) subset ker rho_{X,n}
```

for every `n`.

Assume no such group exists.  Then no product-prefix group `P_j` satisfies
this inclusion.  Therefore, for each `j`, choose `n_j` and

```text
alpha_j in K_{P_j}(n_j)
```

such that

```text
rho_{X,n_j}(alpha_j) != 1.
```

Apply `proofs/point_pushing_kernel_layer_criterion.md` to the finite group
`P_j`.  The contrapositive of that criterion says that a moving braid in
`K_{P_j}` has a moving last-strand point-pushing layer which still lies in
`K_{P_j}`.  Hence there are `r_j`, `w_j`, and

```text
lambda_j=iota_{r_j}(w_j) in K_{P_j}(r_j)
```

with

```text
rho_{X,r_j}(lambda_j) != 1.
```

Choose a moved tuple `x_j in X^{r_j}`.

Now right-stabilize by adding `j` unused strands.  Since `X` is nonempty,
choose any `x_0 in X` and extend

```text
tilde x_j=(x_j,x_0,...,x_0) in X^{r_j+j}.
```

The stabilized braid `beta_j` still moves `tilde x_j`, because it acts as
`lambda_j` on the first `r_j` strands and trivially on the added strands.
Also `q_j=r_j+j -> infinity`.

Right stabilization preserves identity finite-longitude data: old longitudes
are unchanged and the added strands have trivial longitude.  Thus

```text
beta_j in K_{P_j}(q_j).
```

Fix any finite group `G`.  Choose `t` such that `G` is isomorphic to `G_t`.
For every `j>=t`, the projection

```text
P_j -> G_t
```

sends identity `P_j` finite-longitude data to identity `G_t`
finite-longitude data.  Transporting along the isomorphism gives

```text
beta_j in K_G(q_j)
```

for all `j>=t`.  Hence the sequence is eventually invisible to every finite
group while still moving `X`.  QED.

## Relation To Ordinary Laws And Derivatives

Each extracted word satisfies the necessary ordinary-law condition

```text
w_j in Law_{r_j-1}(P_j),
```

because `iota_{r_j}(w_j) in K_{P_j}(r_j)`.  This is only a consequence, not
the certificate.  The certificate is the actual finite-longitude condition

```text
iota_{r_j}(w_j) in K_{P_j}(r_j).
```

Equivalently, in the derivative-detector language of
`proofs/point_pushing_kernel_layer_criterion.md`, `w_j` fixes every
endpoint-identity detector state for `P_j`.  A stronger but sufficient
certificate would be that `w_j` is a law on the full derivative detector
`D_{r_j-1}(P_j)`.

Thus the repaired B route is:

```text
for every j, construct a moving point-pushing layer in K_{P_j},
then right-stabilize it.
```

A word which is merely an ordinary law on `P_j` is not enough.
