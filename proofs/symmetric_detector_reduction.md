# Symmetric detector reduction

Date: 2026-05-30

This note simplifies both sides of the final A/B fork.  Arbitrary finite group
detectors can be replaced by symmetric group detectors.  Consequently, a
negative normalized-law construction only has to diagonalize against the
sequence of finite symmetric groups.

The statement is symbolic and all-`n`; it is not finite-search evidence.

## Lemma 1: finite detectors may be taken symmetric

Let `G` be a finite group of order `m`.  Embed `G` into `S_m` by the left
regular representation

```text
g |-> (h |-> gh).
```

For every braid index `n`,

```text
K_{S_m}(n) subset K_G(n),
```

where

```text
K_H(n) = { beta : Lambda_{H,n}(beta)=Lambda_{H,n}(1) }.
```

Proof.  If `beta in K_{S_m}(n)`, then the Artin strand permutation is trivial
and every recursive longitude evaluates to the identity under every assignment
`F_n -> S_m`.  Any assignment `phi:F_n->G` followed by the regular embedding is
an assignment into `S_m`.  Hence the embedded values of all
`phi(L_i(beta))` are identity permutations.  The regular representation is
injective, so `phi(L_i(beta))=1` in `G` for every `phi` and every `i`.
Therefore `beta in K_G(n)`.  QED.

If a finite group `G` detects a local interval, then `S_|G|` also detects it:

```text
K_{S_|G|}(n) subset K_G(n) subset ker residual action.
```

Thus the Master Local-Minimal Detector Theorem can equivalently ask for a
number `m=m(pi,Q)` such that `S_m` is a valid fixed detector group.

## Lemma 2: normalized-law B may diagonalize over symmetric groups only

Suppose a local interval has no finite detector group.  Then no symmetric group
`S_j` is a detector.  For each `j`, choose

```text
alpha_j in N_{n_j} cap K_{S_j}(n_j)
```

with

```text
Delta_{n_j}(alpha_j) != 1.
```

Right-stabilize by adding `j` unused strands, obtaining

```text
beta_j in B_{q_j},       q_j=n_j+j.
```

Then `beta_j` is eventually invisible to every finite group.  Indeed, let `H`
be any finite group and let `h=|H|`.  By Lemma 1,

```text
K_{S_h}(n) subset K_H(n).
```

For `j>=h`, embed `S_h` into `S_j` by fixing the remaining `j-h` points.  The
same assignment-restriction argument gives

```text
K_{S_j}(n) subset K_{S_h}(n).
```

Therefore, for all `j>=h`,

```text
beta_j in K_{S_j}(q_j) subset K_{S_h}(q_j) subset K_H(q_j).
```

So the sequence is invisible eventually to `H`.  Since `H` was arbitrary, it is
a normalized-law obstruction sequence once the residual tuple movement is
included.

## Consequences

Positive route.  It is enough to construct one integer `m(pi,Q)` for each
local-minimal interval such that

```text
beta in ker rho_{Q,n},
Lambda_{S_m,n}(beta)=Lambda_{S_m,n}(1)
    => Delta_n(beta)=1
```

for all `n`.

Negative route.  It is enough to construct an explicit local interval and
braids `alpha_j` that are invisible to `S_j`, rather than invisible to an
arbitrary product of finite groups.  Right stabilization then supplies
`q_j->infinity`, and Lemma 2 promotes invisibility from symmetric groups to all
finite groups.

This is compatible with the product-prefix certificate format:

```text
P_j = G_1 x ... x G_j
```

may be replaced by a single symmetric detector `S_j` after re-indexing by group
order.  The symmetric formulation is usually easier to state; the product
formulation remains useful when a proposed construction naturally lists finite
groups in another order.

## Executable audit

The helper

```text
symmetric_detector_reduction_audit(G,n,beta,degree=m)
```

uses the left regular embedding `G -> S_m` and records the implication

```text
Lambda_{S_m,n}(beta)=Lambda_{S_m,n}(1)
    => Lambda_{G,n}(beta)=Lambda_{G,n}(1).
```

The helper is a convention/audit check, not a proof that a given interval is
detected.
