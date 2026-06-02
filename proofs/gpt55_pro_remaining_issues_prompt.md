# Self-contained remaining-issues resolution prompt

Date: 2026-06-02

This is a standalone prompt.  Everything needed to understand the current
proof state and the remaining tasks is stated here.  Do not use the internet
or rely on any prior conversation.

## Current Reduced Status

The problem is not resolved by the supplied data.  Outcome A is conditional
on one remaining local existence theorem, and outcome B still lacks a
concrete finite counterexample with a normalized-law obstruction sequence.

The global assembly gap is closed conditionally: if every surviving
post-linear local interval has the U/C/M endpoint observers described below,
then the fixed product detector group `G(pi,Q)` and the sharp rack detector
give finite-rack domination along any finite congruence chain.

Unsupported companion block-image rows are no longer an endpoint seed
obstruction.  In a left triangular row
`T_{a,b}(x,y)=(alpha(x),beta_x(y))`, an unsupported injective-nonsurjective
companion section forces `alpha` injective and `|A_b|<|A_d|`, hence
`|A_a||A_b|<|A_c||A_d|`, contradicting bijectivity of
`T_{a,b}:A_a x A_b -> A_c x A_d`.  The right triangular case is dual with
`delta` and `gamma_y`.  Thus these rows close by the finite
`finite_triangular_bijection_cardinality_contradiction` ledger.  The
post-linear finite-obstruction data must still expose that effective
certificate: the unsupported row keys, proved flag, exact expected and covered
row ledgers, contradiction rows, and contradiction-failure list are present
even when the cardinality certificate closes the branch automatically.

The exact remaining A-side lemma is:

```text
Uniform U/C/M endpoint-observer existence lemma.
```

For every finite local-minimal post-linear coloured YBE interval surviving
the stated reductions, and for every active family `E in {U,C,M}` hit by the
current `K_nabla` seed classifier `kappa`, construct finite,
braid-index-independent observer data

```text
S_E^reach,
H_E or S_mE,
rho_E:Pi_E->Sym(S_E^reach),
W_s,
Gamma^{E,+/-},
exact cutoff readouts where needed,
and residual-faithfulness rows.
```

The data must have exact reachable-state closure, a finite monodromy
representation of the positive local-context presentation, word-potential
coboundary defects that are constant on sound detector domains, inverse
negative rows, exact C/M cutoff readouts when used, family-by-family product
separation, and residual faithfulness for the actual fibre action:

```text
all active routed endpoint channels killed => Delta_n(beta)=1.
```

One routed identity subcase is already closed at the finite-system classifier
level and must not be counted as part of the remaining obstruction.  If the
current `kappa` ledger has a routed System U seed and the local interval is a
strict identity fibre interval, the canonical identity endpoint observer over
the actual current triangular-recovery unit group `U_tri`, together with the
strict-identity residual-faithfulness theorem, closes the system as
`closed_by_triangular_recovery_endpoint_observer_family_build`.  The closure
checks the full `D_Gamma` domain, the current `kappa` entries, the current
`U_tri` finite group-table fingerprint, and leaves no routed U remaining
obligation.  This is only a closed subcase; it is not a proof that arbitrary
non-identity U endpoints admit observers.
The same strict-identity observer also closes strict-identity product
endpoint rows at the main classifier level.  Routed U+C, U+M, C+M, and
U+C+M products close only with the current `U_tri` target for U when U is
present, exact C/M cutoff-readout data when C or M is present, exact family
coverage, and a proved product residual-faithfulness theorem.  These are
family-by-family closures; no cross-family endpoint cancellation is used.
Routed multi-family products U+C, U+M, C+M, and U+C+M are also closed at the
main classifier level for the singleton-fibre, coordinate-identity, supplied
fibre-label identity, and canonical fibre-label identity residual subcases.
In those non-strict closures, U still uses the current `U_tri` finite group
table when present, C and M still use exact cutoff/readout data, and the
product residual theorem must expose the same endpoint-channel reason ledger
and full endpoint-channel key ledger by family as the per-family residual
theorems.  These closures cover only residually trivial non-strict local
motion, not arbitrary nontrivial U/C/M endpoint dynamics.
Any retained family observer build must also expose auxiliary construction
rows that match the retained build internals.  The advertised word-potential
certificate, detector-track initialization rows, endpoint-target audit,
C/M cutoff-readout audit, and residual-faithfulness theorem for a family must
be the same finite objects used inside that family build.  A proof may not
close with a proving build object while displaying stale or different
auxiliary rows as the construction ledger.

The exact missing B-side ingredient is:

```text
One fixed finite YBE solution carrying a routed U/C/M endpoint action
nontrivial on a normalized-law braid sequence invisible to every finite
group.
```

That would require a full `R_X` table, a symbolic YBE proof, explicit
braids `beta_j in B_{q_j}` with `q_j->infinity`, explicit moved tuples in
`X^{q_j}`, and a proof that every finite group has eventually trivial
Artin-longitude data on the sequence.  No such object is supplied here.

Your task is to completely resolve the finite-rack domination problem for
finite bijective set-theoretic Yang-Baxter solutions.  Return exactly one of
the following outcomes if you can prove it:

A. A complete proof of finite-rack domination for every finite bijective
set-theoretic Yang-Baxter solution.

B. An explicit finite bijective set-theoretic Yang-Baxter counterexample not
dominated by any finite rack, together with a normalized-law obstruction
sequence defeating every finite rack.

Do not present a partial argument as a resolution.  If neither A nor B is
complete, state the exact missing lemma or exact missing counterexample
ingredient and the shortest route to settle it.

## 1. Basic Definitions

A finite bijective set-theoretic Yang-Baxter solution is a finite set `X`
with a bijection

```text
R_X : X x X -> X x X
```

satisfying the set-theoretic Yang-Baxter equation on `X^3`:

```text
R_X^{12} R_X^{23} R_X^{12}
=
R_X^{23} R_X^{12} R_X^{23}.
```

This gives a right action of the braid group `B_n` on `X^n`; the braid
generator `sigma_i` acts by applying `R_X` to coordinates `i,i+1` and
leaving all other coordinates unchanged.  Write this action as

```text
rho_{X,n} : B_n -> Sym(X^n).
```

A finite rack is a finite set `Y` with a binary operation `triangleright`
whose left translations are bijective and which satisfies self-distributivity

```text
a triangleright (b triangleright c)
=
(a triangleright b) triangleright (a triangleright c).
```

The associated rack Yang-Baxter solution gives actions
`rho_{Y,n}: B_n -> Sym(Y^n)`.

The finite-rack domination problem is:

```text
For every finite bijective set-theoretic Yang-Baxter solution X,
does there exist one finite rack Y, independent of n, such that

ker rho_{Y,n} <= ker rho_{X,n}

for every braid index n?
```

The rack `Y` is not allowed to depend on `n`.

## 2. Hard Constraints

- Do not give finite-search-only evidence.
- Do not use timeout evidence.
- Do not use a rack, detector group, quotient, or obstruction group that
  depends on braid index `n`.
- A finite computation can be used only as a certificate checker, convention
  audit, example, or counterexample-discovery aid.  Every decisive step must
  become a symbolic all-`n` proof.
- Do not rely on an implicit attachment, codebase, spreadsheet, proof note,
  or external citation.  If a definition, lemma, or certificate is needed,
  state it in the answer.

## 3. Artin-Longitude Detector Framework

Let `F_n` be the free group on generators `x_1,...,x_n`.  The standard Artin
action of `B_n` on `F_n` gives, for every braid `beta`, a permutation
`p_beta in S_n` and recursive Artin longitudes `L_i(beta) in F_n` such that

```text
beta(x_i) = L_i(beta) x_{p_beta(i)} L_i(beta)^-1.
```

For a finite group `G`, define the finite-`G` Artin-longitude data
`Lambda_{G,n}(beta)` to be the complete finite datum of the Artin permutation
`p_beta` together with all evaluations

```text
phi(L_i(beta))
```

over all homomorphisms `phi:F_n->G` and all strands `i`.

For a braid `beta` and finite group `G`, define the longitude-value subgroup

```text
V_beta(G) <= G
```

to be the subgroup generated by all elements `phi(L_i(beta))` as `phi` ranges
over all homomorphisms `F_n->G` and `i` ranges over all strands.  An endpoint
element `h in G` is killed by identity finite-`G` longitude data if one can
prove

```text
h in V_beta(G).
```

For finite abelian `A`, `V_beta(A)` is the subgroup generated by the
abelianized longitude exponent matrix: if `L_i(beta)` has exponent vector
`m_i=(m_{i1},...,m_{in})`, then `V_beta(A)` is generated by the values
`a_1^{m_{i1}} ... a_n^{m_{in}}` over `a_j in A`.

Functoriality guardrails:

- A fixed finite group homomorphism `f:G->H` sends `V_beta(G)` into
  `V_beta(H)`.
- If `f:G->H` is surjective, then `f(V_beta(G))=V_beta(H)`.
- Direct products behave exactly:

```text
V_beta(prod_s G_s) = prod_s V_beta(G_s).
```

Thus finitely many fixed detector factors may be multiplied into one fixed
finite product group without introducing any `n`-dependence.

## 4. Sharp Finite-Group Obstruction Theorem

For a finite group `G`, there is a finite rack detector `A_G` with underlying
finite set

```text
T_2 x (G x G)
```

and rack operation conventionally written

```text
(a,u) triangleright (b,v) = (a b a^-1, a v),
```

where `T_2` is the two-element transposition rack layer and the displayed
formula encodes the standard finite Artin-longitude detector.  The only fact
needed here is the sharp detector consequence:

If, for a finite quotient interval, one constructs a finite group `G`
independent of `n` such that identity finite-`G` Artin-longitude data forces
the residual action to be trivial for every `n`, then multiplying the base
rack by `A_G` gives a finite rack that dominates the interval.

More explicitly, let `pi:X->Z` be a quotient of finite YBE solutions, and
suppose `Z` is already dominated by a finite rack `Q`.  For each `n`, set

```text
N_n = ker rho_{Q,n}.
```

For a quotient-colour tuple `z=(z_1,...,z_n) in Z^n`, let

```text
X_z = prod_i pi^{-1}(z_i).
```

Since every `beta in N_n` fixes `z`, it acts fibrewise on `X_z`; write the
fibre action as

```text
delta_{n,z}: N_n -> Sym(X_z).
```

Bundle all fibre actions into

```text
Delta_n(beta) = (delta_{n,z}(beta))_z.
```

The local finite-group target is:

```text
Find one finite group G=G(pi,Q), independent of n, such that
for every n and beta in N_n,

Lambda_{G,n}(beta) = Lambda_{G,n}(1)  =>  Delta_n(beta)=1.
```

Equivalently, equality of finite-`G` Artin-longitude data for two braids in
`N_n` forces equality of their residual fibre actions.  If this target holds,
then the sharp rack `Q x A_G` dominates the interval.

For a maximal congruence chain

```text
Delta_X = kappa_0 < kappa_1 < ... < kappa_m = Nabla_X,
```

prove the local target for every interval
`X/kappa_i -> X/kappa_{i+1}`.  Then iterating the sharp construction along
the chain gives a final finite rack for `X`.  No factor in this chain may
depend on `n`.

## 5. Local Interval Setup

A local interval over quotient colours `C` consists of finite fibres
`A_c` for `c in C`, a quotient solution

```text
R_C(a,b) = (a dot b, a*b),
```

and local bijections

```text
T_{a,b}: A_a x A_b -> A_{a dot b} x A_{a*b}
```

satisfying the coloured Yang-Baxter equation

```text
T^{12}_{a dot b,(a*b) dot c}
T^{23}_{a*b,c}
T^{12}_{a,b}
=
T^{23}_{a*(b dot c),b*c}
T^{12}_{a,b dot c}
T^{23}_{b,c}.
```

The interval is local-minimal if every admissible fibre congruence family
`theta_c` transported by all local maps is either all equality or all
universal.  Semisplit local-minimality must also be handled: one must not
ignore congruence families that mix equality and universal behaviour across
colours when the local maps allow them.

The current proof program has eliminated many standard branches:

- nondegenerate and guitar branches;
- rack-type, involutive, and permutation-form branches;
- product and swapped-product branches once their fixed product detector
  factors are included;
- principal and transport-state gauge rows;
- finite-linear overlap branches;
- raw nonunit/reset semigroup branches that cannot carry residual
  permutation motion;
- proper intermediate congruence closures, which contradict local
  minimality.

The remaining target is the post-linear nonlinear bottleneck described below.
The label `bi_free_universal_corridor_bottleneck` is only shorthand for the
branch that has survived the listed reductions: the local interval is
coloured-YBE and local-minimal, semisplit congruence families have been ruled
out, the known rack-type/nondegenerate/product/permutation/linear branches
have been routed to fixed detectors, and the remaining coordinate-kernel
closures are universal rather than equality or proper intermediate
quotients.  Do not use the label as an extra theorem.  Its only role here is
to say that the K/U/C/M transition laws below are the remaining finite
state-machine obligations.

## 6. Current Remaining Post-Linear Systems

After the finite-linear overlap reductions, every unresolved primitive
local-minimal bottleneck interval must be routed into one of the following
finite systems.  The names are bookkeeping labels; a final proof must supply
the actual all-`n` mathematics.

### Finite Row Vocabulary

Fix colours `(a,b)`, write

```text
R_C(a,b)=(c,d),
T_{a,b}(x,y)=(u,v) in A_c x A_d.
```

The left coordinate section at `x in A_a` is

```text
L_x^{a,b}: A_b -> A_c,     y |-> pr_1 T_{a,b}(x,y).
```

The pair has a left triangular row when every `L_x^{a,b}` is constant.  In
that case write

```text
T_{a,b}(x,y)=(alpha(x), beta_x(y)),
```

where `alpha:A_a->A_c` is the left constant map and
`beta_x:A_b->A_d` are the left companion sections.  The left opposite
sections are the maps

```text
O_y^{left}: A_a -> A_d,     x |-> beta_x(y).
```

Dually, the right coordinate section at `y in A_b` is

```text
R_y^{a,b}: A_a -> A_d,     x |-> pr_2 T_{a,b}(x,y).
```

The pair has a right triangular row when every `R_y^{a,b}` is constant.  In
that case write

```text
T_{a,b}(x,y)=(gamma_y(x), delta(y)),
```

where `delta:A_b->A_d` is the right constant map,
`gamma_y:A_a->A_c` are the right companion sections, and the right opposite
sections are

```text
O_x^{right}: A_b -> A_c,     y |-> gamma_y(x).
```

For any finite map `f:P->Q`, its kernel kind is:

```text
equality   if every kernel block has size 1,
universal  if there is exactly one kernel block,
proper     otherwise.
```

A section is a unit section when it is bijective.  It is an
injective-nonsurjective section when it is injective but not surjective.  It
is constant when its image has one point.

A left or right triangular row is a Latin-unit triangular row exactly when:

```text
the constant map is bijective,
every companion section is bijective,
every opposite section is bijective.
```

The rack-kink theorem requires these Latin-unit triangular rows for every
relevant colour pair.  System K records the finite places where that all-pairs
Latin condition has not yet been supplied.

When a side is not triangular, its missing-triangular profile is obtained by
inspecting the corresponding coordinate sections (`L_x` for a missing left
triangular row, `R_y` for a missing right triangular row).  The profile
ledger is keyed by `(side,left_color,right_color)` and must be duplicate-free;
if that key is duplicated, even with different section-profile payloads or
explanations, the supplied profile ledger is ambiguous and the raw K row
remains live.  Within each profile row, the section-profile rows must match
the parent side and colour pair and must have duplicate-free fixed inputs; if
a fixed input is duplicated or a section-profile row has the wrong side or
colour pair, the profile is `unclassified_missing_triangular_profile` and the
raw K row remains live.  Each section-profile row must also be an exact
finite-map summary: its rank must equal the number of duplicate-free image
values and the number of kernel blocks, the kernel blocks must be nonempty,
pairwise disjoint, and cover the recorded domain size, and the rank must lie
within the recorded domain and codomain sizes.  If a section-rank row is
internally inexact, the profile is again
`unclassified_missing_triangular_profile` and the raw K row remains live.  A
valid profile has exactly one of the following
explanations:

```text
proper_section_kernel_visible
injective_non_surjective_section
coordinate_side_unit_not_triangular
partial_constant_hidden_rank_loss
nonconstant_hidden_rank_loss
unclassified_missing_triangular_profile
```

The meanings are:

- `proper_section_kernel_visible`: some coordinate section has proper kernel.
- `injective_non_surjective_section`: some coordinate section is injective
  but not surjective.
- `coordinate_side_unit_not_triangular`: every coordinate section on that
  side is bijective, so the side is unit but not triangular.
- `partial_constant_hidden_rank_loss`: after the proper-kernel and
  injective-nonsurjective cases are removed, the nonunit sections are
  constant, at least one unit section exists, and not all sections are
  constant.
- `nonconstant_hidden_rank_loss`: a nonunit hidden section remains but is not
  constant.
- `unclassified_missing_triangular_profile`: none of the finite alternatives
  above was certified.

In the left-rack-base branch,

```text
R_C(a,b)=(a triangleright b, a),
```

the finite cardinality/profile closure eliminates
`injective_non_surjective_section`, `nonconstant_hidden_rank_loss`, and
`unclassified_missing_triangular_profile` once the section-domain and
codomain cardinalities are checked equal and the finite-map trichotomy above
is proved.  These rows are not endpoint systems.

### K/U/C/M Transition Laws

The state machine starts from a raw post-linear K row only after all earlier
branch closures listed in Section 5 have been removed.  A raw K row is a
tuple

