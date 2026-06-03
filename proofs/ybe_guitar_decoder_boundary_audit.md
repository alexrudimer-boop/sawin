# YBE guitar decoder boundary audit

Date: 2026-06-03

This generated audit records the exact boundary between the
one-sided nondegenerate guitar-map theorem and the genuinely
degenerate finite-state decoder problem.  In the nondegenerate
branch, the decoder state is a finite group of suffix actions.  In
the degenerate branch, the corresponding transformation monoid is
still finite, but inverse branches are not canonical and become a
deterministic cocycle obligation.

## Flags

- right-guitar hypothesis recorded: `True`;
- derived rack operation recorded: `True`;
- all-arity kernel equality recorded: `True`;
- finite-state decoder realization recorded: `True`;
- degenerate J2 failure recorded: `True`;
- monoid inverse-branch gate recorded: `True`;
- no automatic unbounded-memory obstruction recorded: `True`;
- deterministic decoder obligation recorded: `True`;
- records guitar decoder boundary: `True`.

## Formulas

- right guitar: `R_y(x)=rho_y(x); if every R_y is bijective, J_n(x_1,...,x_n)=(R_{x_n}...R_{x_2}(x_1),...,x_n)`;
- derived rack: `a < b = R_a(lambda_{R_b^-1(a)}(b))`;
- kernel equality: `J_n rho_X,n(beta)=rho_Y,n(beta) J_n, hence ker rho_Y,n = ker rho_X,n for every n`;
- decoder state: `Q=G_rho, d(q,a)=q^-1(a), tau(q,a)=q R_{q^-1(a)}`;
- degenerate J2 failure: `J_2(x,y)=(R_y(x),y), so nonbijective R_y makes J_2 nonbijective`;
- monoid gate: `Q=M_rho requires d(q,a) in q^-1(a), tau(q,a)=q R_{d(q,a)}, and the finite-state cocycle equations`.

## Rows

### right_nondegenerate_guitar_theorem

- role: `positive_known_theorem`;
- statement: if every right action R_y(x)=rho_y(x) is bijective, the right-guitar maps J_n are triangular bijections in every arity;
- consequence: the relevant nondegenerate branch is not a search result; it is closed by the standard guitar-map conjugacy theorem.

### derived_rack_domination

- role: `positive_domination`;
- statement: the derived operation a < b = R_a(lambda_{R_b^-1(a)}(b)) is a finite rack operation and its braid action is conjugate to the YBE action;
- consequence: taking Y to be this derived rack gives kernel equality, hence finite rack domination, for every braid arity.

### finite_state_decoder_realization

- role: `decoder_model`;
- statement: the inverse guitar map is a finite-state decoder with Q=G_rho, d(q,a)=q^-1(a), and tau(q,a)=q R_{q^-1(a)};
- consequence: the finite-state rack-cover equations are solved exactly in the one-sided nondegenerate case.

### degenerate_j2_failure

- role: `first_failure`;
- statement: if some R_y is not bijective, then J_2(x,y)=(R_y(x),y) is not bijective and the derived formula needs a noncanonical preimage R_b^-1(a);
- consequence: the degenerate obstruction begins at inverse-branch choice, not at high arity or whole-image exponent growth.

### monoid_inverse_branch_gate

- role: `finite_repair_gate`;
- statement: the transformation monoid M_rho is finite, but a decoder using Q=M_rho needs choices d(q,a) in q^-1(a) and updates tau(q,a)=q R_{d(q,a)};
- consequence: finite memory is available, but braid compatibility becomes a finite inverse-branch cocycle system.

### deterministic_decoder_obligation

- role: `remaining_obligation`;
- statement: relation-valued or nondeterministic inverse branches do not give Sawin kernel inclusion unless they determinize to finite labels satisfying rack self-distributivity and decoder equations;
- consequence: the unresolved degenerate regime is exactly the search for coherent deterministic finite decoder labels.

## Meaning

The one-sided nondegenerate branch is closed: the finite derived
rack has braid-action kernels equal to the original YBE solution
in every arity.  This is precisely the finite-state decoder
criterion with `Q=G_rho` and inverse suffix states.

The degenerate branch does not automatically require unbounded
memory, because `M_rho` is finite.  The missing theorem is sharper:
choose coherent inverse branches over `M_rho` that satisfy the
finite-state decoder equations and make the induced operation a
rack.  Failure of those deterministic branch choices is the next
direct-cover obstruction.
