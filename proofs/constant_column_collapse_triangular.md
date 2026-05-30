# Constant-column collapse for triangular bottleneck rows

Date: 2026-05-30

This note records the next reduction in the final constant-observer
universal-continuation case.  It does not prove the Master Local-Minimal
Residual Theorem.  It removes the non-Latin half of the constant-section
triangular obstruction and leaves a sharper last target: Latin-unit triangular
longitude visibility.

## Setup

Work in a local-minimal interval that has reached the
`bi_free_universal_corridor_bottleneck`, after the certified Green,
Schutzenberger, atom, quotient, known-branch, and endpoint/unit observers have
all become fibrewise constant on the remaining lower continuation branch.

The remaining rank-one triangular row has the form

```text
T_{a,b}(x,y) = (alpha_{a,b}(x), beta_{a,b,x}(y)),
```

with

```text
x in A_a,      y in A_b,
alpha_{a,b}(x) in A_{a*b},      beta_{a,b,x}(y) in A_a.
```

The first output is independent of `y`.  The opposite columns are

```text
C_y : A_a -> A_a,
C_y(x) = beta_{a,b,x}(y).
```

The same discussion has a side-dual version for rows whose second output is
independent of `x`.

## Theorem

In the constant-observer universal-continuation case, if any opposite column
`C_y` is non-bijective while remaining hidden from the certified observers,
then the triangular row collapses to product form:

```text
T_{a,b}(x,y) = (alpha_{a,b}(x), gamma_{a,b}(y)).
```

Thus this row is a product/permutation holonomy row and is routed to an already
closed branch.  A genuine remaining triangular bottleneck must have all
opposite columns bijective.

## Proof

Let

```text
N_t = |A_t|.
```

Since the local row

```text
T_{a,b}: A_a x A_b -> A_{a*b} x A_a
```

is bijective, cardinalities give

```text
N_a N_b = N_{a*b} N_a,
```

so

```text
N_b = N_{a*b}.
```

For a fixed output value `u in A_{a*b}`, the target slice

```text
{u} x A_a
```

has size `N_a`.  Its preimage under the triangular row is

```text
alpha_{a,b}^{-1}(u) x A_b.
```

Therefore

```text
|alpha_{a,b}^{-1}(u)| N_b = N_a.
```

In the connected triangular continuation component, applying the same
cardinality argument to the swapped or side-dual row gives `N_a | N_b`; hence
the colours in the component have equal fibre size.  Consequently every fibre
of `alpha_{a,b}` has size one, so

```text
alpha_{a,b}: A_a -> A_{a*b}
```

is bijective.

Now fix `x`.  The restriction of `T_{a,b}` to the source slice

```text
{x} x A_b
```

lands in the target slice

```text
{alpha_{a,b}(x)} x A_a.
```

Because the whole row is bijective and `alpha_{a,b}` is bijective, this
restriction must fill that target slice exactly once.  Hence every companion
section

```text
beta_{a,b,x}: A_b -> A_a
```

is bijective.

Now inspect the opposite columns

```text
C_y(x)=beta_{a,b,x}(y).
```

In the final constant-observer case, a proper nontrivial kernel profile cannot
remain hidden: the fixed detector product already contains the Green
kernel-block and Schutzenberger readouts that expose such profiles.  Thus a
hidden non-bijective column has only the universal kernel option; it is
constant.

Assume `C_{y_0}` is constant with value `c`:

```text
beta_{a,b,x}(y_0)=c
```

for every `x`.  Since each `beta_{a,b,x}` is bijective, no other input
`y != y_0` can map to `c` for that same `x`.  Therefore for every `y != y_0`,

```text
C_y(A_a) subset A_a \ {c}.
```

So `C_y` is not surjective and hence not bijective.  The only hidden
non-bijective alternative is constant, so every `C_y` is constant.  Define

```text
gamma_{a,b}(y) = C_y(x),
```

which is independent of `x`.  Then

```text
T_{a,b}(x,y) = (alpha_{a,b}(x), gamma_{a,b}(y)).
```

Since every `beta_{a,b,x}` is bijective, `gamma_{a,b}` is bijective as well.
The row is therefore a direct product of coordinate bijections.  This is a
product/permutation holonomy row, not a genuine mixed continuation obstruction.
QED.

## Executable audit

The helper

```text
triangular_column_collapse_audit(interval)
```

records this split for every constant-section triangular row.  For each row it
stores:

- the constant coordinate map `alpha` or its side-dual;
- the companion sections `beta_x` or their side-duals;
- the opposite columns `C_y` or their side-duals;
- whether the row has product collapse for hidden nonunit columns;
- whether the row is Latin-unit triangular;
- whether a proper opposite kernel is still visible and must route back through
  the Green or Schutzenberger observers.

The tests distinguish the two intended cases:

```text
T(x,y)=(x,y)
```

is classified as product collapse, while

```text
T(x,y)=(x,x+y mod 2)
```

is classified as Latin-unit triangular.

## Consequence

The constant-section triangular obstruction is now much smaller.  A hidden
opposite nonunit column forces product form and routes to the existing
product/permutation holonomy branch.

The only remaining triangular obstruction is therefore:

```text
Latin-unit triangular:
alpha is bijective,
each y -> beta_x(y) is bijective,
each x -> beta_x(y) is bijective.
```

Let `U_triangle` be the fixed finite group generated by these triangular unit
transports.  The final positive target becomes:

```text
Every residual Latin-unit triangular endpoint lies in V_beta(U_triangle).
```

If this Latin-unit triangular longitude theorem is proved, the remaining
constant-observer universal-continuation case closes: product triangular rows
are already closed, strand-continuing rows are detected by transport-state
rackification, and proper-rank nonunit rows are Green/Schutzenberger-visible.

If it fails, a B route still needs more than a bounded miss.  It must produce a
Latin-unit triangular bottleneck interval and upgrade the residual endpoint
failure

```text
S_beta notin V_beta(U_triangle)
```

to a normalized-law sequence invisible to every finite group while still moving
an explicit residual tuple.

