# Two-colour fibre-2 all-base audit

Date: 2026-05-28

This generated audit enumerates arbitrary local bijection tables with
two quotient colours and two-point fibres over every two-point YBE
quotient base.  It is candidate-search evidence only; it is not a
proof of the arbitrary-fibre or arbitrary-colour theorem.

For each local-minimal interval it records two-sided
retraction/coretraction kind, known branch tags, product/direct
witnesses, and the output coordinate-kernel corridor closure.

## Totals

Two-point quotient bases: `5`.
Local tables checked: `1658880`.
Coloured-YBE local tables: `629`.
Local-minimal intervals: `120`.
Semisplit leaks among local-minimal intervals: `0`.
Output kernel closures: `equality`: `80`, `universal`: `40`.
Output universal depths: `0`: `40`.
Unknown universal-output examples retained: `0`.

## base_0

Checked local tables: `331776`.
Coloured-YBE tables: `33`.
Local-minimal intervals: `32`.
Semisplit leaks: `0`.
Retraction/coretraction: `retraction=universal|coretraction=equality`: `32`.
Output kernel closures: `equality`: `32`.
Output universal depths: `{}`.
Unknown universal-output examples: `0`.

Corridor rows:

- retraction `universal`, coretraction `equality`, tags `involutive`, output `equality` depth `0`, all-coordinate `universal` depth `0`, product `True`, direct `False`: `16`.
- retraction `universal`, coretraction `equality`, tags `(untagged)`, output `equality` depth `0`, all-coordinate `universal` depth `0`, product `True`, direct `False`: `16`.

## base_1

Checked local tables: `331776`.
Coloured-YBE tables: `520`.
Local-minimal intervals: `12`.
Semisplit leaks: `0`.
Retraction/coretraction: `retraction=equality|coretraction=equality`: `8`, `retraction=equality|coretraction=universal`: `4`.
Output kernel closures: `universal`: `12`.
Output universal depths: `0`: `12`.
Unknown universal-output examples: `0`.

Corridor rows:

- retraction `equality`, coretraction `equality`, tags `involutive`, output `universal` depth `0`, all-coordinate `universal` depth `0`, product `False`, direct `False`: `8`.
- retraction `equality`, coretraction `universal`, tags `involutive`, output `universal` depth `0`, all-coordinate `universal` depth `0`, product `False`, direct `True`: `4`.

## base_2

Checked local tables: `331776`.
Coloured-YBE tables: `10`.
Local-minimal intervals: `10`.
Semisplit leaks: `0`.
Retraction/coretraction: `retraction=equality|coretraction=universal`: `2`, `retraction=universal|coretraction=equality`: `8`.
Output kernel closures: `equality`: `8`, `universal`: `2`.
Output universal depths: `0`: `2`.
Unknown universal-output examples: `0`.

Corridor rows:

- retraction `equality`, coretraction `universal`, tags `(untagged)`, output `universal` depth `0`, all-coordinate `universal` depth `0`, product `False`, direct `True`: `2`.
- retraction `universal`, coretraction `equality`, tags `permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate`, output `equality` depth `0`, all-coordinate `universal` depth `0`, product `True`, direct `False`: `8`.

## base_3

Checked local tables: `331776`.
Coloured-YBE tables: `10`.
Local-minimal intervals: `10`.
Semisplit leaks: `0`.
Retraction/coretraction: `retraction=equality|coretraction=universal`: `2`, `retraction=universal|coretraction=equality`: `8`.
Output kernel closures: `equality`: `8`, `universal`: `2`.
Output universal depths: `0`: `2`.
Unknown universal-output examples: `0`.

Corridor rows:

- retraction `equality`, coretraction `universal`, tags `(untagged)`, output `universal` depth `0`, all-coordinate `universal` depth `0`, product `False`, direct `True`: `2`.
- retraction `universal`, coretraction `equality`, tags `permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate`, output `equality` depth `0`, all-coordinate `universal` depth `0`, product `True`, direct `False`: `4`.
- retraction `universal`, coretraction `equality`, tags `rack_type+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate`, output `equality` depth `0`, all-coordinate `universal` depth `0`, product `True`, direct `False`: `4`.

## base_4

Checked local tables: `331776`.
Coloured-YBE tables: `56`.
Local-minimal intervals: `56`.
Semisplit leaks: `0`.
Retraction/coretraction: `retraction=equality|coretraction=equality`: `20`, `retraction=equality|coretraction=universal`: `4`, `retraction=universal|coretraction=equality`: `32`.
Output kernel closures: `equality`: `32`, `universal`: `24`.
Output universal depths: `0`: `24`.
Unknown universal-output examples: `0`.

Corridor rows:

- retraction `equality`, coretraction `equality`, tags `involutive`, output `universal` depth `0`, all-coordinate `universal` depth `0`, product `False`, direct `False`: `20`.
- retraction `equality`, coretraction `universal`, tags `involutive`, output `universal` depth `0`, all-coordinate `universal` depth `0`, product `False`, direct `True`: `4`.
- retraction `universal`, coretraction `equality`, tags `involutive+left_nondegenerate+right_nondegenerate+nondegenerate`, output `equality` depth `0`, all-coordinate `universal` depth `0`, product `True`, direct `False`: `4`.
- retraction `universal`, coretraction `equality`, tags `involutive+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate`, output `equality` depth `0`, all-coordinate `universal` depth `0`, product `True`, direct `False`: `4`.
- retraction `universal`, coretraction `equality`, tags `left_nondegenerate+right_nondegenerate+nondegenerate`, output `equality` depth `0`, all-coordinate `universal` depth `0`, product `True`, direct `False`: `20`.
- retraction `universal`, coretraction `equality`, tags `permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate`, output `equality` depth `0`, all-coordinate `universal` depth `0`, product `True`, direct `False`: `4`.

## Consequence

This all-base extension closes a small audit hole in the fibre-size-two
local search.  Across every two-point quotient base, the arbitrary
two-point-fibre local-minimal intervals still produce no untagged
universal output-kernel corridor.  Since fibre-size-two affine
`F_2` branches are already bookkept as finite-G measurable, this
does not prove a new theorem; it just removes the smallest
two-colour/two-fibre hiding place for a transported-corridor
counterexample.
