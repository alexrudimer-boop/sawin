# Involutive and permutation-form detector branch

Date: 2026-05-28

This note records the symbolic finite-rack domination argument for two known
finite-G-measurable branches.  It is a branch proof used by the local
reduction ledger; it is not the Master Local-Minimal Residual Theorem.

## Involutive Solutions

Let `X` be a finite bijective YBE solution such that `R_X^2=id` on `X x X`.
For every braid index `n`, the braid generators

```text
R_i = id^{i-1} x R_X x id^{n-i-1}
```

satisfy the braid relations and the Coxeter relations `R_i^2=id`.  Therefore
the braid action factors through the symmetric group `S_n`.

Let `T_2` be the two-point trivial rack.  Its braid action on `T_2^n` is the
ordinary coordinate-permutation action, so

```text
ker rho_{T_2,n} = P_n,
```

the pure braid group.  Since every involutive solution factors through
`S_n`, every pure braid acts trivially on `X^n`.  Hence

```text
ker rho_{T_2,n} subset ker rho_{X,n}
```

for every `n`.

In the sharp-obstruction language this is the case `G=1`: identity
finite-group longitude data for the trivial group is exactly identity Artin
permutation, and the residual involutive action is already trivial on pure
braids.  The purity condition comes from the `T_2` factor in `A_G`; see
`proofs/purity_stabilization.md`.

The same argument applies to a local interval whose total residual table is
involutive: after the quotient action is fixed, the residual table still has
only Coxeter motion, so the trivial group factor kills the interval.

## Permutation-Form Solutions

Now suppose

```text
R_X(x,y) = (sigma(y), tau(x))
```

for commuting permutations `sigma,tau in Sym(X)`.  The Yang-Baxter equation
for such a table is exactly the commutation relation `sigma tau = tau sigma`.
Set

```text
h = sigma tau,
m = order(h).
```

The finite detector group for this branch is the cyclic group `C_m`.

For a positive crossing, the strand moving left receives `sigma` and the
strand moving right receives `tau`.  For a negative crossing, the same
statement holds with `sigma^{-1}` and `tau^{-1}`.  Since `sigma` and `tau`
commute, the action of a braid on a labelled strand is recorded by two
integer exponents together with the Artin strand permutation.  The formula
below is intentionally only for pure braids: for a single positive crossing
it would be false, and the detector implication does not need it there.

More precisely, let `L_j(beta)` be the recursive Artin longitude and let

```text
epsilon:F_n -> Z,    x_i |-> 1
```

be the total-exponent homomorphism.  A direct induction over braid letters,
using the same update rules as the Artin longitude recursion, gives for
`beta in P_n`:

```text
rho_{X,n}(beta)(x)_j = h^{epsilon(L_j(beta))}(x_j).
```

Thus if the finite-`C_m` Artin-longitude data of `beta` is trivial, then the
Artin permutation is identity and every `epsilon(L_j(beta))` is `0 mod m`.
It follows that every `h^{epsilon(L_j(beta))}` is the identity permutation of
`X`, so `rho_{X,n}(beta)=1`.

Therefore the rack `A_{C_m}` from the sharp obstruction theorem dominates
every finite permutation-form solution, and the group `C_m` is independent of
the braid index.

## Local Use

For a quotient interval `pi:X->Z` dominated at the base by `Q`, if the
residual local table belongs to either of these branches, the local detector
is:

- `G=1` for the involutive case;
- `G=C_m`, where `m=order(sigma tau)`, for the permutation-form case.

Then `Q x A_G` dominates the interval by the sharp obstruction theorem, and
the congruence-chain induction may pass this factor down to lower intervals.

The helper functions

```text
permutation_solution_maps(X)
permutation_solution_twist_order(X)
permutation_solution_pure_longitude_factorization(X,beta,x)
```

extract `sigma`, `tau`, and `m`, and check the pure-longitude formula against
the direct braid action for finite permutation-form tables.  They are audit
helpers only; the proof above is the all-`n` argument.
