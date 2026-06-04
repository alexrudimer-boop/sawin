# Finite transducer rackification certificate

This note records the restricted finite-state certificate that is strong
enough to prove rack domination when it exists.  It is a certificate theorem,
not a universal existence theorem.

## Setup

Let `(X,r_X)` be a finite bijective YBE solution, and let

```text
pi:X -> Z
```

be a finite YBE quotient already dominated by a finite rack `R_Z`.

A hidden-fibre transducer certificate over `Z` consists of:

- a finite rack `S`;
- a deterministic Mealy transducer `M=(Q,q0,delta,omega)` with

  ```text
  delta: Q x X -> Q,
  omega: Q x X -> S;
  ```

- optionally, a deterministic invariant transducer `N=(P,p0,Delta,nu)` with

  ```text
  Delta: P x X -> P,
  nu: P x X -> I
  ```

  for a finite invariant alphabet `I`;

- an all-length injectivity condition for the combined outputs.

The transducer outputs are read left-to-right.  For `x=(x_1,...,x_n)`,

```text
q_1=q0,
q_{i+1}=delta(q_i,x_i),
F_n(x)_i = omega(q_i,x_i).
```

The invariant output `N_n:X^n -> I^n` is defined similarly.

## Local equivariance

The rack transducer must satisfy a finite local condition.  For every
`q in Q` and `x,y in X`, write

```text
r_X(x,y)=(u,v).
```

Then require

```text
delta(delta(q,x),y) = delta(delta(q,u),v)
```

and

```text
R_S(omega(q,x), omega(delta(q,x),y))
  =
(omega(q,u), omega(delta(q,u),v)).
```

These two identities say exactly that

```text
F_n(rho^X_n(sigma_i) x) = rho^S_n(sigma_i) F_n(x)
```

for every `n`, every adjacent generator, and every tuple.  Since the generator
actions are bijective, equivariance for positive generators gives equivariance
for inverse generators.

The invariant transducer must satisfy the analogous finite identities

```text
Delta(Delta(p,x),y) = Delta(Delta(p,u),v)
```

and

```text
(nu(p,x), nu(Delta(p,x),y))
  =
(nu(p,u), nu(Delta(p,u),v)).
```

These say that `N_n` is braid-invariant.

## All-length injectivity

Define

```text
C_n:X^n -> Z^n x I^n x S^n
C_n(x) = (pi^n(x), N_n(x), F_n(x)).
```

The certificate needs `C_n` injective for every `n`.  This is finite
checkable by a pair automaton.

The pair automaton states are

```text
(Q x P) x (Q x P) x {0,1}.
```

The two `(Q x P)` factors track the transducer states for two simultaneous
input words.  The final bit records whether the two input words have already
differed.  The initial state is

```text
(q0,p0,q0,p0,0).
```

For each pair of letters `x,x' in X`, add an edge from
`(q,p,q',p',b)` only if the one-letter combined outputs agree:

```text
(pi(x), nu(p,x), omega(q,x))
  =
(pi(x'), nu(p',x'), omega(q',x')).
```

The next state is

```text
(
  delta(q,x), Delta(p,x),
  delta(q',x'), Delta(p',x'),
  b or [x != x']
).
```

Then `C_n` is injective for every `n` if and only if no state with final bit
`1` is reachable.  Thus all-length injectivity is a finite graph-reachability
test.

## Certificate theorem

Assume:

```text
R_Z dominates Z,
M satisfies local rack equivariance,
N is braid-invariant,
C_n is injective for every n.
```

Then the product rack

```text
R_Z x S
```

dominates `X`.

Proof.  Let `beta in B_n` act trivially on `(R_Z x S)^n`.  Then `beta` acts
trivially on `R_Z^n`, so domination of `Z` gives

```text
rho^Z_n(beta)=1.
```

Thus

```text
pi^n(rho^X_n(beta)x)=pi^n(x).
```

Rack-transducer equivariance gives

```text
F_n(rho^X_n(beta)x)
  =
rho^S_n(beta)F_n(x)
  =
F_n(x),
```

and invariant-transducer equivariance gives

```text
N_n(rho^X_n(beta)x)=N_n(x).
```

Therefore

```text
C_n(rho^X_n(beta)x)=C_n(x).
```

By injectivity, `rho^X_n(beta)x=x` for every `x in X^n`.  Hence

```text
ker(B_n -> Sym((R_Z x S)^n)) <= ker(B_n -> Sym(X^n))
```

for every `n`.

## Fixed-candidate obstruction automaton

The certificate theorem is different from testing an arbitrary proposed rack
detector.  If `T_n` is any finite marked braid factor for `X` in degree `n`
and `theta^T_n` is its braid action, define

```text
G_n(X,T) =
< (rho^X_n(sigma_i), theta^T_n(sigma_i)) : 1 <= i < n >
<= Sym(X^n) x Sym(T_n).
```

Equivalently, close the finite automaton whose states are pairs
`(g_X,g_T)`, whose start state is `(1,1)`, and whose transitions multiply by
the positive and negative standard braid generators in both coordinates.
Accepting states are those with

```text
g_T = 1 and g_X != 1.
```

For a fixed degree `n`, the accepting set is nonempty exactly when there is a
braid `beta in B_n` that is invisible to the proposed detector but still moves
`X^n`.

Thus, for a fixed finite rack `Y`,

```text
Y dominates X
```

is equivalent to emptiness of this automaton for every `n`.  Each fixed `n`
check is finite; the hard part is still the unbounded arity quantifier.  A
Sawin-negative sequence is the diagonal version: enumerate finite racks
`Y_1,Y_2,...`, set `P_m=Y_1 x ... x Y_m`, and find

```text
beta_m in ker rho^{P_m}_{n_m}
```

with `rho^X_{n_m}(beta_m) != 1` and `n_m -> infinity`.

## Status

This criterion captures the size-four Type A affine cyclic-rack model: the
invariant transducer outputs the parity coordinates, and the rack transducer
outputs the fibre coordinates carrying the two-element cyclic rack action.
The executable checker in `src/ybe_domination/transducer_certificate.py`,
backed by `tests/test_transducer_certificate.py`, verifies this finite
certificate directly.  In the causal Mealy convention used there, the Type A
rack transducer stores whether the first coordinate has already been read and
then carries the offset in the recurrence `H_{j+1}=H_j+p_{j+1}+1`.

The checker also captures any future finite-state hidden-fibre gauge of the
same kind: it audits the quotient equation, local rack-equivariance,
local invariance, and the pair-automaton injectivity condition.

The exact all-detector tower behind this fixed-candidate check is isolated in
`proofs/rack_residual_obstruction_tower.md`.  In that language, a transducer
certificate proves vanishing of the rack-residual tower for one finite
detector.  The missing completeness theorem would show that every vanishing
relative tower is witnessed by some finite Mealy/invariant certificate.

However, the criterion is not a proof of Sawin by itself.  The remaining
universal statement would be:

```text
Every actual finite YBE solution has such a finite transducer certificate
after the known quotient, involutive, left-nondegenerate, and flip-union
branches are removed.
```

No proof of that universal existence theorem is currently available in the
ledger.  Failure of one proposed finite transducer class is only a gap.
Failure for all finite rack detectors is the normalized-law negative branch.
