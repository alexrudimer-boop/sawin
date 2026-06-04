# Affine F2 Hidden Cyclic Gauge

Date: 2026-06-04

This note closes the first left-degenerate non-involutive affine `F_2^3`
pressure row from `proofs/affine_f2_q3_pressure_audit.md`.

The row is not recognized by the ordinary table-level `branch_tags`, but it is
all-arity braid-kernel equivalent to the two-element cyclic rack.  Thus `Q_2`
already dominates it, and every fixed-`Q_3` bounded-deletion obstruction is
trivial.

The later note `proofs/non_bisectional_transducer_gauge_fork.md` records a
second role for this row: it refutes universal single-strand bisectional
endpoint enrichment.  For fixed `x=(a,z)`, the map

```text
lambda_x(b,w)=(a,Jw)
```

has image `{a} x W`, so no finite permutation-fibre semiconjugacy can
reconstruct the actual local update.  This failure is not Sawin-negative
because the position-dependent gauge below still gives kernel equality with
the two-element cyclic rack.

## The Row

Let `X=F_2^3` and write elements as

```text
x=(x1,x2,x3).
```

The affine table is

```text
R(x,y)=(x1,y3,y2, y1,x3+1,x2+1),
```

or, in matrix form over `F_2`,

```text
100000
000001
000010
000100
001000
010000
```

with offset

```text
000011.
```

It is left-degenerate and non-involutive.  The two-strand crossing has order
`4`, so `a_X(2)=2`.

## Gauge

Write each element as

```text
x=(a,z),       a in F_2, z=(z1,z2) in W=F_2^2.
```

Let

```text
J(z1,z2)=(z2,z1),
c=(1,1).
```

Then

```text
R((a,z),(b,w))=((a,Jw),(b,Jz+c)).
```

The `F_2` coordinate is inert.  All braid action is carried by `W`.

For arity `n`, define a position-dependent bijection

```text
Theta_n:X^n -> (F_2)^n x W^n
```

by

```text
u_i = J^i z_i + epsilon_i c,
epsilon_i = i mod 2
```

with one-based positions.  Since `J^2=1` and `Jc=c`, the braid generator
`sigma_i` acts in the `u` coordinates by

```text
(u_i,u_{i+1}) -> (u_{i+1}+c, u_i).
```

This is exactly the constant-action rack on `W` whose common left translation
is

```text
pi(u)=u+c.
```

Therefore, for every `n`, the action on `X^n` is conjugate to the identity
action on `(F_2)^n` times this constant-action rack on `W^n`.

## Kernel Equivalence

The permutation `pi:u -> u+c` has order `2`.  A constant-action rack with a
common permutation of order `2` has the same braid kernels as the two-element
cyclic rack

```text
C_2: R(p,q)=(q+1,p).
```

For a pure braid `beta`, the action is

```text
u_i -> u_i + w_i(beta)c,
```

where `w_i(beta)` is the row-sum of pairwise pure-braid linking numbers.
Thus the kernel condition is:

```text
beta is pure and w_i(beta)=0 mod 2 for every i.
```

This is also the kernel condition for the two-element cyclic rack.  Hence

```text
ker rho^X_n = ker rho^{C_2}_n
```

for every arity `n`.

Since `Q_2` contains `C_2`, and the other size-at-most-two racks only impose
the same permutation/purity condition already visible in `C_2`,

```text
D_2(n)=ker rho^{C_2}_n=ker rho^X_n.
```

So `Q_2` dominates `X`, in fact with kernel equality.

## Consequence

Since `D_3(n) subset D_2(n)`, every `D_3`-blind braid is already `X`-trivial.
Therefore

```text
E^{(3)}_{X,h,n}=1
```

for every `h,n`.

This explains the exact computations

```text
E^{(3)}_{X,2,3}=1,
E^{(3)}_{X,2,4}=1.
```

The `n=5` stabilizer run is unnecessary for this row.

## Brunnian Family Check

The fixed-`Q_3` Brunnian family from
`proofs/fixed_q3_affine_rack_obstruction.md` cannot produce an obstruction
here.  Its words `beta_N` lie in `D_3(N)`, hence in `D_2(N)`, and are therefore
`X`-trivial by the kernel equality above.

Local augmented-affine matrix checks also verify this directly for
`3 <= N <= 6`.
