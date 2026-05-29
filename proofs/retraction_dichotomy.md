# Two-sided retraction dichotomy for local-minimal intervals

## Statement

Let `pi : X -> Z` be a finite local interval, written as coloured fibres
`A_a` and maps

```text
T_{a,b}: A_a x A_b -> A_{a.b} x A_{a*b}.
```

The usual one-sided profile of `x in A_a` records all maps

```text
y -> pr_1 T_{a,b}(x,y),
y -> pr_2 T_{b,a}(y,x).
```

For arbitrary finite bijective YBE solutions this one-sided profile is too
dangerous to use by cancellation: the one-sided maps need not be bijections.
The safe local relation used in this workspace is therefore two-sided.  It
requires the same profile equality for the inverse local table as well, then
iteratively refines by all opposite unary contexts for both orientations.

The stable two-sided context relation is an admissible local congruence family
for every finite coloured local bijection.  Consequently, in a local-minimal
interval it is either all equality or all universal.

## Construction

Let `T^{-1}` denote the inverse local interval.  Its base map is the inverse of
`R_Z`, and its fibre table is defined by

```text
T^{-1}_{c,d}(u,v) = (x,y)
when R_Z(a,b)=(c,d) and T_{a,b}(x,y)=(u,v).
```

Let `P^+` be one-step profile equality for `T`, let `P^-` be one-step profile
equality for `T^{-1}`, and put

```text
theta_0 = P^+ meet P^-.
```

For a relation family `theta`, define `C_T(theta)` by keeping a pair
`x theta_a x'` only when every opposite unary context also lands in the
corresponding `theta`-block:

```text
pr_1 T_{b,a}(y,x)  theta_{b.a}  pr_1 T_{b,a}(y,x'),
pr_2 T_{a,b}(x,y)  theta_{a*b}  pr_2 T_{a,b}(x',y).
```

Define `C_{T^{-1}}` analogously for the inverse table and iterate

```text
theta_{k+1} = C_T(theta_k) meet C_{T^{-1}}(theta_k).
```

The fibres are finite, so this descending chain stabilizes.  Denote the stable
family by `theta_infty`.

## Exactness proof

First suppose `theta <= P^+` and `theta <= C_T(theta)`.  If

```text
x theta_a x',  y theta_b y',
T_{a,b}(x,y)    = (u,v),
T_{a,b}(x',y')  = (u',v'),
```

then a two-step triangle proves forward compatibility.

Change `x` to `x'` while holding `y` fixed.  The first outputs are equal
because `theta <= P^+`; the second outputs are `theta`-related by the
opposite-context condition in `C_T`.

Then change `y` to `y'` while holding `x'` fixed.  The second outputs are
equal because `theta <= P^+`; the first outputs are `theta`-related by the
opposite-context condition in `C_T`.

By transitivity,

```text
u theta_{a.b} u',  v theta_{a*b} v',
```

so

```text
T_{a,b}(theta_a x theta_b) subset theta_{a.b} x theta_{a*b}.
```

The same argument applied to `T^{-1}` gives the reverse inclusion after
inverting the table.  Therefore, for `theta_infty`,

```text
T_{a,b}(theta_infty,a x theta_infty,b)
  = theta_infty,a.b x theta_infty,a*b
```

for every colour pair `(a,b)`.  Thus `theta_infty` is an exact admissible local
congruence family.  This proof uses only finiteness and bijectivity of each
coloured table, not nondegeneracy of one-sided maps and not finite search.

## Local-minimal dichotomy

If the interval is local-minimal, every admissible local congruence family is
one of the two extremes.  Since `theta_infty` is admissible, exactly one of the
following holds.

1. `theta_infty` is equality on every fibre.  This is the remaining
   two-sided-retraction-free branch.

2. `theta_infty` is universal on every fibre.  Because
   `theta_infty <= P^+`, every point in a fixed fibre has the same forward
   one-sided profile.  Hence for every colour pair

   ```text
   T_{a,b}(x,y) = (L_{a,b}(y), R_{a,b}(x)).
   ```

   Since `T_{a,b}` is a bijection, the coordinate maps `L_{a,b}` and
   `R_{a,b}` are bijections between the corresponding fibres.  This is exactly
   the product-permutation branch handled in
   `proofs/product_permutation_branch.md`.

Semisplit families are covered here because they are admissible local
congruence families when they work.  Local-minimality excludes every proper
semisplit family before the dichotomy is applied.

## Relation to the published retraction theorem

For nondegenerate/birack solutions, the usual one-sided retraction relation is
known to be a congruence.  The birack retraction paper records the relation
used by Lebed and Vendramin for finite invertible solutions, namely equality
of all first-output maps and all second-output maps, and says that the
solution descends to the quotient.

That literature result is a consistency check, but the reduction above does
not use it as a black box for arbitrary degenerate bijective solutions.  The
two-sided inverse-closure argument is the local replacement that avoids
nondegenerate cancellation.

Sources:

- Jedlicka, Pilitowska, and Zamojska-Dzienio, "The retraction relation for
  biracks", especially the introduction discussion of the Lebed-Vendramin
  relation and Theorem 3.3:
  https://jedlicka.tf.czu.cz/publications/a/biracks.pdf
- Lebed and Vendramin, "On structure groups of set-theoretic solutions to the
  Yang-Baxter equation":
  https://arxiv.org/abs/1707.00633

## Remaining branch

The only remaining local-minimal case after this dichotomy is the
two-sided-retraction-free branch.  The master local theorem is now reduced to
proving that this branch is always in the already measurable families
(nondegenerate/guitar, involutive/permutation, affine/coboundary, finite
semidirect affine, or pairwise-linking) or is detected by the finite symmetric
kernel-block/Schutzenberger groups.
