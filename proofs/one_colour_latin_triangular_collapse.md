# One-colour Latin triangular collapse

Date: 2026-05-30

This note removes the one-colour version of the remaining companion-shear
obstruction.  It does not prove the Master Local-Minimal Residual Theorem for
arbitrary quotient colours.  It shows that a nontrivial one-colour
Latin-unit triangular bottleneck cannot satisfy the Yang-Baxter equation.

## Setup

Let there be one colour and a left triangular row

```text
T(x,y) = (alpha(x), beta_x(y))
```

on a finite fibre `A`.  Assume the triangular unit hypotheses:

- `alpha:A->A` is bijective;
- each companion map `beta_x:A->A` is bijective;
- each opposite column `x->beta_x(y)` is bijective.

## Collapse

The Latin triangular YBE split gives three equations.  In the one-colour case,
the alpha equation is

```text
alpha alpha = alpha.
```

Since `alpha` is bijective, multiply by `alpha^{-1}` to get

```text
alpha = id.
```

Substitute this into the middle companion equation.  It becomes

```text
beta_x(beta_x(y)) = beta_x(y)
```

for every `x,y`.  Since each `beta_x` is bijective, cancel `beta_x` on the
left:

```text
beta_x(y)=y.
```

Thus every companion map is the identity.

But then each opposite column is

```text
x -> beta_x(y) = y,
```

which is constant.  It is bijective only when `|A|=1`.

Therefore:

```text
No nontrivial one-colour Latin-unit triangular row satisfies YBE.
```

For `|A|>1`, the row collapses out of the Latin-unit branch and into the
product/permutation triangular branch already handled by the preceding
constant-column collapse.

## Executable audit

The helper

```text
one_color_latin_triangular_collapse_audit(interval)
```

records this check for a one-colour local interval.  It reports:

- whether a left triangular row is present;
- whether the full coloured YBE holds;
- whether `alpha` is the identity;
- whether all companion sections are identity maps;
- whether the row is still Latin-unit triangular;
- whether a nontrivial one-colour Latin-unit YBE candidate remains.

The tests verify both sides of the split:

- `T(x,y)=(x,y)` is a true one-colour YBE row, but its opposite columns are
  constant, so it routes to product collapse rather than Latin-unit shear;
- `T(x,y)=(x,x+y mod 2)` is Latin-unit triangular as a bijective row, but it
  fails the endpoint-shear YBE equation and is not a YBE bottleneck.

## Updated obstruction

A normalized-law B route can no longer start from a one-colour Latin-unit
triangular shear.  Any remaining companion-shear obstruction must use genuinely
coloured quotient transport, where the alpha maps do not reduce to a single
idempotent permutation.

The next target is therefore:

```text
Multi-colour companion-shear longitude visibility.
```

A proof of A must show that the coloured shear endpoint lies in the fixed
longitude subgroup `V_beta(U_shear)`.  A proof of B must produce an explicit
multi-colour shear endpoint miss and upgrade it to the normalized-law sequence
required by the sharp obstruction theorem.