```text
((a,b), reason)
```

where `reason` is one of:

```text
no_left_triangular_row
no_right_triangular_row
left_constant_map_proper_kernel
right_constant_map_proper_kernel
left_constant_map_universal_kernel
right_constant_map_universal_kernel
left_companion_sections_injective_non_surjective
right_companion_sections_injective_non_surjective
```

The companion injective-nonsurjective reason is active only when it is
supported by a same-side constant-map kernel reason for the same colour pair.
Without that support it is an earlier structural inconsistency, not a live K
row.

Define `live_k_missing_latin_row_defects` from the raw K tuple by applying
the following transition laws, and leaving a row live whenever the matching
certificate is absent, duplicate-key ambiguous, or fails.

K terminal proper-closure law:

```text
If any triangular constant-map kernel edge or partial-constant missing-row
edge generates a proper admissible congruence closure, and the corresponding
closure-key ledger is duplicate-free, then local-minimality is contradicted.
The branch is terminal:

closed_by_triangular_latin_proper_closure
or
closed_by_missing_triangular_partial_constant_proper_closure.

No U/C/M endpoint obligation is created by a proper closure.

If a closure key is duplicated, even with different generated-congruence
kinds, the supplied closure ledger is ambiguous and cannot close System K or
route the row to U/C/M.
```

K-to-U recovery law:

```text
A constant-map kernel reason routes to System U only for the universal
closure rows.  For each constant-map kernel edge on that side and colour
pair:

1. the generated admissible closure of the collapsed input pair is universal,
   with a duplicate-free triangular closure key ledger;
2. the triangular recovery inverse table is bijective on the relevant
   triangular row;
3. the recovery table separates the two collapsed inputs by output pairs,
   meaning the recovered left input (left case) or recovered right input
   (right case) distinguishes the collapsed pair;
4. the recovery-route key
   (side, colour pair, domain colour, collapsed input pair, closure kind)
   is duplicate-free in the supplied route ledger.

If all universal constant-map kernel edges for that side and pair satisfy
these checks, remove the corresponding constant-map reason from live K and
record it in recovery_routed_k_missing_latin_row_defects.
```

The same K-to-U recovery law removes a supported companion
injective-nonsurjective reason only when its supporting same-side constant-map
kernel reason has been routed by the recovery table.  Other reasons for the
same colour pair remain live.

K-to-C partial-constant law:

```text
A no-triangular row with profile partial_constant_hidden_rank_loss is
examined through its constant nonunit sections.  For a left missing row,
if L_x is constant on distinct inputs y0,y1, write

T_{a,b}(x,y_i)=(u,v_i).

Bijectivity forces v0 != v1, and at least one v_i differs from x in the
continuing fibre.  That gives a continuation seed x ~ v_i.  The right-side
case is dual.

The row routes to System C only when every relevant partial-constant edge has:

1. universal generated admissible closure for the collapsed input pair, with a
   duplicate-free partial-constant closure key ledger;
2. a supplied continuation route keyed to the same side, colour pair, fixed
   input, domain colour, collapsed input pair, and closure kind, with no
   duplicate route key;
3. distinct companion outputs;
4. at least one continuation seed witness;
5. a universal continuation-seed generated closure among those witnesses;
6. the original partial-constant collapsed edge contained in that seed
   closure.

If the partial-constant closure row is nonuniversal, if a closure key is
duplicated, if the supplied route does not match that closure row including
closure kind, if a route key is duplicated, if the route reaches only a
nonuniversal continuation-seed closure, or if any listed check fails, the
original no-triangular row remains live in System K.
```

K-to-M coordinate-unit law:

```text
A no-triangular row with profile coordinate_side_unit_not_triangular is
grouped by colour pair.  The coordinate-unit routing certificate must include
the coloured-YBE premise.  Its listed coordinate-unit sides must be nonempty,
duplicate-free, drawn from `{left,right}`, must have matching
`coordinate_side_unit_not_triangular` explanations, and must actually be unit
sides in the supplied section data.  The route-row ledger itself must also be
duplicate-free.

For each grouped pair:

1. if both coordinate sides are unit, the row is a two-sided-unit pair and
   closes only when the global locally-nondegenerate/guitar branch has been
   proved for the whole interval;
2. if the opposite coordinate side has nonunit data, the row is a mixed-unit
   context row and routes to System M;
3. if the listed side is not actually unit, if a listed side is duplicated,
   if a route row is duplicated, if its explanation does not match the
   coordinate-unit profile, or if neither row alternative is certified, the
   row remains live in System K.

The coordinate-unit routing ledger proves only when there are no unrouted
coordinate-unit rows, no unclosed two-sided-unit rows, and at least one
coordinate-unit row is present.  An empty or duplicate coordinate-unit routing
ledger is not a proof.
```

### Universal-K Row Normal Forms And Seed Classifier

The transition laws above must be converted into an explicit finite domain
before any signed endpoint generator can be addressed.  This subsection is
that domain.

For a finite interval `I=(C,(A_c),R_C,T)`, an admissible fibre congruence is a
family `theta=(theta_c)_{c in C}` of equivalence relations on the finite
fibres such that whenever

```text
x0 theta_a x1,     y0 theta_b y1,
T_{a,b}(x_i,y_i)=(u_i,v_i),
R_C(a,b)=(c,d),
```

then

```text
u0 theta_c u1,
v0 theta_d v1,
```

and the same condition holds after applying the inverse bijection
`T_{a,b}^{-1}`.  For a seed edge `e=(p0,p1)` in one fibre, write
`<e>_adm` for the least admissible fibre congruence containing that edge.
Its kind is:

```text
equality     if every block in every active fibre is a singleton,
universal    if every active fibre has one block,
proper       otherwise.
```

Here an active fibre is any fibre used by the local interval after the
standard reductions in Section 5; semisplit equality/universal mixtures are
not ignored.

Use side symbols `L` and `R`, with `side_name(L)=left`,
`side_name(R)=right`, `coord_L=L_x`, `coord_R=R_y`, `const_L=alpha`,
`const_R=delta`, `comp_L=beta_x`, and `comp_R=gamma_y` as defined in the
finite row vocabulary.  A universal-K row descriptor is a finite tuple

```text
d = (a,b,lambda,rho,xi),
lambda in {L,R},
```

where `rho` is one of:

```text
constant_map_kernel
supported_companion_block_image
partial_constant_hidden_rank_loss
coordinate_side_unit_not_triangular
unsupported_companion_block_image
```

and `xi` is the finite witness data below.  The descriptor is always read
directly from `T_{a,b}` and its coordinate projections.

Constant-map kernel descriptor:

```text
lambda = L:
  LeftTri(a,b) holds.
  xi=(domain_color=a, collapsed_inputs=(x0,x1), kernel_kind, closure_kind,
      recovery_witness_table).
  x0 != x1 and alpha(x0)=alpha(x1).
  kernel_kind is the kernel kind of alpha.
  closure_kind is the kind of <(x0,x1)>_adm.

lambda = R:
  RightTri(a,b) holds.
  xi=(domain_color=b, collapsed_inputs=(y0,y1), kernel_kind, closure_kind,
      recovery_witness_table).
  y0 != y1 and delta(y0)=delta(y1).
  kernel_kind is the kernel kind of delta.
  closure_kind is the kind of <(y0,y1)>_adm.
```

It is a universal-K seed only when `closure_kind=universal` and the
triangular recovery witness table is present, bijective, and separates both
collapsed inputs.  If `closure_kind=proper`, local-minimality is contradicted
and no endpoint seed is produced.  If `closure_kind=equality` or the recovery
separation is absent, the row stays live in System K.

Supported companion block-image descriptor:

```text
lambda = L:
  LeftTri(a,b) holds and some left companion section beta_x is injective
  but not surjective.
  xi names a same-side constant-map kernel descriptor
  (a,b,L,constant_map_kernel,xi0) for the same colour pair.

lambda = R:
  RightTri(a,b) holds and some right companion section gamma_y is injective
  but not surjective.
  xi names a same-side constant-map kernel descriptor
  (a,b,R,constant_map_kernel,xi0) for the same colour pair.
```

This descriptor is a universal-K seed exactly when the named support
descriptor is a universal-K seed.  It uses the same recovery route and the
System U companion defect-reason state for that side and colour pair.  If no
same-side constant-map kernel support exists, the descriptor has reason
`unsupported_companion_block_image` and is a structural inconsistency, not a
member of `K_nabla`.

This exclusion is now closed by a finite cardinality contradiction.  For
every unsupported companion block-image row, the finite
structural-contradiction certificate has an exact expected row ledger

```text
(side,left_color,right_color)
```

for all unsupported companion block-image rows, an exact covered-row ledger
with no missing, extra, or duplicate rows, and the contradiction row

```text
already_closed_branch:
  (side,left_color,right_color,
   closed_branch = finite_triangular_bijection_cardinality_contradiction)
```

The proof is: in the left triangular case
`T_{a,b}(x,y)=(alpha(x),beta_x(y))`, an unsupported injective
nonsurjective companion section gives `|A_b|<|A_d|`, while absence of
same-side constant-map kernel support makes `alpha` injective, so
`|A_a|<=|A_c|`; hence `|A_a||A_b|<|A_c||A_d|`, contradicting bijectivity of
`T_{a,b}:A_a x A_b -> A_c x A_d`.  The right triangular case is dual:
unsupported injective nonsurjectivity of some `gamma_y:A_a->A_c` gives
`|A_a|<|A_c|`, while injectivity of `delta` gives `|A_b|<=|A_d|`, again
contradicting bijectivity.  Thus unsupported companion rows are structural
contradictions, not endpoint seeds and not members of `K_nabla`.

Partial-constant hidden-rank descriptor:

```text
lambda = L:
  LeftTri(a,b) fails.
  The left missing-triangular profile is
  partial_constant_hidden_rank_loss.
  xi=(fixed_input=x, domain_color=b, collapsed_inputs=(y0,y1),
      companion_output_color=d, companion_outputs=(v0,v1),
      closure_kind, continuation_seed_witnesses,
      continuation_seed_closure_kinds,
      partial_edge_contained_in_seed_closure).
  y0 != y1, L_x(y0)=L_x(y1), and
  T_{a,b}(x,y_i)=(u,v_i).

lambda = R:
  RightTri(a,b) fails.
  The right missing-triangular profile is
  partial_constant_hidden_rank_loss.
  xi=(fixed_input=y, domain_color=a, collapsed_inputs=(x0,x1),
      companion_output_color=c, companion_outputs=(u0,u1),
      closure_kind, continuation_seed_witnesses,
      continuation_seed_closure_kinds,
      partial_edge_contained_in_seed_closure).
  x0 != x1, R_y(x0)=R_y(x1), and
  T_{a,b}(x_i,y)=(u_i,v).
```

It is a universal-K seed only when:

```text
closure_kind=universal,
companion_outputs are distinct,
continuation_seed_witnesses is nonempty,
universal is among continuation_seed_closure_kinds,
partial_edge_contained_in_seed_closure is true.
```

If `closure_kind=proper`, local-minimality is contradicted and no endpoint
seed is produced.  If `closure_kind=equality`, if the continuation seed
closure is nonuniversal, or if any listed check fails, the no-triangular row
stays live in System K.

Coordinate-unit descriptor:

```text
lambda = L:
  LeftTri(a,b) fails.
  The left missing-triangular profile is
  coordinate_side_unit_not_triangular.
  Every left coordinate section L_x is bijective.
  xi contains the left and right section-profile rows, the listed unit side
  L, and the coloured-YBE premise.

lambda = R:
  RightTri(a,b) fails.
  The right missing-triangular profile is
  coordinate_side_unit_not_triangular.
  Every right coordinate section R_y is bijective.
  xi contains the left and right section-profile rows, the listed unit side
  R, and the coloured-YBE premise.
```

It is a universal-K seed only in the mixed-unit case: the listed side is
really unit, the opposite side has nonunit section data, the row is not a
two-sided-unit pair, and the coloured-YBE premise is present.  If both sides
are unit, the row belongs to the two-sided nondegenerate/guitar branch and
closes only when that branch is proved.  If the side listing, explanation,
unit condition, or coloured-YBE premise fails, the row stays live in System K.

Now define `K_nabla` to be the finite set of all descriptors
`d=(a,b,lambda,rho,xi)` satisfying exactly one of the four universal seed
conditions:

```text
constant_map_kernel universal-K seed,
supported_companion_block_image whose support is a constant_map_kernel
  universal-K seed,
partial_constant_hidden_rank_loss universal-K seed,
coordinate_side_unit_not_triangular mixed-unit universal-K seed.
```

Proper-closure descriptors, equality-closure descriptors, failed-route
descriptors, two-sided-unit descriptors, and unsupported companion
descriptors are excluded from `K_nabla`; they are respectively terminal,
still live in K, routed to the nondegenerate/guitar branch, or structural.

The seed state spaces are finite:

```text
S_U =
  { (a,b,reason) :
      reason in {left_constant_map_proper_kernel,
                 right_constant_map_proper_kernel,
                 left_constant_map_universal_kernel,
                 right_constant_map_universal_kernel,
                 left_companion_sections_injective_non_surjective,
                 right_companion_sections_injective_non_surjective}
      and the corresponding recovery descriptor is in K_nabla }.

S_C =
  { (a,b,side_name(lambda),fixed_input,domain_color,collapsed_inputs,
     companion_output_color,companion_outputs) :
      the corresponding partial-constant descriptor is in K_nabla }.

S_M =
  { (a,b,side_name(lambda)) :
      the corresponding coordinate-unit mixed descriptor is in K_nabla }.
```

The seed classifier is the total finite map

```text
kappa : K_nabla -> ({U} x S_U) union ({C} x S_C) union ({M} x S_M)
```

defined by:

```text
kappa(a,b,L,constant_map_kernel,xi)
  = (U,(a,b,left_constant_map_proper_kernel)) if the constant-map kernel
    kind is proper, and
  = (U,(a,b,left_constant_map_universal_kernel)) if the constant-map kernel
    kind is universal.

kappa(a,b,R,constant_map_kernel,xi)
  = (U,(a,b,right_constant_map_proper_kernel)) if the constant-map kernel
    kind is proper, and
  = (U,(a,b,right_constant_map_universal_kernel)) if the constant-map kernel
    kind is universal.

kappa(a,b,L,supported_companion_block_image,xi)
  = (U,(a,b,left_companion_sections_injective_non_surjective)).

kappa(a,b,R,supported_companion_block_image,xi)
  = (U,(a,b,right_companion_sections_injective_non_surjective)).

kappa(a,b,lambda,partial_constant_hidden_rank_loss,xi)
  = (C,(a,b,side_name(lambda),fixed_input,domain_color,collapsed_inputs,
        companion_output_color,companion_outputs)).

kappa(a,b,lambda,coordinate_side_unit_not_triangular,xi)
  = (M,(a,b,side_name(lambda))).
```

The values `fixed_input`, `domain_color`, `collapsed_inputs`,
`companion_output_color`, and `companion_outputs` in the C line are read from
`xi`.  This map is the routing-domain table required before signed endpoint
generators can be written.  After `kappa(d)=(E,s)` is known, and only then,
the remaining signed generator table has addressable entries

```text
Gamma^{E,+/-}_{a,b}(s,x,y) = (s',x',y',h),
```

where `(x',y')=T_{a,b}^{+/-}(x,y)`.

### Signed Endpoint Generator Tables

This is the uniform finite monodromy-coboundary endpoint-observer and
residual-faithfulness lemma.  It is now the first decisive A-side missing
object after the `K_nabla` and `kappa` layer.

For every endpoint family `E in {U,C,M}`, define the initial routed seed set

```text
S_E^0 = { s in S_E : kappa(d)=(E,s) for some d in K_nabla }.
```

The missing endpoint lemma must first construct a finite reachable state set

```text
S_E^reach superset S_E^0.
```

This set must be exact: it is the least closure of `S_E^0` under the signed
transition rows that are actually supplied.  Equivalently, start with
`S_E^0`; whenever a row

```text
Gamma^{E,epsilon}_{a,b}(s,x,y)=(s',x',y',h)
```

has `s` already in the closure, add `s'`; iterate to a fixed point.  The
result must be exactly `S_E^reach`.  A declared state outside this transition
closure is an extra endpoint channel, and a transition target outside
`S_E^reach` is a missing reachable state.  The reachable-state ledger must be
duplicate-free; exactness is not proved by silently converting a repeated list
of states into a set.

The classifier `kappa` used to seed the signed tables must also be a
function on `K_nabla`: no row descriptor may appear twice, and no descriptor
may be assigned to two different endpoint-family/state targets.  A
conflicting or duplicate classifier ledger is not a usable seed map for the
signed endpoint layer.  Every classifier target and every reachable-state
family must lie in the fixed set `{U,C,M}`; introducing a fourth bookkeeping
family does not close a routed endpoint obligation.

Let `H_E` be the fixed finite endpoint group for that family, or let `S_mE`
be the fixed symmetric cutoff group in a cutoff proof.  The group must be
finite and independent of braid index `n`.

The fixed endpoint target itself must be certified family-by-family.  For
the routed families

```text
F = { E : S_E^0 is nonempty },
```

