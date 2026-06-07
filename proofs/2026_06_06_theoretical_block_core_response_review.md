# Review: Theoretical Block-Core Response

Date: 2026-06-06

Verdict: C.

The response does not prove Sawin's finite-rack domination statement and does
not give a cofinal rack-prefix counterexample.  It does give proof-grade
progress: the finite-image obstruction can be narrowed from the pairwise core
to the triple/block-core hierarchy.

The MathOverflow page for Sawin's question was checked during this review and
still shows the question with zero answers.  This is external status context,
not mathematical evidence.

## Theorem/Proof Content

The following claims are valid progress.

1. Block-core interpolation.  For normal subgroups
   `N_1,...,N_r triangleleft G`, define

   ```text
   N_S = product_{i in S} N_i
   ```

   and

   ```text
   Theta_s(G;N_1,...,N_r)
     =
   intersection_{P={S_1,...,S_s}}
     [N_{S_1},...,N_{S_s}]_Sigma.
   ```

   Then, for `r>=3`,

   ```text
   [N_1,...,N_r]_Sigma
     =
   Theta_r <= Theta_{r-1} <= ... <= Theta_3
     <=
   intersection_{i<j}[N_i,N_j].
   ```

   The proof is sound, using the standard fat-commutator theorem and the
   previous pairwise-depth lemma.

2. Strictness.  The class-two `p`-group example with three normal subgroups
   has nontrivial pairwise core but trivial triple/all-meridian core.  This
   correctly shows that `Theta_3` is a strict improvement over the pairwise
   core in general.

3. Finite-image consequence.  In the Brunnian finite-image setup,

   ```text
   C_n=[N_{1,n},...,N_{n-1,n}]_Sigma
      <= Theta_{n,3} <= D_n.
   ```

   Hence the earlier sufficient condition `K_n cap D_n=1` can be replaced by
   the sharper sufficient condition

   ```text
   K_n cap Theta_{n,3}=1
   ```

   for all sufficiently large `n`, plus fixed-arity rack detectors for the
   remaining arities.

4. Relative quotient criterion.  If `Z` is a dominated braided quotient of
   `X`, with

   ```text
   E_n=ker(G^X_n -> G^Z_n),
   M_{i,n}=<<rho^X_n(x_i)>>_{G^X_n},
   ```

   and if, for a fixed `s>=3`,

   ```text
   E_n cap Theta_s(G^X_n;M_{1,n},...,M_{n-1,n}) = 1
   ```

   for all sufficiently large `n`, then one finite rack dominates `X`.
   The proof correctly projects `K_n cap C_n` into both `E_n` and the
   `X`-block core, then uses `K_n cap L_n=1`.

5. Comparison with the previous `gamma_2` criterion.  Since

   ```text
   Theta^X_{n,3} <= gamma_3(G^X_n) <= gamma_2(G^X_n),
   ```

   the block-core criterion is weaker than requiring
   `E_n cap gamma_2(G^X_n)=1`.

6. Chief-factor sharpening.  Any central Type C obstruction must be a
   prime-order central chief factor covered by every triple-block commutator,
   not only by every pairwise commutator.

## Finite Evidence

The response itself gives no new finite computation.  The repository already
contains separate finite evidence:

```text
arity 2 endpoint coverage: complete
arity 3 endpoint coverage: complete after q=5
arity 4 detector-product stabilizer audit: all 55 rows trivial
arity 5 partial stabilizer probes: 43 of 55 rows trivial, 12 q=5 rows open
```

These computations remain fixed-arity evidence only.

## Heuristic Content

The useful heuristic is that a genuine Brunnian obstruction must be
partition-deep: it must survive every three-way meridian partition, and indeed
every fixed-depth block partition.  Pairwise commutator intersections contain
class-two artifacts that are not true all-meridian obstructions.

## Unsupported Claims

The following are not proved by the response.

1. Sawin's problem for all finite bijective set-theoretic YBE solutions.
2. A finite rack detector `Q` with `K_n cap Theta_{n,3}=1` for all large `n`
   for every finite `X`.
3. A dominated quotient `Z` with
   `E_n cap Theta^X_{n,3}=1` for all large `n` for every finite `X`.
4. A cofinal rack-prefix obstruction sequence.
5. Any all-arity conclusion from the arity-2, arity-3, arity-4, or partial
   arity-5 computations.

## Extracted Progress

The next theoretical target is now sharper:

```text
exists Q=Y^0 x T_2 such that, for all sufficiently large n,
K_n cap Theta_{n,3}=1.
```

Equivalently, through a dominated quotient:

```text
E_n cap Theta^X_{n,3}=1
```

for all sufficiently large `n`.

A negative answer must produce, for every finite rack prefix, unbounded
arities and nontrivial elements in `K_n cap C_n`; these elements automatically
lie in the triple/block-core hierarchy.  Producing noise in one pairwise
commutator, or even in the whole pairwise core but outside `C_n`, is
insufficient.
