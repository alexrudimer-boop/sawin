# Escape-rack strand-separation counterexample

## Verdict

The minimal-ideal escape-rack strand-separation lemma is false as stated.
This is not a counterexample to Sawin finite-rack domination. It kills the
proposed minimal-ideal escape-rack orbit-injectivity route unless extra
rigid-core hypotheses or additional finite state are added.

The refuted assertion is:

```text
w' in B_n w and Psi_n(w') = Psi_n(w)  =>  w' = w.
```

## The solution

Let

```text
X = F_2^2 = {00,01,10,11}.
```

Define

```text
r((a,b),(c,d)) = ((d, a+b+d), (a+c+d+1, a+1))
```

over `F_2`.

Index the four elements by

```text
0 = 00, 1 = 01, 2 = 10, 3 = 11.
```

This is a finite bijective set-theoretic YBE solution. Both sides of the YBE
on a triple `(a,b),(c,d),(e,f)` expand to

```text
(c+d+f,
 a+b+c+d+f,
 c+1,
 d+1,
 a+c+d+e+f,
 a+c+d).
```

The solution is everywhere singular: every left map and every right map has
image size `2`.

## Minimal-image objects

The left and right minimal-image objects are both:

```text
E_0 = {0,3},   E_1 = {1,2}.
```

For `p,i,j in F_2`, write

```text
e_{pij} = eta(x; E_i, E_j)
```

where `x` has parity `p`.

The escape quotient includes the relations `b' ~ a`. In this example those
relations force the spanning-tree collapse:

```text
e000 ~ e001
e000 ~ e010
e010 ~ e110
e001 ~ e100
e100 ~ e011
e011 ~ e101
e101 ~ e111
```

Therefore all elementary escape labels have the same image in `Y_esc`, and
`Psi_n` is constant for every arity `n`.

## Same-orbit collision

In arity `2`, take

```text
w  = (00,01)
w' = (00,10).
```

They are distinct, but they lie in the same `B_2` orbit:

```text
(00,01) -> (11,01) -> (11,10) -> (00,10) -> (00,01).
```

Thus

```text
w' = sigma_1^3 w.
```

Since `Psi_2` is constant,

```text
Psi_2(w') = Psi_2(w),
```

but `w' != w`. This refutes the escape-rack orbit-injectivity lemma.

## Consequence

The minimal-ideal escape-rack construction may still produce an equivariant
finite-rack label. It does not, by itself, prove orbit separation. The route
needs extra rigid-core hypotheses excluding this affine Type A collapse, or it
needs additional finite state beyond the minimal-ideal escape labels.
