# YBE inverse-branch determinization gate

Date: 2026-06-03

This note records the sharpened degenerate-guitar obstruction.

The previous guitar boundary leaves the genuinely degenerate case as a finite
inverse-branch problem.  The finite transformation monoid

```text
M_rho=<R_x:x in X> <= End(X),    R_y(x)=rho_y(x),
```

is finite, so a degenerate repair is not blocked by infinite suffix memory.
The tempting move is to determinize the missing inverse branches by using
subsets, partial inverse sections, Green `R`-classes, Schutzenberger
coordinates, or triples carrying preimage sets.

The total version of this strategy fails.

## Total Decoder Obstruction

Use the right-oriented rack switch convention

```text
S_Y(a,b)=(a > b,a).
```

A finite-state decoder consists of a state set `Q`, an initial state `q0`, and
maps

```text
d:Q x Y -> X,
tau:Q x Y -> Q.
```

The decoded maps `Phi_n:Y^n -> X^n` are built by reading a rack word with this
state update, and a total rack cover must have every `Phi_n` surjective.

The local two-symbol decoder equation includes

```text
d(tau(q,a > b),a)=rho_{d(tau(q,a),b)}(d(q,a)).
```

Together with total surjectivity, this equation forces the relevant right
actions to be surjective.  Indeed, `Phi_1` realizes every `x in X` as
`d(q0,a)`, and `Phi_2` realizes every next symbol `y` from the one-step
reachable state.  The displayed equation then realizes every `rho_y(x)` as a
decoded value with the copied rack symbol `a`.  For a monoid-guitar decoder,
that is exactly the requirement that the inverse branch at the corresponding
suffix state be defined for all outputs:

```text
R_y(X)=X for every y.
```

Since `X` is finite, every `R_y` is then bijective.  Thus a total
deterministic monoid-guitar decoder cannot cover a genuinely right-degenerate
solution.  The left-oriented convention gives the analogous statement for the
maps `lambda_x`.

## Rank-Drop Form

In monoid language, a deterministic branch selector would need

```text
d(q,a) in q^-1(a),
tau(q,a)=q R_{d(q,a)}.
```

If a transition drops image rank,

```text
rank(q R_x) < rank(q),
```

then some output `a` has empty inverse fibre under `q R_x`.  No deterministic
total branch value `d(q R_x,a)` exists.  In particular, a non-surjective
generator already creates the obstruction from the identity state.

Green `R`-classes and Schutzenberger coordinates can describe the regular
parts of `M_rho`, but they do not undo this rank drop.  They are useful
semigroup diagnostics rather than a universal repair.

## Why Powersets Do Not Repair It

Powerset or relation-valued constructions preserve possible branches, but
Sawin kernel inclusion requires a finite rack action or an equivalent marked
quotient with functional decoding.  If the decoder is nondeterministic, a
braid may preserve the relation of possible decodings without acting
trivially on each point of `X^n`.

At the rack-operation level, natural subset maps also fail to be rack
translations in the degenerate case.  Direct images are not injective when the
transformation is not injective, and inverse images are not injective when it
is not surjective.  Restricting to saturated or image subsets loses singleton
separation, so it no longer proves pointwise kernel inclusion.

## Remaining Restricted Problem

If one abandons total decoding on all of `Y^n` and instead works on a proper
invariant language where empty fibres are avoided, the obstruction becomes a
branch-cocycle problem.  The selected partial inverse branches must be closed
under the local decoder equations and must satisfy the rack
self-distributivity condition.  The first genuine coherence condition is an
arity-3 branch cocycle.

Thus the degenerate inverse-branch problem is not solved by finite monoid
determinization.  Any positive degenerate theorem must either find a different
finite rack-cover mechanism or prove that a restricted finite language with
coherent arity-3 branch selectors is enough to recover Sawin's marked kernel
inclusion.

The generated audit

```text
proofs/ybe_inverse_branch_determinization_audit.md
```

records this route gate.
