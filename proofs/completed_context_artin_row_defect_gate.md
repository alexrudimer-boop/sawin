# Completed-context Artin row-defect gate

Date: 2026-06-03

This note sharpens the final endpoint-unit obstruction isolated in
`proofs/unit_continuation_final_obstruction.md` and
`proofs/unit_composite_longitude_criterion.md`.  It does not prove finite-rack
domination and it does not construct a counterexample.  It records the exact
local row identity whose proof would make the endpoint-unit longitude theorem
formal.

## Setup

Let `M <= End(S)` be the fixed finite transformation monoid attached to one
completed-context endpoint branch of a local residual interval.  Let

```text
U = U(M)
```

be its group of permutation elements.  If a residual endpoint

```text
h_beta = f_t ... f_1 in M
```

is a residual fibre permutation, then `h_beta in U`.  Since `S` is finite, a
composition of total maps is bijective only when every factor is bijective.
Thus every factor in an actual moving endpoint branch is already a unit.  The
last semigroup obstruction is therefore genuinely a finite `U`-valued row
problem, not a nonunit/reset problem.

## Desired Row Factorization

For each actual retained completed-context germ `e`, write its unit readout as

```text
(a_e,l_e) in U x U.
```

Here `a_e` is the local meridian/unit label and `l_e` is the accumulated
endpoint label.  Consider an actual supported completed row

```text
e=(s,x),        f=(s tau_x,y)
```

with

```text
r(x,y)=(u,v),
```

and output germs

```text
e'=(s,u),       f'=(s tau_u,v).
```

The positive row identity is that this actual row is an active Artin detector
row over `U`:

```text
(a_{e'},l_{e'}) = (a_e a_f a_e^-1, a_e l_f),
(a_{f'},l_{f'}) = (a_e, l_e).
```

Equivalently, the completed-context unit readout factors through the finite
rack

```text
A_U = T_2 x (U x U),

(a,l) * (b,m) = (a b a^-1, a m),
```

with the `T_2` coordinate carrying the strand permutation.

This is exactly the row hypothesis of
`proofs/artin_detector_lift_criterion.md`.  Once it holds, induction on braid
words gives, for the initial assignment `phi:F_n -> U` with `phi(x_i)=a_i`,

```text
l_j(beta)=phi(L_j(beta)).
```

Any endpoint composite built from the terminal `l_j(beta)` labels therefore
lies in

```text
V_beta(U)=<phi(L_j(beta)) : phi:F_n -> U, 1<=j<=n>.
```

Thus the endpoint-unit longitude theorem follows immediately from actual
`A_U` row factorization.

## Row Defects

The obstruction is that ordinary YBE cube coherence does not by itself imply
the split identities above.  It may only give equality of total row transport
around cubes.  In the meridian part, the product relation

```text
a_e a_f = a_{e'} a_{f'}
```

does not force

```text
a_{f'} = a_e,
a_{e'} = a_e a_f a_e^-1.
```

Define the actual Artin row defects

```text
delta_a(e,f) = a_{f'}^-1 a_e,
delta_l(e,f) = l_{e'}^-1 a_e l_f.
```

The detector-lift row identity is exactly

```text
delta_a(e,f)=1,
delta_l(e,f)=1
```

for every actual supported completed row.  YBE cube identities can force these
defects to satisfy flatness or cocycle identities on actual supported cubes,
but flatness is weaker than vanishing.  This is the endpoint-unit analogue of
the Green section transport distinction in
`proofs/green_section_transport_rigidity_gate.md`: actual cube coherence gives
path-independence of the defect system, not automatically trivial holonomy.

## Consequence For A

The remaining positive target can now be stated without reference to
finite-index searches:

```text
Completed-context Artin row-defect vanishing.
Every completed-context unit row in an actual local-minimal
bi_free_universal_corridor_bottleneck interval satisfies
delta_a=delta_l=1 in U(M).
```

Together with the existing nonunit exclusion and endpoint-product assembly,
this would prove every residual endpoint unit belongs to `V_beta(U(M))`.
Multiplying the finitely many unit, Green, Schutzenberger, atom, quotient, and
known-branch detector factors would then give the fixed group `H(pi,Q)` needed
by the sharp obstruction theorem.

## Consequence For B

A nontrivial row defect is not yet a counterexample to finite rack domination.
It only says that the actual endpoint transition system is not explained by
the particular Artin detector rack over `U(M)`.

To prove outcome B from such a failure, one would still need a normalized-law
sequence

```text
beta_j in B_{n_j},      n_j -> infinity,
```

such that every finite group `G` eventually has identity recursive-longitude
data on `beta_j`, while a residual endpoint unit remains nonidentity and moves
an explicit tuple.  A finite miss against `U(M)` alone can still be detected
by some larger finite group, because nontrivial free-group words are residually
finite.

Thus the live endpoint fork is:

```text
prove actual A_{U(M)} row factorization for every completed-context unit row,
or upgrade a genuine row-defect failure to an all-finite-group
normalized-law residual mover.
```
