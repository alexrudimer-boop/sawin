# One-colour product-permutation branch

Date: 2026-05-28

This note closes the one-colour swapped product-permutation branch for
arbitrary finite fibre size.  It is a symbolic subcase of the product branch,
not a finite search.

## Setup

Let there be one quotient colour and a finite fibre `A`.  In swapped product
form the local table is

```text
T(x,y) = (L(y), R(x)),
```

where `L,R in Sym(A)`.

The swapped product cocycle equations reduce to one condition:

```text
R L = L R.
```

Thus the fibre labels generate a finite abelian permutation group

```text
H = <L,R> <= Sym(A).
```

## Local-minimality

For a one-colour product branch, admissible local congruences are exactly the
partitions of `A` invariant under `H`.  Local-minimality says the only such
partitions are equality and universal, i.e. the action of `H` on `A` is
primitive.

A transitive abelian permutation group is regular: if an element of an
abelian transitive group fixes one point, it fixes every point.  A regular
action is primitive only when the acting group has no nontrivial proper
subgroups, since cosets of any proper subgroup form a nontrivial block
system.  Therefore the local-minimal one-colour product branch has

```text
H ~= C_p
```

for a prime `p`, acting regularly on `A`.

## Detector

Let `m=p`.  In the one-colour swapped product branch, a pure braid with
trivial Artin permutation acts on each fibre coordinate by a power of the
single `p`-cycle generator.  The exponent is controlled by the abelianized
recursive Artin longitude matrix.

Write the label accumulated on coordinate `j` as

```text
L^{alpha_j(beta)} R^{beta_j(beta)}.
```

Let

```text
E_jk(beta)
```

be the exponent of `x_k` in the recursive Artin longitude `L_j(beta)`.
For every pure braid,

```text
alpha_j(beta) = sum_k E_jk(beta),
beta_j(beta)  = sum_k E_kj(beta).
```

This follows by induction on braid words.  At a positive crossing
`sigma_i`, the one-colour swapped product action sends the old right strand
to the left and appends `L`, while sending the old left strand to the right
and appending `R`.  Hence

```text
alpha_i' = alpha_{i+1}+1,   beta_i' = beta_{i+1},
alpha_{i+1}' = alpha_i,     beta_{i+1}' = beta_i+1.
```

For `sigma_i^{-1}`, the appended labels are `R^{-1}` and `L^{-1}`:

```text
alpha_i' = alpha_{i+1},     beta_i' = beta_{i+1}-1,
alpha_{i+1}' = alpha_i-1,   beta_{i+1}' = beta_i.
```

These are exactly the row-sum and column-sum recurrences obtained from the
recursive Artin longitude update after abelianization.  For example, a
positive crossing replaces the `i`-th longitude row by the old image vector
of strand `i` plus the old `(i+1)`-st longitude row, and swaps the image
vectors.  In abelianization the image vectors are standard basis vectors
following the strand permutation, so in the pure endpoint case the accumulated
increments are precisely the row and column sums above.  The inverse crossing
uses the corresponding negative update.  The empty word has all exponents
zero, so the induction proves the formula.

The cyclic finite group `C_p` detects exactly these exponents: if

```text
Lambda_{C_p,n}(beta) = Lambda_{C_p,n}(1),
```

then every recursive Artin longitude has zero abelianized exponent vector
modulo `p`.  Hence every row sum and column sum is zero modulo `p`, so every
accumulated fibre-label power is trivial.  The detector is independent of
braid index `n`.

The code-level helpers

```text
one_color_swapped_label_exponent_action(n,beta)
artin_longitude_row_column_sums(n,beta)
```

record the two sides of this formula and are tested against each other on
bounded braid words to guard the convention.

This proves the one-colour product-permutation branch is finite-G measurable.
It also explains why noncyclic regular abelian examples, such as the regular
`C_2 x C_2` action on four points, are not local-minimal: subgroup cosets
give invariant block systems.

## Direct Form

In the one-colour direct product form

```text
T(x,y) = (L(x), R(y)),
```

the direct cocycle equations force `L^2=L` and `R=R^2`.  Since `L` and `R`
are bijections, both are identities.  Thus the direct one-colour branch is
trivial.
