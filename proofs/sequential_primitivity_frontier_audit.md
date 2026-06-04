# Sequential-Primitivity Frontier Audit

This generated audit packages the current finite evidence around the
sequential-primitivity obstruction.  It is exact for the size-three
whole-table corpus and certificate-based for the named pressure
representatives.  It is not a proof of Sawin's problem.

## Size 3 Corpus

- exhaustive: `True`;
- YBE solution count: `73`;
- known branch count: `73`;
- candidate count: `0`;
- known branch reasons: `{'involutive_artin_permutation': 19, 'left_nondegenerate_guitar_derived_rack': 35, 'permutation_twist_subgroup': 12, 'rack_inner_group_subgroup': 7}`;
- conclusion: `no size-3 sequential-primitivity candidate`.

## Pressure Representatives

### size4_affine_type_a

- solution size: `4`;
- YBE: `True`;
- certificate kind: `sequential cyclic rack gauge plus parity observer`;
- finite conditions hold: `True`;
- injectivity witness: `None`;
- remains candidate: `False`.

### size4_type_b_flip_across

- solution size: `4`;
- YBE: `True`;
- certificate kind: `two proper active quotient factors`;
- finite conditions hold: `True`;
- injectivity witness: `None`;
- remains candidate: `False`.

### affine_f2_hidden_cyclic_pressure_row

- solution size: `8`;
- YBE: `True`;
- certificate kind: `two-state hidden cyclic rack gauge plus inert observer`;
- finite conditions hold: `True`;
- injectivity witness: `None`;
- remains candidate: `False`.

### affine_f2_q3_tetrahedral_pressure_row

- solution size: `8`;
- YBE: `True`;
- certificate kind: `all-arity kernel equality with the four-element tetrahedral rack plus fixed observer bits`;
- finite conditions hold: `True`;
- injectivity witness: `None`;
- remains candidate: `False`.
- proof artifact: `proofs/affine_f2_q3_full_tetrahedral_conjugacy_audit.md`.

## Conclusion

- representative candidate count: `0`;
- candidate names: `[]`;

The exhaustive size-3 corpus has no sequential-primitivity candidate, and the current size-4/affine pressure representatives are closed by explicit active-factor certificates, sequential rack gauges, or all-arity kernel equality with a small rack. The next falsifiable search frontier starts at larger nonterminal tables, for example size 5 or structured affine-linear families beyond the hidden cyclic and tetrahedral affine guardrails.
