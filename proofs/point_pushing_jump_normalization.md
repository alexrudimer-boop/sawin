# Point-Pushing Jump Normalization

Date: 2026-05-30

This note sharpens the point-pushing `mu_X(k)` fork.  It shows that any
increase in the symmetric detector degree profile can be witnessed in one
relative kernel: the word may be chosen to become trivial after deleting the
newly added far-left stationary strand.

It does not prove outcome A or B.  It replaces arbitrary high-arity failures by
one-new-strand Brunnian failures.

## Setup

Use right-based point-pushing coordinates.  At arity `k`, let

```text
F_k=<a_1,...,a_k>
```

where `a_i` maps to `A_{k+1-i,k+1}` in `P_{k+1}`.  Thus `a_1` is the
point-push around the stationary strand nearest the moving last strand, and
`a_k` is the farthest one.

For a finite solution `X` and integer `m`, define

```text
delta_{m,k}: F_k -> D_k(S_m),
pi_{X,k}:   F_k -> P_k(X),
```

and set

```text
R_{m,k}=ker(delta_{m,k}),
N_{X,k}=ker(pi_{X,k}).
```

The marked quotient condition at arity `k` is exactly

```text
R_{m,k} <= N_{X,k}.
```

Passing from arity `k` to arity `k+1` adds one new far-left stationary strand.
In right-based coordinates this gives maps

```text
s_k:F_k -> F_{k+1},      s_k(a_i)=a_i,
r_k:F_{k+1}->F_k,        r_k(a_i)=a_i for i<=k,   r_k(a_{k+1})=1.
```

## Theorem

Assume

```text
R_{m,k} <= N_{X,k}.
```

Then arity `k+1` fails,

```text
R_{m,k+1} not <= N_{X,k+1},
```

if and only if there exists a word

```text
w in ker(r_k)
```

such that

```text
w in R_{m,k+1}
```

but

```text
w notin N_{X,k+1}.
```

Equivalently, every detector-degree jump can be witnessed by a point-pushing
braid that becomes the identity after deleting the newly added far-left
stationary strand.

## Proof

The reverse implication is immediate.

For the forward implication, choose

```text
u in R_{m,k+1} \ N_{X,k+1}.
```

Apply deletion:

```text
v=r_k(u) in F_k.
```

Deleting the newly added stationary strand sends derivative-detector identity
in arity `k+1` to derivative-detector identity in arity `k`; hence

```text
v in R_{m,k}.
```

Since `S_m` is assumed to detect arity `k`, we have

```text
v in N_{X,k}.
```

Lift `v` back by the suffix inclusion:

```text
s_k(v) in F_{k+1}.
```

The suffix subgroup acts on the old suffix coordinates and leaves the newly
added far-left coordinate untouched.  Therefore `s_k(v)` acts trivially on
`X^{k+2}`:

```text
s_k(v) in N_{X,k+1}.
```

Detector suffix compatibility also gives

```text
s_k(v) in R_{m,k+1}.
```

Now set

```text
w = u s_k(v)^{-1}.
```

Then

```text
r_k(w)=r_k(u) r_k(s_k(v))^{-1}=v v^{-1}=1,
```

so `w in ker(r_k)`.  Since both factors lie in `R_{m,k+1}`, also

```text
w in R_{m,k+1}.
```

Finally, `w` cannot lie in `N_{X,k+1}`: otherwise

```text
u = w s_k(v)
```

would lie in `N_{X,k+1}`, contrary to the choice of `u`.  Thus `w` is the
desired one-new-strand Brunnian witness.  QED.

## Consequences

Let

```text
mu_X(k)=min { m : R_{m,k} <= N_{X,k} }.
```

If `mu_X(k)` diverges, choose `k_j` minimal such that

```text
mu_X(k_j)>j.
```

Then `S_j` works at arity `k_j-1` and fails at arity `k_j`.  By the theorem
there is a right-based word

```text
w_j in ker(r_{k_j-1})
```

with

```text
w_j=1 in D_{k_j}(S_j),
w_j!=1 in P_{k_j}(X).
```

The point-pushing braid

```text
beta_j=iota_{k_j+1}(w_j)
```

is a Brunnian normalized-law obstruction after right stabilization: deleting
the newly added far-left stationary strand kills it, it is invisible to
`S_j`, and it still moves `X`.

Thus a B route cannot rely on an arbitrary high-arity relation.  It must
produce unbounded one-new-strand Brunnian vertical witnesses.

The matching A-side target is the extension theorem:

```text
exists m=m(X) such that
R_{m,k+1} cap ker(r_k) <= N_{X,k+1}
for every k.
```

Then induction on `k` gives `R_{m,k} <= N_{X,k}` for all arities, and the
sharp rack `A_{S_m}` dominates `X`.

## Audit Hook

The helper

```text
point_pushing_brunnian_witness_certificate(...)
```

checks one right-based candidate word by:

1. converting it to the existing left-based point-pushing convention;
2. deleting the newly added far-left generator in right-based coordinates;
3. checking the paired vertical-kernel certificate against the derivative
   detector and the YBE action.

It is a finite certificate checker for candidate B-tail witnesses.  The
normalization theorem above is symbolic.
