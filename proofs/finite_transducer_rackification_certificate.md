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

The later same-chat Pro refinement identifies this note as the precise finite
certificate theorem rather than as a broad theorem.  A proposed sequential
rack gauge certificate consists of finite data

```text
(Z,R_Z,S,Q,P,delta,omega,Delta,nu)
```

where `Z` is an optional known quotient dominated by `R_Z`, `S` is the rack
readout, `Q` is the causal Mealy state set for the rack readout, and `P` is an
optional invariant observer.  For fixed size bounds on these data, certificate
existence is a finite constraint-satisfaction problem plus the finite
pair-automaton reachability test above.  Thus fixed-candidate and
fixed-bound searches are terminating.

The next same-chat Pro refinement gives an equivalent canonical algebraic
form of the same certificate.  Let

```text
M_X = < X | xy=uv whenever r_X(x,y)=(u,v) >
```

be the structure monoid.  A sequential rack certificate is equivalent to
finite data

```text
Q, H, F, h_{q,x} in H, f_{q,x} in F,
```

where `Q` is a finite right `M_X`-set with base state `q0`, `H` is a finite
group acting on the finite set `F`, and the assignments are defined for
reachable `q in Q` and `x in X`.  For every reachable `q` and
`r_X(x,y)=(u,v)`, the finite equations are:

```text
qxy = quv,                                      (Q)
h_{q,u} = h_{q,x} h_{qx,y} h_{q,x}^{-1},       (H1)
h_{qu,v} = h_{q,x},                            (H2)
f_{q,u} = h_{q,x} . f_{qx,y},                  (F1)
f_{qu,v} = f_{q,x}.                            (F2)
```

The all-length reconstruction map is

```text
C_n(x_1,...,x_n)
  =
((h_{q_{i-1},x_i}, f_{q_{i-1},x_i}))_{i=1}^n,
q_i = q0 x_1 ... x_i,
```

possibly with the known quotient and invariant observer coordinates appended.
The certificate condition is that `C_n` is injective for every `n`, again
checked by the finite pair automaton.

Given such canonical data, form the finite rack

```text
Y = H x F,
(alpha,z)*(beta,w) = (alpha beta alpha^{-1}, alpha.w).
```

The left translations satisfy the rack identity because

```text
L_(alpha,z) L_(beta,w)
  =
L_((alpha,z)*(beta,w)) L_(alpha,z).
```

Equations `(H1),(F1),(H2),(F2)` say exactly that a local YBE crossing in `X`
is sent by `C_n` to the rack crossing in `Y`.  Hence `C_n` is
`B_n`-equivariant, and all-length injectivity gives domination by `Y`.

Conversely, any sequential certificate with finite rack `S` has this
canonical form by embedding

```text
S -> Inn(S) x S,        s |-> (L_s,s),
```

using `H=Inn(S)`, `F=S`, `h_{q,x}=L_{omega(q,x)}`, and
`f_{q,x}=omega(q,x)`.  The rack identity gives

```text
L_{s*t}=L_s L_t L_s^{-1},
```

which is exactly `(H1),(H2)`, while the second coordinate gives
`(F1),(F2)`.  Therefore:

```text
rack-active part of a finite sequential rack certificate
  <=> finite canonical quotient data (Q,H,F,h,f).
```

There is an important degenerate caveat.  If all-length injectivity is
required from the rack-active `Q,H,F` outputs alone, then such a rack-only
canonical certificate forces left-nondegeneracy.  Indeed, suppose
`lambda_x(y_1)=lambda_x(y_2)=u` with `y_1 != y_2`, and write the canonical
output as `O(q,x)`.  For `r(x,y_i)=(u,v_i)`, local equivariance gives

```text
O(q,u)=O(q,x)*O(qx,y_i),        i=1,2.
```

Since rack left translations are bijective,

```text
O(qx,y_1)=O(qx,y_2).
```

Thus `(x,y_1)` and `(x,y_2)` have the same rack-active canonical output,
contradicting all-length injectivity.  Therefore genuinely degenerate rows
need the observer-augmented form: some finite information may be
braid-invariant by position rather than rack-active.

The current sharp positive sublemma is consequently observer-augmented:
prove that every remaining finite bijective YBE solution admits finite
canonical quotient data together with finite invariant observer data, or find
one explicit table failing all finite rack detectors.

The canonical form is now executable.  The helper

```text
canonical_quotient_audit(solution,data,invariant_transducer=None)
```

checks optional quotient equivariance, the finite group action, the equations
`(Q),(H1),(H2),(F1),(F2)`, optional invariant observer equations, and
all-length pair-automaton injectivity.  Thus the executable certificate now
keeps three channels separate: quotient data, rack-active canonical data, and
position-invariant observer data.  The helper

```text
canonical_quotient_product_rack(data)
```

constructs the rack `H x F`.  The regression
`tests/test_transducer_certificate.py::test_affine_f2_hidden_cyclic_gauge_has_canonical_certificate`
checks the affine `F_2^3` row using

```text
Q=Z/2, H=C2, F=F_2^2, h_{q,x}=1, f_{q,(a,z)}=J^q z + q c,
```

with the inert `a` coordinate supplied by the invariant observer.
The companion regression
`test_affine_f2_canonical_certificate_needs_invariant_output` records the
two-letter collision proving that this row has no rack-only `Q,H,F` injective
certificate.

The affine `F_2^3` pressure row from
`proofs/affine_f2_hidden_cyclic_gauge.md` is now also a regression for this
certificate format.  For

