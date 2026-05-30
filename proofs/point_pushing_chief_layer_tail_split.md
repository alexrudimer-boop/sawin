# Point-Pushing Chief-Layer Tail Split

Date: 2026-05-30

This note refines `proofs/point_pushing_monolithic_compression.md`.

It does not prove outcome A or B.  It separates the minimal monolithic
quotients left by product-prefix Brunnian first failures into two mechanisms:
large chief factors and abelian Frattini depth.

## Setup

Let a product-prefix Brunnian first failure be compressed to a smallest
separating quotient

```text
phi:P_k(X)->H
```

with unique minimal nontrivial normal subgroup

```text
M normal H.
```

Let `B_H` be the paired Brunnian orbit subgroup in the quotient row, and let

```text
V_H = B_H cap ({1} x H)
```

be its vertical kernel.  By monolithic compression,

```text
1 != V_H <= M,
```

and every nontrivial normal subgroup of `H` contains `V_H`, hence contains
`M`.

## Theorem

Exactly one of the following obstruction types occurs.

### Type I: Large-Chief Obstruction

Either `M` is nonabelian, or `M` is abelian but

```text
M not<= Phi(H).
```

In the nonabelian case,

```text
H embeds in Aut(M).
```

In the abelian non-Frattini case,

```text
H = M semidirect L
```

for some `L <= Aut(M)`.

Thus in either Type I case, `|H|` is bounded solely in terms of `|M|`.  Any
product-prefix tail of Type I escaping all bounded prefixes must therefore
have

```text
|M_j| -> infinity.
```

### Type II: Frattini-Depth Obstruction

The remaining case is

```text
M abelian and M <= Phi(H).
```

Here every nontrivial normal quotient of `H` kills the vertical witness.  The
failure is not caused by large simple or complemented module content; it is a
bottom abelian chief layer lying inside the Frattini subgroup.

## Proof

By minimality of the separating quotient, every nontrivial normal quotient of
`H` kills the vertical failure.  Equivalently, for every nontrivial
`N normal H`,

```text
V_H <= N.
```

Therefore `H` has a unique minimal nontrivial normal subgroup `M`, and
`1 != V_H <= M`.

### Nonabelian Monolith

If `M` is nonabelian, then

```text
M ~= S^r
```

for a nonabelian finite simple group `S`.  The centralizer `C_H(M)` is normal
in `H`.  If it were nontrivial, uniqueness of the minimal normal subgroup
would force `M <= C_H(M)`.  But

```text
C_M(M)=Z(M)=1,
```

because `M` is a direct product of centerless nonabelian simple groups.  Hence
`C_H(M)=1`, and conjugation gives a faithful embedding

```text
H -> Aut(M).
```

So `|H| <= |Aut(M)|`, which is bounded by `|M|` alone.

### Abelian Non-Frattini Monolith

Assume `M` is abelian and `M not<= Phi(H)`.  Then some maximal subgroup
`L<H` does not contain `M`.  Since `M` is normal and minimal,

```text
H = M L.
```

The intersection `M cap L` is normalized by `L`; because `M` is abelian, it is
also normalized by `M`.  Thus `M cap L normal H`.  Minimality of `M` gives

```text
M cap L = 1
```

because the alternative `M cap L=M` would put `M` inside `L`.

Therefore

```text
H = M semidirect L.
```

Let `K=C_L(M)`.  Then `K normal L`, and since it centralizes `M`, it is also
normalized by `M`.  Thus `K normal H`.  If `K` were nontrivial, every
nontrivial normal subgroup of the monolithic group `H` would contain `M`,
contradicting `K cap M=1`.  Hence `K=1`, so the conjugation action embeds

```text
L <= Aut(M).
```

Thus `|H| <= |M| |Aut(M)|`, again bounded by `|M|` alone.

### Remaining Case

The only remaining possibility is

```text
M abelian and M <= Phi(H).
```

Modulo `M`, the vertical kernel disappears, so the Brunnian row succeeds in
`H/M`.  The obstruction is therefore a lift value in a bottom abelian
Frattini chief layer.  QED.

## Consequence For Product-Prefix B

Every product-prefix negative tail has a subsequence of one of two forms:

1. **Large-chief tail.**  The monoliths satisfy `|M_j|->infinity`.  This
   includes nonabelian simple-power wreath tails and large complemented
   abelian module tails.
2. **Frattini-depth tail.**  The monoliths are abelian and satisfy
   `M_j<=Phi(H_j)`.

Bounded nonabelian simple content and bounded complemented abelian module
content cannot be the final escaping mechanism: in both cases the whole
minimal quotient has bounded order, and a sufficiently large product-prefix
detector would include the needed finite quotient.

## Consequence For Outcome A

To prove finite-rack domination through the global product-prefix route, it is
enough to rule out:

```text
large-chief first-failure tails,
abelian Frattini-depth first-failure tails.
```

If both are uniformly impossible for a finite solution `X`, then the
product-prefix detector profile is bounded.  Hence some fixed finite
product-prefix group `Pi_J` satisfies

```text
D_k(Pi_J) -> P_k(X)
```

for every `k`, and the sharp detector rack `A_{Pi_J}` dominates `X`.

## Consequence For Outcome B

A negative proof must now produce one explicit finite `X` and an infinite
tail of one of the following forms:

```text
large-chief tail with |M_j| -> infinity,
abelian Frattini-depth tail with M_j <= Phi(H_j).
```

The corresponding point-pushing braids lie in `K_{Pi_j}` and move `X`; the
product-prefix obstruction mechanism then right-stabilizes them into a
normalized-law obstruction sequence invisible to every fixed finite group.
