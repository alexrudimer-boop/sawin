# Finite-group Artin-longitude detector convention

Date: 2026-05-28

This note records the executable convention now used for finite-group
Artin-longitude data.  The point is to align the proof log with the actual rack
`A_G` in the sharp obstruction theorem, not with an arbitrary reduced
conjugator convention.

## Artin action

For the positive braid generator `sigma_i`, with zero-based free generators in
code and one-based braid generators in user-facing braid words, the Artin
automorphism is

```text
x_i     -> x_i x_{i+1} x_i^{-1}
x_{i+1} -> x_i.
```

The inverse generator is

```text
x_i     -> x_{i+1}
x_{i+1} -> x_{i+1}^{-1} x_i x_{i+1}.
```

The tests verify the braid relation

```text
sigma_1 sigma_2 sigma_1 = sigma_2 sigma_1 sigma_2
```

at the free-word image level.

## Recursive longitude convention

If an Artin image is written

```text
beta(x_k) = L_k x_{p(k)} L_k^{-1},
```

then `L_k` is not intrinsically unique: it can be multiplied on the right by a
power of `x_{p(k)}` without changing the conjugate.  Therefore the detector
must use the recursive Artin longitude convention recorded by the rack `A_G`,
rather than a canonical reduced conjugator extracted after free reduction.

The recursion maintained by `src/ybe_domination/artin_longitudes.py` is:

For a positive generator at positions `i,i+1`, with current images `M_i,M_j`
and longitudes `L_i,L_j`,

```text
M_i' = M_i M_j M_i^{-1},    L_i' = M_i L_j,
M_j' = M_i,                 L_j' = L_i.
```

For a negative generator,

```text
M_i' = M_j,                 L_i' = L_j,
M_j' = M_j^{-1} M_i M_j,    L_j' = M_j^{-1} L_i.
```

This is exactly the update induced by applying the rack

```text
(a,u) rack (b,v) = (a b a^{-1}, a v)
```

to starting coordinates `(g_i,e)`.

## Code-level bridge

The function `detector_rack_state(G, assignment, braid_word)` applies `A_G` to
the tuple `((g_1,e),...,(g_n,e))`.  Tests assert that its first coordinates
are the evaluated Artin images and its second coordinates are the evaluated
recursive Artin longitudes.

This confirms the executable version of the sharp obstruction theorem's
finite-group detector:

```text
Lambda_{G,n}(beta) = Lambda_{G,n}(1)
```

means that the braid permutation is trivial and all recursive longitudes
evaluate to the identity for every assignment in `G^n`.

## Abelian longitude matrix

The abelianized longitude matrix records the exponent vector of each recursive
longitude:

```text
E_i(beta)_j = exponent sum of x_j in L_i(beta).
```

The helper `artin_longitude_exponent_matrix(n,beta)` computes this matrix.
For the standard pure generator `A_{i,j}`, the matrix has the expected
pairwise-linking support: the `i`-th longitude contains `x_j` once and the
`j`-th longitude contains `x_i` once, up to the indexing convention used by
the recursive longitude update.

For a cyclic group `C_m`, longitude invisibility is exactly the congruence

```text
E_i(beta)_j = 0 mod m  for all i,j,
```

together with trivial braid permutation.  Indeed, evaluating a free word in
an abelian group depends only on its exponent vector, and requiring identity
for every assignment in `C_m^n` forces every coefficient to vanish modulo
`m`.  The helper `has_trivial_abelian_longitudes_mod(m,n,beta)` records this
criterion.

This supplies the finite cyclic detector used by pairwise-linking and
one-colour product-permutation branches: if all fibre permutations have
orders dividing `m`, then `C_m` detects every nontrivial residual action that
factors through the abelian longitude matrix modulo `m`.

For the one-colour swapped product branch this factorization is explicit.
The helper `artin_longitude_row_column_sums(n,beta)` returns, for each
coordinate, the row sum and column sum of the abelian longitude matrix.  The
companion product helper `one_color_swapped_label_exponent_action(n,beta)`
records the exponents of the two commuting labels `L` and `R`.  For pure
braids these two tuples agree: the `L` exponent on coordinate `j` is the row
sum of the `j`-th longitude, and the `R` exponent is the `j`-th column sum.
Thus cyclic longitude invisibility modulo the common label order forces the
one-colour product labels to vanish.

## Limitation

The code can find bounded evidence of a word that is invisible to a chosen
finite group but moves a chosen finite YBE solution.  Such evidence is not a
counterexample to Sawin domination.  A counterexample still needs a normalized
sequence `beta_j` that eventually defeats every finite group `G`, and a proof
that the sequence has that universal finite-law property.
