# YBE coskeletal mechanism audit

Date: 2026-06-03

This generated audit records the YBE-specific side of the
pullback-coskeletal question.  The point is not to add another
bounded prefix computation.  The point is to state what kind of
finite-type theorem would turn bounded prefix data into an
all-arity pullback theorem.

Finite bijective YBE data gives finite local transition rules and
local generation of braid/deletion moves.  It does not automatically
give local detection of the nonabelian deletion-cohomology class.
The desired bounded theorem becomes formal only after adding finite
operator labels satisfying genuine bounded-width descent for the
point-pushing groupoids and their deletion coefficient bands.

## Flags

- finite bijectivity gives local generation: `True`;
- finite bijectivity does not give local cohomology detection: `True`;
- bounded-state recursion would imply coskeletality: `True`;
- high cross-effect bisections are a live obstruction: `True`;
- w-local operator-label descent is an extra hypothesis: `True`;
- coefficient inverse-limit condition recorded: `True`;
- comparison commutes with inverse-limit reconstructions: `True`;
- bounded relation arity cutoff recorded: `True`;
- Brunnian cross-effect criterion recorded: `True`;
- records YBE coskeletal mechanism boundary: `True`.

## Conditional theorem

Let the finite operator-label enrichment be `w`-local: the labelled
point-pushing groupoid in arity `I` is the inverse limit of its
restrictions to subsets of size at most `w`, and for deletion sets
`D` with `|D| <= 3` the coefficient band `A_D^I` is the inverse
limit of the `A_D^J` with `D subset J` and `|J| <= |D|+w`.
The base coefficients must satisfy the same condition, and the
comparison maps must be the inverse-limit extensions of their
bounded-subset restrictions.

If transport, cocycle, and gauge equations are generated in relation arity `r`, the cutoff is `N0 = max(r, w + 3)`.
[Omega] is in im Pi^sharp iff the truncation [Omega_<=N0] is in im Pi^sharp_<=N0, equivalently all-arity base cocycle and gauge data exist iff they exist through arity N0

The proof is formal from these hypotheses: nonabelian cochains,
cocycles, gauges, and pullback equations are assembled by finite
products, finite fibre products, and finite equalizers, which are
preserved by the right Kan extension from the bounded arities.

## Brunnian obstruction

`cr_ij^I(A) = intersection over k in I\{i,j} of ker(A_ij^I -> A_ij^{I\{k}})`.

bounded pullback-coskeletality for a fixed labelled tower requires Br^2_I(C,A;B)=1 for all sufficiently large I, together with effective low-arity coefficient descent

Positive YBE-specific theorem obligations:

- prove w-local inverse-limit reconstruction for operator labels;
- prove coefficient inverse-limit reconstruction for one-, two-, and three-deletion bands;
- prove bounded relation arity for transport, cocycle, and gauge equations;
- prove vanishing of Brunnian relative deletion 2-obstructions above the cutoff;

## Mechanisms

### formal_w_local_descent_theorem

- role: `conditional_positive_theorem`;
- mechanism: right Kan descent from arity at most w for the labelled point-pushing groupoid and from arity at most |D|+w for the deletion coefficient bands;
- finite YBE status: finite bijectivity alone does not provide this descent; it must be proved after adding suitable finite operator labels;
- theorem obligation: prove w-local inverse-limit reconstruction and bounded relation arity r, then use N0=max(r,w+3);
- obstruction signature: compatible low-arity gauge/base solutions fail to extend because a high-arity Brunnian deletion 2-class survives.

### fadell_neuwirth_recursion

- role: `necessary_but_insufficient_structure`;
- mechanism: point-pushing generators and point-forgetting maps are recursive under the Fadell-Neuwirth tower;
- finite YBE status: finite YBE tables make each local transition finite and computable;
- theorem obligation: prove that recursive generator descriptions also generate all deletion 2-cocycle relations in bounded arity;
- obstruction signature: Brunnian vertical classes restrict trivially to all bounded faces while remaining nontrivial in higher arity.

### finite_operator_state_recursion

- role: `positive_candidate`;
- mechanism: augment tuples by finite operator labels so every Artin conjugacy update is read by a fixed finite transducer;
- finite YBE status: finite labels can make local moves deterministic on a chosen finite state space;
- theorem obligation: show the transducer state is complete for vertical fibre-bisection cohomology, not merely for tuple motion;
- obstruction signature: two towers with identical finite operator-state histories but different high-arity vertical 2-cocycles.

### garside_or_automaton_normal_forms

- role: `possible_finite_type_tool`;
- mechanism: use braid or pure-braid normal forms to recognize Artin conjugacy words by finite or noetherian rewriting;
- finite YBE status: normal forms control braid words but not automatically the deletion-gauge cohomology quotient;
- theorem obligation: prove that normal-form rewriting induces a finite complete rewriting system on vertical cocycle representatives;
- obstruction signature: normal-form length grows while all bounded deletion shadows stay gauge-trivial.

### fi_fb_finite_generation

- role: `strong_positive_hypothesis`;
- mechanism: view vertical bisection groups, deletion cochains, and 2-cocycles as an FI/FB-type module or nonabelian analogue;
- finite YBE status: finite sets supply finite fibres in each arity but not finite generation as a tower;
- theorem obligation: establish finite generation/noetherianity for the relevant coefficient and obstruction functors;
- obstruction signature: new orbit types or coefficient generators appear in unbounded arity.

### brunnian_cross_effect_obstruction

- role: `negative_countermechanism`;
- mechanism: construct vertical bisections supported only on genuinely multi-point interactions;
- finite YBE status: finite bijectivity does not by itself forbid high-order cross-effects;
- theorem obligation: rule out or bound Brunnian cross-effects using YBE-specific identities;
- obstruction signature: for every bound d, a nontrivial deletion 2-cocycle appears whose restriction to every d-skeleton is gauge-trivial.

## Meaning

The positive theorem route needs more than finite local moves.
It needs `w`-local inverse-limit descent for the operator-labelled
tower and coefficient bands, plus bounded relation arity for the
transport, cocycle, and gauge equations.

The negative route should not look for unbounded whole-image
orders.  It should look for genuinely high-arity vertical
`2`-cocycle classes whose restrictions to every bounded skeleton
are gauge-trivial but whose all-arity class is not pulled back
from one fixed finite operator-label base.  Equivalently, it should
force nontrivial Brunnian relative deletion `2`-obstruction sets
in arbitrarily large arities.
