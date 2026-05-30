# Symmetric tower monotonicity

Date: 2026-05-30

This note records the monotonicity used by the symmetric-tower B certificate.
The tower of detector kernels is descending:

```text
K_{S_1}(n) >= K_{S_2}(n) >= K_{S_3}(n) >= ...
```

for every braid index `n`.

## Lemma

For integers `1 <= m <= M` and every `n`,

```text
K_{S_M}(n) subset K_{S_m}(n).
```

Proof.  Embed `S_m` into `S_M` by fixing the last `M-m` points.  If
`beta in K_{S_M}(n)`, then the Artin strand permutation of `beta` is trivial
and all recursive Artin longitudes evaluate to the identity under every
assignment

```text
F_n -> S_M.
```

Every assignment `F_n -> S_m`, followed by the fixed-point inclusion, is an
assignment into `S_M`.  Hence its longitude values are identity permutations in
the embedded copy of `S_m`.  The inclusion is injective, so those longitude
values are identity in `S_m`.  Thus `beta in K_{S_m}(n)`.  QED.

## Consequence for B certificates

If a sequence has

```text
beta_j in K_{S_j}(q_j),
```

then for every fixed `m`, it has

```text
beta_j in K_{S_m}(q_j)
```

for all `j>=m`.

Combined with the left-regular embedding of any finite group `G` into
`S_|G|`, this proves eventual invisibility to every finite group:

```text
beta_j in K_{S_j}
    subset K_{S_|G|}
    subset K_G
```

for all sufficiently large `j`.

Thus a symmetric-tower counterexample certificate really is a normalized-law
certificate in the original all-finite-group sense.

## Consequence for A certificates

The positive local theorem can be stated as existence of one degree `m(pi,Q)`
such that

```text
beta in N_n cap K_{S_m}(n) => Delta_n(beta)=1
```

for all `n`.  If such an `m` works, then every larger `M>=m` also works,
because

```text
K_{S_M}(n) subset K_{S_m}(n).
```

So positive detector degrees are upward closed.

## Executable audit

The helper

```text
symmetric_tower_monotonicity_audit(m,M,n,beta)
```

checks the fixed-point inclusion `S_m -> S_M` and records the implication

```text
Lambda_{S_M,n}(beta)=Lambda_{S_M,n}(1)
    => Lambda_{S_m,n}(beta)=Lambda_{S_m,n}(1).
```

As usual, this is a certificate-level convention check for supplied data, not a
finite search proof of the local theorem.
