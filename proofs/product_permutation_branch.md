# Product-permutation branches

## Swapped Normal Form

If the stable two-sided local retraction relation is universal, then it is
below the forward one-step profile relation.  Hence each coloured table has
the form

```text
T_{a,b}(x,y) = (L_{a,b}(y), R_{a,b}(x)),
```

where `L_{a,b}: A_b -> A_{a.b}` and `R_{a,b}: A_a -> A_{a*b}` are bijections.
The script-level witness is `product_permutation_witness(interval)`.

For any braid word and any fixed base-colour tuple, the residual fibre action
has an exact normal form:

```text
final fibre coordinate j
  = phi_j(initial fibre coordinate dependency[j]).
```

At a positive crossing of colours `(a,b)`, the dependency strands swap and the
new coordinate maps are composed with `L_{a,b}` and `R_{a,b}`.  At a negative
crossing, the inverse base edge is used and the coordinate maps are composed
with `R_{a,b}^{-1}` and `L_{a,b}^{-1}`.

The implementation is in `src/ybe_domination/product_permutation.py`.
The companion helper `swapped_product_label_word_action()` records the same
normal form before evaluating the finite fibre maps: each coordinate carries
a formal word in labels `L_{a,b}^{+/-1}` and `R_{a,b}^{+/-1}`.  Evaluating
these words with `evaluate_swapped_product_label_word()` recovers exactly the
coordinate maps in `product_permutation_action()`.

For a genuine coloured-YBE interval these fibre bijections satisfy explicit
cocycle equations.  Writing

```text
R_Z(a,b)=(ab,a_b),    R_Z(b,c)=(bc,b_c),
R_Z(a_b,c)=(a_b c,a_b*c),
R_Z(a,bc)=(a bc,a_bc),
```

the swapped equations are

```text
L_{ab,a_b c} L_{a_b,c} = L_{a,bc} L_{b,c},
R_{ab,a_b c} L_{a,b}   = L_{a_bc,b_c} R_{b,c},
R_{a_b,c} R_{a,b}      = R_{a_bc,b_c} R_{a,bc}.
```

They are exactly the three coordinate equalities obtained by expanding the
coloured braid relation `T_12 T_23 T_12 = T_23 T_12 T_23` in the swapped
normal form.

## Direct Normal Form

The dual universal coretraction branch gives the direct form

```text
T_{a,b}(x,y) = (L_{a,b}(x), R_{a,b}(y)).
```

Here no final fibre coordinate depends on a different initial fibre
coordinate.  For any braid word and fixed base-colour tuple, the residual
fibre action has the exact normal form

```text
final fibre coordinate j = phi_j(initial fibre coordinate j).
```

At a positive crossing of colours `(a,b)`, the coordinate maps at the two
crossing positions are composed with `L_{a,b}` and `R_{a,b}`.  At a negative
crossing, the inverse base edge is used and the coordinate maps are composed
with `L_{a,b}^{-1}` and `R_{a,b}^{-1}`.  The dependency vector remains the
identity throughout.

The implementation is `direct_product_action(interval, color_tuple, word)`.
The companion word-level helper `direct_product_label_word_action()` records
the unevaluated labels, and `evaluate_direct_product_label_word()` evaluates
one such coordinate word.  Tests verify that these formal words recover the
same coordinate maps as the direct normal form.

The direct branch has the analogous cocycle equations:

```text
L_{ab,a_b c} L_{a,b} = L_{a,bc},
R_{ab,a_b c} L_{a_b,c} R_{a,b}
  = L_{a_bc,b_c} R_{a,bc} L_{b,c},
R_{a_b,c} = R_{a_bc,b_c} R_{b,c}.
```

These equations are the finite coloured groupoid-label constraints that the
remaining coboundary reduction must exploit.

## Coboundary Audit

The product labels are a fibre-gauge coboundary when one can choose bijections

```text
g_a: A_a -> B_C
```

on each connected colour/fibre-size component so that every crossing label is
just transport between gauges.

For the swapped branch this means

```text
L_{a,b} = g_{a.b}^{-1} g_b,
R_{a,b} = g_{a*b}^{-1} g_a.
```

