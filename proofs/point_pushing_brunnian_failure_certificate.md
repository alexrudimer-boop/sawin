# Point-Pushing Brunnian Failure Certificate

Date: 2026-05-30

This note turns one non-base Brunnian gate failure into a full braid-action
certificate: a right-based Brunnian word, proof that it lies in the symmetric
detector kernel, and an explicit moved tuple of `X`.

It does not prove outcome A or B.  It gives the exact finite row format needed
for a homogeneous infinite B tail.

## Finite Row Certificate

Fix a finite bijective YBE solution `X`, a finite group `G`, and an arity
`k>=2`.  A Brunnian failure certificate consists of:

1. a failure kind

   ```text
   stabilizer, orbit_label, or orbit_relation;
   ```

2. a right-based word

   ```text
   w in F_k
   ```

   killed by deletion of the newly added far-left stationary strand;

3. detector identity

   ```text
   w=1 in D_k(G);
   ```

4. nontrivial YBE action

   ```text
   w!=1 in P_k(X),
   ```

   witnessed by a tuple of `X^{k+1}`.

Equivalently, for the point-pushing braid

```text
beta=iota_{k+1}(w),
```

one has

```text
beta in K_G(k+1),
rho_{X,k+1}(beta) != 1.
```

## Proof

The Brunnian orbit, stabilizer, and orbit-quotient notes prove that each of
the three real failure kinds produces a word in the relative kernel

```text
ker(F_k -> F_{k-1})
```

whose detector value is trivial and whose `X` action value is nontrivial.
The derivative detector criterion identifies detector-triviality of this word
with membership of the point-pushing braid in `K_G(k+1)`.  Direct evaluation
of the point-pushing braid on the displayed moved tuple proves the action is
nontrivial.

Thus a valid finite row certificate is a genuine point-pushing
detector-kernel mover.  QED.

## Infinite Tail Certificate

Suppose there is a finite solution `X` and, for every sufficiently large `j`,
a finite Brunnian failure certificate for `G=S_j` at arity `k_j`, with

```text
k_j -> infinity.
```

Let

```text
beta_j=iota_{k_j+1}(w_j).
```

Then

```text
beta_j in K_{S_j}(k_j+1),
rho_{X,k_j+1}(beta_j) != 1.
```

Right-stabilize by adding `j` trivial strands:

```text
q_j=k_j+1+j.
```

Stabilization preserves detector-kernel membership: the old recursive
longitudes are just stabilized, and the new straight strands have trivial
longitudes.  The moved tuple persists after filling the new coordinates by
any fixed element of `X`, so the stabilized braid still satisfies
`rho_{X,q_j}(beta_j) != 1`.

For every fixed finite group `H`, choose `j>=|H|`.  The left-regular embedding

```text
H -> S_|H| -> S_j
```

implies

```text
K_{S_j}(q_j) <= K_H(q_j).
```

Therefore the stabilized braids are eventually invisible to every finite
group while still moving `X`.  This is exactly the normalized-law obstruction
sequence required for outcome B.

## Audit Hook

The helper

```text
point_pushing_brunnian_failure_certificate(...)
```

wraps `point_pushing_brunnian_orbit_audit(...)` and, when a real failure kind
is found, rechecks the returned right-based word using
`point_pushing_brunnian_witness_certificate(...)`.  A valid row has:

```text
valid_failure_certificate == True.
```

The helper is finite-row infrastructure.  A complete B proof still needs an
explicit infinite symmetric-tail family of such rows.
