# Sawin finite-rack domination

This repository is an auditable workspace for the finite-rack domination
question for finite bijective set-theoretic Yang-Baxter solutions.

Problem.  Given a finite bijective braided set `X`, decide whether there is a
finite rack `Y`, independent of the braid index `n`, such that

```text
ker rho_{Y,n} <= ker rho_{X,n}  for every n.
```

Current target.  Resolve the problem by producing exactly one final outcome:

- a complete proof of finite-rack domination, including the Master
  Local-Minimal Residual Theorem; or
- an explicit finite YBE counterexample with a normalized-law obstruction
sequence defeating every finite rack.

This checkout deliberately separates three kinds of evidence:

- `proofs/`: mathematical reductions, proof logs, and gap audits.
- `src/`: executable finite braided-set and local-interval verifiers.
- `tables/`: spreadsheet summaries of the reduction audit and branch status.

For a compact current-state map, start with
`proofs/progress_summary.md`.  It records what has been reduced, what is
proved only as guardrail machinery, and the exact remaining bottleneck.

The code is not allowed to serve as a finite-search-only proof of the global
theorem.  Its role is to check examples, audit local-minimality including
semisplit congruence families, verify the finite-group longitude detector
convention, audit quotient/residual kernel implications, and make candidate
obstructions reproducible.  It also includes small finite congruence-lattice
utilities for checking the mechanics of the congruence-chain reduction and a
bounded local-obstruction scanner for debugging candidate examples.  The proof
logs now isolate the `T_2` purity stabilization inside the sharp detector
rack `A_G`, so pure-braid branch formulas are used only after the full
finite-longitude identity has killed the Artin permutation.
The sharp rack-construction step is executable as
`sharp_obstruction_rack(Q,G)`, with `is_rack_solution()` checking rack form and
`product_solution()` building the finite Cartesian product `Q x A_G`.
The formal congruence-chain recursion is executable as
`assemble_congruence_chain_rack(Q_m, (G_{m-1},...,G_0))`: it iterates the
sharp step, records the size multiplication `|Q| -> |Q|*2*|G|^2` at each
interval, and has no braid-index parameter.  This is only the assembly layer;
the still-open burden is finding the local detector groups `G_i` uniformly in
`n`.
The local branch router now uses an exact single-pair closure criterion for
local-minimality, so arbitrary finite fibre sizes no longer require
Bell-number partition enumeration before routing.  The generated closure
audits now also carry canonical first-derivation rows for each nontrivial
relation edge, separating a proof-carrying local-minimality certificate from
a bare final universal/equality verdict.
The finite-longitude subgroup layer now includes a functoriality lemma:
fixed finite group homomorphisms send `V_beta(G)` into `V_beta(H)`, with
equality for surjections.  This keeps product-label, normalized holonomy,
unit-holonomy, Green, and Schutzenberger detector factors compatible under
quotients and projections without introducing any `n`-dependent detector.
It also includes the matching direct-product lemma
`V_beta(prod_i G_i)=prod_i V_beta(G_i)`, so factorwise branch detectors can
be multiplied into the single finite group required by the sharp obstruction
theorem.
The same facts are now certificate-level as well:
`pushforward_longitude_subgroup_witness(...)` moves an explicit witness
through a fixed homomorphism, and
`direct_product_longitude_subgroup_witness(...)` assembles factor witnesses
into one product witness without enumerating the product subgroup.
The Green detector factor list is synchronized with the atom-rack lift
criterion: `two_sided_green_detector_groups(X)` now includes symmetric
kernel-block factors, Schutzenberger action groups, and atom-quotient inner
groups from both `X` and `X^op`, deduplicated as concrete finite group
tables.
The detector-action version is also recorded: the active state of
`A_{prod_i G_i}` projects to the active states of all factor detector racks,
so separate branch readouts can be combined into one fixed product detector
readout.  The direct symmetric route now has a named fixed-index wrapper,
`symmetric_detector_readout_audit(X,n)`, which forms the one-point quotient
and tests the single group `Sym(X)` without changing the all-`n` target.
The semigroup bridge now has a unit-factorization gate: a product of total
maps of a finite set can be a residual permutation only when every factor is
a unit/permutation, so reset-like nonunit labels cannot be used as a final B
obstruction.
It now also has a unit-section detection criterion:
`unit_section_detection_audit()` combines monoid membership, unit
factorization, and `V_beta(U(M))` subgroup membership into the exact
finite-group implication an all-`n` corridor proof must supply.
The endpoint version, `unit_composite_detection_audit()`, weakens the target:
after a residual word telescopes, it is enough that the final unit composite
lies in `V_beta(U(M))`; individual section factors need not all lie there.
The product version, `unit_section_product_detection_audit()`, checks that
separate fixed unit-section factors combine into one direct-product detector
group, so a proof cannot accidentally rely on a detector list that changes
with the braid index.
The endpoint product helper, `unit_composite_product_detection_audit()`, is
the preferred audit when those section factors telescope before readout; it
records the endpoint tuple in the direct-product unit group and tests direct
membership in the one product longitude subgroup when enumeration is feasible.
Its product-endpoint flags separate the sharp-obstruction condition in
`prod_i U(M_i)` from the factorwise display, so the proof target is one fixed
finite product detector rather than a list of informal branch checks.
The single-endpoint route helper
`unit_composite_longitude_route_audit()` now records the endpoint proof ladder:
identity endpoint, single evaluated-longitude witness, and membership in the
full longitude-value subgroup.  Only the last failure shape is serious for a
future B route.
For proof-side use, `unit_composite_longitude_expression_audit()` now checks a
non-enumerative certificate: the endpoint is displayed as a word in evaluated
recursive longitudes for one assignment into the fixed unit group.  Such an
expression proves membership in `V_beta(U(M))` directly and is the preferred
symbolic target for all-`n` corridor endpoint proofs.  The product version
`unit_composite_product_longitude_expression_audit()` packages finitely many
such expressions into one product endpoint certificate and now returns an
explicit subgroup witness in `V_beta(prod_i U(M_i))`, whose letters may use
different product-group assignments.  This matches the single finite group
demanded by the sharp obstruction theorem without relying on product-subgroup
enumeration.
The newest endpoint refinement is the Artin-defect sieve:
`proofs/artin_defect_longitudinalization_sieve.md` proves that values of
`beta(w)p_beta(w)^-1` always lie in the longitude-value subgroup of any finite
target group, because these defects are in the normal closure of the recursive
Artin longitudes.  The helpers `artin_permutation_defect_witness_audit()`,
`endpoint_artin_defect_audit()`, and
`endpoint_product_artin_defect_audit()` verify supplied defect displays and
turn them into literal longitude-subgroup witnesses.  This narrows the open
bi-free corridor target to proving such Artin-defect displays for every
elementary group-like Green/corridor endpoint generator in the fixed factors
of `H(pi,Q)`.
The detector-lift criterion now handles the braid-word recursion behind those
displays: `artin_detector_lift_transition_audit()` checks one finite local
row against the active `G x G` update rules of the sharp Artin detector, and
`artin_detector_lift_braid_audit()` verifies that the resulting terminal
endpoint labels are exactly evaluated recursive Artin longitudes for every
braid word.  The remaining corridor theorem is thereby reduced to a
row-by-row finite identity check in the fixed Green, Schutzenberger,
atom-inner, quotient, and endpoint-unit factors.  The atom-inner part of this
list is now closed once atom descent and totality are known:
`proofs/atom_inner_detector_lift_rows.md` proves that every rack-like atom
quotient inner group satisfies the detector-lift rows automatically, with the
negative rows following as inverse positive rows.  The genuinely open row
checks are now the Green kernel-block, Schutzenberger, and lower endpoint/unit
holonomy factors.
The Green and Schutzenberger row burden has now been compressed further by
`proofs/green_first_output_defect_criterion.md`.  A group-valued Green row
has the normal form determined by the single defect
`d_C(a,q)=g(q^a)g(q)^-1`; the second output is forced from
`g(a)g(q)=g(q^a)g(a^q)`.  When no local-only edge-germs occur, kernel-block
defects are pushforwards of Schutzenberger defects through a fixed finite
homomorphism.  The follow-up note
`proofs/green_defect_kernel_quotient_detection.md` quotients each
Green/Schutzenberger observer `U_C` by the normal closure of these defects;
on `U_C/Def_C`, every row is exactly side-opposite rack-Artin and is therefore
handled by the detector-lift theorem.  The next note
`proofs/green_defect_potential_coboundary.md` proves that every elementary
defect in `Def_C` is a finite nonabelian coboundary
`eta(q^a)eta(q)^-1` on the retained edge-germ graph.  Thus the open Green
target is now the Artin-transport principalness of this potential: prove the
transported defect product `D_C(beta)` lies in `V_beta(Def_C)`, plus the
already isolated lower endpoint/unit holonomy problem.
The semisplit audit now has an exact Boolean-CSP view: each coloured crossing
lists the allowed equality/universal bit patterns on its two source and two
target colours, and satisfying non-extreme assignments agree with the
relation-level semisplit audit after singleton-fibre canonicalization.
The proof log now states the master local dichotomy explicitly: all local
finite-G detectors imply the global finite rack by congruence-chain induction,
while one explicit detector-free local interval diagonalizes to the required
normalized obstruction sequence.
The proof
logs also track failed normalized-law shortcuts so that finite-search evidence
is not mistaken for a counterexample, and they record a pure-braid law
embedding framework for future counterexample attempts.  Action-image audits
track when such law words must vanish in fixed finite braid-action images and
measure small moving-image growth as braid index increases.  Tiny YBE table
screens are included only as candidate search, never as proof evidence.
The proof notes now also isolate the bounded-degree action-image limitation:
finite groups such as `rho_X(B_n)` or degree-`n` orbit holonomy groups are
useful diagnostics, but they are not valid Sawin detectors unless they factor
through one fixed finite group independent of `n`.
The moving-law route now has a fixed-variety barrier: if all relevant moving
pure-image or residual holonomy groups lie in the variety generated by one
finite group `G_0`, then any normalized-law sequence eventually invisible to
`G_0` acts trivially through that route.  Thus a B construction must show
finite-variety escape, not just growing finite action images.
The assigned-generator law separator is now explicit:
`short_law_separating_permutation_assignment()` searches for a word that is a
law on listed detector groups but moves the particular supplied tuple of
permutation images.  Structure-orbit B diagnostics use this sharper condition
on restricted pure braid generators, not merely failure of a law somewhere in
the generated image group.
The diagonal normalized-obstruction lemma is also now backed by executable
convention audits: `diagonal_product_invisibility_audit()` checks that
finite-longitude invisibility in a direct product is exactly factorwise
invisibility, and `right_stabilization_longitude_audit()` checks that adding
unused right strands preserves old Artin data while adding only trivial new
strands.  These helpers support the formal diagonal argument after an
explicit all-finite-group detector failure has been proved.
The moving-variety counterexample route now uses an assigned-generator
structure-orbit separator, and the small symmetric-law separator audit finds
no length-6 mover against the full `Sym(X)` detector in the checked size-2
and size-3 rows.  The notes also record that the direct `Sym(X)` route cannot
be proved by a literal rack-style coordinate formula except in the rack-type
case; the required target is a global Artin verbal-quotient factorization.
The executable wrapper `symmetric_detector_readout_audit(X,n)` now records
the fixed-degree readout form of that route; on the size-three affine stress
row it proves the `n=2` direct symmetric readout exactly, but this remains
fixed-index evidence rather than a proof.
The direct symmetric route now also has a symbolic known-branch filter:
rack-type, involutive, permutation-form, and nondegenerate/guitar rows are
directly detected by `Sym(X)` via subgroup monotonicity or Artin-permutation
factorization.  The regenerated size-2 and size-3 symmetric audit has no
unknown rows under this filter, so its exact `n=3` truncations are not
candidate obstructions.
The two-strand part of this direct route is now exact: finite-`G` longitude
data on `B_2` has period `2*exp(G)`, so `A_{Sym(X)}` passes the two-strand
test exactly when `ord(R_X)` divides `2*lcm(1,...,|X|)`.
The two-strand obstruction is also bounded on the other side:
`two_strand_cyclic_detector_certificate(X)` records that `C_r`, for
`r=ord(R_X)`, always detects the two-strand crossing action.  Thus a
crossing-order mismatch can kill a proposed detector but cannot be the whole
normalized-law counterexample.
This exact gate is now proved branchwise for rack-type, permutation-form, and
nondegenerate/guitar solutions.  The size-3 conservative leftovers are exactly
the nondegenerate branch and are now classified by the derived-rack
two-strand guitar conjugacy; a direct two-strand `Sym(X)` failure must come
from outside those known forms.  The gate is also closed under Cartesian
products of finite solutions, so a product-built two-strand failure must
already contain a failing factor rather than arise from taking products of
passing branches.
There is now a separate all-degree product-domination closure lemma: if
finite solutions `X_i` are dominated by finite racks `Y_i`, then the
Cartesian product solution `prod_i X_i` is dominated by the product rack
`prod_i Y_i`, for every braid index `n`.  This is a symbolic kernel
intersection argument, not a search result, and it rules out product assembly
from already dominated factors as a counterexample strategy.
The same hereditary bookkeeping is now recorded for quotients and
subsolutions: domination passes from a finite solution to every braided-set
homomorphic image and every crossing-closed subset.  Thus a genuine B
counterexample can be sought quotient-minimal and subsolution-minimal, and a
bad quotient/subsolution already defeats the larger solution.  A parallel
cover guardrail now rules out a different shortcut: quotients of finite
nondegenerate solutions remain nondegenerate, so degenerate solutions cannot
be handled by taking hidden finite nondegenerate covers and applying the
guitar theorem upstairs.
The current hidden-holonomy work also includes a Green R-class
coordinate-action audit for the local branch-choice obstruction, including a
bounded completed-context category and a local-minimal congruence-cover scan.
The bounded Green category now separates raw atom-trivial context collapse
from group-like atom-trivial holonomy by extracting the finite permutation
group generated by total bijective atom-trivial context loops.  This new gate
keeps a reset-like corridor from being mistaken for a counterexample: a B
route through Green/corridor data must move in the group part, while an A
route must factor that group part through the fixed Green/Schutzenberger
detector product.
The Green audit now also checks atom-action descent:
`atom_action_summary()` verifies whether the completed-row value `p(a^q)`
depends only on the two saturated atoms `p(a),p(q)` and whether the inverse
bookkeeping operation is well-defined.  The current tiny exhaustive Green
scans have no atom-action conflicts, sharpening the open branch from raw
branch-choice ambiguity to all-`n` unit holonomy in this finite atom layer.
When that action is total, `atom_quotient_solution()` constructs the finite
atom crossing `(A,Q)->(Q,A^Q)`.  The current tiny scans produce only
right-rack-like YBE atom quotients, and `atom_quotient_rack_audit()` records
bijective right translations plus right self-distributivity directly.  The
descent-closed variant `atom_descent_quotient_rack_audit()` now distinguishes
controlled coarsening from a genuine obstruction: if the least closed
coarsening is still a rack layer, the lost lower information must be handled
by endpoint/unit holonomy.  So the atom quotient itself is routed to a finite
rack layer whenever the saturated or closed quotient is total; any remaining
Green obstruction must survive in the section/unit holonomy below it.
The new descent-closure audit `atom_descent_closure_summary(audit)` makes the
atom-action gap exact: it computes the least coarsening needed for completed
rows to act on atoms.  In the current size-2/3 exhaustive scans this closure
adds no pairs and has no failures, so the symbolic target is now to prove that
local-minimal Green/corridor intervals force the same stable atom action, or
to turn a genuine coarsening into the normalized-law obstruction required for
B.
The lift criterion in `proofs/green_atom_rack_lift_criterion.md` packages
that split into one detector group: the atom inner group
`atom_quotient_inner_group(audit)` is multiplied with the lower finite unit
groups, and the endpoint tuple must lie in the product longitude-value
subgroup.  This is the current cleanest formulation of the Green/corridor
A-route.
The most recent local branch work isolates a coordinate-kernel closure
dichotomy and a kernel-corridor audit: equality closure is the nondegenerate
case, while universal closure is the remaining corridor branch to control
symbolically or realize as a normalized-law counterexample.  Product-label
work is separated from this last branch by the new bi-free
universal-corridor target: a final proof must factor all residual motion
through the fixed two-sided Green kernel-block, Schutzenberger, and
atom-inner detector product, together with any fixed quotient, known-branch,
or endpoint/unit detector factors passed as `extra_groups` in the corridor
certificate helpers.  A counterexample must land in that exact verdict and supply a
normalized-law sequence moving explicit residual tuples.  The corridor audit
now closes each elementary coordinate-kernel pair separately, so a genuine
local-minimal corridor candidate cannot hide behind an aggregate kernel
closure: every such elementary pair must already generate the all-universal
admissible family.  The corresponding
side-opposite closure is now theorem-level: if a finite group detects a
solution `X`, the same group detects `X^op=P R P`, because opposite braid
actions are strand-reversed original actions and finite-G longitude identity
is invariant under strand reversal.  This justifies using left and right
detector factors symmetrically in the local program.  The corresponding
subgroup-certificate helper now profiles candidate braid words against those
fixed detector factors and records moved residual tuples, so finite stages of
an A proof or B construction use the same `V_beta(H)` convention.  The local
proof log now also includes a fixed detector-action factorization criterion:
if residual fibre motion is a quotient or readout of the fixed rack detector
action `A_G^n`, then the sharp finite-G kernel implication follows
immediately, with `G` still independent of `n`.  The local
certificate layer now also exposes an exact fixed-index image closure using
the same corridor factor list; on the affine commutator stress row it proves
the `n=2` implication exactly and records that the commutator mover is seen
by the order-`6` symmetric kernel-block factor.  The corridor certificate now
also has a direct-product subgroup audit, so the displayed factor list is
checked against the single finite product detector required by the sharp
obstruction theorem whenever the product is small enough to enumerate.
The local
semigroup bridge now has a unit-holonomy longitude gate: for a finite
transition monoid, only the permutation-unit group can carry residual
permutation motion, and proposed unit labels must lie in the subgroup
generated by recursive Artin-longitude values in that fixed unit group.  This
keeps reset-like observer collapse out of the B route and gives A proofs a
precise subgroup-membership target.  The unit-section criterion packages this
as a branch detector: once a residual section word is proved to live in one
fixed finite monoid and its unit labels lie in `V_beta(U(M))`, identity
finite-`U(M)` longitude data kills the branch.  Its product-detector
companion packages any finite list of such unit groups into one fixed direct
product detector for the sharp obstruction theorem.  The local
endpoint criterion further relaxes this: a proof may show only that the
residual endpoint unit/composite lies in `V_beta(U(M))`, allowing internal
Green or product-label transports to cancel before the detector readout.
The endpoint-product helper then multiplies those endpoint unit groups into
the one fixed finite detector group demanded by the sharp obstruction theorem,
including an explicit endpoint-tuple membership check in that product group.
The local
router now also splits product witnesses into closed finite-G product
subbranches: coboundary telescope, one-colour pairwise cyclic detector, or
genuinely coloured holonomy already covered by a known total branch.  The
product longitude route audit now records, for a fixed product word, whether
the closed labels are explained by a common assignment, by separate
single-longitude witnesses, or only by membership in the longitude-value
subgroup `V_beta(H_prod)`.  This is explicitly diagnostic; the all-`n` target
remains a symbolic subgroup-membership proof or a normalized-law failure.  The
`affine_cyclic` classifier remains an audit tag only: it is not a known-total
detector unless another symbolic all-`n` branch or closed product subbranch
supplies the finite group.  The
first local-minimal cover audit for this certificate now routes all size-2/3
product rows to `product_finite_g_branch` and the six formerly target-shaped
size-3 rows to the known involutive whole-solution branch, so the size-2/3
corpus has no remaining product or corridor target rows.  This remains
narrowing evidence rather than a proof.
The involutive/permutation known branch is now written as a symbolic detector
note: involutive tables are dominated by the two-point trivial rack, while
permutation-form tables use a cyclic detector whose order is that of
`sigma tau`; the pure-longitude formula is locked to the code convention by
regression tests.
The pairwise-linking branch is now likewise centralized as a symbolic
cyclic-detector note: if every residual label is an integer linear function of
the abelian Artin-longitude matrix, the fixed group `C_m`, with `m` divisible
by the relevant finite fibre-permutation orders, gives the required
finite-G implication for all braid indices.
Product-label
work now also has a longitude-value subgroup criterion: closed product labels
must lie in the subgroup generated by all recursive-longitude values in the
fixed product label group, or else they become a sharper B-route target.  The
product branch now also has an exact primitivity certificate: swapped/direct
product-label pair closures close each fibre pair under the finite label
groupoid, so product local-minimality no longer relies on enumerating all
partition families.
swapped product branch is also symbolically closed over nondegenerate
quotient colours: nondegeneracy lifts through the swapped fibre bijections,
so arbitrary-fibre holonomy there is already in the guitar branch.  The
product target is now also gauge-normalized to the actual finite holonomy
groups left after coboundary transport, separating true residual holonomy
from tagged-fibre bookkeeping; the normalized subgroup audit now scans the
smallest arbitrary two-colour/two-point-fibre product corpus, checking
`2,048` nonidentity normalized holonomy rows with no subgroup failures.  The
fixed-degree exact holonomy audit then removes word-length cutoffs on
representative tuples and records a guardrail: raw normalized holonomy alone
misses a known nondegenerate/permutation row, while multiplying by the
expected `S_4` known-branch factor removes the displayed miss.  The
smallest arbitrary product corpus with two colours and two-point fibres now
has an exact subgroup audit with no failures in the bounded three-strand
scan.  The identity-base product subbranch has also been sharpened to an
explicit fibrewise central-label normal form `K_a`, with a fixed cyclic
detector in the nontrivial local-minimal swapped case and identity labels in
the direct case.  The two-colour/fibre-3 product audit now also records the
central router verdict: all `2,064` swapped primitive rows and all `24`
direct primitive rows route to `product_finite_g_branch`, with `0` open
product targets.  A complementary three-colour/fibre-2 product audit solves
the `S_2` product cocycle equations linearly over `F_2`; after the router
recognizes the symbolic fibre-size-two affine subbranch, all `2,472`
primitive rows also route to `product_finite_g_branch`, including the `144`
direct rows that otherwise look like genuinely coloured product holonomy.
Product closed-label tests now include an exact fixed-degree
image audit, removing word-length cutoffs for concrete fixed-tuple detector
checks while keeping the global all-`n` theorem burden explicit.  The exact
audit can use the quotient colour solution as its base condition or a
stronger supplied base detector, matching the sharp-kernel setup with a rack
`Q`.  In the smallest product corpus at braid degree two, the quotient-base
audit has no truncations and no untagged failures; the raw product label
group failures that do appear are all in known nondegenerate/rack rows,
confirming that known-branch detector factors cannot be omitted from the
product theorem.  A regression fixture records one such row: the raw product
label group misses a fixed-degree closed label, while the detector product
with a finite symmetric known-branch factor detects it.

## Current external references

- Will Sawin's MathOverflow question, "Set-theoretic solutions to the
  Yang-Baxter equations and racks" (asked April 7, 2026).
- The linked MathOverflow local obstruction question, "Local branch-choice
  rigidity in Green R-classes of finite set-theoretic Yang-Baxter solutions"
  (asked May 2, 2026).
- Victoria Lebed and Leandro Vendramin, "Homology of left non-degenerate
  set-theoretic solutions to the Yang-Baxter equation", especially the guitar
  map/rack domination result for left non-degenerate solutions.
