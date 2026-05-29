# Quotient/residual kernel checks

Date: 2026-05-28

This note records the executable form of the quotient/residual setup and the
kernel form of the sharp obstruction theorem.

## Implemented objects

`src/ybe_domination/residual.py` adds:

- `QuotientMap(total, quotient, pi)`, validating that `pi : X -> Z` is an
  onto braided-set homomorphism.
- `fibre(z)`, computing `X_z = product_i pi^{-1}(z_i)`.
- `residual_action(n,beta)`, computing `Delta_n(beta)` whenever `beta` fixes
  every base tuple in `Z^n`.
- `residual_is_identity(n,beta)`, checking whether `Delta_n(beta)=1`.
- `product_solution(X,Y)`, building the Cartesian product braided set.
- `sharp_kernel_implication_failures(...)`, a bounded audit of:

```text
beta in ker rho_{Q,n}
and Lambda_{G,n}(beta)=Lambda_{G,n}(1)
but Delta_n(beta) != 1.
```

## Sanity witness

The test suite includes a deliberately too-small detector.  Let the quotient
be the one-point identity solution, and let the total fibre be the two-element
permutation rack with a nontrivial flip `phi`:

```text
R(a,b) = (phi(b), a).
```

Then `sigma_1^2` is pure and invisible to the trivial group `G=1`, but it
moves the fibre tuple by applying `phi` to both coordinates.  The bounded
sharp-implication audit correctly reports this as a failure.

This is not a counterexample to Sawin domination.  It only shows that `G=1`
is too small.  A larger finite group, or equivalently the detector rack
`A_G`, can see nontrivial Artin longitudes of pure braids such as
`sigma_1^2`.

## Role in the proof search

The residual code gives an exact finite audit harness for candidate local
intervals:

1. verify the quotient map and fibre decomposition;
2. enumerate selected braid words in `N_n = ker rho_{Q,n}`;
3. evaluate the finite-group recursive longitude signature;
4. test whether the residual fibre action is trivial.

The harness cannot prove the master theorem by finite search.  Its useful role
is to prevent convention errors and to produce reproducible witnesses when a
candidate local obstruction is proposed.

The remaining theorem-level gap is still the uniform statement:

```text
there exists finite G = G(pi,Q), independent of n,
such that the kernel implication holds for all n and all beta in N_n.
```

