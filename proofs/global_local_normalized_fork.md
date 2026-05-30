# Global-local normalized fork

Date: 2026-05-30

This note removes the remaining global ambiguity from the Sawin problem.  It
does not prove the Master Local-Minimal Residual Theorem.  It proves that the
global theorem is equivalent to that local theorem, and that failure at one
local-minimal interval automatically has the normalized-law form required for
outcome B.

Thus there is no third global obstruction:

```text
prove the fixed finite detector theorem for every local-minimal interval,
or construct one local normalized-law obstruction.
```

## Setup

Let `X` be a finite bijective set-theoretic Yang-Baxter solution and let

```text
Delta_X = kappa_0 < kappa_1 < ... < kappa_m = Nabla_X
```

be a maximal congruence chain.  Put

```text
X_i = X/kappa_i,
pi_i : X_i -> X_{i+1}.
```

For an interval `pi:X->Z`, with `Z` dominated by a finite rack `Q`, set

```text
N_n = ker rho_{Q,n}.
```

For `z in Z^n`, write

```text
X_z = product_i pi^{-1}(z_i)
```

and let

```text
delta_{n,z}:N_n -> Sym(X_z)
```

be the residual action.  Let `Delta_n(beta)` denote the tuple of all residual
actions over the fixed base tuples.

The local detector theorem for `pi` says that there is a finite group
`G(pi,Q)`, depending only on the interval and `Q`, such that for all `n`:

```text
beta in N_n,
Lambda_{G(pi,Q),n}(beta)=Lambda_{G(pi,Q),n}(1)
    => Delta_n(beta)=1.
```

## Lemma 1: chain intervals are local-minimal

Each `pi_i:X_i->X_{i+1}` in a maximal congruence chain is local-minimal.

Proof.  A local admissible congruence family on the fibres of `pi_i` is the
same thing as an intermediate congruence between `kappa_i` and `kappa_{i+1}`:
the family is admissible exactly when the local crossing maps

```text
T_{a,b}: A_a x A_b -> A_{a.b} x A_{a*b}
```

carry equivalence classes to equivalence classes on the target fibres.  That is
precisely the congruence condition for the quotient crossing table.

Maximality leaves no strict intermediate congruence.  Hence every admissible
family is all equality or all universal.  In particular, a semisplit family
would be an intermediate congruence unless it collapsed to one of these two
extremes.  So semisplit leaks are absent in each chain interval.  QED.

## Lemma 2: a local detector dominates the interval

Suppose `Z` is dominated by a finite rack `Q` and `pi:X->Z` has a finite local
detector group `G=G(pi,Q)`.  Let

```text
A_G = T_2 x (G x G)
```

be the sharp Artin-longitude detector rack.  The sharp obstruction theorem gives

```text
ker rho_{A_G,n}
  = { beta : Lambda_{G,n}(beta)=Lambda_{G,n}(1) }.
```

Set

```text
Q' = Q x A_G.
```

Then

```text
ker rho_{Q',n}
  = ker rho_{Q,n} cap ker rho_{A_G,n}.
```

If `beta` lies in this kernel, then it fixes the quotient base through `Q`, has
identity finite-`G` longitude data, and therefore has trivial residual action by
the local detector implication.  Thus it fixes every fibre over every base
tuple, so

```text
ker rho_{Q',n} subset ker rho_{X,n}
```

for every `n`.  The rack `Q'` is finite and independent of `n`.  QED.

## Lemma 3: local detectors along a chain imply global domination

Start at the terminal one-point quotient `X_m`, dominated by the one-point rack
`Q_m`.

Assume by downward induction that `Q_{i+1}` dominates `X_{i+1}`.  Apply the
local detector theorem to

```text
pi_i:X_i -> X_{i+1}
```

with quotient detector `Q_{i+1}`.  Let the resulting finite group be `G_i`.
Lemma 2 shows that

```text
Q_i = Q_{i+1} x A_{G_i}
```

dominates `X_i`.  Since the chain is finite and each `G_i` is fixed at the
interval level, the final rack

```text
Q_0 = Q_m x A_{G_{m-1}} x ... x A_{G_0}
```

is a single finite rack independent of braid index.  It dominates
`X_0=X`.  QED.

## Lemma 4: failure of a local detector diagonalizes

Fix a local-minimal interval `pi:X->Z` with `Z` dominated by `Q`.  Suppose no
finite group `G` satisfies the local detector implication.  Enumerate the
finite groups up to isomorphism:

