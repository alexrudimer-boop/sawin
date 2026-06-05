# Product Semigroup Observer Theorem

Date: 2026-06-05

This note records the arity-dependent observer theorem for everywhere-singular
finite bijective YBE solutions.

It changes the meaning of the residual rigid-core endpoint: an
everywhere-singular solution cannot be observer-rigid if observers are allowed
to be arbitrary finite-valued `B_n`-invariant maps on `X^n`.

## Theorem

Let `X` be finite, let `r:X^2 -> X^2` be bijective, and write

```text
r(x,y)=(L_x(y),R_y(x)).
```

Assume the first coordinate YBE identity

```text
L_{L_x(y)} L_{R_y(x)} = L_x L_y.          (Y1)
```

If every `R_a` is singular, then for every `n >= 2` the map

```text
Lambda_n(x_1,...,x_n)=L_{x_1} L_{x_2} ... L_{x_n}
```

from `X^n` to the finite semigroup `S_L=<L_x>` is a nonconstant
`B_n`-invariant observer.

Dually, assuming the third coordinate identity

```text
R_z R_y = R_{R_z(y)} R_{L_y(z)},          (Y3)
```

if every `L_a` is singular, then for every `n >= 2`

```text
Gamma_n(x_1,...,x_n)=R_{x_n} R_{x_{n-1}} ... R_{x_1}
```

is a nonconstant finite `B_n`-invariant observer.

## Bijectivity lemma

Fix `a in X`.  If the map

```text
x -> L_x(a)
```

is constant, say `L_x(a)=c` for every `x`, then

```text
r(x,a)=(c,R_a(x)).
```

Since `r` is injective on `X^2`, the values `R_a(x)` are all distinct.  Thus
`R_a` is injective, hence bijective because `X` is finite.

Therefore, if every `R_a` is singular, then for every `a`,

```text
x -> L_x(a)
```

is nonconstant.

The dual statement is: if `y -> R_y(a)` is constant, then `L_a` is bijective.

## Invariance of Lambda

The braid generator `sigma_i` replaces

```text
(x_i,x_{i+1})
```

by

```text
(L_{x_i}(x_{i+1}), R_{x_{i+1}}(x_i)).
```

By `(Y1)`, the adjacent product

```text
L_{x_i} L_{x_{i+1}}
```

is unchanged.  Hence the total product `Lambda_n` is unchanged by every
generator, and therefore by every braid.

## Nonconstancy of Lambda

Assume `Lambda_n` is constant for some `n>=2`.  Fix a suffix

```text
(x_2,...,x_n)
```

and set

```text
s=L_{x_2}...L_{x_n}.
```

Then `L_x s` is independent of `x`.  Choose `a in im(s)`, say `a=s(t)`.  Then

```text
L_x(a)=L_x s(t)
```

is independent of `x`.  By the bijectivity lemma, `R_a` is bijective,
contradicting the assumption that every `R_a` is singular.

Thus `Lambda_n` is nonconstant.

The proof for `Gamma_n` is dual, using `(Y3)`.

## Consequence

If `X` is finite, bijective, YBE, and every `L_a` and every `R_a` is singular,
then `X` has nonconstant finite invariant observers in every arity `n>=2`.

Therefore the package

```text
everywhere singular + broad observer-rigid
```

is inconsistent.

This does not contradict earlier one-state observer filters.  Those filters
forbid nonconstant maps `nu:X -> I` preserving each local row.  The product
semigroup observers above are arity-dependent finite observers

```text
X^n -> S_L or S_R.
```

## Minimal-ideal sandwich obstruction

Let `I_L` be the minimal-rank ideal of `S_L` and choose an idempotent `e`.
Although `eS_Le` is a finite local group on `im(e)`, the product law does not
automatically descend to the sandwiched local group.

From `(Y1)` one gets

```text
e L_{L_x(y)} L_{R_y(x)} e = e L_x L_y e.
```

But one does not automatically get

```text
e L_{L_x(y)} e L_{R_y(x)} e = e L_x e L_y e.
```

The insertion of `e` between factors may change the local group element.  Thus
minimal-ideal local groups do not by themselves inherit a YBE product law.

The product observers `Lambda_n` and `Gamma_n` avoid this sandwich problem by
remaining in the full finite transformation semigroups.  They still do not
produce a finite rack detector.

## Remaining gap

To prove Sawin-positive from this theorem, one needs an additional theorem:

> Product-observer rackification/reduction.  The invariant observers
> `Lambda_n` and `Gamma_n` either allow induction on observer fibers through
> smaller dominated YBE factors, or combine with a finite rack output to give
> an injective braid-equivariant code
>
> ```text
> X^n -> Y^n x I_n
> ```
>
> for all `n`.

This is now the exact post-observer endpoint.