the certificate must list exactly the expected families `F`, exactly the
covered families, and for each covered family at least one fixed finite
target: either a finite endpoint group order or a symmetric cutoff degree.
It must also prove that these targets are independent of braid index and that
product endpoint families are separated componentwise.  A bare assertion
that an endpoint target is fixed is not a certificate; if the target list
omits a routed family, includes an unrouted family, has a nonpositive or
noninteger order or cutoff degree, uses a boolean as a size, uses a family
outside `{U,C,M}`, repeats a family, assigns both a group target and cutoff
target to the same family, depends on `n`, or allows cross-family
cancellation, the signed endpoint layer remains open.  A supplied endpoint
group table is not an implicit endpoint-target certificate, even when only
one routed family is active.  The group table is used to check finite
multiplication and label identities; the target ledger is separate finite
data proving exact family coverage, braid-index independence, and
componentwise product separation.
When two or more of U/C/M are active, product-family separation must still be
certified by that explicit target ledger; otherwise the certificate could
hide cross-family cancellation in one undifferentiated group.
If a fixed endpoint group is declared as a product over more than one
endpoint family, the certificate must also prove row-level family support:
an emitted label from family `E` has identity components in every endpoint
group factor belonging to a different active family.  Equivalently, the
certificate may give explicit finite projection/homomorphism tables proving
that each row lands in its own family factor and that
`V_beta(prod_E H_E)=prod_E V_beta(H_E)` kills the factors separately.  A
nonidentity off-family component is an unclosed product-family separation
failure, even if the total product group order matches the listed factor
orders.
The concrete product group must also have the declared coordinate factors.
For target rows `(E_1,m_1),...,(E_t,m_t)`, every group element must be a
tuple of length `t`; coordinate `j` must have exactly `m_j` distinct values;
the element set must be the full Cartesian product of the coordinate
supports; and multiplication in coordinate `j` must be determined only by the
two coordinate-`j` inputs.  A product with swapped factor coordinates, a
diagonal subgroup, or an entangled tuple multiplication is not a
family-separated endpoint target even if its total order is
`m_1...m_t` and every emitted label has identity off-family coordinates.
Endpoint-target braid-index independence and product-family separation must
be explicit finite target certificates, and the per-family target ledger must
support them through positive fixed group orders or cutoff degrees, exact
family coverage, and duplicate-free one-target-per-family rows.  A
well-formed size ledger without those explicit assertions remains open, and
the assertions alone remain nondecisive without the finite target rows.
Each target size row must be a positive integer attached to a known endpoint
family.  Strings, booleans, missing values, zero, and negative values are
malformed endpoint-target rows, not finite detector factors.
Each endpoint target-size row must also have exactly two fields,
`(family, size)`.  A non-sequence target-size ledger, or a row with an extra
field, a missing field, or a non-tuple shape, is a malformed endpoint-target
row even if one can read a plausible family and size from it.
The `family` field in every endpoint target-size row must be a hashable known
endpoint family in `{U,C,M}`.  Unknown or unhashable family labels in either
the expected/covered endpoint-target ledgers or the target-size rows are
certificate failures, not implicit endpoint factors.
For C or M routed through a symmetric cutoff, the target ledger's cutoff
degree must equal the symmetric degree used by the cutoff-readout table for
that same family.  A certificate that declares a degree-`m` cutoff target but
uses readout permutations in `S_k` with `k != m` has not connected the
declared endpoint target to the residual readout that is supposed to kill it.
In addition, a cutoff-routed family may not emit a nonidentity label in the
endpoint-group coordinate of the signed generator row.  Such a label is an
extra endpoint channel outside the symmetric cutoff readout, so the cutoff
certificate has not covered exactly the routed ledger.  Every signed row
whose family is listed by a cutoff-degree target must have identity
endpoint-group emission; the only nontrivial cutoff motion may appear in the
faithful readout into the declared `S_m`.

If a symmetric endpoint-family fork is used as a cutoff route, it must also
be finite-row backed.  For endpoint factor orders

```text
|H_1|,...,|H_t|,
```

the certificate must include one row for every factor index:

```text
(factor_index, endpoint_group_order, endpoint_witness_supplied,
 faithful_readout).
```

The factor rows must cover exactly the listed endpoint factors, with no
missing, extra, or duplicate indices and no order mismatch.  The cutoff
requires every factor row to have an endpoint witness, and family faithfulness
is the conjunction of the row faithful-readout entries.  A boolean assertion
that all endpoint witnesses are supplied or that the endpoint family is
faithful is not a certificate without these finite rows.

If the symmetric fork is used on the B side as an endpoint-family symmetric
seed, the attachment must also be finite-row backed.  The seed row must list
the symmetric degree, endpoint channel value, endpoint identity, residual
input tuple, and residual output tuple.  It proves a B-side seed only when
the endpoint value is nonidentity, the residual input/output tuple is moved,
and those tuples match the stabilized fibre tuple and stabilized image in the
local normalized-law prefix row.  A boolean assertion that an endpoint
channel is nonidentity or that the endpoint miss matches residual motion is
not a certificate.

The smaller endpoint-observer object is a finite
monodromy-coboundary-faithfulness certificate.  For each active endpoint
family `E`, let the positive local context set be

```text
R = { r=(a,b,x,y) : a,b in C, x in A_a, y in A_b }.
```

Write `T_{a,b}(x,y)=(u,v)` and introduce a formal generator `g_r` for every
positive context `r`.  For every compatible local triple
`(a,b,c;x,y,z)`, compute the three contexts on the positive `121` path and
the three contexts on the positive `212` path.  Add the adjacent relation

```text
g_{r_3} g_{r_2} g_{r_1}
=
g_{r'_3} g_{r'_2} g_{r'_1}.
```

For every nontrivial disjoint pair of positive contexts add the far relation

```text
g_r g_{r'} = g_{r'} g_r.
```

The case `r=r'` is a tautological self-swap and should be omitted from the
finite relation ledger.  The resulting finitely presented endpoint monodromy
group `Pi_E` may be infinite; the certificate only needs a finite permutation representation

```text
rho_E: Pi_E -> Sym(S_E^reach).
```

Equivalently, for each context `r` the certificate gives a permutation
`F^E_r` of `S_E^reach`, and these permutations satisfy all adjacent and far
relations above.  The positive endpoint state update is then `s'=F^E_r(s)`.
Thus the endpoint state table is not arbitrary: it is exactly a finite
representation of the routed local monodromy presentation on the exact
reachable seed states hit from `kappa(K_nabla)`.

The emitted endpoint labels are likewise not primitive data.  Given a fixed
endpoint group `H_E` and word potentials `W_s`, define for every context `r`
and reachable state `s` the nonabelian coboundary defect

```text
D^E_{r,s}(U,M)
=
W_s(U)^-1 W_{F^E_r(s)}(A_r^+(U,M)).
```

Here `A_r^+` is the positive Artin detector substitution for that local
context, `U` denotes current evaluated longitude variables, and `M` denotes
the fixed carrier labels from detector-track initialization.  The defect must
be constant on a sound finite detector-variable domain.  The safest sound
domain is the full finite set `H_E^V`, where `V` is the finite variable
support of `D^E_{r,s}`; a smaller domain is valid only with a proof that all
reachable detector values lie in it.  If the defect is constant, its value
is the forced emission

```text
eta^E_r(s)=h^E_{r,s}.
```

The positive row is then

```text
Gamma^{E,+}_{a,b}(s,x,y)
=
(F^E_r(s), T_{a,b}(x,y), eta^E_r(s)),
```

and the negative row is forced by inversion.  A certificate that chooses
endpoint emissions first and later searches for word-potential witnesses is
not the reduced object; the emissions must be exactly the constant
coboundary-defect values.

With those target data fixed, a signed endpoint generator table is a finite
table

```text
Gamma^{E,epsilon}_{a,b}(s,x,y) = (s',x',y',h),
epsilon in {+1,-1},
s,s' in S_E^reach,
x in A_a,
y in A_b,
h in H_E.
```

For `epsilon=+1`, if `R_C(a,b)=(c,d)`, the coordinate part must satisfy

```text
(x',y') = T_{a,b}(x,y) in A_c x A_d.
```

For `epsilon=-1`, the input colours are already the output colours of a
positive row.  The coordinate part must satisfy

```text
T_{a,b}(x',y')=(x,y),
```

with the corresponding inverse colour routing.  Thus `Gamma^-` is indexed by
the inverse local row data, not by an unrelated table.

The exact signed-generator domain for the routed K layer is the finite set
derived from the interval fibres and reachable states:

```text
D_Gamma =
{ (E,epsilon,s,a,b,x,y) :
  s in S_E^reach,
  S_E^reach is exactly the signed-transition closure of S_E^0,
  epsilon in {+1,-1},
  x in A_a,
  y in A_b,
  and the local row T^{epsilon}_{a,b} is defined }.
```

Every entry of `D_Gamma` must have exactly one table value and no extra table
value outside `D_Gamma` may be used to close a routed endpoint family.  The
signed table must be checked against the actual `kappa` table for the
interval; a table built for a different seed classifier is irrelevant.  A
certificate must enumerate this derived full entry domain `D_Gamma`, not a
prover-selected subdomain and not merely one entry per seed and sign.
Covering both signs for a seed while omitting some local input `(a,b,x,y)` is
still an incomplete signed table.
The current `K_nabla` and `kappa` data must be computed first, and the signed
endpoint audit must then be derived against that current classifier; an
endpoint table whose seed keys come from any other classifier does not address
the interval.  If the reachable state set is not supplied independently, it
must be derived as the least transition closure of the current `kappa` seeds
under the supplied signed rows, and the full `D_Gamma` domain must then be
formed over that derived closure.

The finite audit must derive these domain and identity checks from the
interval data, the reachable closure, the supplied rows, the endpoint group
or cutoff target, and the row witnesses.  Unbacked boolean assertions such as
"coordinate components verified" or "YBE cocycle verified" are not
certificates unless accompanied by the finite table evaluation that proves
the assertion.  The full entry domain itself must be marked as derived from
the interval fibres and reachable states; a prover-selected `D_Gamma`
subdomain is not a certificate even if all supplied rows satisfy the local
identities on that smaller domain.  A checker receiving an already-built
audit must recompute `D_Gamma` from the current interval and current
reachable closure and compare it with the audit's required-entry ledger; a
bare flag saying "derived from interval" is not enough.  The checker must
also recompute the coordinate, inverse-pairing, inverse-cancellation,
positive state/coordinate YBE, and far state/coordinate commutativity checks
against the current interval table and supplied endpoint group.  An
already-built audit whose booleans say those checks passed is still stale or
irrelevant if these recomputed current-interval row checks fail.  The finite
row checks themselves must be marked as derived from the supplied signed rows,
actual interval table, endpoint group or cutoff multiplication, and explicit
detector-lift data; manually asserted success flags for coordinate
compatibility, inverse-derived negatives, positive state/coordinate YBE,
state/coordinate far-commutativity, rowwise longitude diagnostics, or
telescoping detector data are not certificates.  If a derived check fails,
the certificate must report the actual failed rows or local triples, not only
a failed boolean.  For group-valued signed rows, inverse cancellation requires
the actual finite endpoint group multiplication table.  The adjacent-YBE and
far-commutativity label products may still be recorded as diagnostics, but
they are not independent closure gates once the word-potential detector lift
is proved: the potential-implies-cocycle argument below derives those label
relations from the state/coordinate braid relations.  A signed endpoint audit
with success booleans but no concrete endpoint group is not a finite row-check
certificate, even if an endpoint target order is listed.
For a retained family observer build, the top-level auxiliary ledgers are part
of the certificate, not optional commentary.  The proof must verify that the
supplied word-potential certificate row equals the build's internal
word-potential certificate, that the supplied detector-track initialization
rows equal the build's internal detector rows family-by-family, that the
supplied endpoint-target row equals the build's endpoint-target audit, that
any C/M cutoff-readout row equals the build's cutoff-readout audit, and that
the supplied residual-faithfulness theorem row equals the build's retained
residual theorem.  A stale auxiliary row leaves the observer family open even
if the retained build object itself proves.
Every supplied signed row must also have a well-formed full `D_Gamma` entry
key `(E,epsilon,s,a,b,x,y)`: `E` must be one of U,C,M, the sign must be `+1`
or `-1`, the seed state must be a hashable tuple state, and the local
colour/fibre inputs must be in the derived domain.  Missing, extra,
duplicate, malformed, or unhashable signed rows are finite certificate
failures.  They must not cause a runtime failure in seed-key, entry-domain,
or monodromy-permutation checks, and they must not be treated as hidden valid
observer states.
Moreover, the concrete endpoint group used for signed-row multiplication must
match the group-valued target ledger: its order must equal the product of the
listed endpoint-group orders for the active group-targeted families.  Symmetric
cutoff degrees are checked by the cutoff-readout certificate and are not
silently folded into this group order.  If the group table has a different
order from the group-valued target product, the certificate has not connected
its endpoint labels to the declared fixed target.
For a routed U family, the post-linear wrapper must do the stronger current
target check: it recomputes the triangular-recovery unit group `U_tri` from
the current endpoint interval and compares the full finite group-table
fingerprint, including elements, identity, inverses, and multiplication.  A
same-order finite group with a different concrete table is diagnostic only;
it may prove an internally coherent signed table but it does not close the
current U obligation.

Every supplied row must also pass the coordinate-component check against the
actual interval table: positive rows must have `(x',y')=T_{a,b}(x,y)`, and
negative rows over colours `(c,d)` must use the unique source colour pair
`(a,b)` with `R_C(a,b)=(c,d)` and satisfy `T_{a,b}(x',y')=(x,y)`.

Before the endpoint-group inverse equation is checked, the signed rows must
also pass the structural inverse-pairing check.  Every positive entry

```text
Gamma^{E,+}_{a,b}(s,x,y)=(s1,u,v,h)
```

with `R_C(a,b)=(c,d)` must have the opposite-sign entry

```text
Gamma^{E,-}_{c,d}(s1,u,v)=(s,x,y,h2).
```

Dually, every negative entry

```text
Gamma^{E,-}_{c,d}(s,u,v)=(s1,x,y,k)
```

with source colours `(a,b)` satisfying `R_C(a,b)=(c,d)` must have

```text
Gamma^{E,+}_{a,b}(s1,x,y)=(s,u,v,k2).
```

This inverse-pairing check is finite and only concerns the existence of the
opposite row and the return of the endpoint state and fibre inputs.  The
separate cancellation check below then proves the label identities in the
fixed endpoint group or cutoff group.

The signed inverse-cancellation law is:

```text
If Gamma^{E,+}_{a,b}(s,x,y)=(s1,u,v,h)
and Gamma^{E,-}_{c,d}(s1,u,v)=(s2,x2,y2,h2),
where R_C(a,b)=(c,d),
then s2=s, x2=x, y2=y, and h h2 = 1 in H_E.

If Gamma^{E,-}_{c,d}(s,u,v)=(s1,x,y,k)
and Gamma^{E,+}_{a,b}(s1,x,y)=(s2,u2,v2,k2),
where R_C(a,b)=(c,d),
then s2=s, u2=u, v2=v, and k k2 = 1 in H_E.
```

The multiplication table of `H_E`, or the corresponding finite cutoff target,
must be supplied so these label products are directly evaluated for every
signed row pair.

The positive local endpoint YBE state/coordinate law is the equality of the
two three-strand table paths obtained from the coloured YBE square.  Starting
from `(s,x,y,z)` over colours `(a,b,c)`, compose the three positive entries
on the left side:

```text
Gamma^{E,+}_{a,b},
Gamma^{E,+}_{a*b,c},
Gamma^{E,+}_{a dot b,(a*b) dot c},
```

with the updated colours, states, and coordinates after each step.  Compose
the three positive entries on the right side:

```text
Gamma^{E,+}_{b,c},
Gamma^{E,+}_{a,b dot c},
Gamma^{E,+}_{a*(b dot c),b*c}.
```

The positive-YBE path check must prove that every row used in both `121` and
`212` paths is present and that the final endpoint state and final three
fibre coordinates agree.  This check ranges over all `s in S_E^reach` and all
local triples `(x,y,z)`.  The ordered products of the three endpoint labels
may be recorded as diagnostics, but after a valid word-potential certificate
is supplied the label equality follows automatically from the path equality
and the Artin braid relation.

The signed endpoint observer must also satisfy state/coordinate
far-commutativity for disjoint crossings.  For every pair of positions with
`|i-j|>1`, every sign pair `epsilon,delta in {+1,-1}`, every compatible
four-strand colour/fibre tuple, and every reachable endpoint state, the two
paths

```text
Gamma_i^epsilon Gamma_j^delta
and
Gamma_j^delta Gamma_i^epsilon
```

must use defined rows and must have the same terminal endpoint state, the
same terminal colour/fibre tuple.  The ordered products of emitted labels in
the endpoint group or cutoff target may be recorded as diagnostics, but they
are not separate closure obligations once the word-potential certificate is
proved.  Equivalently, the endpoint observer must respect the braid
presentation at the state/coordinate level, not only one adjacent
Yang-Baxter square.  If negative rows are proved to be genuine inverses, it is
enough to derive the signed far-commutativity variants from positive
state/coordinate far-commutativity and inverse cancellation, but the proof
must still contain some explicit finite far-commutativity path gate.  Without
it, endpoint accumulation may depend on the chosen braid word.

Potential-implies-cocycle lemma.  Write a positive endpoint row as

```text
Gamma_i^+(q)=(tau_i(q),h_i(q)),
q=(s, fibre tuple).
```

Assume every positive row satisfies the word-potential identity

```text
W_{tau_i(q)}(A_i(U,M)) = W_s(U) h_i(q).
```

Here `A_i` is the Artin detector substitution and `M` is the fixed carrier
data from detector-track initialization.  For any positive word `w=i_1...i_m`,
induction gives

```text
W_{tau_w(q)}(A_w(U,M)) = W_s(U) h_w(q),
```