For the direct branch this means

```text
L_{a,b} = g_{a.b}^{-1} g_a,
R_{a,b} = g_{a*b}^{-1} g_b.
```

If such gauges exist, the fibre labels are conjugate to the colour-base
motion and contribute no hidden residual holonomy once the base action is
fixed.  The helper `swapped_product_coboundary_audit()` or
`direct_product_coboundary_audit()` solves these finite gauge equations by
propagating gauges through the finite colour graph and recording any loop
inconsistency.

The coboundary case is now closed as an all-`n` braid-action statement in
`proofs/product_coboundary_telescope.md`.  Any composable coboundary label
word telescopes to `g_target^{-1}g_source`.  Hence if the base colour tuple is
fixed, the direct product branch has identity residual fibre action; in the
swapped branch the same conclusion holds when the Artin permutation is
trivial, which is part of the finite-group longitude identity condition.
Thus the coboundary product subcase needs no nontrivial detector factor.

Failure of this coboundary audit is not automatically a counterexample.  In
the one-colour swapped case with commuting nontrivial fibre permutations, the
cocycle equations hold but the coboundary audit fails; this is precisely the
pairwise-linking subbranch detected by the cyclic abelian-longitude group
described below.  In fact, for one quotient colour the cocycle equations only
say `LR=RL`.  Local-minimality forces the abelian group `<L,R>` to act
primitively; a finite abelian primitive permutation group is cyclic of prime
order acting regularly.  Hence the whole one-colour swapped product branch,
for arbitrary fibre size, is cyclic pairwise-linking measurable.

When every fibre has size `2`, all product labels are translations of `F_2`
after choosing fibre coordinates.  The swapped and direct product cocycle
equations become linear equations over `F_2`, and the residual action in the
sharp-kernel setting is an affine `F_2` translation.  This places the entire
fibre-size-two product branch inside the already eliminated affine `F_2`
finite-G-measurable branch; see `proofs/fibre2_product_branch.md`.

The helpers `swapped_product_holonomy_summary()` and
`direct_product_holonomy_summary()` turn these loop inconsistencies into
finite permutation groups.  After a spanning gauge is chosen, each failed
constraint gives a permutation of the model fibre

```text
h = (expected gauge) (actual gauge)^{-1}.
```

The subgroup generated by these permutations is the residual coloured
groupoid holonomy.  Coboundary branches have trivial holonomy.  The
one-colour commuting swapped example has holonomy group `C_3`; this is the
same branch detected by the cyclic abelian-longitude criterion.  A genuinely
coloured non-coboundary product branch would now appear as a finite holonomy
group attached to the colour graph, rather than as an unnamed failure of the
normal form.

## Local-Minimality as Primitivity

For a product-permutation branch, the local congruence-family condition has a
finite groupoid interpretation.  A partition family `theta_a` is admissible
exactly when every product label transports source partitions to target
partitions.

For the swapped branch this means

```text
L_{a,b}(theta_b) = theta_{a.b},
R_{a,b}(theta_a) = theta_{a*b}.
```

For the direct branch this means

```text
L_{a,b}(theta_a) = theta_{a.b},
R_{a,b}(theta_b) = theta_{a*b}.
```

Thus product-branch local-minimality is exactly primitivity of the finite
coloured permutation groupoid: the only invariant partition families are
all equality and all universal.  The helpers
`swapped_product_invariant_families()` and
`direct_product_invariant_families()` enumerate these invariant families for
small fibres and agree with `LocalInterval.admissible_congruence_families()`
on the test fixtures.

The product branch now also has an arbitrary-fibre pair-closure certificate,
parallel to `proofs/local_minimality_gate.md` but computed purely in the
product-label groupoid:

```text
swapped_product_label_pair_closure_audits()
swapped_product_label_pair_closure_failures()
direct_product_label_pair_closure_audits()
direct_product_label_pair_closure_failures()
```

