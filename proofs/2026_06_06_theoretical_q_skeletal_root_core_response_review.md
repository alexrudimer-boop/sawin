# Review: Theoretical Q-Skeletal Root-Core Response

Date: 2026-06-06

Verdict: C.

The response does not prove Sawin's finite-rack domination statement and does
not give a cofinal rack-prefix counterexample.  It gives proof-grade progress:
the recursive root-core target can be sharpened by imposing exact
small-support all-meridian conditions.

The MathOverflow page was checked during this review.  It states Sawin's
finite-rack domination question and displays zero answers.  This is current
status context, not mathematical evidence.

## Theorem/Proof Content

The following claims are valid progress.

1. Exact support monotonicity.  For normal subgroups `N_i triangleleft G` and
   nonempty `T subset S`,

   ```text
   C_S=[N_i | i in S]_Sigma <= C_T=[N_i | i in T]_Sigma.
   ```

   The proof can be made rigorous by induction on the commutator tree:
   if the selected labels all lie on one child, normality keeps the upper
   commutators inside `C_T`; if they split across the two children, the
   root-split/fat-commutator containment sends `[C_{T_a},C_{T_b}]` into
   `C_T`.

2. Q-skeletal root cores.  For fixed `q>=3`, define

   ```text
   J_{S,q}=intersection_{empty != T subset S, |T|<=q} C_T
   ```

   and

   ```text
   Sk_{S,q}^{(0)}=R_S^(0) cap J_{S,q},
   Sk_{S,q}^{(d+1)}
     =
   Sk_{S,q}^{(d)}
     cap
   product_{ {A,B} in Bip(S) } [Sk_{A,q}^{(d)},Sk_{B,q}^{(d)}].
   ```

   Then

   ```text
   C_S <= Sk_{S,q}^{(d+1)} <= Sk_{S,q}^{(d)} <= R_S^(d).
   ```

3. Monotonicity in `q`.  If `q' >= q`, then

   ```text
   Sk_{S,q'}^{(d)} <= Sk_{S,q}^{(d)}.
   ```

4. Eventual exactness.  The hierarchy reaches the exact all-meridian subgroup
   at depth

   ```text
   d >= max(0, |S|-q).
   ```

   This improves the previous `|S|-3` depth bound for fixed `q>3`.

5. Finite-image criterion.  In the finite-image setup, if there are fixed
   integers `q>=3` and `d>=0` such that

   ```text
   K_n cap Sk_{n,q}^{(d)}=1
   ```

   for all sufficiently large `n`, then one finite rack dominates `X` after
   adding fixed-arity detectors for the remaining small arities.

6. Relative quotient criterion.  If there is a dominated braided quotient
   `Z` and fixed `q,d` such that

   ```text
   E_n cap Sk_{n,q}^{X,(d)}=1
   ```

   for all sufficiently large `n`, then one finite rack dominates `X`.

## Finite Evidence

The response itself gives no new finite computation.

The repository now contains proof-grade fixed-arity evidence through arity 5
for the non-permutation size-three detector product:

```text
arity 4: 55 / 55 rows trivial
arity 5: 55 / 55 rows certified trivial
```

This remains fixed-arity evidence only.

## Heuristic Content

The useful heuristic is that a genuine high-arity obstruction must be
exact-small-support-deep: it must lie in every exact `q`-meridian commutator
subgroup for each fixed `q`, not only in weighted block collapses or
fixed-depth root-core approximations.

## Strictness Model

The response proposes a nilpotent Lie algebra construction to show
`Sk_{S,3}^{(0)}<R_S^(0)`.  This strictness model is plausible but not needed
for the finite-image criterion.  It should not be used as a proof dependency
until the quotient and Hall-support assertions are independently checked.

## Unsupported Claims

The following are not proved by the response.

1. Sawin's problem for all finite bijective set-theoretic YBE solutions.
2. A finite rack detector `Q` and fixed `q,d` with
   `K_n cap Sk_{n,q}^{(d)}=1` in all sufficiently large arities for every
   finite `X`.
3. A dominated quotient `Z` and fixed `q,d` with
   `E_n cap Sk_{n,q}^{X,(d)}=1` in all sufficiently large arities for every
   finite `X`.
4. A cofinal rack-prefix obstruction sequence.
5. Any all-arity conclusion from the finite arity-4 or arity-5 computations.

## Extracted Progress

The next theoretical target is:

```text
exists Q=Y^0 x T_2, fixed q>=3, and fixed d>=0 such that
K_n cap Sk_{n,q}^{(d)}=1
for all sufficiently large n.
```

The quotient target is:

```text
exists dominated quotient Z, fixed q>=3, and fixed d>=0 such that
E_n cap Sk_{n,q}^{X,(d)}=1
for all sufficiently large n.
```

A negative answer must still produce cofinal nontrivial elements in
`K_n cap C_n`.  Such elements automatically survive every fixed `q,d`
skeletal root-core test, but membership in `Sk_{n,q}^{(d)}` alone is not a
counterexample unless membership in the exact all-meridian subgroup `C_n` is
also proved.