where `h_w(q)` is the ordered product of emitted labels along the word.  If
two positive words have the same state/coordinate map and the same Artin
substitution, their left sides are equal, so cancellation in `H_E` gives the
same endpoint-label product.  Therefore adjacent label YBE and far label
commutativity follow from the word-potential identity plus the positive
state/coordinate braid relations.  If negative rows are defined as actual
inverses of positive rows, signed label cancellation follows as well.

The rowwise signed two-strand Artin-longitude identity is not a decisive
closure condition.  Under the fixed Artin convention

```text
sigma_1(x_1)=x_1 x_2 x_1^-1,
sigma_1(x_2)=x_1,
```

the recursive longitudes satisfy

```text
L_1(sigma_1)=x_1,
L_2(sigma_1)=1,
L_1(sigma_1^-1)=1,
L_2(sigma_1^-1)=x_2^-1.
```

Thus for any finite group `H` and any emitted label `h in H`, the positive
row identity is satisfied by the homomorphism `phi(x_1)=h, phi(x_2)=1`, and
the negative row identity is satisfied by `phi(x_1)=1, phi(x_2)=h^-1`.  A
certificate that only lists

```text
h = product_r phi_r(L_{j_r}(sigma_1^epsilon))^{delta_r}
```

for each local row is therefore only a row-shape diagnostic.  It does not
prove that the accumulated endpoint over an arbitrary braid word lies in
`V_beta(H_E)`.

The decisive replacement is a finite word-potential detector-lift
certificate.  For a finite group `H`, braid index `n`, and a homomorphism
`phi:F_n->H`, write `a_i=phi(x_i)`.  For a braid prefix `beta_t`, let

```text
p_t=p_{beta_t},
u_i(t)=phi(L_i(beta_t)).
```

Initially `p_0=id` and `u_i(0)=1`.  If the next generator is `sigma_k`, then

```text
p_{t+1}=p_t o (k k+1),
u_k(t+1)=u_k(t) a_{p_t(k)} u_k(t)^-1 u_{k+1}(t),
u_{k+1}(t+1)=u_k(t),
u_i(t+1)=u_i(t) for i not in {k,k+1}.
```

If the next generator is `sigma_k^-1`, then

```text
p_{t+1}=p_t o (k k+1),
u_k(t+1)=u_{k+1}(t),
u_{k+1}(t+1)=u_{k+1}(t) a_{p_t(k+1)}^-1 u_{k+1}(t)^-1 u_k(t),
u_i(t+1)=u_i(t) for i not in {k,k+1}.
```

A valid endpoint certificate must choose finitely many detector tracks
`phi_r:F_n->H_E` before reading the braid word.  The track assignments may
depend on the interval, the active endpoint family, the initial colour/fibre
tuple, and the routed seed state, but the finite endpoint group and detector
family may not depend on `n` and may not be chosen by search after seeing a
failed detector.  For each track, the certificate must define the initial
values `a_{r,i}=phi_r(x_i)` from the initial interval data and update
`u_{r,i}(t)` by the Artin detector recurrence above.

The detector-track initialization must also be finite table data, not a
boolean.  For every active endpoint family `E`, the certificate must list the
positive number of tracks `R_E` and then provide exactly one initialization
row for every key

```text
(E,r),     0 <= r < R_E.
```

Each family track-count row must use one of the known endpoint families
`U`, `C`, or `M`, and its count must be a positive integer.  Booleans,
strings, zero, negative values, missing counts, and unknown family names are
malformed detector-track ledgers; they do not define empty or harmless
families.  The family label must be a hashable certificate atom equal to
`U`, `C`, or `M`; an unhashable list-like label or any other structured object
is an invalid family row, not alternate syntax, and it must not create
detector-track keys or initialized raw-variable scope.  Each family
track-count row must also have the exact two-field
finite shape `(endpoint_family, positive_track_count)`; shortened rows and
rows with extra fields are malformed detector-track data.  Each
initialization row must name a known endpoint family, a
nonnegative integer track index, an assignment rule, the finite dependencies
used by that rule, and the local assignment template for the raw variables
`A_{r,j}`.
Allowed dependencies are only interval and initial-state data:

```text
interval_data, endpoint_family, routed_seed_state,
initial_colour_tuple, initial_fibre_tuple,
strand_index, strand_colour, local_input, local_output.
```

Dependencies such as

```text
braid_word, braid_prefix, braid_index, failed_detector,
finite_search_result, normalized_law_sequence, timeout
```

are forbidden.  The initialization ledger must have no missing, extra, or
duplicate `(E,r)` rows.  A claim that detector tracks are "fixed before the
braid" or that initialization is "verified" is not a certificate unless this
finite row table is present and exact.
Every detector-track initialization entry must be an actual initialization
row object carrying the endpoint family, track index, assignment rule,
dependencies, and local assignment template.  A tuple-shaped stand-in is a
malformed initialization row, not an abbreviation.
The fixed-before-braid check is separate from template validity: forbidden
braid-prefix, braid-word, search, timeout, or braid-index dependencies make a
row unfixed, while an otherwise fixed row with a malformed local assignment
template is a template error rather than a braid-dependence error.
The local assignment template in each row must also be checked: it may assign
only raw variables `A_{r,j}` for that same track `r`, may not repeat an
assigned raw variable, and every assigned value must be an element of the
fixed endpoint group `H_E`.  A dependency-valid row with an invalid template
does not initialize a detector track.
The initialization template must also cover the raw assignment variables that
the word-potential substitutions actually use.  If a local Artin substitution
contains `A_{r,j}`, then the initialization row for `(E,r)` must include that
same raw variable.  Otherwise the substitution is using an uninitialized
generator assignment, so the detector track is not really fixed before the
braid.

The same certificate must define finite word templates `W_s`, one for every
reachable endpoint state `s in S_E^reach`.  Each word template is a fixed
word in current longitude variables `U_{r,j}` only.  It may not use raw
generator-assignment variables `a_{r,j}` in the terminal readout word.  The
raw assignments may appear only in the local Artin substitution that updates
the formal variables.
Every template-state key, word-potential seed-state ledger key, and
initial-normalization key must be a well-formed endpoint state `(E,s)` with
`E in {U,C,M}` and tuple-valued reachable seed state `s`.  Malformed state
keys are not harmless extra metadata: they invalidate the certificate before
template scope, track scope, or normalization checks can close.
Every track index appearing in a terminal template or in a local substitution
must be backed by the declared fixed track count for that endpoint family.
For example, if the target family has `R_E` tracks, no variable `U_{r,j}` or
`A_{r,j}` with `r >= R_E` is a valid detector-lift variable.  Otherwise the
terminal word is not a word in initialized evaluated longitudes, even if it
uses the letter `U`.

For every positive endpoint row

```text
Gamma^{E,+}_{a,b}(s,x,y)=(s',x',y',h),
```

the certificate must give the corresponding Artin substitution
`A_gamma^+` on formal variables, induced by the positive Artin recurrence.
The decisive finite local identity is

```text
W_{s'}(A_gamma^+(U,A)) = W_s(U) h
```

inside `H_E`, for every assignment of the involved formal variables to
elements of `H_E`.  Equivalently, the nonabelian defect

```text
W_s(U)^-1 W_{s'}(A_gamma^+(U,A))
```

must be a constant element of `H_E` on a sound finite detector domain, and
that constant must equal the emitted label `h`.  This is finite because
`H_E`, the reachable state set, the positive row table, and the formal
variable support are finite.  Negative endpoint rows must still be present in
the signed endpoint observer, but their word-potential identities are not
independent certificate rows when the negative table is proved to be the
actual inverse of the positive table.

The certificate must be supplied as finite table data, not as a boolean.  It
must include:

```text
template table:
  (E,s) |-> W_s

monodromy table:
  (E,r,s) |-> F^E_r(s)

identity-row table:
  (E,+,s,a,b,x,y) |->
  (next state s', emitted label h, Artin substitution A_gamma^+,
   sound detector-domain descriptor)
```

The identity-row table must cover exactly the positive part of `D_Gamma(E)`
for the same signed endpoint table.  It is not allowed to omit a positive
reachable-state/fibre input, and it is not allowed to add extra positive
channels.  Its `s'` must be the monodromy image `F^E_r(s)`, and its `h`
must be the constant value of the coboundary defect on the declared sound
domain.  These must agree with the positive signed row

```text
Gamma^{E,+}_{a,b}(s,x,y)=(s',T_{a,b}(x,y),h).
```

Executable construction discipline.  A valid observer should be built from
the monodromy-coboundary table, not by independently inventing signed
emissions.  The finite construction is:

```text
positive local-context monodromy presentation:
  generators are all positive contexts r=(E,a,b,x,y);
  adjacent relations are the 121/212 context paths computed from T;
  far relations are nontrivial disjoint context swaps within each active
    family, with tautological self-swaps omitted;
  every active colour/fibre triple must have readable 121 and 212 paths in
    the actual R_C and T tables; missing base rows or local rows are finite
    presentation failures, not omitted relations;
  every endpoint-family label in the presentation and in every context must
    be a hashable member of {U,C,M}; unknown or unhashable family labels are
    finite monodromy-presentation failures, not omitted generators;

positive rows:
  Gamma^{E,+}_{a,b}(s,x,y)
  =
  (s', T_{a,b}(x,y), h)

where (s',h) is read from the positive identity-row table.

negative rows:
  Gamma^{E,-}_{c,d}(s',u,v)
  =
  (s,x,y,h^{-1})

whenever R_C(a,b)=(c,d) and T_{a,b}(x,y)=(u,v).
```

Then compute `S_E^reach` as the exact signed-transition closure of the
current `kappa` seed image under these derived rows, recompute the full
signed domain `D_Gamma(E)` from the interval fibres and reachable states, and
audit the constructed observer against that domain.  The finite monodromy
presentation itself should be attached to the observer build so that the
permutation representation is checked against explicit positive local
contexts and explicit adjacent/far relations, not hidden as later boolean
claims.  The representation audit must read the positive rows as maps on
reachable seed states, prove every local context acts by a permutation of the
seed states in its endpoint family, and verify every explicit adjacent and
far relation in the monodromy presentation.  If the positive identity-row
table omits any reachable local context, if a next state leaves the reachable
closure, if the negative table is not single-valued, if the coboundary defect
is not constant on a sound detector domain, or if residual faithfulness is
not supplied, the observer remains open.  No default endpoint emission is
allowed.
Malformed or unhashable reachable-state rows in the monodromy representation
are finite ledger failures; they must not crash the permutation check and
must not be treated as hidden observer states.
The signed endpoint proof gate itself must consume this explicit monodromy
representation audit.  It is not enough to assert separate state/coordinate
YBE and far-commutativity booleans: the finite representation audit must
show that the supplied positive state maps define a representation of the
declared positive local-context presentation on the exact reachable states.
The preferred handoff is therefore the finite monodromy-coboundary
certificate itself: endpoint group or cutoff target, detector-track
initialization rows, templates `W_s`, positive identity rows, C/M cutoff
readouts if needed, and residual-faithfulness rows.  The signed endpoint
table should then be derived from that data and rechecked against the current
`kappa` seed ledger and interval table.
The implementation also includes the constructor
`universal_k_word_potential_certificate_from_monodromy(...)`.  This is not an
existence theorem.  It is a finite certificate builder: given positive
endpoint-state monodromy rows, state-indexed templates `W_s`, and a fixed
endpoint group, it derives the reachable seed-state closure from the current
`kappa` seeds, computes the positive entry domain, inserts the Artin
substitution forced by each next-state template, and evaluates the
nonabelian coboundary defect
`W_s(U)^-1 W_{F_r(s)}(A_r^+(U,A))`.  The emitted label `h` is the constant
defect value.  On the full finite detector-variable domain this accepts only
defects constant for all assignments.  A smaller detector-domain subset is
accepted only with explicit soundness witness data, such as an exhaustive
reachable-value enumeration or a symbolic detector-domain invariant.  The
derived constructor must not assign a placeholder endpoint label to a
nonconstant defect; if the defect takes two values on the sound detector
domain, the derived endpoint emission is absent/outside the endpoint group
and the observer remains open.  The returned word-potential certificate is
still audited normally, so missing
positive monodromy rows, nonconstant defects, malformed templates,
unsound detector-domain subsets, and missing residual-faithfulness rows keep
the U/C/M observer open.  Thus endpoint emissions are no longer arbitrary
primitive data once `rho_E` and the potentials are supplied; they are forced
by the finite coboundary computation.
The family-level handoff is
`universal_k_endpoint_observer_builds_from_monodromy_by_family(...)`.  It
accepts one fixed endpoint group, positive monodromy row table, template
ledger, and optional detector-domain soundness data for each active endpoint
family; derives the per-family word-potential certificates; and then calls
the ordinary family observer audit.  Therefore the smallest constructive
A-side input format is now the finite data
`(H_E,rho_E,W_E,D_E,RF_E)` for each active routed family, with endpoint
emissions and signed rows derived and rechecked against the current interval.
If no restricted detector-domain assignment map is supplied for a positive
entry, the constructor checks the coboundary defect on the full finite
detector domain.  A defect constant on that full domain needs no separate
soundness witness.  The raw monodromy front door has been checked to build a
complete U/C/M family observer package from identity monodromy rows, empty
word potentials, full-domain constant defects, fixed endpoint targets, exact
C/M cutoff readouts, per-family residual rows, and a product
residual-faithfulness theorem.  This validates the constructive handoff for
future nontrivial observers; it does not supply nontrivial `rho_E` and `W_E`
data for every surviving interval.
The monodromy handoff also composes with the same explicit residual-trivial
helper flags used by the identity observer constructor.  When one of those
flags is supplied, for example the coordinate-identity residual helper, the
handoff may derive the per-family residual-faithfulness rows and the
multi-family product residual theorem from the current interval instead of
requiring those rows to be hand-supplied.  This is still limited to the
already-proved residual-trivial subcases; it only removes duplicated
certificate data from otherwise explicit monodromy-coboundary observer
packages.
The identity and monodromy observer constructors now share one residual-helper
selector for these subcases.  Thus strict identity, coordinate identity,
singleton-fibre, supplied fibre-label identity, and canonical fibre-label
identity rows are derived in one fixed order for both handoff paths, with
failed supplied fibre-label ledgers remaining sticky rather than being hidden
by the canonical fallback.
The top-level `post_linear_remaining_finite_system_audit(...)` can consume
this package directly through its `universal_k_monodromy_*_by_family`
inputs.  It derives the current `K_nabla`/`kappa` ledger first, builds the
family observer from the monodromy-coboundary data, and retains the ordinary
family-build diagnostics.  Extra, stale, malformed, or unproved family data
does not close anything; it remains diagnostic unless it matches the current
routed endpoint families and passes target, cutoff, product, and
residual-faithfulness checks.
The raw monodromy-coboundary input package must itself be audited before it
is used.  The finite input ledger must cover exactly the active routed
families hit by `kappa`, with no duplicate family rows and no stale extra
families.  For each active family it must supply:

```text
H_E or S_mE,
state-indexed templates W_s,
positive monodromy rows defining F^E_r,
and, when a restricted detector domain is used, detector-domain assignments
plus soundness witnesses.
```

Malformed endpoint-group rows, malformed template rows, positive monodromy
rows from the wrong family or wrong sign, unknown family names, missing
active families, extra stale families, and restricted detector-domain
assignments without soundness witnesses are finite input-ledger failures.
The top-level by-family ledgers themselves must be finite row ledgers:
non-sequence endpoint-group, template, positive-row, detector-domain, or
detector-witness ledgers are reported as malformed row objects rather than
being iterated character-by-character, ignored as absent input, or allowed to
crash the handoff.
Any nonempty monodromy subledger is enough to trigger the monodromy input
audit and family-observer build diagnostic, including detector-domain
assignments or detector-domain soundness witnesses supplied without endpoint
groups, templates, or positive rows.  Such auxiliary-only packages are not
valid observers, but they must be reported as incomplete or malformed
observer attempts rather than ignored as if no U/C/M endpoint-observer data
were supplied.
They must not be interpreted as an unproved observer with unspecified
emissions.  A valid monodromy-derived observer begins only after this raw
package ledger is exact.
Every positive monodromy row must have a well-formed positive signed endpoint
entry key: the family must be one of U,C,M, the seed state must be a hashable
tuple state for that family, the sign must be positive, and the local colour
and fibre inputs must lie in the current positive context domain.  Malformed
or unhashable seed states are finite bad ledger data; they must not cause a
runtime failure and must not be treated as valid hidden observer states.
The next seed state of each positive monodromy row is also finite
permutation data.  It must be a hashable tuple state for the same family.
Malformed, unhashable, or non-tuple next states must be rejected as malformed
positive monodromy package rows at the handoff, and a direct monodromy
representation audit must report them as next-state-outside-family
context-map failures rather than accepting them as hidden observer states.
Raw positive monodromy rows define only the finite state map F^E_r.  They
must not carry primitive endpoint emissions.  A non-None endpoint value in a
raw positive monodromy row is stale emission data and must be rejected before
construction; the actual emitted labels must be exactly the constant
coboundary defects forced by rho_E and W_s.
The direct coboundary constructor must apply the same admissible-row filter:
malformed next states and stale primitive emissions may not seed the
reachable monodromy closure and may not produce word-potential identity rows.
The family-level audit should report such bad raw rows, while the lower-level
constructor must be unable to use them to derive hidden emissions.
Restricted detector-domain assignments are also entry-key scoped.  Each
assignment map key must be a well-formed positive signed endpoint entry for
the same endpoint family as the family row, and, when the interval table is
available, must be one of the positive entry keys forced by the current
reachable seed-state closure.  Every restricted-domain assignment key must
have exactly a matching soundness-witness key, and a soundness-witness key
without a restricted-domain assignment is an extra witness channel, not a
proof of soundness.
The restricted-domain map values must also be finite row data.  Each
assignment value must be a nonempty tuple of finite tuple assignment rows;
each assignment entry must contain a valid word-potential variable and an
element of the fixed endpoint group.  Each soundness-witness value must be a
nonempty duplicate-free tuple of recognized detector-domain soundness
witness labels.  A correctly keyed row with malformed assignment values or
malformed witness values is still an invalid observer handoff.
Detector-domain soundness flags and witnesses are meaningful only when an
actual restricted detector-domain assignment subset is supplied for that
positive row.  In the full finite-domain case, any soundness flag or witness
is stale certificate data and must keep the word-potential certificate open;
it is not an extra proof channel.
With the interval in hand, this raw ledger must also derive the reachable
monodromy seed-state closure from the positive rows, recompute the full
positive local-context entry domain from the actual fibres, and check that
the positive monodromy table has:

