# Right-rack kink cancellation for Latin triangular rows

Date: 2026-05-31

This note is the side-dual companion to
`proofs/kink_predecessor_latin_triangular_cancellation.md`.  It proves the
right-rack orientation needed by System K-dual in
`proofs/triangular_recovery_side_dual_completion.md`.

## Setup

Let the base have right-rack form

```text
R(a,b) = (b, b*a).
```

Assume every lower row is left Latin-unit triangular:

```text
T_{a,b}(x,y) = (alpha_{a,b}(x), beta_{a,b,x}(y)).
```

Here

```text
alpha_{a,b}: X_a -> X_b,
beta_{a,b,x}: X_b -> X_{b*a}.
```

Latin-unit means that, for every colour pair `(a,b)`,

```text
y -> beta_{a,b,x}(y)
```

and

```text
x -> beta_{a,b,x}(y)
```

are bijections.

## Theorem

Every fibre is singleton.

## Proof

For a right-rack base, the first projection of the Latin triangular YBE gives

```text
alpha_{b,c} alpha_{a,b} = alpha_{a,c}.      (1)
```

Putting `a=b` in `(1)` gives

```text
alpha_{b,c} alpha_{b,b} = alpha_{b,c}.
```

Since `alpha_{b,c}` is bijective,

```text
alpha_{b,b}=id.                              (2)
```

The endpoint projection of the Latin triangular YBE is, in this orientation,

```text
beta_{b*a,c, beta_{a,b,x}(y)}(z)
=
beta_{c*a,c*b,
  beta_{a,c,x}(alpha_{b,c}(y))}
  (beta_{b,c,y}(z)).                         (3)
```

Set `c=b`.  Using `(2)`, equation `(3)` becomes

```text
beta_{b*a,b, beta_{a,b,x}(y)}(z)
=
beta_{b*a,b*b, beta_{a,b,x}(y)}
  (beta_{b,b,y}(z)).                         (4)
```

Fix `a,b,z` and a value

```text
p in X_{b*a}.
```

For each fixed `y`, the map

```text
x -> beta_{a,b,x}(y)
```

is bijective, so `p=beta_{a,b,x}(y)` can be achieved.  Equation `(4)` says

```text
beta_{b*a,b,p}(z)
=
beta_{b*a,b*b,p}(beta_{b,b,y}(z)).
```

For fixed `p,z`, the left side is independent of `y`.  The map

```text
t -> beta_{b*a,b*b,p}(t)
```

is bijective, hence

```text
beta_{b,b,y}(z)
```

is independent of `y`.  But Latin-unit says that, for fixed `z`, the map

```text
y -> beta_{b,b,y}(z)
```

is bijective.  A constant bijection exists only when `|X_b|=1`.  Since `b`
was arbitrary, every fibre is singleton.  QED.

## Executable audit

The helper

```text
right_rack_kink_latin_triangular_collapse_audit(interval)
```

records:

- right-rack base form `(b,b*a)`;
- bijective right translations and right self-distributivity;
- left Latin-unit triangular rows for every colour pair;
- side-dual Latin YBE equations;
- `alpha_{b,b}=id`;
- constancy of the diagonal columns `y -> beta_{b,b,y}(z)`.

The nonlinear side-dual audit applies this helper to

```text
side_opposite_local_interval(interval).
```

Thus a System K-dual row whose side-dual Latin YBE equations hold is closed:
non-singleton fibres contradict the theorem, while singleton fibres carry no
remaining lower-row obstruction.
