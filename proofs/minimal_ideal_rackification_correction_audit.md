# Minimal-Ideal Rackification Correction Audit

Date: 2026-06-05

This note records the corrected scorecard for the minimal-ideal rackification
route.

## Correct statements

Bijectivity of

```text
r(x,y)=(L_x(y),R_y(x))
```

forces global balance and Latin fibres.  For every `u in X`,

```text
|{(x,y): L_x(y)=u}| = |X|,
```

and the map

```text
(x,y) -> R_y(x)
```

is a bijection from that fibre to `X`.  The dual statement holds for each
right output fibre.

If `p:Y -> X` is a surjective morphism of YBE solutions, then `p^n` is
surjective and `B_n`-equivariant, so

```text
ker rho^Y_n subset ker rho^X_n.
```

If `Y` is a rack solution in the convention

```text
r_Y(a,b)=(a*b,a),
```

then a surjective morphism `Y -> X` forces

```text
R_y(x)=x
```

for all `x,y`.  Thus a rack cover can cover only a rack-type solution.  An
everywhere-singular solution cannot be dominated by a rack cover.

If every `L_x` is singular, the finite semigroup

```text
S_L=<L_x>
```

contains no permutations.  Its minimal ideal is the set of minimal-rank
elements.  Idempotents `e` in this ideal have images `Omega_e=im(e)`, and the
local groups `eK_Le` act faithfully on `Omega_e`.

The correct canonical object is the minimal-ideal transport groupoid, not one
canonical group.  Choosing `e` chooses a base object.

## Corrections

Idempotents act constantly on the set of minimal images, but not pointwise
constantly on minimal images.  If `e` is idempotent and `Omega_s=im(s)` is a
minimal image, then

```text
e(Omega_s)=Omega_e,
```

but the restriction

```text
e : Omega_s -> Omega_e
```

is a bijection.

The subsolution dichotomy needs the combined left/right action.  If a nonempty
proper subset `A` is invariant under all `L_x` and all `R_y`, then

```text
r(A^2) subset A^2,
```

and bijectivity gives `r(A^2)=A^2`.  Left-invariance alone does not control the
second coordinate.

Kernel containment is not equivalent to an equivariant surjection

```text
Y^n -> X^n.
```

An equivariant surjection implies kernel containment, but not conversely.  A
claim that one finite rack `Y` has

```text
ker rho^Y_n subset ker rho^X_n
```

for all `n` is exactly Sawin for `X`, not a smaller theorem unless `Y` is
constructed by a constrained mechanism.

## Current exact endpoint

The minimal-ideal route has proved finite semigroup structure and flat
left/right transport.  It has not produced a finite rack detector.

The best current theorem target is:

> Minimal-ideal rackification theorem.  Every everywhere-singular rigid core
> has a finite rack `Y` and finite observers built from the combined left/right
> minimal-ideal transport groupoids such that
>
> ```text
> X^n -> Y^n x I_n
> ```
>
> is braid-equivariant and injective for every `n`.

The first missing proof input is a Y2-coupling theorem: the middle
Yang-Baxter identity must turn the left/right minimal-ideal groupoids and the
finite product observers into actual coordinate rack colours, or else force a
proper quotient, subsolution, or observer.