```text
no duplicate positive entry keys,
no missing positive entry keys,
no extra positive entry keys,
and coordinate outputs exactly equal to T_{a,b}(x,y).
```

Only after this positive domain check passes may the coboundary defects be
evaluated and used as endpoint emissions.  A partial `rho_E` table, a stale
context row, or a row whose coordinate part does not match the interval is
not a valid observer input.
The template ledger must also be exact for the same derived reachable
closure.  There must be exactly one word-potential template `W_s` for each
reachable endpoint seed state `(E,s)`, and there must be no extra stale
template states.  Duplicate, missing, or extra template states are raw
input-ledger failures before any coboundary defect is evaluated.
The executable audit also has a canonical identity-emission constructor
`universal_k_identity_endpoint_observer_builds_by_family(...)`.  It builds
the identity monodromy-coboundary candidate for every active family in the
current `kappa` image: U uses the current triangular-recovery unit group
`U_tri`; C and M use symmetric cutoff groups with enough distinct readout
permutations for their routed seed states.  This constructor is useful
bookkeeping, not a proof of A.  It may close only when the required
per-family residual-faithfulness rows, and the product residual-faithfulness
row for multi-family endpoint products, are supplied and pass the finite
scope checks.  Otherwise it must remain an open observer candidate rather
than a default endpoint-emission proof.
If the identity constructor is supplied explicit cutoff degrees, that
cutoff-degree table is finite certificate data.  Each row must have exact
two-field shape `(family, positive_degree)`, the family must be a hashable
active cutoff family `C` or `M`, and the degree must be a positive integer
that is not a boolean.  Duplicate families, unknown family labels, U-family
degree rows, unhashable family labels, nonpositive degrees, and malformed row
shapes must be reported as identity cutoff-degree ledger failures.  A
non-sequence degree ledger is also malformed finite data.  They may not be
silently ignored while the constructor falls back to a default symmetric
degree.
The top-level post-linear audit may derive this canonical candidate by an
explicit opt-in flag, `universal_k_identity_endpoint_observer_candidates`.
This flag only retains the identity monodromy-coboundary ledger in the
post-linear proof object.  It is nondecisive by design: with no active
`kappa` endpoint family it reports an empty active-family ledger, and with
active endpoint families but no residual-faithfulness theorem it reports an
open observer candidate rather than closing any U, C, or M endpoint system.
All automatic residual-faithfulness helpers require the supplied local
interval table to be complete and type-correct: `R_C` must be a bijection on
colour pairs, every local `T_{a,b}` row must be present exactly on its fibre
domain, and every local output must land in the fibres prescribed by
`R_C(a,b)`.  A malformed raw interval object is never an automatic residual
closure proof, even if the rows inspected by a particular subcase look
harmless.
There is one narrow automatic residual-faithfulness subcase.  If every
quotient row fixes its colour pair and every local fibre row is strictly
`(x,y)->(x,y)`, then every braid word has trivial residual fibre action after
quotient stabilization.  The audit helper
`universal_k_strict_identity_residual_faithfulness_audit(...)` may then emit
one schematic all-`n` residual row per active endpoint family, with
dependencies only on the interval, local row table, routed seed state,
residual input tuple, endpoint channel, and local fibre coordinate.  The
identity observer
constructor may consume this theorem when
`derive_strict_identity_residual_faithfulness=True`.  This closes only the
strict identity-fibre subcase; any non-identity U, C, or M endpoint observer
still requires its own residual-faithfulness theorem.
There is also a coordinate-identity residual-faithfulness subcase.  If every
local row preserves the raw fibre coordinate pair `(x,y)`, then along every
braid word the fibre coordinate tuple is unchanged, even when the quotient
colour tuple moves.  This subcase is valid only when the raw coordinates are
type-correct in the output fibres: if `R_C(a,b)=(c,d)` and
`T_{a,b}(x,y)=(x,y)`, then `x` must be an element of `A_c` and `y` must be
an element of `A_d`.  A raw-equality table whose output fibres do not contain
those values is not a coordinate-identity residual proof.  For a braid in the
quotient kernel, the final quotient colours return, so the residual fibre
action is identity.  The helper
`universal_k_coordinate_identity_residual_faithfulness_audit(...)` may emit
one schematic all-`n` residual row per active endpoint family, and the
identity observer constructor may consume it only when
`derive_coordinate_identity_residual_faithfulness=True`.
There is also a singleton-fibre residual-faithfulness subcase.  If every
fibre `A_c` has exactly one point, then every fibre product `X_z` is a
singleton for every quotient-colour tuple `z`; hence the bundled residual
fibre action is trivial for every braid index, even if quotient colours move.
The helper `universal_k_singleton_fibre_residual_faithfulness_audit(...)`
may emit one schematic all-`n` residual row per active endpoint family, and
the identity observer constructor may consume it only when
`derive_singleton_fibre_residual_faithfulness=True`.  This closes only the
singleton-fibre subcase and does not solve nontrivial U/C/M endpoint
observers.
There is also a fibre-label identity residual-faithfulness subcase.  A
finite ledger of rows `(color, fibre_point, label)` defines maps
`ell_c:A_c->L` only when the rows cover every fibre point exactly once, each
label is finite hashable certificate data, and each `ell_c` is injective.
The local row table must preserve labels coordinatewise: whenever
`R_C(a,b)=(c,d)` and `T_{a,b}(x,y)=(u,v)`, one must have
`ell_c(u)=ell_a(x)` and `ell_d(v)=ell_b(y)`.  This check must range over
every colour pair and every fibre input; a missing quotient row or a missing
local `T` row is a finite preservation failure, not a vacuous pass.  Then
every braid word preserves
the ordered label tuple.  For `beta` in the quotient kernel, quotient colours
return to the original tuple, and fibrewise injectivity of the returned
labels forces the final fibre tuple to equal the initial tuple.  The helper
`universal_k_fibre_label_identity_residual_faithfulness_audit(...)` may emit
one schematic all-`n` residual row per active endpoint family, and the
identity observer constructor may consume it only when
`derive_fibre_label_identity_residual_faithfulness=True` with the supplied
`fibre_label_identity_rows` ledger.  That label ledger must be audited as
finite row data: a non-sequence object such as `None` or a string is one
malformed label row, not a character-by-character ledger and not a runtime
exception.  This closes only the fibre-label
identity subcase and does not solve general nontrivial U/C/M endpoint
observers.
There is also a canonical fibre-label identity subcase that does not require
supplying the label ledger by hand.  Build the least equivalence relation on
the finite nodes `(color,fibre_point)` generated by the local preservation
constraints
`(a,x)~(c,u)` and `(b,y)~(d,v)` for every row
`R_C(a,b)=(c,d)` and `T_{a,b}(x,y)=(u,v)`.  Use the resulting equivalence
classes as component labels.  This canonical ledger is valid exactly when
the component-label map is injective on every fibre and every local row
preserves the two component labels coordinatewise.  If two distinct points in
one fibre lie in the same generated component, the subcase must fail with a
finite noninjectivity obstruction.  When the canonical ledger is valid, the
same all-`n` proof as the supplied fibre-label case shows that quotient-kernel
braids have trivial residual fibre action.  The identity observer constructor
may consume this proof only with the explicit canonical-label residual flag;
it is still only an automatic residual-faithfulness subcase, not a general
U/C/M endpoint observer.
There is also an aggregate identity-residual consumer flag,
`derive_automatic_residual_faithfulness=True`, and at the top-level audit
`universal_k_identity_automatic_residual_faithfulness=True`.  This flag tries
only the already-proved automatic subcases: strict identity, coordinate
identity, singleton fibres, supplied fibre-label identity when a label ledger
is present, and canonical fibre-label identity.  It is a convenience route for
closing those symbolic residual-triviality cases.  It is not an existence
proof for the nontrivial U/C/M endpoint observers, and if none of the finite
hypotheses holds the observer candidate must remain open.
The reusable helper
`universal_k_automatic_residual_faithfulness_audit(...)` is exactly this
selector: it returns the first proving residual-faithfulness audit in that
order.  If a supplied fibre-label ledger is present after the strict,
coordinate-identity, and singleton helpers fail, that ledger is treated as
certificate data: a failed supplied-label audit must be returned open and may
not be silently bypassed by the canonical-label fallback.  If no supplied
label ledger is present, the helper may fall back to canonical fibre-label
identity and returns the open canonical audit when it does not prove.  Thus
the automatic path cannot silently discard bad seed data or bad supplied
label data, and it cannot manufacture residual faithfulness outside the listed
symbolic subcases.
At the top-level post-linear audit, any individual identity residual-helper
flag must also derive and retain the identity observer candidate ledger:
`universal_k_identity_strict_residual_faithfulness`,
`universal_k_identity_coordinate_residual_faithfulness`,
`universal_k_identity_singleton_residual_faithfulness`,
`universal_k_identity_fibre_label_residual_faithfulness`, or
`universal_k_identity_canonical_fibre_label_residual_faithfulness`.  These
flags must not be ignored merely because the aggregate automatic flag is not
set.
At the top-level post-linear audit, the same residual-trivial identity
observer path has been explicitly regression-tested for each one-family
routed endpoint system.  A U-only route closes under the verdict
`closed_by_triangular_recovery_endpoint_observer_family_build`; a C-only
route closes under
`closed_by_universal_continuation_endpoint_observer_family_build`; and an
M-only route closes under `closed_by_mixed_unit_endpoint_observer_family_build`.
For one-family cases the per-family residual-faithfulness theorem already
has the full active-family scope, so a separate product residual theorem is
not required.  The ledger still records the residual channel reason by
family, requires the observer rows to match the current interval, requires
the current `K_nabla`/`kappa` seed ledger to match, and in U requires the
current triangular-recovery unit target.  Thus the already-proved
singleton-fibre, strict identity, coordinate-identity, supplied fibre-label
identity, and canonical fibre-label identity residual-trivial subcases are
consumed for individual U, C, and M endpoint obligations.  This is not an
existence proof for the remaining nontrivial U/C/M endpoint observers.
The aggregate automatic selector is likewise checked at the one-family routed
level: if an interval satisfies one of the selector hypotheses, for example
coordinate-identity residual motion, the derived family ledger closes the
single active U, C, or M endpoint obligation without requiring a product
residual theorem.
The identity observer constructor must enforce the same rule when the
explicit supplied-label and explicit canonical-label derivation flags are
both set.  If the supplied fibre-label residual theorem is attempted and
fails, that failed certificate data is sticky: the canonical fibre-label
helper may not replace it in the same per-family observer candidate or in the
same product-family residual theorem.
All automatic residual-faithfulness helpers must preserve the full
supplied routed seed-state ledger in the theorem.  They may use only
well-formed U/C/M seed states to emit schematic rows, but malformed,
wrong-family, or unhashable seed-state entries must remain in the expected
and covered theorem ledgers and must make the theorem fail.  No automatic
helper may silently discard bad seed data and prove residual faithfulness for
a smaller endpoint scope.
The post-linear proof object should retain the resulting endpoint-observer
build record, not only the derived signed-generator audit.  A complete
certificate should expose whether the build is present, whether it proves the
observer, the positive entry keys forced by the word-potential table, and the
positive local-context monodromy presentation used by the build.
For product endpoint rows, the proof should also provide a family-scoped
observer-build ledger: one constructed observer for each active family in
`{U,C,M}` hit by `kappa`, no duplicates, no extras, and no malformed build
rows.  Each retained family build must be single-family scoped, must use
exactly that family's seed classifier entries and reachable seed states, and
must itself prove the endpoint observer.  A successful U observer cannot
stand in for a missing C or M observer.
The retained family-build ledger may not be opaque.  Even if a prebuilt
observer object internally proves its signed tables, the family-level closure
certificate must expose the exact input ledgers used to construct it: one
word-potential certificate row, one detector-track initialization family
ledger, one endpoint-target audit row, and one residual-faithfulness theorem
row for every active routed family.  C and M additionally require exact
cutoff-readout audit rows when they are active cutoff families.  A family
observer wrapper with proving build objects but missing these explicit input
rows is diagnostic evidence only; it is not a U/C/M closure proof.
The observer-build ledger must also validate the `kappa` input rows before
using them to infer active families.  A classifier entry with the wrong row
shape, an unhashable seed-state key, a non-tuple seed state, or a target
family outside `{U,C,M}` is a finite certificate error.  Such data must be
reported as a malformed or invalid seed-classifier ledger; it may not be
converted into a generic missing-observer symptom and may not crash raw set
comparisons.
The main post-linear proof object must retain or derive this family ledger
from per-family word-potential certificates and must expose expected,
covered, missing, extra, duplicate, malformed, scope-mismatched, and unproved
family builds as finite data.  This ledger is separate from the combined
signed-generator audit: it is evidence that the U/C/M observers were
constructed family-by-family, not by an opaque product certificate.
The retained family ledger must also be rechecked against the current
`K_nabla` seed classifier and the current interval table.  The checker must
compare the family ledger's seed classifier entries with the current
`kappa` entries, recompute the full `D_Gamma` domain for each family build
from the current interval and that build's reachable seed states, and compare
that domain with the build's required-entry ledger.  It must also recompute
coordinate compatibility, inverse pairing, inverse cancellation, positive
state/coordinate YBE, and far state/coordinate commutativity against the
current interval table and endpoint group.  A per-family observer built for
a stale interval, stale reachable-state domain, or stale seed classifier may
remain diagnostic data, but it does not close the current routed endpoint
obligation.
For a U-family observer build, the checker must also recompute the current
triangular-recovery unit observer `U_tri` from the same endpoint interval.
The U build closes System U only when its endpoint target is exactly the
current `U_tri` target, recorded by the exact finite group-table fingerprint,
not merely by endpoint-group order.  The fingerprint includes the concrete
element set, identity, inverse table, and multiplication table.  A
word-potential observer over a different same-order finite group may still be
retained as diagnostic data, but it cannot close a U obligation routed by the
current `kappa` ledger.  The checker should report this exact obstruction as
`signed_endpoint_generator_current_u_tri_target_mismatch` for a combined
signed-generator table and as
`endpoint_observer_family_build_current_u_tri_target_mismatch` for a
per-family observer build.
When more than one of `U`, `C`, and `M` is active, the retained family ledger
must also include a product residual-faithfulness theorem scoped to the full
active family set and the full set of endpoint seed states hit by `kappa`.
Per-family residual-faithfulness rows are enough to prove the individual
observers, but they do not by themselves prove that killing all active
endpoint channels forces the true bundled residual fibre action to be
trivial.  The product theorem must have exact family coverage, exact seed
state coverage, exact residual input rows, product-family row separation, and
must prove

```text
all active endpoint channels killed => Delta_n(beta)=1
```