```text
X = F_2 x F_2^2,
R((a,z),(b,w)) = ((a,Jw),(b,Jz+c)),
J(z1,z2)=(z2,z1), c=(1,1),
```

take the two-state transducer `Q=Z/2`,

```text
delta(q,(a,z)) = q+1,
omega(q,(a,z)) = J^q z + q c,
```

take the constant-action rack on `F_2^2`,

```text
s*t = t+c,
```

and take the invariant observer `nu(a,z)=a`.  The combined output

```text
(a_i,z_i)_i |-> ((a_i)_i,(J^i z_i + (i mod 2)c)_i)
```

is injective in every arity, and the local equations hold.  The regression
`tests/test_transducer_certificate.py::test_affine_f2_hidden_cyclic_gauge_has_sequential_certificate`
checks this finite certificate directly.  This is the clean executable
replacement for trying to force a non-surjective local YBE row into a
single-strand bisectional fibre model.

## Recursive active-factor certificate

The latest same-chat Pro refinement identifies the next finite information
type beyond a rack-active channel and a position-invariant observer.  Let `T`
be a finite YBE solution that is already known to be dominated by a finite
rack `R_T`.  A recursive active-factor certificate consists of a finite
Mealy transducer

```text
delta: Q x X -> Q,
omega: Q x X -> T,
```

together with optional quotient and invariant-observer channels as above.
For every reachable `q` and every `r_X(x,y)=(u,v)`, the active-factor channel
must satisfy

```text
delta(delta(q,x),y) = delta(delta(q,u),v)
```

and

```text
r_T(omega(q,x), omega(delta(q,x),y))
  =
(omega(q,u), omega(delta(q,u),v)).
```

Thus the sequential map `F_n:X^n -> T^n` is `B_n`-equivariant.  If the
combined output

```text
(pi^n, N_n, F_n):X^n -> Z^n x I^n x T^n
```

is injective in every arity, then the product of the known rack detector for
`Z` and the known rack detector for `T` dominates `X`.  The proof is exactly
the equivariant reconstruction argument: a braid invisible to both detector
racks fixes all visible coordinates, and injectivity forces it to fix the
original `X^n` tuple.

This strictly generalizes the earlier certificate classes:

```text
invariant observer      = active factor with trivial braid action,
rack-active output      = active factor T is a rack,
quotient/color detector = active factor T is a smaller dominated solution.
```

For fixed finite `Q`, `T`, and optional observer data, the check is still
finite: local two-letter equations plus the same pair-automaton all-length
injectivity test.  The executable helper

```text
active_factor_certificate_audit(...)
```

now implements this generalized fixed-candidate check.  The affine
`F_2^3` hidden cyclic row is also tested through this active-factor interface,
with `T` equal to the constant-action cyclic rack on the hidden `F_2^2`
coordinate.

This refinement also explains why a Myhill-Nerode finite prefix congruence is
not by itself decisive.  A finite prefix quotient `Q` only gives the monoid
relation `qxy=quv`.  One must still solve the nonabelian crossed-cocycle
realization problem, for example the finite equations

```text
h_{q,u}=h_{q,x}h_{qx,y}h_{q,x}^{-1},
h_{qu,v}=h_{q,x},
f_{q,u}=h_{q,x}.f_{qx,y},
f_{qu,v}=f_{q,x},
```

or, more generally, the finite active-factor equation with target `T`, and
then prove all-length injectivity.  Failure of this restricted certificate
class is therefore not yet a Sawin-negative theorem; the genuine negative
branch remains the cofinal rack-prefix obstruction below.

The exact all-detector tower behind this fixed-candidate check is isolated in
`proofs/rack_residual_obstruction_tower.md`.  In that language, a transducer
certificate proves vanishing of the rack-residual tower for one finite
detector.  The missing completeness theorem would show that every vanishing
relative tower is witnessed by some finite Mealy/invariant certificate.

However, the criterion is not a proof of Sawin by itself.  The remaining
universal statement would be:

```text
Recursive active-factor observability lemma.

Every actual finite YBE solution has a finite sequential output into already
rack-dominated active factors, with enough quotient and invariant observer
coordinates to reconstruct `X^n` in every arity, after the known quotient,
involutive, left-nondegenerate, flip-union, and small kernel-equivalence
branches are removed.
```

No proof of that universal existence theorem is currently available in the
ledger.  The observer-augmented canonical `Q,H,F` certificate is the special
case where the active factor is a rack of the form `H x F`; it is not known to
be complete.  Failure of one proposed finite transducer class is only a gap.
Failure for all finite rack detectors is the normalized-law negative branch.

Equivalently, the exact finite-rack negative test for a fixed rack prefix is
as follows.  Enumerate finite racks and let

```text
P_m = Y_1 x ... x Y_m.
```

For fixed `m,n`, form

```text
Gamma_{m,n}(X)
  =
< (rho^{P_m}_n(sigma_i),rho^X_n(sigma_i)) : 1 <= i < n >
<= Sym(P_m^n) x Sym(X^n)
```

and

```text
N_{m,n}(X) = { g_X : (1,g_X) in Gamma_{m,n}(X) }.
```

Then `N_{m,n}(X)!=1` is an explicit finite braid word invisible to the rack
prefix `P_m` and nontrivial on `X^n`.  A genuine Sawin-negative proof requires

```text
forall m exists n,  N_{m,n}(X) != 1.
```

That cofinal rack-prefix obstruction, not failure of any bounded transducer
search by itself, is the normalized-law no-rack sequence.
