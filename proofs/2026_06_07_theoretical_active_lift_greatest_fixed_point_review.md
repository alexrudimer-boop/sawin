# Theoretical Review: Active-Lift Greatest Fixed Point

Date: 2026-06-07.

## Verdict

This is theorem-level progress.  It makes the active-lift existence problem
canonical: there is a greatest active lift system obtained by monotone pruning.
There is no arbitrary choice of active sets left.

It does not prove A, because it still must be shown that the fixed point is
nonempty for every finite bijective YBE solution, and all-arity orbit
separation remains independent.

## Construction

For the finite contextual quotient `P=P_X`, let

```text
lambda_p : D_p -> P
```

be the forced partial left translation.

Start with all local extensions:

```text
V_p = {g in Sym(P): g|_{D_p}=lambda_p}.
```

Because `lambda_p` is injective, each `V_p` is nonempty.

For a family `C=(C_p)` with `C_p subseteq V_p`, define the monotone pruning
operator:

```text
T(C)_p =
  { g in C_p :
      for every q in D_p and every h in C_q,
      g h g^{-1} in C_{lambda_p(q)}
  }.
```

Start with `C^(0)=V` and iterate

```text
C^(k+1)=T(C^(k)).
```

Since the sets are finite, this stabilizes to

```text
C^(infty)=intersection_k C^(k).
```

## Exactness

There exists an active lift system iff

```text
C^(infty)_p != empty
```

for every `p`.

If the fixed point is nonempty everywhere, it is itself an active lift system.
Conversely, any active lift system `C` satisfies `C subseteq C^(0)`.  Since it
is closed under the forced-pair conjugacy rule, `C subseteq T(C^(0))=C^(1)`.
Inductively `C subseteq C^(k)` for all `k`, hence `C subseteq C^(infty)`.
Therefore an empty fixed-point fibre proves no active lift system exists.

## Consequence

For a fixed finite `X`, the positive route is reduced to two statements:

```text
C^(infty)_p != empty for every p in P_X;
J_n:X^n -> P_X^n is braid-orbit-injective for every n.
```

If both hold, then the canonical rack

```text
P_X x Sym(P_X)
```

dominates `X`.

## Negative Target

A finite counterexample candidate can now be searched for by the canonical
pruning algorithm:

```text
find X and p such that C^(infty)_p is empty.
```

If no such `X` exists, then the active-lift completion part of A is solved and
the only remaining obstruction is all-arity orbit separation.
