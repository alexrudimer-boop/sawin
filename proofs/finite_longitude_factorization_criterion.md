# Finite-longitude factorization criterion

Date: 2026-05-28

This note isolates the exact all-`n` bridge needed after the Green and
coordinate-kernel corridor diagnostics.  It is a theorem-level criterion, not
a proof that every local-minimal interval satisfies the criterion.

## The Finite-G Verbal Quotient

Fix a finite group `G` and a braid degree `n`.  Let

```text
F_n = <x_1,...,x_n>
```

and define

```text
K_G(n) = intersection ker(phi),
```

where `phi` ranges over all homomorphisms `F_n -> G`.  Equivalently, a word
`w in F_n` lies in `K_G(n)` exactly when `w` evaluates to the identity for
every assignment of the generators to elements of `G`.

The quotient

```text
W_G(n) = F_n / K_G(n)
```

is finite: the diagonal map from `F_n` to the product of all copies of `G`
indexed by assignments `G^n` has kernel `K_G(n)`.  Thus `W_G(n)` embeds in a
finite direct product of copies of `G`.

The quotient `W_G(n)` depends on `n`, but the detector rack `A_G` does not.
This distinction is important: using `W_G(n)` as a proof object does not make
the dominating rack depend on `n`.

## Relation with Artin Longitudes

For a braid `beta in B_n`, write its recursive Artin longitude data as

```text
beta(x_i) = L_i(beta) x_{p(i)} L_i(beta)^{-1},
```

with permutation `p`.  The executable convention is recorded in
`proofs/finite_group_longitudes.md`.

The finite-G longitude identity condition

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)
```

is exactly:

```text
p = identity
L_i(beta) in K_G(n) for every i.
```

Therefore such a braid acts trivially on `W_G(n)`: each generator satisfies

```text
x_i |-> L_i x_i L_i^{-1} = x_i        in W_G(n).
```

This proves the following sufficient criterion.

There is also a useful equivalent finite-subgroup viewpoint for a fixed
branch label group.  For a braid `beta`, let

```text
V_beta(G)=< phi(L_i(beta)) : phi:F_n -> G, 1<=i<=n > <= G.
```

If every residual label or holonomy element attached to `beta` lies in
`V_beta(G)`, then identity finite-`G` longitude data kills those residual
labels, because every generator of `V_beta(G)` is forced to be the identity.
The helpers `longitude_value_generators()` and
`longitude_value_subgroup_elements()` compute this fixed-word subgroup for an
explicit finite group.  The compact multi-group audit helper
`longitude_subgroup_profile()` records the Artin permutation, number of
longitude-value generators, and subgroup size for each listed group.  The
product-label version is recorded in
`proofs/product_longitude_subgroup_criterion.md`, and the generic profile is
summarized in `proofs/longitude_subgroup_profile.md`.

## Criterion

Let `pi : X -> Z` be a local interval over a quotient dominated by `Q`, and
let `N_n = ker rho_{Q,n}`.  Suppose there is a finite group `G`, depending on
the interval and on `Q` but not on `n`, such that for every `n` and every
base word `z in Z^n`, the residual action

```text
delta_{n,z}: N_n -> Sym(X_z)
```

factors through the Artin action on `W_G(n)`.

Then `G` satisfies the sharp kernel implication:

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)  =>  Delta_n(beta)=1
```

for every `n` and every `beta in N_n`.

Indeed, the left side says that `beta` acts trivially on `W_G(n)`, and the
factorization then forces every residual fibre action `delta_{n,z}(beta)` to
be trivial.

## What Remains

The Green/corridor program can now be phrased without ambiguity:

1. Construct a finite group `G(pi,Q)` from the interval data, for example from
   the two-sided symmetric Green kernel-block groups, Schutzenberger groups,
   and known-branch detector factors.
2. Prove that every residual corridor transport and Green branch choice
   factors through the Artin action on `W_G(n)` for all `n`.
3. Apply the criterion above and then the congruence-chain induction.

The current audits verify pieces of this picture only in finite diagnostic
windows.  They do not prove the factorization in item 2.

## Counterexample Translation

A B counterexample must violate every possible fixed finite-G factorization.
Equivalently, it must provide braid words `beta_j in B_{q_j}`, with
`q_j -> infinity`, such that for every finite group `G`,

```text
L_i(beta_j) in K_G(q_j) for all i
```

eventually, while the residual action on the proposed finite YBE solution is
nontrivial.  This is precisely the normalized-law obstruction sequence in the
problem statement.
