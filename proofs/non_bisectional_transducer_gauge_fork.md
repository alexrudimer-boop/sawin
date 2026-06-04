# Non-Bisectional Transducer-Gauge Fork

Date: 2026-06-04

This note records the same-chat Pro answer after
`proofs/rackable_endpoint_absorption.md`.  The bisectional endpoint repair is
correct, but it is not universal: genuinely degenerate finite YBE rows can
have local residual movement that no finite single-strand permutation fibre
can reconstruct.

This does not produce a Sawin counterexample.  The explicit obstruction row is
already braid-kernel equivalent to a finite rack by a position-dependent
finite gauge.  The remaining positive target is therefore a finite
transducer/rack gauge theorem, not a universal bisectional endpoint theorem.

## Semiconjugacy Obstruction

Let `G` be a finite retained germ set.  For a supported row

```text
B(e,f) = (e',f')
```

write the local right-strand update determined by the left germ `e` as the
partial map

```text
lambda_e(f) = e'.
```

A finite bisectional/probe-complete enrichment that reconstructs this local
movement would require finite data

```text
p: G_tilde -> G,          Phi_e in Sym(G_tilde),
```

with `p` surjective and

```text
p Phi_e = lambda_e p.                         (1)
```

If `G_tilde` is finite and `Phi_e` is a permutation, then `lambda_e` must be
surjective on the image of `p`.  Indeed, for any `g in G`, choose
`g_tilde in p^{-1}(g)`.  Since `Phi_e` is surjective, there is
`f_tilde` with

```text
Phi_e(f_tilde) = g_tilde.
```

Then

```text
g = p(g_tilde) = p Phi_e(f_tilde) = lambda_e p(f_tilde).
```

So `g in im(lambda_e)`.  Since `G` is finite, a total `lambda_e` is then
bijective.

Therefore:

```text
finite bisectional reconstruction => local right-strand updates are surjective.
```

Any actual finite YBE interval with a non-surjective local update is a real
failure of universal bisectional enrichment.

## Affine F2^3 Witness

The left-degenerate affine pressure row from
`proofs/affine_f2_hidden_cyclic_gauge.md` gives an actual witness.  Let

```text
X = F_2 x W,          W = F_2^2,
J(z1,z2) = (z2,z1),  c = (1,1).
```

Define

```text
R((a,z),(b,w)) = ((a,Jw),(b,Jz+c)).           (2)
```

Equivalently, in coordinates

```text
R(x,y) = (x1,y3,y2, y1,x3+1,x2+1).
```

This is an actual finite bijective YBE table.  Bijectivity is immediate from
the displayed formula, and YBE follows from the position-dependent gauge

```text
u_i = J^i z_i + (i mod 2)c,
```

which conjugates the braid action to the constant-action order-2 rack action

```text
sigma_i:(u_i,u_{i+1}) -> (u_{i+1}+c,u_i).
```

For fixed left input `x=(a,z)`, the first output map is

```text
lambda_x(b,w) = (a,Jw).
```

This does not depend on `b`.  Its image is `{a} x W`, of size `4`, while
`|X|=8`.  Thus `lambda_x` is not surjective.

By the semiconjugacy obstruction, no finite probe set with permutation
operators can semiconjugate this local update to the actual `X`-movement.
The row is genuinely non-bisectional.

## Why It Is Sawin-Harmless

The same row is already closed in
`proofs/affine_f2_hidden_cyclic_gauge.md`.  The position-dependent gauge

```text
u_i = J^i z_i + (i mod 2)c
```

identifies the `W`-part of the braid action with the constant-action order-2
rack, while the `F_2` coordinate is inert.  Hence

```text
ker rho^X_n = ker rho^{C_2}_n
```

for every arity `n`.  The two-element cyclic rack dominates `X`, in fact with
kernel equality.

Thus non-bisectional movement exists, but this example is absorbed by a finite
sequential/position-dependent rack gauge.

## Correct Remaining Positive Theorem

The positive endpoint theorem cannot be:

```text
every actual endpoint becomes bisectional.
```

That statement is false by the affine row above.

The plausible positive theorem is instead:

```text
Finite transducer/rack gauge theorem.

For every actual finite YBE completed-context interval I, the residual
movement decomposes into faithful bisectional endpoint factors plus finite
sequential gauges whose combined marked braid factor is jointly
reconstructive on X^n, uniformly in n.
```

