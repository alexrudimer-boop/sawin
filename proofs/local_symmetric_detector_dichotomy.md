# Local symmetric detector dichotomy

Date: 2026-05-30

This note packages the current A/B fork into one local statement using only
symmetric group detectors.

It does not prove the Master Local-Minimal Residual Theorem.  It shows that,
for a fixed local-minimal interval, the only remaining alternatives are:

```text
some fixed S_m detects the residual action for all braid indices;
or for every j there is a residual mover invisible to S_j.
```

## Setup

Fix a local-minimal interval

```text
pi:X -> Z
```

with `Z` dominated by a finite rack `Q`, and put

```text
N_n = ker rho_{Q,n}.
```

For a finite group `G`, write

```text
K_G(n) = { beta : Lambda_{G,n}(beta)=Lambda_{G,n}(1) }.
```

The symmetric reduction shows that any finite group detector can be replaced
by a symmetric detector, while the symmetric tower monotonicity gives

```text
K_{S_M}(n) subset K_{S_m}(n)       for M >= m.
```

## The dichotomy

For the fixed interval `pi` and quotient detector `Q`, exactly one of the
following holds.

1. There is an integer `m=m(pi,Q)` such that for all `n`,

   ```text
   beta in N_n cap K_{S_m}(n) => Delta_n(beta)=1.
   ```

2. For every `j>=1`, there exist `n_j` and

   ```text
   alpha_j in N_{n_j} cap K_{S_j}(n_j)
   ```

   such that

   ```text
   Delta_{n_j}(alpha_j) != 1.
   ```

Proof.  If (1) fails, then no `S_j` is a fixed detector.  Hence for each `j`
there is a braid `alpha_j` in some degree `n_j` lying in
`N_{n_j} cap K_{S_j}(n_j)` with nontrivial residual action.  This is exactly
(2).

Conversely, if (2) holds, then no `S_m` can be a fixed detector, because the
row with `j=m` is a witness against it.  Thus (1) and (2) are mutually
exclusive and exhaustive.  QED.

## From (1) to the positive local rack

If (1) holds, then the sharp obstruction theorem gives the local rack detector

```text
Q x A_{S_m}.
```

Indeed, `ker rho_{A_{S_m},n}=K_{S_m}(n)`, and therefore

```text
ker rho_{Q x A_{S_m},n}
  = N_n cap K_{S_m}(n)
  subset ker residual action.
```

So the interval is dominated by a finite rack independent of `n`.

## From (2) to the normalized-law B route

Assume (2).  Right-stabilize `alpha_j` by adding `j` unused strands:

```text
q_j = n_j+j,
beta_j = iota_j(alpha_j).
```

Then `q_j -> infinity`, `beta_j in N_{q_j}`, and the moved residual tuple
remains moved after extending it by fixed fibre entries.  Also
`beta_j in K_{S_j}(q_j)`.

For each fixed finite group `G`, let `g=|G|`.  For all `j>=g`,

```text
K_{S_j}(q_j) subset K_{S_g}(q_j) subset K_G(q_j).
```

The first containment is symmetric tower monotonicity, and the second is the
left-regular embedding reduction.  Hence `beta_j` is eventually invisible to
every finite group while still moving the residual action.  This is the local
normalized-law obstruction required by the global-local fork.

## Executable finite-prefix audit

The helper

```text
local_symmetric_tower_prefix_sequence_audit(...)
```

checks a supplied finite prefix of case (2).  It verifies:

1. the degrees are the initial segment `1,...,k`;
2. each row uses a single symmetric group of the expected order `j!`;
3. each row was right-stabilized by exactly `j` strands;
4. each row passes the local symmetric normalized-law prefix audit.

It is deliberately only a finite-prefix checker.  A final B proof still needs a
symbolic construction for every `j`.
