# Minimal Ideal Image Gate

Date: 2026-06-05

This note records the automatic part of the finite transformation semigroup
route for an everywhere-singular minimal counterexample to Sawin's finite-rack
domination problem.

It is deliberately modest.  It proves the left semigroup image trap that is
forced by finite semigroup theory, and identifies the exact right-coordinate
closure obstruction that remains before one obtains a proper crossing-closed
subsolution.

## Setup

Let `X` be a finite bijective set-theoretic Yang-Baxter solution and write

```text
r(x,y) = (L_x(y), R_y(x)).
```

Let

```text
M_L = <L_x : x in X>^1
```

be the finite left coordinate transformation monoid.  Let `I` be the minimal
two-sided ideal of `M_L`.  Define the minimal-ideal image support

```text
Omega_L = union_{f in I} im(f).
```

Since `M_L` is finite, `I` is nonempty.  If every `L_x` is singular, then every
element of `I` has rank strictly smaller than `|X|`.  Individual images
`im(f)` are therefore proper subsets, although their union `Omega_L` may still
be all of `X`.

## Lemma 1: left image support is L-stable

For every `a in X`,

```text
L_a(Omega_L) subset Omega_L.
```

Proof.  Let `y in Omega_L`.  Then `y=f(t)` for some `f in I` and `t in X`.
Because `I` is a left ideal of `M_L`,

```text
L_a f in I.
```

Thus

```text
L_a(y) = L_a f(t) in im(L_a f) subset Omega_L.
```

This proves the claim.

## Corollary 2: a one-sided trap becomes a subsolution exactly at right closure

If `Omega_L` is a nonempty proper subset of `X` and satisfies

```text
R_y(x) in Omega_L    for all x,y in Omega_L,
```

then `Omega_L` is a nonempty proper crossing-closed subsolution:

```text
r(Omega_L^2) = Omega_L^2.
```

Proof.  For `x,y in Omega_L`, Lemma 1 gives

```text
L_x(y) in Omega_L.
```

The displayed extra hypothesis gives

```text
R_y(x) in Omega_L.
```

So

```text
r(Omega_L^2) subset Omega_L^2.
```

Since `r` is a bijection of the finite set `X^2`, its restriction maps the
finite set `Omega_L^2` injectively into itself.  Hence the image has the same
cardinality as `Omega_L^2`, so the inclusion is equality.

## Dual statement

Let

```text
M_R = <R_y : y in X>^1
```

and let `J` be its minimal ideal.  Define

```text
Omega_R = union_{g in J} im(g).
```

Then every right coordinate map preserves `Omega_R`:

```text
R_a(Omega_R) subset Omega_R.
```

If `Omega_R` is proper and additionally

```text
L_x(y) in Omega_R    for all x,y in Omega_R,
```

then `Omega_R` is a proper crossing-closed subsolution.

## Consequence for a rigid core

A minimal rigid core with no proper crossing-closed subsolution must satisfy
the following dichotomy for the left minimal ideal:

1. `Omega_L = X`; or
2. there exist `x,y in Omega_L` such that

   ```text
   R_y(x) notin Omega_L.
   ```

Similarly, on the right:

1. `Omega_R = X`; or
2. there exist `x,y in Omega_R` such that

   ```text
   L_x(y) notin Omega_R.
   ```

Thus the minimal-ideal image route cannot close Sawin by ordinary finite
semigroup theory alone.  It must prove that the cross-coordinate escape in
case 2 is impossible under the full Yang-Baxter identities, or show that the
escape itself creates a quotient, observer, or finite active rack factor.

## Kernel-family transport

The same minimal ideal records a second automatic structure.  For `f in I`,
write `ker(f)` for the kernel partition of `X`.  If

```text
y ~_f y',
```

meaning `f(y)=f(y')`, then for every `a in X`,

```text
L_a(y) ~_{L_a f} L_a(y').
```

This is only a family-level invariance: the kernel relation is transported
from `f` to `L_a f`, another element of `I`.  It does not by itself give a
single invariant equivalence relation on `X`.

The exact next theoretical lemma is therefore:

> In an everywhere-singular quotient-rigid and subsolution-rigid finite
> bijective YBE solution, the minimal-ideal kernel family of `M_L` and `M_R`
> either collapses to a nonconstant invariant observer or its cross-coordinate
> escapes produce a finite observer-rack factor.

This is the first unproved step in the minimal-ideal route.  The current
`ask_now` prompt should push on precisely this lemma rather than on more
bounded enumeration.

