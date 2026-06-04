# A size-four affine degenerate solution with cyclic-rack braid action

This note records an all-arity mechanism for one Type A size-four degenerate
non-involutive solution.  It is stronger than bounded-level domination: its
braid action is fibrewise conjugate to the two-element cyclic rack action.

Let

```text
X = F_2^2.
```

Write `x=(a,b)` and `y=(c,d)`.  Define

```text
r(x,y) =
(
  (d, a+b+d),
  (a+c+d+1, a+1)
)
```

with all additions in `F_2`.

This is bijective.  If `r(x,y)=(u,v)` with `u=(u_1,u_2)` and
`v=(v_1,v_2)`, then

```text
a = v_2+1,
d = u_1,
b = u_2+v_2+1+u_1,
c = v_1+v_2+u_1.
```

The solution is left-degenerate and non-involutive:

```text
lambda_(0,0)(0,0) = lambda_(0,0)(1,0) = (0,0),
r((0,0),(0,0)) = ((0,0),(1,1)),
r^2((0,0),(0,0)) = ((1,1),(1,1)).
```

## Fibrewise cyclic-rack coordinates

For a tuple `x_j=(a_j,b_j)`, set

```text
p_j = a_j+b_j.
```

A direct substitution in the formula for `r` shows that each `p_j` is
preserved by every adjacent braid generator.  Thus the braid action preserves
each parity fibre.

Fix a parity vector `p=(p_1,...,p_n)`.  Define offsets

```text
H_1 = 0,
H_{j+1} = H_j + p_{j+1} + 1,
```

and fibre coordinates

```text
t_j = a_j + H_j.
```

For an adjacent generator `sigma_i`, another direct substitution gives

```text
(t_i,t_{i+1}) -> (t_{i+1}+1,t_i),
```

with all other `t_j` unchanged.  This is exactly the braid action of the
two-element cyclic rack

```text
R(s,t) = (t+1,s).
```

Therefore, on every parity fibre of `X^n`, the braid action is conjugate to
the same cyclic-rack action on `{0,1}^n`.  Consequently

```text
ker(B_n -> Sym(cyclic_rack^n)) = ker(B_n -> Sym(X^n))
```

for every `n`.

The finite verification of this coordinate formula is in
`tests/test_size4_degenerate_mechanisms.py`.

This proves finite rack domination for this Type A model.  The remaining
classification step for the full forced size-four census is to show that the
other reported Type A tables are isomorphic, side-opposite, relabelled, or
otherwise braid-equivalent to this affine model.