The affine row is the model positive case: its gauge is not a local
single-strand bisection of the original `X` coordinate, but it is a finite
position-dependent marked braid factor.

The sharper certificate formulation is recorded in
`proofs/finite_transducer_rackification_certificate.md`.  There the remaining
positive lemma is renamed finite sequential-rack observability: after the
known positive reductions, find finite data

```text
(Z,R_Z,S,Q,P,delta,omega,Delta,nu)
```

whose local two-letter equations make the sequential readouts
braid-equivariant/invariant and whose pair automaton proves all-length
injectivity.  Such data prove domination by `R_Z x S`.  Conversely, absence of
such data under any fixed size bounds is only a bounded certificate failure,
not a no-rack theorem.

The next refinement makes this certificate canonical.  Equivalently, for the
structure monoid `M_X=<X | xy=uv>`, one seeks a finite right `M_X`-set `Q`, a
finite group `H` acting on a finite set `F`, and assignments
`h_{q,x} in H`, `f_{q,x} in F` satisfying the local equations recorded in
`proofs/finite_transducer_rackification_certificate.md`, with all-length
injectivity into `(H x F)^n`.  The detector rack is then the canonical product
rack

```text
(alpha,z)*(beta,w)=(alpha beta alpha^{-1},alpha.w).
```

This canonical form is equivalent to the earlier sequential rack certificate
via `S -> Inn(S) x S`.

The rack-only version of this canonical form is too narrow.  If the
all-length reconstruction uses only `Q,H,F` rack-active outputs, then any
left-degeneracy collision `lambda_x(y_1)=lambda_x(y_2)` forces the two
rack-output words `(x,y_1)` and `(x,y_2)` to coincide, because rack left
translations are bijective.  Thus rack-only canonical data force
left-nondegeneracy.  The affine row above is therefore the minimal route
obstruction: it has no rack-only canonical certificate, but it is still
dominated by the observer-augmented cyclic gauge.

The newest refinement broadens the certificate target one more step.  A finite
prefix congruence `Q` does not itself give domination: after `qxy=quv` one
still has to solve the nonabelian crossed-cocycle equations and prove
all-length injectivity.  The exact recursive certificate class therefore lets
the active output land in any finite YBE factor `T` already known to be
rack-dominated.  The local equation is

```text
r_T(omega(q,x),omega(qx,y))=(omega(q,u),omega(qu,v)),
```

with the same state equation, optional observer outputs, and finite
pair-automaton injectivity test.  The helper
`active_factor_certificate_audit(...)` now checks fixed candidates of this
kind.  The canonical `Q,H,F` certificate is the special case in which `T` is
the rack `H x F`.

## Exact Negative Search Target

A genuine Sawin counterexample must now have all three properties:

1. non-bisectional local movement, so
   `proofs/rackable_endpoint_absorption.md` does not apply;
2. no finite recursive active-factor/transducer gauge reconstructing the
   hidden motion;
3. a cofinal Artin-null Brunnian branch family: for every finite rack prefix
   `P_m`, some braid `beta_m` satisfies

```text
rho^{P_m}_{n_m}(beta_m) = 1,
rho^X_{n_m}(beta_m) != 1.
```

The affine `F_2^3` row has property 1 but fails property 2 because the gauge
above reduces it to a constant-action rack.  Failure of bisectional enrichment
alone is therefore only a search filter.

The actual all-rack negative test is the cofinal rack-prefix obstruction from
`proofs/finite_transducer_rackification_certificate.md`: for every finite rack
prefix `P_m`, some arity `n` must have a nontrivial

```text
N_{m,n}(X) = { g_X : (1,g_X) in
< (rho^{P_m}_n(sigma_i),rho^X_n(sigma_i)) > }.
```

That condition supplies the normalized-law braid sequence.  It remains stronger
than failing to find a finite sequential certificate in a bounded search.

For a concrete finite YBE table `X`, the first filter is

```text
N_X = { x in X : lambda_x:X -> X is not surjective }.
```

The remaining computational search should look for actual finite YBE tables
with `N_X` nonempty, outside the known positive branches, and with no finite
recursive active-factor gauge certificate visible through growing arities.
Only after that would one try to build the cofinal Artin-null Brunnian
sequence.