for the actual product endpoint row.  In the one-family case this extra
product theorem is not required because the individual observer's
residual-faithfulness theorem already has the full active-family scope.
The product theorem must also expose the same endpoint-channel reason ledger
by family as the per-family residual-faithfulness theorems.  A product theorem
whose rows have the right active families and seed states but replace the
routed U/C/M channel names with a placeholder or a different channel reason is
not an exact residual-faithfulness theorem for the product row.  It must be
reported as
`endpoint_observer_product_residual_faithfulness_channel_scope_mismatch`, and
it cannot close the product endpoint family build.  This prevents a product
residual theorem from proving faithfulness for a different set of endpoint
channels than the observers actually kill.
The product theorem must also match the full well-formed endpoint-channel key
ledger by family.  Endpoint-channel keys have shape
`(E,s,channel_name,optional_local_data...)`; the optional local data are part
of the concrete channel.  Thus a product theorem that keeps the same
`channel_name` but changes, drops, or invents optional local channel data is
not proving faithfulness for the same endpoint channels as the per-family
observers.  It must be reported as
`endpoint_observer_product_residual_faithfulness_channel_key_scope_mismatch`,
and it cannot close the product endpoint family build.
The product theorem's active and covered family ledgers must themselves be
finite well-formed `{U,C,M}` ledgers.  Unknown or unhashable family labels do
not match the active product scope; they are product residual family-scope
mismatches and leave product closure open.
If the retained family ledger matches the current `kappa`, matches the
current interval, proves every active family observer, and passes the product
residual-faithfulness gate, then it should be treated as a routed endpoint
closure certificate.  The proof object must list exactly which active
families are closed by this endpoint-observer family build, and those
families must be removed from the unclosed U/C/M endpoint tuple.  A family
observer ledger that is only diagnostic, stale, or missing product residual
faithfulness must not close any active endpoint family.
The per-family word-potential certificate input rows must also be audited as
finite data.  A malformed two-field row, a non-certificate value, an unknown
family, a duplicate family, a missing active-family certificate, or an extra
certificate family must be reported explicitly rather than silently turning
into a missing observer build.  The family label in every build, certificate,
detector-track, endpoint-target, cutoff-readout, and residual-theorem row must
be a hashable certificate atom equal to `U`, `C`, or `M`; unhashable list-like
labels or other structured objects are invalid family rows, not alternate
syntax, and they must not instantiate per-family observers or initialized
detector-track scope.
The top-level direct family-observer ledgers themselves must be finite row
ledgers.  A non-sequence certificate, detector-track, endpoint-target,
cutoff-readout, residual-theorem, or identity-cutoff-degree ledger is one
malformed row object.  It must not be iterated character-by-character,
ignored as absent input, or allowed to crash the handoff.
Likewise, any direct auxiliary family ledger, including detector-track,
endpoint-target, cutoff-readout, or by-family residual-faithfulness rows
without a word-potential certificate ledger, must still trigger the direct
family-observer audit.  It remains an incomplete observer attempt until the
word-potential and residual-faithfulness data are exact, but it is not
silently absent.
Direct signed-generator detector-lift auxiliaries obey the same finite-ledger
discipline.  Supplying detector-track count rows or detector-track
initialization rows directly to the post-linear audit without a
word-potential certificate must create a diagnostic telescoping audit rather
than silently dropping those rows.  A non-sequence count ledger such as
`None` is one malformed count row; a non-sequence initialization ledger is one
malformed initialization row.  Unknown families, duplicate track keys,
nonpositive counts, malformed initialization templates, missing
word-potential templates, and missing initial normalization must be exported
as signed-generator detector-lift failures.  Such diagnostics do not close
an endpoint family; they only make the incomplete direct detector-lift data
visible.
The same exact finite-ledger rule applies to the auxiliary rows used to build
the family observers.  Detector-track initialization rows must cover exactly
the active routed families with no malformed rows, unknown families, or
duplicate track keys.  They must also be fixed before braid reading at the
family aggregation gate itself: forbidden dependencies such as braid words,
braid prefixes, failed detector searches, timeout data, finite-search
results, or normalized-law sequences are reported as unfixed detector rows.
Their assignment templates are finite row data checked against the family's
word-potential endpoint group: each entry must assign a raw `A_{r,j}`
variable for the same detector track, may not duplicate a variable, and must
use a value in the fixed endpoint group.  Endpoint-target audit rows and
residual-faithfulness theorem rows must cover exactly the active routed
families; absence of such rows is a missing-family certificate failure, not
an optional diagnostic omission.  C/M cutoff-readout audit rows must cover
exactly the active cutoff families, and are likewise mandatory when C or M
is active.  Malformed rows, unknown families, duplicate families or keys,
missing active families, and extra auxiliary families must be reported
separately.  A wrong-typed auxiliary value is malformed finite data: an
endpoint-target ledger may select only endpoint target audits, a cutoff
ledger may select only cutoff readout audits, and a residual ledger may
select only residual-faithfulness audits.  Selecting the first valid auxiliary
row for a family is not enough: an extra, duplicate, malformed, missing, or
stale detector-track, endpoint-target, cutoff-readout, or residual theorem
row must keep the family-build ledger from proving exact observer coverage.
Positive observer rows may be forced only from actual word-potential identity
row objects.  A tuple-shaped identity-row stand-in is a malformed certificate
entry: it must be reported at the word-potential gate, must not be interpreted
as a positive endpoint row, and must leave the observer open.

Each `W_s` is a word in variables `U_{r,j}` only.  The local substitution may
use both `U_{r,j}` and raw assignment variables `A_{r,j}`, but the terminal
template may not contain any `A` variable.  All such variables must use track
and local-position indices that are genuine nonnegative integers in the
finite declared ranges for the endpoint family.  Boolean indices, strings,
negative values, and other non-index objects are malformed formal variables,
not detector tracks.  Malformed or unhashable formal-variable objects must be
reported as certificate errors rather than crashing duplicate, detector-domain,
or normalization checks.  Each word-potential letter, Artin substitution row,
detector-domain assignment entry, and detector-track assignment entry must
have its declared two-field finite-row shape; malformed row shapes are
certificate errors rather than implicit abbreviations.  The template table
itself is also a finite row ledger: each row must have exactly two fields,
`((E,s), W_s)`.  A short, extra-field, non-tuple, or otherwise malformed
template row is a certificate error.  Every identity-row entry must be an
actual word-potential identity row carrying the required fields; an arbitrary
tuple-shaped object is a malformed identity-row object, not an implicit
abbreviation.  For the active two
local strands, the positive
substitution must be the Artin detector
recurrence:

```text
U_{r,0} -> U_{r,0} A_{r,0} U_{r,0}^{-1} U_{r,1}
U_{r,1} -> U_{r,0}
```

Variables outside the active local pair are unchanged.  The finite checker
must evaluate the coboundary defect for every assignment of the variables in
that positive row to elements of the fixed group `H_E`, or to a smaller
declared domain only after proving that domain contains all reachable detector
values.  The defect must be constant, and the constant must be the emitted
endpoint label.
If a smaller detector domain is supplied, it must be finite row data: every
assignment row must list exactly the variables in that row's coboundary
defect support, no missing variables, no extra variables, no duplicate
variables, and no value outside `H_E`.  The certificate must also contain a
soundness witness proving that all reachable detector values for that local
context and state lie in the listed subset, for example an exhaustive
reachable-detector-value enumeration or a symbolic detector-domain invariant.
Without such a witness, the only accepted domain is the full finite group
power `H_E^V`.
If negative substitutions are recorded, they are diagnostics only; closure
comes from inverse-derived negative rows plus the positive telescope.
Rows with any sign other than `+1` or `-1` are malformed certificate rows and
must be rejected rather than silently ignored.
The expected and covered telescoping entry ledgers must obey the same sign
discipline: their closure comparison is positive-only, but any malformed sign
in either ledger invalidates the certificate.
More generally, every word-potential identity row and telescoping ledger key
must be a full `D_Gamma` key `(E,epsilon,s,a,b,x,y)` with `E in {U,C,M}`,
`epsilon in {+1,-1}`, and a tuple-valued reachable state `s`.  A shortened or
wrong-family key is malformed even if its sign field is `+1`.
Malformed keys must be rejected before any downstream template, detector-track,
or identity diagnostic tries to interpret their fields.
For every positive word-potential identity row, the `next_seed_state` must
also be a tuple-valued hashable state in the same endpoint family.  A
malformed or unhashable next state is a certificate error; it cannot be
interpreted as a missing template after a crashing map lookup.
Reachable seed-state ledgers, signed-entry ledgers, and telescoping ledgers
must use duplicate-safe normalization before set comparison, so unhashable
malformed keys are reported as malformed finite data rather than becoming
runtime failures or silently filtered rows.
The same hashability-safe comparison discipline applies to word-potential
template scope, positive identity-entry scope, Artin-substitution variable
support, and raw-assignment initialization support.  A malformed or
unhashable formal variable appearing in a substitution row is therefore a
finite certificate error; it cannot be used as an implicit detector track and
must not make the checker crash while deciding whether a U/C/M endpoint
observer has been built.
If optional negative diagnostic identity rows or telescoping ledger keys are
recorded, each such key must still belong to the actual signed `D_Gamma(E)`
domain for the current interval and reachable states.  Positive closure is
positive-only, but out-of-domain negative diagnostics are extra channels and
do not form a valid certificate.

The initial routed state must be normalized:

```text
W_{s_0}(1,...,1)=1.
```

For a family with several routed initial seeds, this normalization must hold
for every seed in `S_E^0` hit by `kappa`.  Normalizing only a later reachable
state, or a state outside the current `kappa` seed image, is not enough to
start the braid-word telescope.  The normalization ledger must be exact:
its states must be precisely the current `kappa` seed image
`{(E,s): kappa(d)=(E,s)}`.  Extra normalized states, even if they are later
reachable states with valid templates, are extra initial channels and do not
constitute an exact telescope start certificate.

Then along a braid word the values `W_{s_t}(u(t))` telescope by the local
identity, so `W_{s_m}(u(m))` equals the accumulated endpoint.  Since every
variable in the terminal word is one of the current longitude values
`u_{r,i}(m)=phi_r(L_i(beta))`, the endpoint lies in `V_beta(H_E)`.  This
word-potential detector-lift, not the rowwise two-strand identity and not a
tautological accumulated potential, is the all-`n` local-to-global bridge.
The Artin detector recurrence and terminal-readout-in-longitudes checks must
therefore be derived from the finite substitution and template tables above.
They are not separate boolean assertions: if the positive substitution is not
the positive Artin recurrence, or if a terminal template contains a raw
assignment variable, the detector lift is incomplete.  Negative
word-potential substitutions are unnecessary once the negative endpoint rows
are proved to be actual inverses.
Likewise, telescoping braid-index independence must follow from the finite
family track counts, exact initialization rows, and the absence of any
`braid_index` dependency in those rows; it is not a separate flag.

For cutoff families, in particular C and M, the proof must define faithful
readouts

```text
chi_C:S_C^reach -> S_mC,
chi_M:S_M^reach -> S_mM,
```

covering exactly the routed identity-continuation ledger for C and exactly
the routed mixed-unit ledger for M, with no extra channels.
The cutoff-readout certificate must list the expected routed C/M seed states,
the covered seed states, the positive symmetric degree `m`, and one finite
readout row for every routed C/M seed state:

```text
((E,s), readout permutation in S_m, killed-readout permutation in S_m).
```

The readout rows must cover exactly the expected seed states, with no
missing, extra, duplicate, or malformed row objects.  A non-sequence
readout-row ledger is treated as malformed finite data.  A malformed readout
row object is reported in
`signed_endpoint_generator_cutoff_readout_malformed_rows`; it is a finite
certificate failure, not a runtime exception and not a row that can be
silently ignored.  Each listed readout and killed-readout value must be an
actual permutation tuple of the integers `{0,...,m-1}`.
Boolean entries, strings, duplicate images, out-of-range entries, or other
malformed values are not elements of the symmetric group.  Faithfulness is
the finite injectivity check on the listed readout permutations.  Identity cutoff
data kills the channel exactly when every killed-readout permutation is the
identity permutation.  A bare assertion that the cutoff readouts are exact,
faithful, or killed by identity cutoff data is not a certificate.  The
expected and covered cutoff seed-state ledgers must also be duplicate-free;
silently deduplicating repeated C or M seed entries is not exact readout
coverage.
Every expected, covered, and row cutoff seed-state key must also be a
well-formed C/M endpoint state `(E,s)` with `E in {C,M}` and tuple-valued
seed state `s`.  A U-family seed state cannot be closed by this C/M cutoff
readout gate.  Malformed cutoff state keys are certificate errors, even if
the malformed expected, covered, and row sets happen to agree.  The cutoff
seed-state ledgers must use hashability-safe finite comparison: an unhashable
malformed seed key is reported as malformed certificate data, not allowed to
crash the checker and not silently removed by a raw set operation.
The readout certificate must also expose the induced C/M family ledger:
expected cutoff families, covered cutoff families, and readout-row cutoff
families must agree exactly with the active routed C/M families.  This family
scope check is deliberately separate from seed-state coverage so that a C
cutoff row cannot be used to certify an M channel, or vice versa, through a
single undifferentiated symmetric readout.
Cutoff braid-index independence requires an explicit certificate flag in
addition to the positive fixed degree and exact finite readout rows.  A
readout table whose finite rows are otherwise valid but whose independence
flag is false is still open.
For each active C/M cutoff family, this positive fixed degree must also match
the cutoff degree listed in the endpoint-target ledger.  If multiple C/M
families are handled by one readout audit, every listed cutoff target degree
must be the same finite symmetric degree used by that audit, or else the
families require separate explicitly scoped cutoff readout certificates.

The endpoint tables and readouts must also prove residual faithfulness:
if all routed endpoint labels or cutoff readouts are killed, then the actual
residual fibre action `Delta_n(beta)` is trivial on the corresponding
interval fibre for every braid index.  This is an independent obligation.
A trivial endpoint group makes every label formally lie in `V_beta(H_E)`,
but it does not prove residual domination unless this residual-faithfulness
map from endpoint channels to real fibre motion is supplied.

A concrete residual-faithfulness certificate must list the residual action
rows it covers.  For each residual input tuple it must give the output tuple,
decompose every moved coordinate into endpoint-controlled coordinates or
cutoff readouts, and prove that identity endpoint data fixes each coordinate.
Every supplied residual row must contain at least one coordinate readout; an
empty coordinate bundle is vacuous and does not prove even the supplied-row
detector implication.
It must also state the exact expected residual input-tuple domain and the
expected number of residual rows for the interval fibre action, then prove
that the listed rows cover that domain without missing, extra, or duplicate
input tuples.  A supplied row subset, or the same row repeated until the row
count matches, proves only a supplied-row implication, not domination of the
whole residual action.  Omitting the expected row count or the expected input
tuple domain is not acceptable for this endpoint lemma, even if every listed
row is internally certified.  The explicit-row certificate must also carry a
finite scope audit: active endpoint families, covered endpoint families,
exact expected and covered routed seed states, and allowed scope
dependencies.  The scope dependencies may use only interval data, routed seed
states, residual input tuples, endpoint channels, local fibre coordinates,
and the local row table; dependencies on `braid_word`, `braid_prefix`,
`braid_index`, failed detector search, normalized-law sequences, or timeouts
are forbidden.  The allowed list is not enough by itself: the scope must
explicitly include both `residual_input_tuple` and `endpoint_channel`, because
those are the finite dependencies that connect killed endpoint data to the
actual residual fibre tuple being fixed.  Endpoint-channel exactness must be
derived from that scope audit.  Braid-index independence must also be
explicitly certified and supported by the scope dependencies; the flag alone
is not proof.  If two or more endpoint families are active, the certificate must also split the
residual-row ledger by family: it must list expected and covered residual row
counts for each active family, with no duplicate family entries,
nonnegative integer counts, matching expected and covered family counts, and
sums equal to the total expected and covered residual row counts.  The total
expected and covered residual row counts are also nonnegative integer data;
strings, booleans, negative values, and other non-count objects are malformed
residual count ledgers, not finite row counts.  The family counts must also
be supplied as exactly two-field rows `(family, count)`; rows with extra
fields, missing fields, or non-tuple shape are malformed residual family
row-count ledgers, distinct from rows whose count field exists but is not a
nonnegative integer.  These family counts must also
match the counts derived from the actual residual rows: a row that names an
endpoint family contributes one row to that family, and no family ledger may
claim zero rows for a family used by a supplied row.  On an explicit
residual-action scope certificate that does not carry row-local family tags,
each active endpoint family must have a positive expected and covered row
count; a zero-row active family is an unproved channel, not a harmless empty
component.  An aggregate row count alone is insufficient for a product
endpoint row because it can hide that one family has no residual readout.
Every residual-action scope seed-state ledger entry must also be a
well-formed endpoint state `(E,s)` with `E in {U,C,M}` and tuple-valued seed
state `s`.  Malformed seed-state keys are not exact routed channels, even if
the malformed expected and covered sets happen to agree.  Residual seed
coverage must be compared using duplicate-safe, hashability-safe markers, so
an unhashable malformed seed key is reported as finite certificate data
rather than becoming a runtime failure.
The active and covered endpoint-family ledgers themselves must also use only
the known families `{U,C,M}`.  A residual scope over an unknown family label
is not an exact endpoint-channel certificate, even if the active and covered
family sets match.

Alternatively, a symbolic residual-faithfulness theorem may replace explicit
action readout rows only if it supplies its own finite residual row table.
For every residual input tuple the theorem table must list:

```text
input_tuple,
actual output_tuple,
identity_endpoint_output_tuple,
endpoint_families,
endpoint_seed_states,
endpoint_channel_keys,
dependencies.
```

The rows must cover exactly the expected residual input-tuple domain, with no
missing, extra, or duplicate input rows.  Every row must use only active
endpoint families and expected routed seed states, and the union of row
families and row seed states must equal the active families and expected
seed-state ledger.  Row-by-row, the families named by the row must equal the
families of the routed seed states named by that same row; a row cannot list
a family whose seed appears only in another row.  Each row must have nonempty
arity-consistent
`input_tuple`, `actual output_tuple`, and `identity_endpoint_output_tuple`,
and its `endpoint_channel_keys` ledger must be nonempty and duplicate-free.
Every endpoint-channel key must be a well-formed tuple

```text
(E,s,channel_name,optional_local_data...)
```

where `E in {U,C,M}`, `s` is a tuple-valued seed state, and
`channel_name` is a nonempty finite channel label.  Row-by-row, the set of
pairs `(E,s)` extracted from `endpoint_channel_keys` must equal exactly that
row's `endpoint_seed_states`; an extra channel key for another seed, a missing
key for a listed seed, or an opaque placeholder channel is not an exact
residual readout.  The key tuple must be finite and hashable so duplicate
channel keys are well defined.
`identity_endpoint_output_tuple` must equal `input_tuple` on every row; this
is the finite row evidence for the implication from killed endpoint data to
identity residual motion.  If this equality fails, the row is invalid at the
row-scope level; a theorem-level implication flag cannot repair it.  The
theorem must also explicitly assert both
theorem-level claims:

```text
endpoint_channels_exact=True,
identity_endpoint_data_forces_residual_identity=True.
```

