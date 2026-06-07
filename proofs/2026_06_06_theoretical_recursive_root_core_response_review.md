# Review: Theoretical Recursive Root-Core Response

Date: 2026-06-06

Verdict: C.

The response does not prove Sawin's finite-rack domination statement and does
not give a cofinal rack-prefix counterexample.  It gives proof-grade progress:
the weighted block-core target can be sharpened by enforcing recursive
root-split coherence of all-meridian commutators.

The MathOverflow page was checked during this review.  It states Sawin's
finite-rack domination question and displays zero answers.  This is current
status context, not mathematical evidence.

## Theorem/Proof Content

The following claims are valid progress.

1. Root-split factorization.  For normal subgroups `N_i triangleleft G` and
   nonempty `S`, define

   ```text
   C_S=[N_i | i in S]_Sigma,
   C_{ {i} }=N_i.
   ```

   Then, for `|S|>=2`,

   ```text
   C_S =
   product_{ {A,B} in Bip(S) } [C_A,C_B].
   ```

   The proof is sound: one inclusion uses the fat-commutator theorem, and the
   other reads off the top bracket of a fully parenthesized all-support
   commutator.

2. Recursive root-core hierarchy.  With

   ```text
   R_S^(0)=Omega_2(G;(N_i)_{i in S}) cap Omega_3(G;(N_i)_{i in S})
   ```

   for `|S|>=3`, exact definitions for `|S|<=2`, and

   ```text
   R_S^(d+1)
     =
   R_S^(d) cap product_{ {A,B} in Bip(S) } [R_A^(d),R_B^(d)],
   ```

   the hierarchy satisfies

   ```text
   C_S <= R_S^(d+1) <= R_S^(d).
   ```

3. Eventual exactness.  The induction proving

   ```text
   R_S^(d)=C_S  whenever d>=|S|-3
   ```

   is valid.  For `|S|<=3` the base core is exact; for larger `S`, all proper
   subsets become exact one step earlier, and the root-split factorization
   gives equality.

4. Finite-image criterion.  In the finite-image setup,

   ```text
   C_n <= R_n^(d) <= Omega_{n,2}^wt cap Omega_{n,3}^wt
   ```

   for every fixed `d`, and `R_n^(d)=C_n` once `d>=n-4`.  Therefore a fixed
   `d` with

   ```text
   K_n cap R_n^(d)=1
   ```

   in all sufficiently large arities implies domination by one finite rack
   after adding fixed-arity detectors for the small arities.

5. Relative quotient criterion.  If `Z` is a dominated braided quotient and

   ```text
   E_n cap R_n^{X,(d)}=1
   ```

   for one fixed `d` in all sufficiently large arities, then one finite rack
   dominates `X`.

## Finite Evidence

The response itself gives no finite computation.

During this cycle, separate finite work closed the arity-5 non-permutation
size-three audit for the current detector product:

```text
43 direct full-product stabilizer rows
12 q=5 rows certified by [2,3] detector subproducts
55 / 55 arity-5 rows certified
full_product_kernel_image_size distribution {1: 55}
```

This is proof-grade fixed-arity evidence only.  It is not an all-arity
theorem.

## Heuristic Content

The useful heuristic is that genuine all-meridian obstructions must be
recursively root-coherent.  They cannot merely survive weighted two-block and
three-block tests; they must decompose into smaller all-support obstructions
across binary root splits at every fixed depth.

## Unsupported Claims

The following are not proved by the response.

1. Sawin's problem for all finite bijective set-theoretic YBE solutions.
2. A finite rack detector `Q` and fixed `d` with `K_n cap R_n^(d)=1` in all
   sufficiently large arities for every finite `X`.
3. A dominated quotient `Z` and fixed `d` with
   `E_n cap R_n^{X,(d)}=1` in all sufficiently large arities for every finite
   `X`.
4. A cofinal rack-prefix obstruction sequence.
5. Any all-arity conclusion from the arity-2, arity-3, arity-4, or arity-5
   finite computations.

## Extracted Progress

The next theoretical target is:

```text
exists Q=Y^0 x T_2 and fixed d>=0 such that
K_n cap R_n^(d)=1
for all sufficiently large n.
```

The quotient target is:

```text
exists dominated quotient Z and fixed d>=0 such that
E_n cap R_n^{X,(d)}=1
for all sufficiently large n.
```

A negative answer must still produce cofinal nontrivial elements in
`K_n cap C_n`.  Such elements automatically survive every fixed-depth
recursive root core, but membership in a root core alone is not enough for a
counterexample unless membership in the exact all-meridian subgroup `C_n` is
also proved.
