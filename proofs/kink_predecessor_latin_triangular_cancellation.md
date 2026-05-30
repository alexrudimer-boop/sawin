# Kink-predecessor cancellation for Latin triangular rows

Date: 2026-05-30

This note closes the last triangular obstruction isolated by the preceding
Latin triangular YBE split.  It proves that, over a rack-base quotient, a
nontrivial Latin-unit triangular lower row cannot survive: every fibre in such
a row must be singleton.

This is still recorded as a local-branch theorem, not as a standalone final
answer to Sawin's problem.  The global A-route also uses the earlier
quotient/residual setup, sharp obstruction theorem, endpoint factorization,
transport-rack closure, and congruence-chain induction.

## Setup

Let the base be a finite rack in left convention:

```text
R_A(a,b) = (a*b, a).
```

Assume the remaining lower row is Latin-unit triangular:

```text
T_{a,b}(x,y) =
  (alpha_{a,b}(x), beta_{a,b,x}(y)),
```

where

```text
x in X_a,       y in X_b,
alpha_{a,b}: X_a -> X_{a*b}
```

is bijective.  Write

```text
x circ_{a,b} y := beta_{a,b,x}(y) in X_a.
```

The Latin-unit hypothesis is that, for every colour pair `(a,b)`,

```text
y -> x circ_{a,b} y
```

and

```text
x -> x circ_{a,b} y
```

are bijections.

## Theorem

Every fibre `X_b` is singleton.

## Proof

The triangular YBE split gives the first-output identity

```text
alpha_{a*b,a*c} alpha_{a,b}
=
alpha_{a,b*c}.                         (1)
```

It also gives the third-output identity

```text
(x circ_{a,b} y) circ_{a,c} z
=
(x circ_{a,b*c} alpha_{b,c}(y))
  circ_{a,b}
(y circ_{b,c} z).                       (2)
```

Let the rack kink map be

```text
kappa(b)=b*b.
```

In a rack, `L_{kappa(b)}=L_b`.  Therefore, if `c=kappa^{-1}(b)`, then

```text
b*c=b.
```

First prove

```text
alpha_{kappa(d),d}=id
```

for every colour `d`.  Put

```text
a=d,       b=d,       c=kappa^{-1}(d)
```

in `(1)`.  Since

```text
d*d=kappa(d),
d*kappa^{-1}(d)=d,
```

equation `(1)` becomes

```text
alpha_{kappa(d),d} alpha_{d,d}
=
alpha_{d,d}.
```

The map `alpha_{d,d}` is bijective, so

```text
alpha_{kappa(d),d}=id.
```

Now fix a colour `b` and set

```text
c=kappa^{-1}(b).
```

Taking `d=c` in the preceding identity gives

```text
alpha_{b,c}=id,
```

because `kappa(c)=b`.  Also `b*c=b`.

Substitute this choice of `c` into `(2)`.  The equation becomes

```text
(x circ_{a,b} y) circ_{a,c} z
=
(x circ_{a,b} y) circ_{a,b} (y circ_{b,c} z).       (3)
```

Fix `a,b,z`.  For each fixed `y`, the map

```text
x -> x circ_{a,b} y
```

is bijective.  Hence

```text
p := x circ_{a,b} y
```

ranges over all of `X_a`.  Equation `(3)` therefore says that, for every
`p in X_a`,

```text
p circ_{a,c} z
=
p circ_{a,b} (y circ_{b,c} z).                      (4)
```

For fixed `p`, the map

```text
t -> p circ_{a,b} t
```

is bijective, hence injective.  The left side of `(4)` is independent of `y`,
so the value

```text
y circ_{b,c} z
```

is independent of `y`.

Thus, for every fixed `z`, the map

```text
y -> y circ_{b,c} z
```

is constant.  The Latin-unit hypothesis says the same map is bijective.  A
constant bijection exists only when

```text
|X_b|=1.
```

Since `b` was arbitrary, every fibre is singleton.  QED.

## Executable audit

The helper

```text
rack_kink_latin_triangular_collapse_audit(interval)
```

records the finite hypotheses and cancellations:

- the base rows have rack form `(a*b,a)`;
- left translations are bijective and self-distributive;
- kink predecessors `kappa^{-1}(b)` exist;
- all colour-pair rows are left Latin-unit triangular;
- the Latin triangular YBE equations hold;
- the maps `alpha_{kappa(d),d}` are identity;
- the predecessor columns `y -> y circ_{b,kappa^{-1}(b)} z` are constant.

The audit exposes the theorem's conclusion by checking that no non-singleton
Latin fibre remains when the hypotheses and cancellations hold.

## Consequence for the local A-route

The previously isolated triangular obstruction was:

```text
nontrivial rack-kink Latin-unit triangular companion-shear holonomy.
```

The theorem proves this obstruction cannot occur.  The remaining lower-row
cases therefore route to already established fixed finite detector mechanisms:

- strand-continuing rows are detected by transport-state rackification;
- product/permutation triangular rows route to product holonomy detectors;
- proper-rank nonunit rows are Green/Schutzenberger-visible;
- nonunit/reset composites cannot be final residual permutations;
- Green/Schutzenberger defects reduce to Artin-visible commutators plus
  terminal gauge;
- one-colour Latin shear is already impossible, and the rack-kink argument
  removes the multi-colour rack-base Latin shear.

Thus, conditional on the preceding branch reductions, the
`bi_free_universal_corridor_bottleneck` has no remaining lower-row obstruction.
The interval-level detector group remains a fixed finite product

```text
H(pi,Q)
```

of Green, Schutzenberger, atom, known-branch, endpoint/unit, and
transport-state factors, with no braid-index parameter.  The endpoint
factorization and product-longitude calculus then give

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
    => Delta_n(beta)=1.
```

The sharp obstruction theorem supplies the local rack `Q x A_H`, and
congruence-chain induction assembles the global rack.