If either assertion is missing or false, the residual-faithfulness theorem is
still open even when the row table itself is syntactically complete.  The
converse is also required: the two booleans alone are not proof unless the
finite row/domain ledgers derive endpoint-channel exactness and identity
residual motion.  The row dependencies may use only interval data, routed
seed states, residual input tuples, endpoint channels, local fibre
coordinates, and the local row table.  Dependencies on `braid_word`,
`braid_prefix`, `braid_index`, failed detector search, normalized-law
sequences, or timeouts are forbidden.  Each row must explicitly include both
`residual_input_tuple` and `endpoint_channel`; a row using only interval data
or routed seed labels is a finite row check, not a bridge from killed endpoint
channels to the actual residual motion.  Endpoint-channel exactness must be
derived from these rows and the family/seed ledgers.  Braid-index
independence and product-family separation must also be explicitly certified
and supported by those ledgers; the flags alone are not proof.
In the multi-family case, the theorem must also include the same expected and
covered residual row counts by family, again as nonnegative integer rows
whose sums match the total nonnegative integer row counts.  A bare assertion
that residual faithfulness holds, or a certificate scoped only by family names while
omitting the routed seed states, is not a certificate.  The expected and
covered family ledgers and the expected and covered seed-state ledgers must
also be duplicate-free; a repeated family or repeated seed is an ambiguous
ledger entry, not an exact coverage proof.  The family row-count ledgers must
match the symbolic theorem rows themselves: after counting, for each active
family, the rows whose `endpoint_families` contain that family, the expected
and covered family counts must equal those derived counts.
Every symbolic residual theorem seed-state ledger entry and every row-local
seed-state entry must be well formed as `(E,s)` with `E in {U,C,M}` and
tuple-valued `s`.  A malformed seed key makes both endpoint-channel
coverage and row scope invalid; it cannot be repaired by matching malformed
expected, covered, and row sets.  The same hashability-safe marker comparison
must be used for theorem seed coverage, so unhashable malformed row or ledger
seeds are explicit certificate errors.
The theorem's active and covered endpoint-family ledgers must likewise be
subsets of `{U,C,M}`, and every row-local endpoint family must be one of
those known families.  Unknown family labels make the theorem scope invalid.
The residual input-tuple domain and the symbolic residual rows must be
compared using duplicate-safe, hashability-safe markers.  Therefore an
unhashable but otherwise exact finite residual input tuple may be used as
explicit interval data, but missing, extra, and duplicate residual rows remain
finite certificate errors.  The family-by-family residual row-count ledgers
must use the same marker-safe comparison for count matching, while only known
endpoint-family labels can contribute to exact family scope; malformed or
unhashable family labels keep residual faithfulness open rather than causing
a runtime failure.  The family labels in the expected and covered
family-count rows are themselves finite certificate data: each must be a
hashable member of `{U,C,M}` before the row-count ledger can support either
residual faithfulness or residual-action scope.

The signed-generator audit for a claimed A proof must therefore establish:

```text
reachable_state_set_contains_initial_seeds,
reachable_state_set_is_signed_transition_closure,
reachable_state_ledger_duplicate_free,
kappa_seed_classifier_functional,
kappa_targets_in_U_C_M,
reachable_state_families_in_U_C_M,
all_signed_row_states_reachable,
fixed_endpoint_group_or_cutoff,
family_scoped_endpoint_target_coverage,
endpoint_target_families_in_U_C_M,
endpoint_target_size_rows_have_positive_integer_values,
endpoint_target_size_rows_have_two_field_shape,
endpoint_target_braid_index_independence,
endpoint_target_product_family_separation,
endpoint_target_ledgers_duplicate_free,
residual_endpoint_seed_state_coverage_exact,
residual_endpoint_family_ledgers_in_U_C_M,
residual_endpoint_seed_state_ledgers_duplicate_free,
residual_endpoint_seed_state_ledgers_well_formed,
multi_family_residual_row_counts_by_family_exact,
residual_row_counts_are_nonnegative_integers,
residual_family_row_counts_are_nonnegative_integers,
residual_family_row_count_rows_have_two_field_shape,
residual_family_row_count_families_in_U_C_M,
residual_rows_have_nonempty_arity_consistent_tuples,
residual_rows_have_duplicate_free_endpoint_channel_keys,
residual_rows_have_well_formed_endpoint_channel_keys,
residual_row_endpoint_channel_keys_match_row_seed_states,
residual_rows_include_required_input_and_channel_dependencies,
residual_action_input_tuple_domain_exact,
residual_endpoint_channel_reasons_exposed,
residual_theorem_rows_cover_input_domain,
residual_theorem_rows_cover_endpoint_families_and_seed_states,
residual_theorem_rows_use_only_allowed_initial_and_interval_data,
identity_endpoint_output_equals_input_on_every_residual_row,
signed_entry_domain_derived_from_interval,
signed_entry_domain_matches_current_interval,
finite_signed_row_checks_derived_from_tables,
signed_generator_domain_exact,
endpoint_observer_build_record_retained,
endpoint_observer_family_build_ledger_exact,
endpoint_observer_family_seed_classifier_ledger_well_formed,
endpoint_observer_family_build_row_failure_reasons_exposed,
endpoint_observer_family_auxiliary_rows_match_builds,
endpoint_observer_family_certificate_rows_match_builds,
endpoint_observer_family_detector_track_rows_match_builds,
endpoint_observer_family_endpoint_target_rows_match_builds,
endpoint_observer_family_cutoff_readout_rows_match_builds,
endpoint_observer_family_residual_theorem_rows_match_builds,
identity_endpoint_observer_constructor_keeps_residual_faithfulness_required,
identity_endpoint_observer_top_level_opt_in_is_nondecisive,
identity_endpoint_observer_cutoff_degree_ledger_exact,
strict_identity_fibre_action_residual_faithfulness_subcase,
coordinate_identity_fibre_action_residual_faithfulness_subcase,
singleton_fibre_action_residual_faithfulness_subcase,
fibre_label_identity_residual_faithfulness_subcase,
canonical_fibre_label_identity_residual_faithfulness_subcase,
automatic_identity_residual_faithfulness_consumer_subcases_only,
endpoint_observer_family_certificate_input_ledger_exact,
endpoint_observer_family_auxiliary_input_ledgers_exact,
endpoint_observer_each_active_family_single_scoped_and_proved,
endpoint_observer_family_build_matches_current_kappa_and_interval,
endpoint_observer_product_residual_faithfulness_for_multifamily_rows,
endpoint_observer_product_residual_family_scope_well_formed,
endpoint_observer_product_residual_channel_scope_matches_per_family,
endpoint_observer_product_residual_channel_key_scope_matches_per_family,
endpoint_observer_product_residual_channel_reasons_exposed,
endpoint_observer_family_build_closes_exact_active_families,
endpoint_observer_positive_rows_forced_from_typed_identity_rows,
endpoint_observer_monodromy_contexts_exposed,
endpoint_observer_monodromy_missing_adjacent_paths_exposed,
endpoint_observer_monodromy_family_labels_in_U_C_M,
endpoint_observer_monodromy_reachable_states_well_formed,
coordinate_components_match_T_plus_and_T_inverse,
all_signed_rows_defined,
signed_inverse_row_pairing,
signed_inverse_cancellation,
positive_state_coordinate_ybe_path,
state_coordinate_far_commutativity_path,
label_cocycles_derived_from_word_potential_not_independent,
fixed_detector_track_initialization,
detector_track_count_rows_use_only_U_C_M_families,
detector_track_count_family_labels_are_hashable_atoms,
detector_track_count_rows_have_positive_integer_counts,
detector_track_count_rows_have_two_field_shape,
detector_track_initialization_rows_exact,
detector_track_initialization_rows_are_finite_row_objects,
detector_track_initialization_rules_use_only_allowed_initial_data,
detector_track_initialization_keys_have_nonnegative_integer_indices,
detector_track_initialization_templates_use_same_track_raw_variables,
detector_track_initialization_values_in_endpoint_group,
artin_detector_recurrence,
word_potential_certificate_table_supplied,
word_potential_certificate_entry_domain_exact,
word_potential_certificate_next_states_and_labels_match_Gamma,
word_potential_identity_next_states_are_well_formed,
word_potential_templates_for_every_reachable_state,
word_potential_template_rows_have_two_field_shape,
word_potential_identity_rows_are_finite_row_objects,
monodromy_coboundary_emissions_derived_from_rho_and_W,
family_observers_derived_from_monodromy_coboundary_data,
monodromy_handoff_derives_explicit_residual_trivial_helpers,
identity_and_monodromy_handoffs_share_residual_helper_selector,
family_observer_auxiliary_family_labels_are_hashable_U_C_M_atoms,
post_linear_audit_consumes_monodromy_coboundary_family_data,
monodromy_family_raw_input_ledger_exact,
monodromy_family_raw_input_reports_missing_extra_duplicate_and_malformed_rows,
monodromy_family_raw_detector_domains_require_soundness_witnesses,
monodromy_family_detector_domain_entry_key_scope_exact,
monodromy_family_detector_domain_value_rows_well_formed,
monodromy_family_positive_entry_domain_exact,
monodromy_family_positive_rows_coordinate_match_interval,
monodromy_family_word_potential_template_state_domain_exact,
restricted_detector_domains_have_soundness_witnesses,
word_potential_templates_use_only_current_longitude_variables,
word_potential_artin_substitution_from_detector_recurrence,
word_potential_identity_for_every_positive_row,
initial_word_potential_normalization,
initial_word_potential_normalizes_every_kappa_seed,
fixed_detector_tracks_chosen_before_braid_word,
exact_cutoff_readouts_for_C_and_M,
cutoff_readout_seed_states_are_C_or_M_only,
cutoff_readout_seed_state_ledgers_duplicate_free,
cutoff_readout_family_scope_matches_exact_routed_C_M_families,
cutoff_readout_permutation_rows_exact_and_faithful,
residual_faithfulness_for_actual_fibre_action.
```

Only after those finite checks and the residual-faithfulness theorem are
proved may one use braid-word induction to claim that all endpoint labels
for family `E` lie in `V_beta(H_E)` for every braid index and that this
forces the true residual fibre action to be trivial.  Without them, endpoint
witnesses or symmetric cutoffs are merely candidate certificate shapes, not
a completed uniform proof.

System activation is then exact:

```text
System K active
  iff the raw post-linear K branch is active, no terminal proper closure has
      fired, and live_k_missing_latin_row_defects is nonempty.

System U active
  iff there is a direct triangular-recovery unit-longitude obstruction, or
      all live K rows have been removed and
      recovery_routed_k_missing_latin_row_defects is nonempty.

System C active
  iff all live K rows have been removed and
      continuation_routed_k_missing_latin_row_defects is nonempty.

System M active
  iff all live K rows have been removed and
      mixed_context_routed_k_missing_latin_row_defects is nonempty.
```

The endpoint systems U, C, and M may be active simultaneously.  Closing one
endpoint family removes only that family from the unclosed tuple; it does not
close the others.

### System K: Kink-Completion Missing-Latin Deficit

System K is the direct remaining triangular row-completion problem.  It
appears only after:

- the interval is in the local-minimal bi-free universal corridor bottleneck;
- triangular recovery is verified;
- product collapse, structural inconsistency, nondegenerate/guitar,
  side-dual Latin completion, and finite-linear routes have already been
  removed;
- the rack-kink all-pairs Latin hypotheses are still missing for at least
  one colour pair.

The live ledger is

```text
live_k_missing_latin_row_defects != empty.
```

Typical row reasons are:

```text
no_left_triangular_row
no_right_triangular_row
left_constant_map_proper_kernel
right_constant_map_proper_kernel
left_constant_map_universal_kernel
right_constant_map_universal_kernel
left_companion_sections_injective_non_surjective
right_companion_sections_injective_non_surjective
```

with the companion injective-nonsurjective case live only when supported by
a same-side constant-map kernel reason.  Unsupported companion block-image
rows are structural inconsistencies, not live System K branches.

For kernel defects, compute the generated admissible congruence closure of
one collapsed pair.  If the closure is proper, this contradicts
local-minimality and is terminal:

```text
closed_by_triangular_latin_proper_closure.
```

Such a row must not be routed into an endpoint family.  Only universal
closure rows can remain and route onward.

Constant-map kernel universal closure rows may be separated by the triangular
recovery inverse table; if that route is supplied and no live K rows remain,
they become System U endpoint obligations.  No-triangular rows may be
profiled into proper-kernel visible, coordinate-unit, partial-constant, or
cardinality/structural cases.  Coordinate-unit rows route to System M if
the coordinate-unit routing audit includes the coloured-YBE premise and the
opposite coordinate side contains nonunit data; partial-constant rows route
to System C if their universal continuation seed closure is supplied.
If a partial-constant no-triangular row has a proper generated closure, that
is also terminal:

```text
closed_by_missing_triangular_partial_constant_proper_closure.
```

Only universal partial-constant closure rows may route onward to System C.
The supplied partial-constant continuation route must match the closure row,
including closure kind, and must also land in a universal continuation seed
closure.  Containment in a nonuniversal continuation seed closure, or a route
whose closure kind does not match the partial-constant closure row, is not
enough to create a System C endpoint obligation; the row remains active
System K.

To prove A through System K, prove that every live K row is impossible in a
genuine local-minimal finite YBE interval, or route it through fixed detector
data to Systems U, C, or M.  Do not use an endpoint certificate to close K
until the K row itself has been eliminated or routed.

To prove B from System K, construct an explicit finite local interval with a
genuine live K defect, prove it survives all fixed finite detector groups,
and upgrade it to the normalized-law obstruction sequence described below.

### System U: Triangular-Recovery Unit Endpoint

System U is reached when a K deficit has been routed through triangular
recovery to a fixed finite unit group `U_tri`.  The group `U_tri` is the
finite permutation/unit group generated by the triangular recovery inverse
rows.  It is fixed by the interval and must not depend on `n`.
For a K-routed U row, the routed endpoint key is

```text
(left_color, right_color, defect_reason),
```

where `defect_reason` is the K reason routed by the recovery law.

The A-side target is:

```text
Every routed triangular-recovery endpoint lies in V_beta(U_tri)
for every braid beta in the relevant kernel N_n.
```

Acceptable proof formats include:

- active detector-lift rows proving the endpoint labels are evaluated
  recursive Artin longitudes;
- explicit endpoint-longitude expressions as products of evaluated
  recursive longitudes;
- derived-series reduction through `U_tri`, with abelian layers handled by
  the abelian longitude matrix criterion and any stable perfect residual
  handled separately;
- direct symbolic subgroup membership in `V_beta(U_tri)`;
- a faithful symmetric endpoint cutoff for the exact finite routed
  `U_tri` endpoint family.

A supplied symmetric endpoint cutoff for U is valid only when:

- it uses exactly the fixed group `U_tri`;
- it covers exactly the nonempty routed U endpoint keys for the K-routed
  family, with no duplicate routed keys and no duplicate covered keys;
- it proves endpoint-family faithfulness;
- identity symmetric-longitude data kills the whole finite U endpoint
  family.

A supplied U endpoint-witness certificate is valid only when:

- it uses the same fixed triangular recovery observer that defines `U_tri`;
- its keys are exactly the routed U endpoint keys, with no extra keys, no
  duplicate routed keys, and no duplicate witness keys;
- every supplied key has an endpoint-longitude expression certificate proving
  membership in `V_beta(U_tri)`;
- the routed key tuple is nonempty for K-routed U rows.

This is a certificate format, not a uniform theorem.  To prove A, construct
such certificates uniformly for every interval.  To prove B, exhibit a real
U endpoint miss that survives all fixed finite detectors and becomes a
normalized-law moving sequence.

### System C: Identity-Routed Universal-Continuation Endpoint

System C is reached when a partial-constant no-triangular row routes to the
universal-continuation seed channel.  The identity-routing ledger lists exact
lost fibre edges of the form

```text
(color, input_0, input_1).
```

The identity-routing ledger is valid only when it is non-vacuous and exact.
It must satisfy all of the following:

```text
lost_edges = seed_saturation_lost_edges,
routed_edges, unrouted_edges, and lost_edges are duplicate-free,
routed_edges union unrouted_edges = lost_edges,
routed_edges cap unrouted_edges = empty,
the routing labels distinguish exactly the routed_edges,
if universal collapse is forced then lost_edges is nonempty.
```

The A-side target is:

```text
Every identity-routed continuation lost edge has a fixed product
endpoint-longitude witness, or the exact continuation endpoint family has a
faithful symmetric endpoint cutoff.
```

A valid System C symmetric fork must:

- match the same identity-routing ledger;
- cover exactly the nonempty identity-routed lost edges, with no duplicate
  routed edges and no duplicate covered edges;
- prove endpoint-family faithfulness;
- prove that identity symmetric-longitude data kills those endpoint channels;
- introduce no extra edges.

Likewise, a System C endpoint-witness certificate must cover a nonempty
identity-routed edge tuple.  An empty witness list can be a harmless absence
of a C obligation, but it cannot close an active System C row.
The C endpoint-witness certificate is valid only when:

- the identity routing ledger itself proves the exact non-vacuous
  universal-continuation route, including duplicate-free lost, routed, and
  unrouted edge ledgers before endpoint witnesses are checked;
- the endpoint witness uses that same routing ledger;
- every routed lost edge has an endpoint-longitude expression certificate;
- no witness is supplied for an edge outside the routed lost-edge tuple;
- the routed-edge ledger and witness-edge ledger are duplicate-free.

To prove B from C, exhibit a genuine routed continuation endpoint miss,
prove that no fixed finite endpoint detector kills it, and upgrade it to a
normalized-law sequence with explicit moved residual tuples.

### System M: Mixed-Unit Context Endpoint

