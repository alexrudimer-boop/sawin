# Diagonal normalized obstruction lemma

Date: 2026-05-28

This note records the exact logical bridge from "no finite detector group" to
the normalized-law obstruction sequence required for outcome B.

## Statement

Fix a finite quotient/residual problem

```text
pi : X -> Z,
N_n = ker rho_{Q,n},
Delta_n : N_n -> product_z Sym(X_z),
```

where `Q` is a finite rack dominating the quotient `Z`.  Suppose that no
finite group `G` satisfies the sharp kernel implication

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)  =>  Delta_n(beta)=1
```

for all `n` and all `beta in N_n`.

Then there is a sequence of braid indices `q_j -> infinity` and braids
`beta_j in N_{q_j}` such that, for every finite group `G`,

```text
Lambda_{G,q_j}(beta_j)=Lambda_{G,q_j}(1)
```

for all sufficiently large `j`, while

```text
Delta_{q_j}(beta_j) != 1.
```

Thus, once an explicit interval is proved to have no finite detector group,
the normalized-law obstruction sequence follows formally.

## Proof

Enumerate the isomorphism classes of finite groups as

```text
G_1, G_2, G_3, ...
```

and set

```text
H_j = G_1 x ... x G_j.
```

The direct-product longitude lemma says that identity longitude data in
`H_j` is equivalent to identity longitude data in every factor `G_i` with
`i <= j`.

Since no finite group detects the residual action, the finite group `H_j`
also fails.  Therefore there exist a braid degree `n_j` and a braid
`alpha_j in N_{n_j}` such that

```text
Lambda_{H_j,n_j}(alpha_j)=Lambda_{H_j,n_j}(1),
Delta_{n_j}(alpha_j) != 1.
```

For any fixed finite group `G_k`, the projection `H_j -> G_k` implies

```text
Lambda_{G_k,n_j}(alpha_j)=Lambda_{G_k,n_j}(1)
```

for every `j >= k`.

It remains only to force braid index growth.  Include `B_{n_j}` into
`B_{q_j}` by adding unused strands on the right, with for instance
`q_j = n_j + j`.  The same braid word acts on the first `n_j` strands and
leaves the added strands fixed.  If `alpha_j` fixes every `Q`-base tuple in
degree `n_j`, then the stabilized braid fixes every `Q`-base tuple in degree
`q_j`; hence the stabilized braid lies in `N_{q_j}`.  A moved residual tuple
for `alpha_j` is extended by arbitrary fibre points on the added strands, so
the stabilized residual action is still nontrivial.

Artin longitude data is stable under this right-strand inclusion: the old
recursive longitudes are unchanged after viewing them in the larger free
group, and the added strands have identity permutation and empty longitudes.
Consequently the stabilized braid is still invisible to `H_j`, and hence to
each `G_i` with `i <= j`.  Since `q_j = n_j+j`, the braid indices tend to
infinity.

## Global one-point case

For a whole finite YBE solution `X`, take the one-point quotient.  Then
`N_n=B_n`, and `Delta_n` is just the braid action on `X^n`.  If no finite
group `G` detects `X` through the sharp kernel form, the same diagonal
argument gives braid words moving explicit tuples in `X^{q_j}` while their
finite-group Artin-longitude data is eventually trivial for every fixed
finite group.

Combined with the sharp obstruction theorem, this explains why a genuine B
counterexample can be presented in normalized-law form.  The hard part is
not the diagonalization; it is proving, for an explicit finite YBE solution,
that every finite group detector fails.

## Executable convention checks

The helper

```text
diagonal_product_invisibility_audit(groups,n,beta)
```

checks the product step: identity finite-longitude signature in
`prod_i G_i` is equivalent to identity finite-longitude signature in every
listed factor `G_i`.  This locks the convention used when the proof replaces
the first `j` finite groups by the single product `H_j`.

The helper

```text
right_stabilization_longitude_audit(n,beta,extra)
```

checks the right-strand inclusion `B_n -> B_{n+extra}`: the old Artin
permutation and recursive longitudes are preserved on the first `n` strands,
and the added strands have trivial permutation and empty longitude data.

The unit tests

```text
test_diagonal_product_invisibility_equivalent_to_factors
test_right_stabilization_preserves_longitude_data
```

exercise these helpers on standard pure braid generators.  These are
convention checks, not finite-search proofs; the all-`n` reason the
diagonalization is valid is the argument above.
