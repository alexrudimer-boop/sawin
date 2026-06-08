# Two-Colour Fibre-2 Contextual Representative Audit

This generated audit consumes the representative interval tables
retained by `two_colour_fibre2_all_bases_audit.json` and applies the
generic two-sided contextual completion/readout helper to the
corresponding four-point total YBE solutions.

It is a representative audit, not a full-row contextual pass over all
120 local-minimal totals.

## Source Corpus

- source audit: `proofs\two_colour_fibre2_all_bases_audit.json`;
- local tables checked by source audit: `1658880`;
- coloured-YBE local tables: `629`;
- local-minimal totals: `120`;
- source unknown universal-output examples: `0`.

## Contextual Representative Checks

- cached representatives checked: `15`;
- tag counts: `{'(untagged)': 3, 'involutive': 5, 'involutive+left_nondegenerate+right_nondegenerate+nondegenerate': 1, 'involutive+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate': 1, 'left_nondegenerate+right_nondegenerate+nondegenerate': 1, 'permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate': 3, 'rack_type+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate': 1}`;
- contextual profile count: `14`;
- contextual completion failure count: `0`;
- orbit-injectivity checked through arity: `6`;
- orbit-injectivity failure count: `0`;
- all claimed checks passed: `True`.

## Contextual Profiles

| cases | tags | retraction | coretraction | M_L | M_R | P | forced | domains | nontriv L |
|---:|---|---|---|---:|---:|---:|---:|---|---:|
| 2 | permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate | universal | equality | 2 | 2 | 8 | 32 | [4] | 8 |
| 1 | (untagged) | equality | universal | 3 | 3 | 12 | 16 | [0, 2] | 8 |
| 1 | (untagged) | equality | universal | 5 | 5 | 20 | 32 | [0, 2] | 16 |
| 1 | (untagged) | universal | equality | 5 | 5 | 20 | 32 | [0, 2] | 16 |
| 1 | involutive | equality | equality | 3 | 13 | 12 | 24 | [0, 3] | 0 |
| 1 | involutive | equality | equality | 5 | 25 | 20 | 48 | [0, 3] | 0 |
| 1 | involutive | equality | universal | 3 | 3 | 12 | 16 | [0, 2] | 0 |
| 1 | involutive | equality | universal | 5 | 5 | 20 | 32 | [0, 2] | 0 |
| 1 | involutive | universal | equality | 3 | 3 | 12 | 16 | [0, 2] | 0 |
| 1 | involutive+left_nondegenerate+right_nondegenerate+nondegenerate | universal | equality | 4 | 4 | 16 | 64 | [4] | 0 |
| 1 | involutive+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate | universal | equality | 2 | 2 | 8 | 32 | [4] | 0 |
| 1 | left_nondegenerate+right_nondegenerate+nondegenerate | universal | equality | 4 | 4 | 16 | 64 | [4] | 16 |
| 1 | permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate | universal | equality | 4 | 4 | 16 | 64 | [4] | 16 |
| 1 | rack_type+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate | universal | equality | 1 | 1 | 4 | 16 | [4] | 4 |

## Consequence

The cached representatives include the untagged rows retained by the
older two-colour/fibre-2 corridor audit.  None of these
representatives exhibits an identity-extension, active-lift, or
checked-arity contextual readout obstruction.  This is finite
candidate-search evidence only; it does not prove all-arity
orbit separation or cover every one of the 120 local-minimal rows.
