# YBE finite-state rack-cover audit

Date: 2026-06-03

This generated audit records the obstruction to the most tempting
direct rack-cover construction.  A rack crossing copies one strand,
whereas a general bijective YBE crossing updates both strands.  Finite
labels attached coordinatewise to `X` do not remove that mismatch.
The only remaining direct-cover formulation is a finite-state decoder
whose state can reinterpret the copied rack strand after a crossing.

## Flags

- coordinatewise rack quotient obstruction identified: `True`;
- fibre-label first-coordinate obstruction identified: `True`;
- rack-shadow identity recorded: `True`;
- label cocycle equation recorded: `True`;
- finite-state decoder criterion recorded: `True`;
- decoder surjectivity requirement recorded: `True`;
- structure-group obstruction recorded: `True`;
- right-update defect identified: `True`;
- records finite-state rack-cover criterion: `True`.

## Formulas

- rack switch: `R_Y(a,b)=(a > b,a)`;
- coordinatewise obstruction: `pi(a)=rho_{pi(b)}(pi(a)); surjectivity implies rho_y(x)=x`;
- rack-shadow identity: `lambda_x lambda_y = lambda_{lambda_x(y)} lambda_x`;
- YBE twisted identity: `lambda_x lambda_y = lambda_{lambda_x(y)} lambda_{rho_y(x)}`;
- label cocycle: `alpha_{x,lambda_y(z)}(s,alpha_{y,z}(t,u)) = alpha_{lambda_x(y),lambda_x(z)}(alpha_{x,y}(s,t),alpha_{x,z}(s,u))`;
- decoder equations: `d(q,a > b)=lambda_{d(q,a)}(d(tau(q,a),b)); d(tau(q,a > b),a)=rho_{d(tau(q,a),b)}(d(q,a)); tau(tau(q,a > b),a)=tau(tau(q,a),b)`;
- right-update defect: `Delta(x,y)=lambda_{rho_y(x)} lambda_x^-1`.

## Rows

### coordinatewise_rack_quotient_obstruction

- role: `negative_coordinatewise`;
- statement: if pi:Y -> X is a coordinatewise quotient from a rack switch R_Y(a,b)=(a > b,a), then pi(a)=rho_{pi(b)}(pi(a)) for all a,b;
- consequence: surjectivity forces rho_y(x)=x for every x,y, so general YBE solutions cannot be covered coordinatewise by a rack.

### fiber_label_first_coordinate_obstruction

- role: `negative_fiber_label`;
- statement: a fibre-labelled operation (x,s)>(y,t) with first coordinate lambda_x(y) requires the maps lambda_x to be bijective and cannot repair first-coordinate identities using labels;
- consequence: left-degenerate solutions are excluded immediately, and even nondegenerate solutions face a rack-shadow identity stronger than the YBE identity.

### rack_shadow_identity_gap

- role: `operator_gap`;
- statement: rack self-distributivity forces lambda_x lambda_y = lambda_{lambda_x(y)} lambda_x, while YBE gives lambda_x lambda_y = lambda_{lambda_x(y)} lambda_{rho_y(x)};
- consequence: the copied rack strand would need to carry future operator lambda_{rho_y(x)} even though it remains the old x-strand.

### label_cocycle_equation

- role: `remaining_label_problem`;
- statement: if the first-coordinate gap vanishes, the fibre labels must still solve a nonabelian rack cocycle equation for alpha;
- consequence: finite labels are extra data; the YBE equations do not by themselves supply the required alpha-cocycle.

### finite_state_decoder_criterion

- role: `positive_reformulation`;
- statement: a marked quotient can only evade the copy obstruction by using a finite decoder state q with maps d:Q x Y -> X and tau:Q x Y -> Q satisfying the local two-symbol equations;
- consequence: finite rack domination by a direct cover reduces to a finite transducer/cocycle problem plus surjectivity of every decoded map Phi_n.

### structure_group_same_copy_obstruction

- role: `group_rack_warning`;
- statement: a finite quotient of the structure group used as a conjugation rack has the same copied second output g in (g,h)->(ghg^-1,g);
- consequence: without finite decoder context, the group-rack approach also cannot make the copied x-strand represent rho_y(x).

## Meaning

The naive coordinatewise construction is not a proof strategy for
Sawin's question.  It would force the right action to be trivial
under the rack convention `R_Y(a,b)=(a > b,a)`, and the opposite
convention analogously forces the left action to be trivial.

The sharper positive route is finite-state rather than
coordinatewise: find a finite rack `Y`, a finite decoder state set
`Q`, maps `d` and `tau`, and surjective decoded maps `Phi_n` for
every arity.  The sharper negative route is to prove that no such
finite decoder can absorb the right-update defect
`Delta(x,y)=lambda_{rho_y(x)} lambda_x^-1` for a given solution.
