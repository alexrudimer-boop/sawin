# Constant-section triangular bundle partition

Date: 2026-05-30

This note follows `proofs/rank_profile_collapse_mixed_unit.md`.  It does not
prove the Master Local-Minimal Residual Theorem.  It records the exact finite
structure forced by bijectivity for the remaining constant-section triangular
rows.

## Setup

Consider one lower local row

```text
T_{a,b}: A_a x A_b -> A_c x A_d.
```

Assume it is left constant-section triangular:

```text
T_{a,b}(x,y) = (alpha(x), beta_x(y)).
```

Here

```text
alpha:A_a -> A_c,
beta_x:A_b -> A_d.
```

The side-dual case is

```text
T_{a,b}(x,y) = (lambda_y(x), gamma(y)),
```

and is obtained by interchanging left and right coordinates.

## Lemma: bijective triangular rows are bundle partitions

If `T_{a,b}` is bijective and has the left triangular form above, then:

1. `alpha` is surjective;
2. every `beta_x` is injective;
3. for each `u in A_c`, the family of images

```text
beta_x(A_b),  x in alpha^{-1}(u),
```

is a partition of `A_d`.

Proof.  Since `T_{a,b}` is surjective, for every `(u,v) in A_c x A_d` there
are `x,y` such that

```text
T_{a,b}(x,y)=(u,v).
```

Thus `alpha(x)=u`, so `alpha` is surjective.  Fix `x`.  If
`beta_x(y_0)=beta_x(y_1)`, then

```text
T_{a,b}(x,y_0)=T_{a,b}(x,y_1),
```

and injectivity of `T_{a,b}` gives `y_0=y_1`.  Hence every `beta_x` is
injective.

Now fix `u in A_c`.  Surjectivity of `T_{a,b}` says that every `v in A_d`
lies in `beta_x(A_b)` for some `x in alpha^{-1}(u)`.  If

```text
v in beta_x(A_b) cap beta_{x'}(A_b)
```

for two distinct `x,x' in alpha^{-1}(u)`, then for suitable `y,y'`,

```text
T_{a,b}(x,y)=(u,v)=T_{a,b}(x',y'),
```

contradicting injectivity.  Therefore the images are disjoint and cover
`A_d`, so they partition `A_d`.  QED.

The side-dual statement is identical: if

```text
T_{a,b}(x,y)=(lambda_y(x), gamma(y)),
```

then `gamma:A_b->A_d` is surjective, every `lambda_y:A_a->A_c` is injective,
and for each `v in A_d`, the images `lambda_y(A_a)` for
`y in gamma^{-1}(v)` partition `A_c`.

## Size consequences

In the left triangular case, for every `u in A_c`,

```text
|alpha^{-1}(u)| * |A_b| = |A_d|.
```

Thus the fibres of `alpha` have uniform size

```text
|A_d| / |A_b|.
```

The constant map is bijective exactly when `|A_b|=|A_d|`, in which case each
`beta_x` is a bijection.  This is the permutation/product triangular subcase
already routed by known product or holonomy branches.

If the fibres of `alpha` are nontrivial, the row is a genuine finite bundle:
over each `u`, the source fibre `alpha^{-1}(u)` indexes a partition of the
companion codomain `A_d` into equal-size blocks of size `|A_b|`.

## Updated obstruction

The remaining constant-section triangular obstruction is therefore not an
arbitrary triangular map.  It is a bundle-partition holonomy problem.

The final hidden local data is:

```text
u in A_c,
x in alpha^{-1}(u),
beta_x(A_b) <= A_d,
```

where the blocks `beta_x(A_b)` partition `A_d`.  Context recovery can only
move residual information by transporting these finite block labels and the
within-block companion bijections.

## Updated positive theorem target

The A-route target becomes:

```text
Triangular bundle holonomy theorem.
```

Every constant-section triangular local-minimal bottleneck row must route to
one of:

1. the bijective-constant-map product/permutation subcase;
2. an affine or product-holonomy closed branch on the bundle labels;
3. a Green/Schutzenberger readout of the bundle block transport;
4. a strand-continuing transport rack after quotienting by those bundle
   labels.

If this holds, then no constant-section triangular row supplies a new
obstruction, and the previously recorded product-detector assembly closes the
local interval.

## Updated B seed

A B route must now exhibit more than a constant section.  It must give an
explicit finite local-minimal bottleneck interval whose triangular
bundle-partition holonomy survives every finite-group recursive-longitude
detector through a normalized-law sequence, while still moving a residual
tuple.

A bounded bundle mismatch or a nontrivial finite block partition is not enough
for outcome B.

## Executable audit

The helper

```text
triangular_bundle_audit(interval)
```

records each left or right constant-section triangular row.  For each row it
stores:

- the constant map (`alpha` or `gamma`);
- each fibre of the constant map;
- the companion image blocks indexed by that fibre;
- whether the companion sections are injective;
- whether the blocks cover and are pairwise disjoint;
- whether the constant map is bijective;
- which fibres are nontrivial bundles.

For a valid bijective triangular local row, the audit should satisfy

```text
bundle_partition_identity_holds = True.
```

This is a row-level structural certificate, not a global proof.  Its purpose
is to reduce the final obstruction to triangular bundle holonomy rather than
an unstructured triangular map.
