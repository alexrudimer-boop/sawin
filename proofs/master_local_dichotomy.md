# Master Local Dichotomy

This note records the exact A/B fork left by the congruence-chain reduction.
It is not a proof of the Master Local-Minimal Residual Theorem; it states why
that theorem is the whole remaining positive burden, and why failure of one
fixed local interval supplies the normalized obstruction required for outcome
B.

## A-Side

Let `X` be a finite bijective YBE solution and choose a saturated congruence
chain

```text
Delta_X = kappa_0 < kappa_1 < ... < kappa_m = Nabla_X.
```

For the interval

```text
X/kappa_i -> X/kappa_{i+1},
```

write its local table as `pi_i : E_i -> Z_i`.  Suppose the master local
theorem is known for every interval in the chain:

```text
there is a finite group G_i = G(pi_i,Q_{i+1})
such that
Lambda_{G_i,n}(beta)=Lambda_{G_i,n}(1)
    => Delta_i,n(beta)=1
for all n and all beta in ker rho_{Q_{i+1},n}.
```

Start with the one-point quotient rack `Q_m`.  Recursively set

```text
Q_i = Q_{i+1} x A_{G_i},
```

where `A_G=T_2 x (G x G)` is the sharp Artin-longitude detector rack.  The
sharp obstruction theorem gives

```text
ker rho_{Q_i,n} <= ker rho_{X/kappa_i,n}
```

for every `n`.  At `i=0`, `X/kappa_0 = X`, so `Q_0` is a finite rack
dominating `X` for all braid indices.

Every group and rack in this recursion is finite, and the chain length is
finite.  The only non-formal input is the local theorem for each
local-minimal interval, with `G_i` independent of `n`.

## B-Side

Conversely, suppose an explicit local-minimal interval

```text
pi:E -> Z
```

over a quotient dominated by a finite rack `Q` has no finite group satisfying
the sharp kernel implication.  The diagonal normalized obstruction lemma
applies to this fixed quotient/residual problem.  It gives braid indices
`q_j -> infinity` and braids `beta_j in ker rho_{Q,q_j}` such that for every
finite group `G`,

```text
Lambda_{G,q_j}(beta_j)=Lambda_{G,q_j}(1)
```

eventually, but

```text
Delta_{q_j}(beta_j) != 1.
```

Choose a base tuple `z_j` and a fibre tuple `x_j in E_{z_j}` moved by this
residual action.  Viewing `E` as the finite YBE solution attached to the
local table, the same braid moves the total tuple corresponding to
`(z_j,x_j)`.

Now let `Y` be any finite rack.  Its inner group `Inn(Y)` is finite, and the
finite-rack longitude quotient says

```text
Lambda_{Inn(Y),q_j}(beta_j)=Lambda_{Inn(Y),q_j}(1)
    => rho_{Y,q_j}(beta_j)=1.
```

The diagonal sequence is eventually invisible to `Inn(Y)`, so every finite
rack eventually kills `beta_j`, while `E` does not.  Thus the finite solution
`E` is not dominated by any finite rack.

Therefore an explicit local interval with no finite detector group is enough
for outcome B, provided its YBE table, local-minimality, and no-finite-group
failure are proved symbolically.

## Consequence

The global problem has been reduced to this dichotomy:

- prove the Master Local-Minimal Residual Theorem for every finite
  local-minimal interval; or
- exhibit one explicit finite local-minimal interval whose residual action
  defeats every finite detector group, then apply the diagonal construction
  above.

Finite searches in the archive can only suggest which side to pursue.  They
cannot prove either side unless upgraded to the all-`n` local detector theorem
or to the all-finite-group normalized obstruction.
