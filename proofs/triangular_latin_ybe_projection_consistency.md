# Triangular Latin YBE projection consistency

Date: 2026-05-31

This note closes the K-ybe residue in
`proofs/post_linear_remaining_finite_system.md`.  It is a consistency check:
for actual interval data satisfying the coloured YBE, the Latin triangular
projection equations cannot fail once the required Latin rows are present.

## Left triangular case

Assume a local interval is coloured YBE and every colour-pair row is left
Latin-unit triangular.  The helper

```text
latin_triangular_ybe_audit(interval)
```

computes the three coordinate projections of the same coloured YBE equation:

```text
alpha
middle
endpoint
```

Therefore, if the interval is coloured YBE and all required left Latin rows
are present, every listed projection failure is impossible.  The nonlinear
refinement records any such supplied inconsistency as:

```text
latin_triangular_ybe_projection_inconsistent
```

This is a closed diagnostic state, not a remaining finite system.

## Side-dual case

The side-opposite interval

```text
side_opposite_local_interval(interval)
```

preserves the coloured YBE.  If all right Latin-unit triangular rows are
present in the original interval, then the side-opposite interval has all left
Latin-unit triangular rows.  Hence any side-dual alpha, middle, or endpoint
projection failure is likewise impossible for actual coloured-YBE data.

The nonlinear refinement records this as:

```text
side_dual_latin_triangular_ybe_projection_inconsistent
```

This closes the K-dual YBE-failure subcase.  Together with
`proofs/right_rack_kink_latin_triangular_cancellation.md`, K-dual is no
longer a live post-linear branch: if the side-dual equations hold, right-rack
diagonal cancellation forces singleton fibres; if they fail, the data was not
a genuine coloured-YBE survivor.

## Remaining K branch

After this consistency check, the live System K branch is:

```text
K-left:
  some left Latin-unit triangular colour pair is missing,
  there is no complete side-dual/right Latin replacement,
  and the missing row has not been routed to product triangular collapse,
  proper-kernel readouts, strand-continuing transport, or a fixed detector.
```

Closing K-left, and then System U, is the remaining post-linear A-route.
