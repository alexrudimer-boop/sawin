# YBE equivariant reconstruction closure audit

Date: 2026-06-03

This generated audit records the sharp gluing theorem for finite
families of known quotient, subsolution, and subquotient detector
towers.  The safe principle is not merely that dominated pieces
exist; their marked braid-action factors must reconstruct the whole
`X^n` action equivariantly and injectively, or the visible kernel
must be proved trivial on hidden reconstruction fibres.

## Flags

- marked tower reconstruction recorded: `True`;
- product kernel implication recorded: `True`;
- total quotient corollary recorded: `True`;
- partial domain totalization required: `True`;
- point separation insufficient recorded: `True`;
- off-diagonal transition data required: `True`;
- arity-3 extension cocycle obstruction recorded: `True`;
- hidden fibre kernel criterion recorded: `True`;
- records equivariant reconstruction closure gate: `True`.

## Formulas

- reconstruction: `R_n:X^n -> product_j T_{j,n} is B_n-equivariant and injective for every n`;
- product kernel: `ker rho_product,n <= ker rho_X,n follows from equivariant injective reconstruction`;
- total quotients: `for genuine YBE quotients pi_j, injective pi:X->product_j Z_j implies injective pi^n:X^n->product_j Z_j^n`;
- visible kernel: `K_vis,n = intersection_j ker(B_n action on T_{j,n}) may still act on hidden fibres if R_n is not injective`;
- hidden fibres: `visible detectors dominate iff K_vis,n acts trivially on every H_t=F_n^-1(t)`;
- partial domains: `partial subquotient data must be totalized by recording domain, incidence, exits, and braid transport of definedness`;
- extension cocycle: `mixed-block extension fibres can carry a coherent omega_{z,z'} action invisible to diagonal detectors`;
- arity-3 stress test: `arity 3 tests whether the two YBE paths agree visibly but differ by hidden fibre transport`.

## Rows

### marked_tower_reconstruction

- role: `sufficient_data`;
- statement: for every n, the chosen quotient, block, and subquotient readouts assemble to a B_n-equivariant map R_n:X^n -> product_j T_{j,n};
- consequence: the product factors describe the same marked braid-action tower only when R_n is injective on the actual X^n states.

### product_kernel_implication

- role: `positive_theorem`;
- statement: if each factor T_j is dominated by a finite rack detector Y_j and R_n is B_n-equivariant and injective for all n, then the product rack detector prod_j Y_j dominates X;
- consequence: a braid acting trivially on every rack factor fixes every T_{j,n}-coordinate, hence fixes R_n(x), hence fixes x by injectivity.

### total_quotient_corollary

- role: `quotient_corollary`;
- statement: if pi_j:X -> Z_j are genuine YBE quotient maps and the combined map pi=(pi_j)_j is injective on X, then pi^n is B_n-equivariant and injective on X^n for every n;
- consequence: point-separating total quotient maps are enough when they are genuine YBE quotients and each Z_j is already dominated.

### partial_subquotient_domain_totalization

- role: `domain_guardrail`;
- statement: partial subquotients and crossing-closed blocks must be encoded as total marked factors, including their defined domain, incidence, and exit data;
- consequence: a partial map that is injective only on its own domain cannot be used in a product proof until the product records which tuples lie in that domain after every braid move.

### point_separation_not_enough

- role: `negative_warning`;
- statement: coordinatewise point-separating quotients, or separately dominated crossing-closed components, need not reconstruct the all-arity marked action tower;
- consequence: two tuples can agree in every visible component while a braid in the visible kernel permutes hidden extension fibres.

### off_diagonal_transition_data

- role: `missing_data`;
- statement: mixed-block crossings require explicit block incidence maps, transition groupoids, and fibre actions over the visible quotient states;
- consequence: the gluing theorem needs the off-diagonal transition data, not just detectors for the diagonal components.

### arity3_extension_cocycle_obstruction

- role: `arity3_stress`;
- statement: at arity 3, the two YBE paths can agree in all visible quotients while differing by a coherent extension-fibre cocycle omega_{z,z'};
- consequence: the YBE equation makes this hidden fibre action coherent, but it does not force it to be visible to the chosen product detectors.

### hidden_fibre_visible_kernel_criterion

- role: `exact_criterion`;
- statement: for any finite family of visible marked factors, the visible kernel K_vis,n must act trivially on every hidden fibre H_t=F_n^-1(t);
- consequence: visible product detectors dominate X if and only if this hidden-fibre action is trivial; injective reconstruction is the simple sufficient case where all H_t are singletons.

## Meaning

If total marked factors `T^alpha_bullet` are dominated by finite
racks and the product map `F_n:X^n -> product_alpha T^alpha_n`
is `B_n`-equivariant and injective for every `n`, then the
coordinatewise product rack dominates `X`.  This is just the
kernel argument through the product action.

For genuine total YBE quotients, point-separating quotient maps
are enough because the coordinatewise product remains injective
in every arity.  For partial subquotients or block data, one must
first promote the data to total marked braid factors.  If the
visible product map is not injective, the exact remaining
criterion is triviality of the visible-kernel action on each
hidden reconstruction fibre.
