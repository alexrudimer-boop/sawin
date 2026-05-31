# Triangular recovery side-dual completion

Date: 2026-05-31

This note refines System K from
`proofs/post_linear_remaining_finite_system.md`.  It does not prove the
remaining nonlinear branch.  It isolates the side-dual Latin subcase that was
previously reported only as missing left Latin rows.

## Side-opposite local interval

For a local interval `I`, define the side-opposite interval

```text
I^op = P I P
```

by

```text
R^op(a,b) = P R(b,a),
T^op_{a,b}(x,y) = P T_{b,a}(y,x).
```

The executable helper is:

```text
side_opposite_local_interval(interval)
```

It is involutive and preserves the coloured YBE, by the same generator check
as the whole-solution side-opposite operation.  It swaps left and right
triangular forms: a right constant-section triangular row in `I` becomes a
left constant-section triangular row in `I^op`.

## System K side-dual markers

The nonlinear refinement audit now records:

```text
missing_right_latin_row_pairs
side_dual_latin_completion_available
side_dual_latin_ybe_failure_triples
```

When

```text
side_dual_latin_completion_available = True,
```

all right Latin-unit triangular rows are present in the original interval, but
the left-handed rack-kink hypotheses are not present in the original
orientation.  Applying `latin_triangular_ybe_audit(...)` to `I^op` exposes the
side-dual alpha, middle, and endpoint Latin equations as ordinary left
triangular YBE projection failures.

## Right-rack cancellation

If the original base is in left rack convention

```text
R(a,b) = (a*b,a),
```

then the side-opposite base is generally right-rack-shaped:

```text
R^op(a,b) = (b, b*a).
```

The companion note
`proofs/right_rack_kink_latin_triangular_cancellation.md` proves the needed
right-rack analogue.  If the side-dual Latin YBE equations hold in `I^op`,
then the diagonal equation forces `alpha_{b,b}=id`, the endpoint equation
with `c=b` makes the diagonal shear columns constant, and Latin-unit forces
all fibres singleton.

The executable helper is:

```text
right_rack_kink_latin_triangular_collapse_audit(
    side_opposite_local_interval(interval)
)
```

Thus K-dual is closed whenever the side-dual Latin equations hold.  What
remains in this subcase is exact:

```text
route the listed side-dual Latin YBE failure triples through a fixed
detector/readout, or upgrade one such failure to normalized-law B.
```

The follow-up consistency note
`proofs/triangular_latin_ybe_projection_consistency.md` removes this last
alternative for actual coloured-YBE interval data: since side-opposite
preserves coloured YBE, side-dual projection failures cannot occur once the
right Latin rows are complete.

## Updated finite target

System K now splits into:

```text
K-left:  missing left Latin rows and no complete right Latin replacement;
K-dual:  right Latin rows are complete; this is closed by side-opposite
         YBE consistency plus right-rack diagonal cancellation;
K-ybe:   left Latin rows are present but alpha, middle, or endpoint Latin YBE
         projections fail; this is inconsistent with actual coloured-YBE data.
```

Closing all three K-subsystems, followed by the System U endpoint route, would
close the current post-linear nonlinear obstruction on the A side.
