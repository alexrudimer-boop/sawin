# Active-Factor Observability Audit

This generated audit checks the active-factor repair on the finite
transport-gluing proof-gap examples.  It is not a proof of Sawin's
question.  It shows that the known monodromy and quotient-routing
gaps are absorbed by finite certificates in these witnesses, so the
remaining issue is the universal existence theorem.

- all examples closed by certificate: `True`.

## identity_base_cyclic_transport

- description: `r((a,x),(b,y))=((a,y),(b,x+1))`;
- solution size: `6`;
- finite conditions hold: `True`;
- factor_size: `3`;
- state_count: `3`;
- invariant_state_count: `1`;
- factor_is_rack: `True`;
- observer: `colour a`;
- position_gauge: `u_i = x_i - i mod 3`;
- factor_failure_count: `0`;
- invariant_failure_count: `0`;
- injectivity witness: `None`.

## flip_base_cyclic_transport

- description: `r((a,i),(b,j))=((b,j+1),(a,i+1))`;
- solution size: `6`;
- finite conditions hold: `True`;
- quotient_size: `2`;
- factor_size: `3`;
- proper_factor: `True`;
- factor_left_nondegenerate: `True`;
- monodromy_witness: `sigma_1^2 sends ((0,0),(1,0)) to ((0,2),(1,2))`;
- quotient_failure_count: `0`;
- factor_failure_count: `0`;
- injectivity witness: `None`.

## dihedral_quotient_inert_fibre

- description: `r((a,i),(b,j))=((a*b,i),(a,j)), a*b=2a-b mod 3`;
- solution size: `6`;
- finite conditions hold: `True`;
- quotient_size: `3`;
- active_factor_count: `0`;
- observer: `inert fibre coordinate i`;
- returning_quotient_word: `(1, 1, 1)`;
- returning_quotient_path: `((0, 1), (2, 0), (1, 2), (0, 1))`;
- changes_colours_midword: `True`;
- quotient_failure_count: `0`;
- invariant_failure_count: `0`;
- injectivity witness: `None`.

## Consequence

The finite monodromy and quotient-routing proof gaps are not negative evidence by themselves: both are absorbed by proper active-factor or quotient+observer certificates in these witnesses. The unresolved theorem is universal existence of such certificates, or a cofinal rack-prefix obstruction.