Starting from one distinct pair in one fibre, the helper closes that pair
under every product label and inverse product label.  A product interval is
primitive/local-minimal exactly when every such closure is universal.  This is
not a search over all set partitions; it is the least invariant congruence
generated by a single pair.  A non-universal closure is an explicit proper
product-label invariant congruence family and therefore a real refinement of
the congruence chain.

## Consequence for the master theorem

Both branches are finite-state and groupoid-permutation valued.  In the
swapped branch, if the Artin permutation of a braid is trivial, the dependency
vector is trivial and the residual action is coordinatewise by finitely many
fibre bijections.  In the direct branch the dependency vector is always
trivial.  Thus both branches reduce to detecting whether finitely generated
coloured permutation-groupoid labels are all identity.

Both product branches have now been sharpened one step further: the residual
coordinate maps are evaluations of explicit formal product-label words.  A
finite-G proof of the product theorem must show that identity Artin-longitude
data forces these label words to evaluate trivially; a product-style
counterexample must keep such a label word nontrivial while defeating every
finite group detector.

These are the precise local objects behind the already logged
permutation/pairwise-linking/coboundary measurable branch.  It does not close
the master theorem alone, but it removes both universal two-sided-retraction
and universal two-sided-coretraction sides from the hidden-holonomy problem:
any remaining obstruction must be bi-free.

## Abelian detector for pairwise-linking subbranches

When the finite coloured permutation labels reduce to a one-colour or
pairwise-linking action, the required finite group can be chosen explicitly.
Let `m` be a common multiple of the orders of all fibre permutations appearing
in the normal form.  The cyclic group `C_m` detects the relevant abelian
Artin-longitude data: `Lambda_{C_m,n}(beta)=Lambda_{C_m,n}(1)` is equivalent
to trivial braid permutation and vanishing abelian longitude matrix modulo
`m`.  Thus every coordinate label whose exponent is a linear combination of
pairwise-linking entries is forced to be the identity permutation.

The executable helper `artin_longitude_exponent_matrix(n,beta)` makes this
criterion explicit, and `has_trivial_abelian_longitudes_mod(m,n,beta)` checks
the cyclic detector condition.  This is still only the pairwise-linking
subbranch.  The genuinely coloured product-permutation case needs a
coboundary or finite groupoid-label reduction before this cyclic detector
argument applies.

## Audit

`tests/test_product_permutation.py` verifies that the swapped and direct
normal forms agree with the full local-interval braid action for positive and
negative generators and for mixed words.  This is an exact algebraic
decomposition for the branches, not a finite-search proof of the global
theorem.

The tests also check `swapped_product_cocycle_failures()` and
`direct_product_cocycle_failures()`.  A deliberately non-YBE product-normal
fixture fails the swapped cocycle check, which guards the distinction between
"has a product normal form" and "is a product normal form satisfying the
coloured Yang-Baxter equation."

The tests additionally check the coboundary audits:

- the one-colour flip branch is swapped-coboundary;
- the two-colour direct gauge fixture is direct-coboundary;
- a one-colour commuting swapped fixture satisfies YBE but is not
  coboundary, isolating the pairwise-linking branch rather than hiding it
  inside the coboundary case.

The generated audit `proofs/two_colour_fibre3_product_audit.md` adds a larger
structured stress test: all swapped and direct product labels in `S_3` over
all two-colour quotient YBE bases.  It finds no unknown primitive row after
removing standard branch tags and the identity-base cyclic case covered by
`proofs/identity_base_product_branch.md`.  The direct side does have
nontrivial holonomy in the full cocycle space, but every primitive direct row
in this exact search is involutive.  The symbolic one-colour argument is
recorded separately in `proofs/one_colour_product_branch.md`.

The identity-base proof now has an executable normal-form audit:
`identity_base_swapped_reduction()` records the fibrewise central maps
`K_a=R_{b,a}L_{b,a}=L_{a,c}R_{a,c}`, verifies their conjugacy under product
labels, and extracts the prime cyclic detector modulus when the nontrivial
local-minimal case remains.  The companion
`identity_base_direct_reduction()` records the direct identity-base
conclusion that all direct labels must be identities.  This is still a
symbolic subbranch proof, not a replacement for the arbitrary-colour product
closed-label subgroup lemma.
