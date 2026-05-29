# Direct rack-cover obstruction

## Statement

A tempting way to prove finite-rack domination would be to cover every finite
bijective YBE solution by a finite rack as a braided set.  This cannot work
except in the rack-type case.

Let `p : Y -> X` be an onto braided-set homomorphism, where `Y` is a rack with
braiding

```text
R_Y(a,b) = (a ▷ b, a).
```

If `p(a)=x`, `p(b)=y`, and

```text
R_X(x,y) = (u,v),
```

then the homomorphism condition gives

```text
(p(a ▷ b), p(a)) = (u,v).
```

Therefore `v=p(a)=x` for every pair `(x,y)` in `X^2`.  In other words,

```text
pr_2 R_X(x,y) = x
```

for all `x,y`.  This is exactly the rack-type condition on the second
coordinate.

## Consequence

The global Sawin domination problem cannot be solved by a naive finite rack
cover of `X`.  Any proof of A must be indirect: the rack must detect the braid
action through Artin-longitude, quotient/residual, Green-kernel, or other
finite detector data, rather than mapping onto `X` as a braided set.  Likewise,
a failure of direct rack cover is not evidence for B; even the identity
solution has this obstruction but may still be dominated by an indirect rack.

The executable helper `rack_quotient_obstructions(X)` records the triples
`(x,y,v)` with `R_X(x,y)=(u,v)` and `v != x`.

## Longitude-Formula Guardrail

The same one-crossing obstruction rules out a second tempting shortcut.  One
might try to prove the direct symmetric detector target by imitating the rack
formula

```text
rho_X(beta)(x)_j = phi_x(L_j(beta))(x_{p(j)})
```

with `phi_x:F_n -> Sym(X)` allowed to depend on the input tuple.  For
`beta=sigma_i`, however, the recursive Artin data has

```text
p(i+1)=i,     L_{i+1}(sigma_i)=1.
```

The formula would force the `(i+1)`-st output of the crossing to be exactly
`x_i`.  Thus any solution admitting this rack-style coordinatewise longitude
formula for the generator is already rack-type.

Consequently, a proof of the possible `A_{Sym(X)}` shortcut cannot be a
literal rack-action formula on `X`.  It must prove the weaker and more
global statement that the entire braid representation factors through the
Artin action on the finite verbal quotient `W_{Sym(X)}(n)`, or else use the
local quotient/residual detector machinery.  This guardrail is why the
non-rack direct-cover obstruction is not by itself a counterexample.

The positive structure monoid has the same limitation if one passes too
quickly to a group and tries to use ordinary Hurwitz conjugation.  A Hurwitz
move in a group sends a pair `(g,h)` to `(g h g^{-1}, g)`, so its second
coordinate is again the left input.  Therefore any proof that identifies
`R_X(x,y)` with a literal group Hurwitz move on representatives of `x,y`
again proves only the rack-type branch.  The structure-monoid orbit
reduction remains useful because it records the finite degree congruence
classes, but the unresolved holonomy inside those classes is not solved by
ordinary group conjugation.
