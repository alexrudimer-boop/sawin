# Prefix-Path Totalization Boundary

Date: 2026-06-05

The product-observer prefix-path factor gives a finite partial Yang-Baxter
action on valid paths in the Cayley graph of the left coordinate monoid.  This
note records why the obvious totalization is not available.

## Valid edge-pair action

Let

```text
E_L = S_L^1 x X.
```

An edge `(p,x)` has source `p` and target `pL_x`.  Valid adjacent edge pairs
are

```text
((p,x),(pL_x,y)).
```

For

```text
r_X(x,y)=(u,v),
```

the prefix-path rewrite is

```text
((p,x),(pL_x,y)) -> ((p,u),(pL_u,v)).
```

This is a bijection on the set of valid adjacent edge pairs, with inverse
induced by `r_X^{-1}`.

## Naive totalization fails

A tempting total operation on all of `E_L^2` is to ignore whether the second
edge starts at `pL_x` and set

```text
((p,x),(q,y)) -> ((p,u),(pL_u,v)),
qquad r_X(x,y)=(u,v).
```

This agrees with the path rewrite on valid pairs.  But it is not bijective as
soon as `|S_L^1|>1`, because the input source `q` is erased.

More generally, any extension whose two output edge sources are functions only
of `p,x,y` and not of the second source `q` cannot be a bijection on
`E_L^2` unless the second source set is singleton.  For fixed `p,x,y`, all
inputs with different `q` have the same output.

## Carrying q does not preserve the path action

The opposite naive repair is to keep the second source:

```text
((p,x),(q,y)) -> ((p,u),(q,v)).
```

This can remember `q`, but on a valid input `q=pL_x` it gives

```text
((p,u),(pL_x,v)),
```

whereas the path rewrite requires

```text
((p,u),(pL_u,v)).
```

Thus it does not preserve the prefix-path code except in the special case
`pL_x=pL_u`.

## Boundary

The prefix-path factor is therefore not automatically a total finite YBE
solution on the edge alphabet `S_L^1 x X`.  A successful totalization must carry
enough extra finite state to remember the off-path source `q` while still
specializing to the composable rewrite on valid pairs.

Equivalently, the rackification problem is not merely:

```text
extend the partial path action to E_L^2.
```

It is:

> Find a finite rack or total finite YBE detector whose action contains the
> valid prefix-path action equivariantly and injectively, while preserving the
> composability constraints as inert observer data.

This boundary explains why the prefix-path theorem is a real sharpening but
not yet a Sawin proof.