System M is reached when a coordinate-unit no-triangular row is routed to a
mixed-unit context.  A mixed context endpoint key has the form

```text
(left_color, right_color, side),
```

where `side` records which coordinate side is the unit side in the mixed
row.

The A-side target is:

```text
Every routed mixed-unit context endpoint factors through fixed
detector/readout data, or the exact mixed endpoint family has a faithful
symmetric endpoint cutoff.
```

A valid System M symmetric fork must:

- match the coordinate-unit routing ledger;
- cover exactly the nonempty mixed-unit context keys, with no duplicate
  routed context keys and no duplicate covered keys;
- prove endpoint-family faithfulness;
- prove that identity symmetric-longitude data kills those endpoint channels;
- introduce no extra keys.

A valid System M endpoint-witness certificate must:

- use the same coordinate-unit routing ledger that created System M;
- require that ledger to prove coloured-YBE and complete coordinate-unit
  routing, including duplicate-free route rows and duplicate-free listed
  coordinate-unit sides;
- form keys `(left_color,right_color,side)` for every mixed-unit context row
  and every routed coordinate-unit side in that row;
- cover exactly that nonempty key tuple with endpoint-longitude expression
  certificates;
- introduce no extra keys;
- the routed mixed-context key ledger and witness-key ledger are
  duplicate-free.

To prove B from M, find a genuine mixed-unit endpoint miss, prove it survives
all fixed finite detector groups, and upgrade it to the normalized-law
obstruction sequence.

## 7. Product Endpoint Guardrail

Systems U, C, and M may appear simultaneously in a product endpoint row.  The
unclosed endpoint tuple is family-wise:

```text
unclosed_routed_endpoint_systems subset {U,C,M}.
```

A witness or symmetric fork for one family removes only that family.  For
example, a U certificate cannot hide an unclosed C or M obligation.  A
complete A proof must close every active endpoint family in the product.  A
complete B proof may use one unclosed family only after proving it cannot be
killed by any fixed finite detector group.

## 8. Endpoint Certificate Formats

An endpoint-longitude expression certificate for a finite endpoint group `H`
is an explicit identity

```text
endpoint(beta) =
product_m phi_m(L_{i_m}(beta))^{epsilon_m}
```

inside `H`, where each `phi_m:F_n->H` is a group homomorphism and each
`epsilon_m` is `+1` or `-1`.  The homomorphisms may vary from factor to
factor because `V_beta(H)` is generated by all evaluated longitude values.
Such an expression proves `endpoint(beta) in V_beta(H)`.

For several endpoint groups `H_s`, factorwise endpoint witnesses assemble
into one witness in the fixed product group `prod_s H_s`, because
`V_beta(prod_s H_s)=prod_s V_beta(H_s)`.

An Artin-defect certificate is a display of an endpoint as a product of
values of

```text
beta(w) p_beta(w)^-1
```

in fixed detector factors.  Such Artin permutation defects lie in the normal
closure of the recursive Artin longitudes, hence their finite-group values
lie in `V_beta(G)`.  This is a strong A-side format when the local algebra
supplies it.

A detector-lift certificate supplies finite local row identities in a fixed
group `U` with live-strand labels `(m_i,u_i)`, proving by induction on braid
words that the terminal `u_i` labels are evaluated recursive Artin
longitudes.  This converts finite row checks into an all-`n` endpoint proof.

A symmetric endpoint cutoff for a finite family of endpoint groups is a
single symmetric degree `m` such that identity Artin-longitude data in
`S_m` kills every endpoint channel in the family, together with a faithful
readout showing that killed endpoints imply the residual endpoint motion is
trivial.  It is valid only for the exact covered family.

## 9. Normalized-Law Counterexample Route

A B outcome cannot be a finite failed detector, a timeout, or a fixed-degree
search result.  It must defeat every finite group, hence every finite rack
through the sharp obstruction theorem.

A normalized-law obstruction sequence consists of:

- finite braid indices `q_j -> infinity`;
- explicit braids `beta_j in B_{q_j}`;
- an explicit finite YBE solution `X`;
- explicit tuples in `X^{q_j}` moved by `rho_{X,q_j}(beta_j)`;
- proof that for every finite group `G`, eventually

```text
Lambda_{G,q_j}(beta_j) = Lambda_{G,q_j}(1);
```

- proof that the movement persists after the right-stabilization or
  Brunnian embedding used to hide from finite groups.

Each local normalized-law prefix row used for this B route must be a finite
table-derived row.  The row must display the source base tuple, source fibre
tuple, source images, stabilized base tuple, stabilized fibre tuple, and
stabilized images.  Quotient-base fixing, staying over the base, and
source/target residual movement must be derived from these tuples.  The row
must also state that the base-detector identity action and finite-group
longitude identity signatures were computed from the supplied braid,
detector, and finite group tables.  Boolean assertions that the residual tuple
is moved or that the row is invisible to the detector are not certificates.

One common way to prove finite-group invisibility is to choose group words
`w_j` that are laws on every finite group of order at most `j`, embed them
as pure or Brunnian braid words, and right-stabilize so that every fixed
finite group is eventually below the threshold.  This is not enough by
itself: the resulting braids must still move explicit residual tuples of one
fixed finite YBE solution `X`.

If returning B, you must give:

- the finite set `X`;
- the full bijection table for `R_X:X^2->X^2`;
- a symbolic proof of the Yang-Baxter equation;
- the explicit braid sequence `beta_j`;
- explicit moved tuples;
- proof of eventual finite-`G` Artin-longitude invisibility for every finite
  group `G`;
- proof that the sharp finite-group obstruction theorem converts this into
  non-domination by every finite rack.

## 10. Conditional Global Assembly

The global assembly is conditionally closed once the local U/C/M endpoint
observer lemma is supplied.  The remaining obstruction is local, not a
separate product or congruence-chain gap.

Conditional theorem: assume that every finite local-minimal post-linear
coloured YBE interval surviving the stated reductions has, for each active
routed endpoint family `E in {U,C,M}`, a finite endpoint observer

```text
S_E^reach,  H_E or S_mE,  Gamma^{E,+/-},  W_s,
```

with exact cutoff readouts where needed, such that:

```text
S_E^reach is the exact signed-transition closure of kappa(K_nabla);
Gamma^{E,+/-} is defined on the full D_Gamma(E);
positive state/coordinate endpoint maps satisfy adjacent YBE and
  far-commutativity;
negative rows are actual inverses of positive rows;
the fixed-assignment word-potential detector lift proves
  endpoint_E(beta) in V_beta(H_E) for every braid index n and every beta in N_n;
product endpoint rows are separated family-by-family;
killed active routed endpoint channels imply Delta_n(beta)=1.
```

Then finite-rack domination follows for every finite bijective
set-theoretic Yang-Baxter solution.

For one quotient interval `pi:X->Z`, suppose `Z` is already dominated by a
finite rack `Q`, and set `N_n=ker rho_{Q,n}`.  Let
`G_known,1,...,G_known,r` be the fixed detector groups for the branches that
were already closed before U/C/M.  Let `F subset {U,C,M}` be the active
routed endpoint family set, and write `H_E=S_mE` when `E` is handled by a
symmetric cutoff.  Define the finite group

```text
G(pi,Q) =
  (prod_{j=1}^r G_known,j) x (prod_{E in F} H_E).
```

This group depends only on the finite interval and the already chosen rack
`Q`, not on the braid index.  If

```text
Lambda_{G(pi,Q),n}(beta)=Lambda_{G(pi,Q),n}(1),
```

then projection to every factor gives identity longitude data in each fixed
factor.  The product identity

```text
V_beta(prod_s G_s)=prod_s V_beta(G_s)
```

kills every known residual channel and every active endpoint channel
componentwise, with no cross-family cancellation.  The local
residual-faithfulness theorem then gives `Delta_n(beta)=1` for every
`beta in N_n`.  Hence the sharp finite-group obstruction theorem says that
`Q x A_{G(pi,Q)}` dominates the interval.

For a maximal congruence chain

```text
Delta_X=kappa_0 < kappa_1 < ... < kappa_m=Nabla_X,
```

start from the one-point quotient, dominated by the one-point rack, and move
down the chain.  If `X/kappa_{i+1}` is dominated by a finite rack `Q_{i+1}`,
apply the local construction to
`X/kappa_i -> X/kappa_{i+1}` and set

```text
Q_i = Q_{i+1} x A_{G(pi_i,Q_{i+1})}.
```

The chain is finite, and every group factor is finite and independent of
braid index, so the final rack `Q_0` is finite, independent of `n`, and
dominates `X`.  Thus a complete A proof now only needs the local U/C/M
endpoint-observer lemma; unsupported companion block-image rows are closed by
the finite triangular bijection cardinality contradiction recorded above.

At the executable handoff level, an endpoint-observer closure verdict may be
fed into the congruence-chain rack assembly only together with the actual
fixed detector product group for that interval.  A bare verdict such as
one of the one-family `closed_by_*_endpoint_observer_family_build` verdicts,
the product verdict `closed_by_endpoint_observer_family_build`, or a legacy
endpoint-witness/symmetric-fork candidate without its group `G(pi,Q)` and
residual-faithfulness bridge is still an open local gap.

## 11. What Must Be Done To Resolve The Problem

1. Prove or repair the post-linear reduction.

   Show symbolically that after the already closed branches listed above,
   every remaining local-minimal primitive overlap is genuinely one of
   System K, U, C, M, with product endpoint rows handled family-by-family.
   If any reduction is only conditional, either prove its missing condition
   or keep that condition as an explicit open obligation.

2. Close or refute System K.

   A direct System K survivor has nonempty `live_k_missing_latin_row_defects`.
   First construct the finite normal-form table `K_nabla` and the seed
   classifier `kappa` exactly as specified above.  To prove A, show that
   every live missing-Latin triangular defect is impossible in a genuine
   local-minimal finite YBE interval, or route it through `kappa` into fixed
   detector data for U, C, or M.  Proper generated closures are already
   terminal contradictions; universal closures are the only endpoint-routing
   candidates.  Unsupported companion block-image rows are not endpoint
   candidates; they are excluded by the exact finite
   `finite_triangular_bijection_cardinality_contradiction` table described
   above.

   To prove B from K, construct a genuine live K interval, prove all fixed
   finite detector groups fail, and upgrade the failure to a normalized-law
   moving sequence.

3. Close or refute System U.

   Define `S_U^reach` from the exact `S_U` values hit by `kappa`, define the
   positive local context monodromy presentation, construct a finite
   permutation representation `rho_U:Pi_U->Sym(S_U^reach)`, define fixed
   detector-track initialization rules, prove the Artin detector recurrence,
   define word templates `W_s` for all reachable states, prove every
   nonabelian coboundary defect is constant on a sound detector domain, and
   derive the positive endpoint emissions from those constant values.  Build
   the observer by deriving positive rows from the identity-row table and
   negative rows as actual inverses, then prove residual faithfulness.  Then
   prove uniformly in `n` that every routed
   triangular-recovery endpoint lies in `V_beta(U_tri)`.  Legacy
   triangular-recovery endpoint-witness or symmetric-fork ledgers may be
   recorded as diagnostics, but they do not close U unless they are lifted to
   this exact `U_tri` observer and residual-faithfulness bridge.  Otherwise,
   extract a normalized-law B sequence from a genuine U endpoint miss.

4. Close or refute System C.

   Define `S_C^reach` from the exact `S_C` values hit by `kappa`, define the
   positive local context monodromy presentation, construct a finite
   permutation representation `rho_C:Pi_C->Sym(S_C^reach)`, construct fixed
   detector-track initialization rules, prove the Artin detector recurrence,
   define word templates, prove every nonabelian coboundary defect is
   constant on a sound detector domain, derive endpoint emissions from those
   constants, build the observer with inverse-derived negative rows, and
   construct exact
   faithful cutoff readouts for the routed identity-continuation ledger.
   Legacy endpoint-witness or symmetric-fork ledgers may be recorded as
   diagnostics, but they do not close C unless they are lifted to this exact
   observer/cutoff-readout and residual-faithfulness bridge.  Otherwise,
   extract a normalized-law B sequence from a genuine C endpoint miss.

5. Close or refute System M.

   Define `S_M^reach` from the exact `S_M` values hit by `kappa`, define the
   positive local context monodromy presentation, construct a finite
   permutation representation `rho_M:Pi_M->Sym(S_M^reach)`, construct fixed
   detector-track initialization rules, prove the Artin detector recurrence,
   define word templates, prove every nonabelian coboundary defect is
   constant on a sound detector domain, derive endpoint emissions from those
   constants, build the observer with inverse-derived negative rows, and
   construct exact
   faithful cutoff readouts for the routed mixed-unit ledger.  Legacy
   endpoint-witness or symmetric-fork ledgers may be recorded as diagnostics,
   but they do not close M unless they are lifted to this exact
   observer/cutoff-readout and residual-faithfulness bridge.  Otherwise,
   extract a normalized-law B sequence from a genuine M endpoint miss.

6. Assemble outcome A if K/U/C/M all close.

   Construct the local detector group `G(pi,Q)` as one fixed finite product
   of all required detector factors: Green, Schutzenberger, atom, known
   branch, endpoint/unit, transport-state, and any new U/C/M endpoint
   factors.  Prove for every `n`:

   ```text
   Lambda_{G,n}(beta)=Lambda_{G,n}(1) => Delta_n(beta)=1.
   ```

   Then apply the sharp rack `Q x A_G` at each congruence-chain interval to
   produce the final finite rack.  Verify that every factor is finite and
   independent of `n`.

7. Assemble outcome B if any system cannot close.

   Provide the explicit finite YBE solution, symbolic YBE proof, braid
   sequence, finite-group invisibility proof, moved tuples, and sharp
   obstruction argument described in Section 9.

## 12. Mandatory Final Audit

Before returning a claimed resolution, explicitly answer:

1. Is any decisive step finite-search-only?
2. Are semisplit local-minimal families fully handled?
3. Is `K_nabla` exactly the finite universal-K row-normal-form domain above,
   with no proper-closure, equality-closure, two-sided-unit, failed-route, or
   unsupported companion row included?
4. Is `kappa(d)` defined for every `d in K_nabla`, with values in exactly
   one of `S_U`, `S_C`, or `S_M`, and is the classifier ledger duplicate-free
   and functional on row descriptors, with no target outside `{U,C,M}`?
5. Are unsupported companion block-image rows proved structural
   inconsistencies rather than endpoint seeds by the exact finite
   `finite_triangular_bijection_cardinality_contradiction` table covering
   every `(side,left_color,right_color)` row, with no missing, extra, or
   duplicate rows and no circular appeal to `triangular_structural_inconsistency`?
6. Are `S_U`, `S_C`, and `S_M` the exact finite seed state spaces, and are
   the finite reachable sets `S_U^reach`, `S_C^reach`, and `S_M^reach`
   constructed as duplicate-free exact signed-transition closures of those
   seeds, with no reachable state family outside `{U,C,M}`?
7. Are all signed endpoint generator tables
   `Gamma^{U,+/-}`, `Gamma^{C,+/-}`, and `Gamma^{M,+/-}` defined on those
   exact reachable state spaces and on every entry of `D_Gamma`, not merely
   one entry per seed and sign?
8. Do the endpoint generator tables satisfy the reduced full-braid observer
   certificate: a finite monodromy presentation on positive local contexts,
   a finite permutation representation on the exact reachable states,
   positive state/coordinate adjacent YBE path, state/coordinate
   far-commutativity for disjoint crossings, negative rows defined as actual
   inverses of positive rows, and the fixed-assignment detector-lift
   telescope?  The telescope must include fixed detector tracks chosen before
   the braid, track initialization from interval data, every raw assignment
   variable used by a substitution initialized by its track, the Artin
   detector recurrence, word templates `W_s` for every reachable endpoint
   state using only current longitude variables whose track indices are
   declared and initialized, the induced positive Artin substitution, the
   constant-defect identity
   `W_s(U)^-1 W_{s'}(A_gamma^+(U,A))=h` for every positive row on a sound
   detector domain, initial normalization on exactly the current `kappa` seed
   image, and exact `D_Gamma` coverage?  Are endpoint emissions derived from
   constant coboundary defects, and are adjacent/far label cocycles treated
   as derived from this word-potential certificate rather than as independent
   local assumptions?
9. For cutoff families C and M, are the readouts faithful on exactly their
   routed ledgers with no extra channels and no duplicated seed-state entries?
10. Is every detector group, endpoint group, cutoff group, and rack
   independent of braid index `n`, and does the endpoint-target certificate
   cover exactly the routed U/C/M families with fixed positive orders or
   cutoff degrees and product-family separation, with the concrete endpoint
   group order matching the product of the group-valued target orders and
   each C/M cutoff target degree matching the cutoff-readout symmetric degree?
11. Are product endpoint rows handled family-by-family without hiding any
   unclosed U, C, or M obligation?
12. Does every residual-faithfulness theorem or residual-action row proof
   cover exactly the routed endpoint seed states hit by `kappa`, not merely
   the family names?
13. Are the endpoint-target, residual-family, and residual-seed ledgers
   duplicate-free, so exact coverage is not obtained only after silently
   deduplicating repeated entries?
14. If returning A, where exactly is `G(pi,Q)` constructed, why does it prove
   the all-`n` residual implication, and how does the congruence-chain
   induction produce the final finite rack?
15. If returning B, why does the obstruction defeat every finite group `G`,
   hence every finite rack through the sharp obstruction theorem?

Return outcome A or outcome B only if the proof is genuinely complete.  If
neither outcome can be completed, state the exact missing lemma or exact
missing counterexample ingredient and the shortest route to settle it.
