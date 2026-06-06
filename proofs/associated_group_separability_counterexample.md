# Associated-Group Separability Counterexample

Date: 2026-06-05

This note records the failure of the Endpoint Associated-Group Separability
Theorem.  The failure is structural, not accidental.

For every rack `R`, the canonical map

```text
eta_R:R -> Conj(As(R))
```

collapses:

```text
eta_R(u triangleright u)
=
g_{u triangleright u}
=
g_u g_u g_u^{-1}
=
g_u
=
eta_R(u).
```

Therefore associated-group methods cannot separate a pair:

```text
e' = e triangleright e, e' != e.
```

Any finite group quotient gives a finite conjugation rack, and conjugation
racks are idempotent:

```text
g triangleright g=g.
```

Arbitrary finite rack quotients need not be idempotent, so finite rack
separation is strictly stronger than associated-group separation.

## Explicit Counterexample

Let:

```text
X={0,1},
tau=(0 1),
r(i,j)=(tau(j),i).
```

This is the constant-action rack solution with rack operation:

```text
i triangleright j=tau(j).
```

The table is:

```text
(0,0)->(1,0)
(0,1)->(0,0)
(1,0)->(1,1)
(1,1)->(0,1)
```

It is bijective.  The YBE holds because both sides send `(i,j,k)` to:

```text
(tau^2(k), tau(j), i).
```

Take the finite quotient:

```text
M=1.
```

Write:

```text
c_i=[1,i,1] in C_1(X).
```

For `r(x,y)=(tau(y),x)`, the `(T)` relation imposes no collapse.  The `(R)`
relation becomes:

```text
c_x triangleright c_y = c_{tau(y)}.
```

So:

```text
c_0 triangleright c_0 = c_1.
```

Let:

```text
e=c_0,
e'=c_1.
```

These are endpoint elements occurring in local principal endpoint transitions.

## Finite Rack Separation

Define the finite rack:

```text
Q={0,1},
i triangleright j=tau(j).
```

Each left translation is `tau`, hence bijective.  Self-distributivity holds:

```text
i triangleright (j triangleright k)
= tau(tau(k))=k,

(i triangleright j) triangleright (i triangleright k)
= tau(tau(k))=k.
```

The assignment:

```text
c_0 -> 0,
c_1 -> 1
```

satisfies all defining `(T)` and `(R)` relations of `C_1(X)`.  Therefore it
extends to a rack homomorphism:

```text
C_1(X) -> Q
```

and separates:

```text
e != e'.
```

Thus `e,e'` are finitely rack-separated.

## Associated Group Collapse

Let:

```text
a_i=g_{c_i}.
```

The associated group has presentation:

```text
As(C_1(X))
=
< a_0,a_1 | a_{tau(y)}=a_x a_y a_x^{-1} for x,y in {0,1} >.
```

Using `x=0,y=0`:

```text
a_{tau(0)}=a_0 a_0 a_0^{-1}.
```

Since `tau(0)=1`, this gives:

```text
a_1=a_0.
```

Therefore:

```text
eta(e')=g_{c_1}=a_1=a_0=g_{c_0}=eta(e).
```

No finite quotient of the associated group can separate equal group elements.

Indeed, in this example:

```text
As(C_1(X)) ~= Z.
```

The failure is not group non-residual-finiteness.  The failure is
non-injectivity of:

```text
eta:C_1(X)->Conj(As(C_1(X))).
```

## General Obstruction

Associated-group separation can only work on endpoint subsets satisfying:

```text
u triangleright u != u
implies
not both u and u triangleright u are distinct relevant endpoints.
```

The counterexample violates this exactly:

```text
e triangleright e=e',
e != e',
eta(e)=eta(e').
```

## Presentation Analysis

For general `X,M`, write:

```text
a_{p,x,s}=g_{[p,x,s]}.
```

The associated group presentation induced by `(T)` and `(R)` is:

```text
a_{p,x,bar{y}s}
=
a_{p bar{x'},y',s},

a_{p,x',bar{y'}s}
=
a_{p,x,bar{y}s}
a_{p bar{x},y,s}
a_{p,x,bar{y}s}^{-1}.
```

In the counterexample, `(T)` is trivial and `(R)` gives:

```text
a_{tau(y)}=a_x a_y a_x^{-1}.
```

Taking `x=y` gives:

```text
a_{tau(y)}=a_y.
```

For `tau=(0 1)`, this collapses `a_0=a_1`.

## Special Cases

The theorem already fails for:

```text
M=1,
X a rack solution,
X left- and right-nondegenerate,
constant-action / permutation solutions,
|X|=2.
```

For constant-action solutions:

```text
r(x,y)=(f(y),x),
```

with `M=1`,

```text
c_x triangleright c_y=c_{f(y)}.
```

The associated group relation with `x=y` gives:

```text
a_{f(y)}=a_y.
```

So `eta` collapses every `f`-orbit.

In involutive solutions the associated-group method behaves better.  The
contextual relations force `u triangleright v=v` after `(T)` reductions, so
the associated group becomes a right-angled Artin-type group on endpoint
`(T)`-classes with commutation relations.  Distinct endpoint classes survive
in abelianization.  This special case does not rescue the general theorem.

## Correct Replacement

The associated-group certificate format is insufficient.  The correct finite
certificate is rack-valued:

```text
finite rack Q,
assignment alpha:M x X x M -> Q,
verification of all (T) relations,
verification of all (R) relations,
alpha(e) != alpha(e').
```

This directly certifies finite rack separation.

Group-valued certificates only certify separation by finite conjugation racks.
They miss non-idempotent finite rack distinctions, exactly as the example
shows.

## Consequence

The Endpoint Associated-Group Separability Theorem is false.

The next viable computational route is the full finite rack SAT/enumeration
detector, not associated-group separation.  Associated-group search may remain
a useful cheap sufficient test, but it cannot be the completeness mechanism
for orbit-relevant finite residuality.
