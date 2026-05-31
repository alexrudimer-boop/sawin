# Triangular K-left recovery routing

Date: 2026-05-31

This note follows `proofs/triangular_k_left_kernel_closure.md` and
`proofs/triangular_k_left_structural_independence.md`.  It does not prove
`[Resolution: A]` or construct `[Resolution: B]`.  It routes one more K-left
kernel subcase to the fixed triangular recovery observer.

## Constant-map kernels are recovery labels

Let

```text
T_{a,b}(x,y) = (alpha(x), beta_x(y))
```

be a bijective left triangular row.  If

```text
alpha(x0)=alpha(x1)=u,   x0 != x1,
```

then the bundle-partition theorem says that the two image blocks

```text
beta_x0(A_b),   beta_x1(A_b)
```

are disjoint blocks in the target slice `{u} x A_d`.

The triangular recovery inverse

```text
T_{a,b}^{-1}(u,v) = (r_u(v), s_{u,v})
```

therefore recovers which member of the constant-map fibre carried the input:

```text
v in beta_x0(A_b)  =>  r_u(v)=x0,
v in beta_x1(A_b)  =>  r_u(v)=x1.
```

Thus a constant-map kernel edge is not an independent K-left motion.  It is a
block-label recovery motion in the fixed triangular recovery unit observer.

The side-dual right triangular case is identical with the recovered right
input in place of the recovered left input.

## Executable object

The helper

```text
triangular_constant_kernel_recovery_route_audit(I)
```

filters the kernel-closure ledger to `constant_map_kernel` rows and checks
that each collapsed pair is separated by the triangular recovery table.  It
records:

```text
triangular_constant_kernel_recovery_route_rows
triangular_constant_kernel_unrouted_universal_rows
```

inside the post-linear finite-system payload.

For a routed row, the audit stores the concrete output pairs witnessing each
recovered input.  In the left triangular case these are output pairs
`(u,v)` whose recovery table has `recovered_left_input=x`; in the right
triangular case they are output pairs with `recovered_right_input=y`.

## Consequence for K-left

[Proved relative to triangular recovery verification] If a K-left
constant-map kernel edge has universal generated closure and the triangular
recovery table is bijective, then the edge routes to System U rather than
remaining a separate System K branch.

Proof.  Universal generated closure says the edge is a live local-minimal
seed rather than a proper quotient edge.  The recovery table separates the two
collapsed constant-map inputs by finite output pairs.  The recovery-row
extension is one of the generators of `U_tri`.  Hence the remaining question
is exactly whether the resulting triangular recovery endpoint word lies in
`V_beta(U_tri)`, which is System U.  QED.

The K-left constant-map-kernel residue is therefore not:

```text
construct a new finite detector for constant-map fibres.
```

It is:

```text
prove the corresponding triangular recovery endpoint is in V_beta(U_tri),
or upgrade an unrouted U_tri endpoint miss to a normalized-law sequence.
```

## Remaining K-left work

This routing does not close the no-triangular-row case and does not prove the
all-`n` System U endpoint theorem.  It only prevents constant-map kernel
edges from being counted as an independent nonlinear obstruction once
triangular recovery has been verified.
