# Fixed Q3 Affine Rack Obstruction

Date: 2026-06-04

This note records a guardrail from the Pro affine discussion: fixed-`Q_3`
bounded deletion is false even in a tiny affine rack.  This does not refute
Sawin, because the example is itself a rack and is therefore dominated by
itself.  It only rules out the over-strong endpoint

```text
a_X(2)=2  =>  exists h such that E^{(3)}_{X,h,n}=1 for all n.
```

The true endpoint must use the actual cutoff `a_X(h)+1`, not the first
nontrivial cutoff `a_X(2)+1`.

## Example

Let

```text
X = F_5
```

with Alexander rack operation

```text
x ▷ y = -x + 2y.
```

The associated braided-set map is

```text
R(x,y) = (x ▷ y, x) = (-x+2y, x).
```

Equivalently, in the affine-linear form over `F_5`,

```text
M = [ 4 2 ]
    [ 1 0 ],
t = 0.
```

The two-strand crossing has order `4`, so the cheap two-strand cutoff is

```text
a_X(2)=2.
```

Thus the first serious bounded-deletion detector is `Q_3`.

## Exact Arity-Three Obstruction

The repository helper reports:

```text
bounded_deletion_support_q3_compressed_audit(X,h=2,n=3)

joint image size = 3456,
E^{(3)}_{X,2,3} has size 2,
obstruction nontrivial = True.
```

One witness word found by the helper is

```text
(1,1,1,1,1,1,2,1,1,-2,1,1,1,1,1,1,2,-1,-1,-2).
```

It moves

```text
(0,0,1) -> (4,4,3)
```

while it is invisible to the compressed `Q_3` detector and has trivial
two-strand `X` deletion shadows.

This exact finite computation is now locked by the regression

```text
test_fixed_q3_affine_rack_has_brunnian_obstruction_at_arity_three.
```

## Recursive Family Guardrail

The Pro response also gives a Brunnian recursive family.  Let `A_ij` be the
standard pure braid generator and set

```text
beta_3 = [A_12,A_23] [A_12,A_13] [A_23,A_13]^{-1},
beta_{N+1} = [beta_N, A_{N,N+1}].
```

The proof sketch is:

1. `beta_3` has trivial pair deletions and lies in `D_3(3)`.
2. If `beta_N` is Brunnian, then `[beta_N,A_{N,N+1}]` is Brunnian.
3. If `beta_N in D_3(N)`, then `beta_{N+1} in D_3(N+1)` because the pairwise
   linking vector is killed by commutators and the dihedral `F_3` matrix of
   `beta_N` is already identity.
4. In the `F_5` Alexander rack representation, the resulting matrices are
   nonidentity for all `N`; the displayed Pro recurrence is
   `B_{N+4}=I_4 direct-sum B_N`.

Locally, direct finite-rack action checks verify `beta_N in D_3(N)` and
`rho^X_N(beta_N) != 1` for `3 <= N <= 6`.

Again, this is a fixed-`Q_3` guardrail, not a Sawin-negative construction:
larger rack detectors may and do kill these effects, since `X` itself is a
finite rack.
