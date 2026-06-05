# Minimal-Ideal Transport Groupoid Boundary

Date: 2026-06-05

This note records the corrected theoretical status of the minimal-ideal
semigroup route for everywhere-singular finite set-theoretic Yang-Baxter
solutions.

## Cover route

Let `p:Y -> X` be a surjective morphism of set-theoretic YBE solutions:

```text
(p x p) r_Y = r_X (p x p).
```

Then `p^n:Y^n -> X^n` is surjective and `B_n`-equivariant for every `n`.
Therefore

```text
ker rho^Y_n subset ker rho^X_n.
```

If `Y` is a rack solution in the convention

```text
r_Y(a,b) = (a*b,a),
```

then a surjective morphism `p:Y -> X` forces

```text
R_y(x) = x       for all x,y in X.
```

Indeed, write `x=p(a)` and `y=p(b)`.  The second coordinate of the morphism law
gives

```text
R_y(x)=p(a)=x.
```

Thus an everywhere-singular solution cannot be dominated by a rack cover.  Any
dominating rack must be a detector, derived/factor object, or observer-code
object, not a surjective solution cover.

## Finite semigroup content

Let

```text
S_L = <L_x : x in X>
```

be the nonempty-product left coordinate transformation semigroup.

If every `L_x` is singular, then every element of `S_L` is singular.  Each
nonempty product has a leftmost singular generator, and for finite sets

```text
im(f g) subset im(f).
```

Thus `S_L` contains no permutation.  Conversely, `S_L` is a permutation
semigroup exactly when all generators are bijective, i.e. in the
left-nondegenerate branch.

Because `S_L` is finite, it has a minimal two-sided ideal `K_L`.  In a finite
transformation semigroup this ideal is the set of minimal-rank elements.  It
contains idempotents.  For an idempotent `e in K_L`, the local monoid

```text
e S_L e = e K_L e
```

is the maximal subgroup at `e`.  It acts faithfully on

```text
Omega_e = im(e).
```

Faithfulness: if `g in eS_Le` is trivial on `Omega_e`, then for every `x`,

```text
g(x)=e g e(x)=e(x),
```

so `g=e`.

For every generator `L_x` and every `s in K_L`, the map `L_x` restricts to a
bijection

```text
im(s) -> im(L_x s),
```

because both images have minimal rank and `im(L_x s)=L_x(im(s))`.

The same construction applies to the right coordinate semigroup

```text
S_R = <R_y : y in X>.
```

## Correction: groupoid, not canonical group

The minimal-ideal object is not one canonical finite group.  Choosing an
idempotent `e` chooses a base object and local group `eK_Le`.  Different
idempotents give isomorphic maximal subgroups inside the Rees/Green structure,
but not canonically without choices.

The canonical object is the minimal-ideal transport groupoid:

- objects: minimal-rank images `im(e)` for idempotents `e in K_L`;
- morphisms: restrictions of elements of `K_L` giving bijections between these
  images;
- vertex groups: `eK_Le`.

This groupoid is canonical up to canonical equivalence.  A single local group
is only a basepointed version.  The right side supplies a second transport
groupoid, and a positive route must use their YBE compatibility.

## Not the classical structure group

In the left-nondegenerate case, `S_L` is a finite permutation group and the
minimal ideal is the group itself with idempotent `id`.  The construction
therefore collapses to the finite left-permutation group image.

It is not literally the classical structure group

```text
< X | xy=uv whenever r(x,y)=(u,v) >,
```

which is generally infinite.  The accurate comparison is with a finite
permutation-image quotient of the structure group.

## What remains open

The transport groupoid does not by itself give Sawin domination.  A positive
proof still needs an actual finite rack `Y` and an all-arity injective code

```text
Phi_n : X^n -> Y^n x I_n
```

with `I_n` inert, or an equivalent kernel-containment detector.

The corrected conjecture is:

> Minimal-ideal rackification conjecture.  For every finite
> everywhere-singular bijective YBE solution surviving the known rigid-core
> filters, the combined left/right minimal-ideal transport groupoids admit a
> finite rackification `Y` and finite observer data reconstructing the
> `X`-braid action in every arity.

This is a genuine positive branch only after the rack `Y`, the observer data,
and the equivariant all-arity code are constructed.