```text
H_1,H_2,H_3,...
```

and put

```text
P_j = H_1 x ... x H_j.
```

Since `P_j` is not a valid detector, there exist `n_j` and
`alpha_j in N_{n_j}` such that

```text
Lambda_{P_j,n_j}(alpha_j)=Lambda_{P_j,n_j}(1),
Delta_{n_j}(alpha_j) != 1.
```

Choose a moved residual tuple over some base tuple.  Stabilize on the right by
adding `j` unused strands:

```text
q_j = n_j+j,
beta_j = iota_j(alpha_j) in B_{q_j}.
```

The stabilized braid remains in `N_{q_j}` because it acts as `alpha_j` on the
old quotient coordinates and trivially on the new ones.  The moved residual
tuple remains moved after extending it by any fixed fibre element on the new
strands.  Also `q_j -> infinity`.

For each fixed finite group `H_r`, whenever `j>=r`, projection
`P_j -> H_r` sends identity `P_j` longitude data to identity `H_r` longitude
data.  Right stabilization preserves the old Artin longitude data and gives
trivial longitudes on the added strands.  Hence

```text
Lambda_{H_r,q_j}(beta_j)=Lambda_{H_r,q_j}(1)
```

eventually.  Thus local detector failure yields a local normalized-law residual
obstruction sequence.  QED.

## Lemma 5: a local obstruction defeats every finite rack

Let `pi:X->Z` have a local normalized-law residual obstruction sequence
`beta_j in B_{q_j}`.  Then the finite solution `X` is not dominated by any
finite rack.

Indeed, let `Y` be any finite rack and let `Inn(Y)` be its finite inner group.
The standard rack longitude formula expresses the braid action on `Y^n` by
recursive Artin longitudes evaluated in `Inn(Y)`.  Since the obstruction
sequence is eventually invisible to every finite group, it is eventually
invisible to `Inn(Y)`.  Therefore `beta_j` eventually lies in
`ker rho_{Y,q_j}`.

But the same `beta_j` moves a residual tuple in `X`, so it acts nontrivially on
`X^{q_j}`.  Therefore

```text
ker rho_{Y,q_j} not subset ker rho_{X,q_j}
```

for all sufficiently large `j`.  Since `Y` was arbitrary, no finite rack
dominates `X`.  QED.

If the interval arose as a quotient interval of a larger solution, this is
already enough for outcome B because the total object `X` of the interval is
itself a finite bijective YBE solution.  Also, any finite rack dominating the
larger solution would dominate each quotient, so non-domination of the quotient
would contradict domination of the larger solution.

## The global-local fork

For a finite solution `X`, the following alternatives are exhaustive.

1. Every local-minimal interval in a maximal congruence chain has a finite
   detector group for every already rack-dominated quotient detector.  Then
   Lemma 3 gives a finite rack dominating `X`.
2. Some local-minimal interval lacks such a detector.  Then Lemma 4 gives a
   local normalized-law obstruction sequence, and Lemma 5 gives a finite YBE
   counterexample not dominated by any finite rack.

So the global Sawin problem is equivalent to the Master Local-Minimal Detector
Theorem:

```text
For every finite local-minimal interval pi:X->Z and every finite rack Q
dominating Z, there is a finite group G(pi,Q), independent of n, such that

beta in ker rho_{Q,n},
Lambda_{G(pi,Q),n}(beta)=Lambda_{G(pi,Q),n}(1)
    => Delta_n(beta)=1

for all n.
```

The current repository gap is exactly this theorem in the remaining
`bi_free_universal_corridor_bottleneck` branch.  A positive proof must give the
fixed interval-level detector group and all endpoint-longitude witnesses
uniformly in `n`.  A negative proof must supply one explicit local interval and
the normalized-law sequence produced abstractly above, with moved residual
tuples.

## Certificate helper

The executable helper

```text
local_normalized_law_prefix_witness_audit(...)
```

checks one supplied local product-prefix record:

1. membership in the quotient/base kernel before and after right stabilization;
2. identity longitude signature in the finite product group `P_j`;
3. identity signatures after projection to the listed factors;
4. preservation of the Artin data under stabilization;
5. survival of a moved residual tuple after stabilization.

The property

```text
proves_one_local_prefix_normalized_law_witness
```

means that one row has the exact shape required by Lemma 4.  A final B proof
must still construct such rows for every product prefix `P_j`.
