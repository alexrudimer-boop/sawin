# Product holonomy-subgroup audit

Date: 2026-05-28

This generated audit applies the gauge-normalized product holonomy
longitude-subgroup criterion to the smallest arbitrary product local
intervals: two quotient colours, two-point fibres, and every
two-point YBE quotient base.

It is finite candidate evidence only.  It removes the coboundary
transport first, then tests only the residual finite holonomy groups.
A theorem still requires the corresponding all-`n` subgroup membership
proof for arbitrary fibre sizes and quotient colours.

For each local-minimal product branch it scans all colour tuples in
`Z^3` and all braid words on three strands up to the configured bounded
length.  In this corpus the normalized holonomy groups have order at
most `2`, so all assignments `F_3 -> H` are enumerated exactly for
each finite word.

## Totals

Word count: `53`.
Maximum word length: `3`.
Local tables checked: `1658880`.
Coloured-YBE tables: `629`.
Local-minimal intervals: `120`.
Product branch scans: `92`.
Closed tuple-word scans with nonidentity normalized holonomy: `1024`.
Nonidentity normalized holonomy rows: `2048`.
Normalized holonomy-subgroup failures: `0`.

Product branch counts:

- `direct`: `12`.
- `swapped`: `80`.

Normalized holonomy group orders:

- `direct|order=2`: `4`.
- `swapped|order=2`: `72`.

## base_0

Checked local tables: `331776`.
Coloured-YBE tables: `33`.
Local-minimal intervals: `32`.
Product branch counts: `swapped`: `32`.
Closed tuple-word scans with nonidentity normalized holonomy: `512`.
Nonidentity normalized holonomy rows: `1024`.
Subgroup failures: `0`.

## base_1

Checked local tables: `331776`.
Coloured-YBE tables: `520`.
Local-minimal intervals: `12`.
Product branch counts: `direct`: `4`.
Closed tuple-word scans with nonidentity normalized holonomy: `0`.
Nonidentity normalized holonomy rows: `0`.
Subgroup failures: `0`.

## base_2

Checked local tables: `331776`.
Coloured-YBE tables: `10`.
Local-minimal intervals: `10`.
Product branch counts: `direct`: `2`, `swapped`: `8`.
Closed tuple-word scans with nonidentity normalized holonomy: `0`.
Nonidentity normalized holonomy rows: `0`.
Subgroup failures: `0`.

## base_3

Checked local tables: `331776`.
Coloured-YBE tables: `10`.
Local-minimal intervals: `10`.
Product branch counts: `direct`: `2`, `swapped`: `8`.
Closed tuple-word scans with nonidentity normalized holonomy: `0`.
Nonidentity normalized holonomy rows: `0`.
Subgroup failures: `0`.

## base_4

Checked local tables: `331776`.
Coloured-YBE tables: `56`.
Local-minimal intervals: `56`.
Product branch counts: `direct`: `4`, `swapped`: `32`.
Closed tuple-word scans with nonidentity normalized holonomy: `512`.
Nonidentity normalized holonomy rows: `1024`.
Subgroup failures: `0`.

## Consequence

No normalized product holonomy outside the longitude-value subgroup
appears in this smallest arbitrary product corpus.  This is not a
proof of the product theorem, but it confirms that the new
gauge-normalized target agrees with the older product-label
subgroup audit on the first arbitrary corpus.

For outcome B, a product candidate should now supply a closed
normalized holonomy label outside this subgroup before attempting
the all-finite-group normalized-law diagonalization.
