# YBE inverse-branch determinization audit

Date: 2026-06-03

This generated audit records the sharpened boundary of the
degenerate guitar route.  Replacing the suffix group `G_rho` by the
finite transformation monoid `M_rho` gives a finite memory set, but
a total deterministic monoid-guitar decoder would force the relevant
one-sided YBE actions to be surjective, hence bijective for finite
`X`.  Thus powersets, relation-valued branches, and Green-class data
do not by themselves give a total rack cover in the genuinely
degenerate case.

## Flags

- total decoder surjectivity recorded: `True`;
- local surjectivity equation recorded: `True`;
- finite side bijection forced: `True`;
- total monoid-guitar negative recorded: `True`;
- powerset/relation failure recorded: `True`;
- Green rank-drop failure recorded: `True`;
- restricted-language cocycle recorded: `True`;
- nondeterministic kernel gap recorded: `True`;
- records inverse-branch determinization gate: `True`.

## Formulas

- initial state: `Phi_1(a)=d(q0,a) is surjective, and Phi_2 is surjective through every one-step reachable state tau(q0,a)`;
- local surjectivity equation: `d(tau(q,a > b),a)=rho_{d(tau(q,a),b)}(d(q,a))`;
- forced bijection: `total decoding implies R_y(X)=X for every y; finite X then implies every R_y is bijective`;
- monoid rank: `rank(q R_x) < rank(q) gives outputs a with (q R_x)^-1(a)=empty`;
- branch cocycle: `on any restricted language, branch selectors must satisfy closure plus the arity-3 rack self-distributivity cocycle`.

## Rows

### total_decoder_surjectivity

- role: `hypothesis`;
- statement: a total finite-state rack decoder must give surjective maps Phi_n:Y^n -> X^n for all n, so every one-step reachable decoder state must still realize every next X-symbol;
- consequence: the local two-symbol equations may be tested at arbitrary right outputs, not only at outputs lying in an image of a rank-dropping suffix transformation.

### local_equation_forces_side_surjectivity

- role: `negative_total_decoder`;
- statement: the decoder equation for the copied rack strand forces every target value rho_y(x) to appear as a decoded value with fixed old rack symbol a once x=d(q,a) and y is the decoded neighbor;
- consequence: for the right-guitar convention, total deterministic decoding forces R_y(X)=X for every y; since X is finite, all R_y are bijections.

### rank_drop_empty_inverse_fibre

- role: `first_failure`;
- statement: if some R_y is not surjective, a monoid state q followed by R_y has an output a with empty inverse fibre under q R_y;
- consequence: the branch value d(q R_y,a) cannot be total; the obstruction appears before any high-arity rack cocycle.

### powerset_relation_not_rack

- role: `failed_determinization`;
- statement: direct or inverse image operations on subsets are not bijective when a finite transformation is nonbijective, and saturated subsets lose singleton separation;
- consequence: powerset or relation-valued guitars preserve possible branches but do not produce a rack action proving pointwise kernel inclusion on X^n.

### green_schutzenberger_no_rank_repair

- role: `semigroup_warning`;
- statement: Green R-class and Schutzenberger coordinates describe the regular part of M_rho but do not undo a transition that drops image rank from the identity state;
- consequence: finite semigroup labels are useful diagnostics, but a rank-dropping generator still creates empty branch fibres for a total decoder.

### restricted_language_branch_cocycle

- role: `remaining_restricted_problem`;
- statement: if one restricts to a proper invariant language where empty fibres are avoided, the selected partial inverse branches must satisfy closure equations and an arity-3 rack self-distributivity cocycle;
- consequence: the obstruction can move from arity 2 to arity 3 only after abandoning total decoding on all of Y^n.

### nondeterministic_kernel_gap

- role: `kernel_gap`;
- statement: a nondeterministic relation-valued decoder can record that some inverse branch exists, but it does not give a functional braid action on a finite rack alphabet;
- consequence: Sawin kernel inclusion requires deterministic finite labels or an equivalent marked quotient, not merely preservation of a relation of possible decodings.

## Meaning

This does not refute finite rack domination.  It refutes a
specific tempting shortcut: a total finite monoid-guitar
determinization on all words.  If a degenerate solution is still
rack-dominated, the cover must either use a non-guitar finite
decoder or work through a restricted invariant language whose
partial branch choices satisfy the remaining arity-3 cocycle.
