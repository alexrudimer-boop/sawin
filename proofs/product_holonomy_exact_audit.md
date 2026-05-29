# Product holonomy exact audit

Date: 2026-05-28

This generated audit closes the finite joint image for normalized
product holonomy at braid degree `3` in the smallest arbitrary product
corpus: two quotient colours, two-point fibres, and every two-point
quotient YBE base.

It is exact only at this fixed degree and corpus.  It is not an
all-`n` proof and not evidence for arbitrary fibre sizes.  Its purpose
is to remove word-length cutoffs from the first normalized-holonomy
product gate and to identify whether raw normalized holonomy groups
must be multiplied by known branch factors.

## Totals

Braid degree: `3`.
State limit per tuple: `20000`.
Local tables checked: `1658880`.
Coloured-YBE tables: `629`.
Local-minimal intervals: `120`.
Nontrivial holonomy branch rows: `76`.
Exact colour-tuple scans: `608`.
Truncations: `0`.
Raw normalized-holonomy detector failures: `64`.
Known-total-tagged failures: `64`.
Untagged failures: `0`.
Maximum visited states in one tuple scan: `48`.

Failure tags:

- `permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate`: `48`.
- `rack_type+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate`: `16`.

Holonomy group orders:

- `direct|order=2`: `4`.
- `swapped|order=2`: `72`.

## First Failure With Known Factor

The first raw failure is known-total tagged.  Rechecking that
same fixed tuple after multiplying by the symmetric group on the
four total interval points gives:

- raw failure braid word: `[1, 1, 1, 1]`.
- extra group orders: `[24]`.
- truncated: `True`.
- failure after extra factor: `False`.
- visited states: `20001`.

## Consequence

The raw normalized holonomy groups alone are not the final product
detectors: exact fixed-degree failures already occur in rows whose
total interval solution is in a known finite-G branch.  This matches
the product-label exact audit and justifies the theorem target's
phrase `possibly after multiplying by known branch factors`.

The audit finds no untagged exact failure in this corpus.  A product
B candidate should therefore either produce an untagged exact
normalized-holonomy failure or prove that every finite detector
fails in a fixed explicit product interval and then diagonalize.
