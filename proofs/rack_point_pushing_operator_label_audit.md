# Rack point-pushing operator-label audit

Date: 2026-06-03

This generated audit checks finite rows of the rack-only
point-pushing structure recorded in
`proofs/rack_point_pushing_operator_label_invariant.md`.
For a rack `Y`, the point-pushing image is compared with its
operator-label quotient on tuples `(L_y)` and with the vertical
kernel acting trivially on those labels.

The audit is finite-prefix evidence only.  The theorem-level
statement is the symbolic rack operator-label extension; this
report only locks down conventions and warning examples.

## Rows

### trivial_rack_2 arity 1

- braid index: `2`;
- tuple count: `4`;
- operator-label tuple count: `1`;
- `|Inn(Y)|`: `1`;
- `exp Inn(Y)`: `1`;
- point-pushing image order: `1`;
- point-pushing image exponent: `1`;
- Hurwitz quotient order: `1`;
- vertical kernel size: `1`;
- vertical kernel exponent: `1`;
- vertical exponent divides `exp Inn(Y)`: `True`;
- verifies checked operator-label extension: `True`.

### trivial_rack_2 arity 2

- braid index: `3`;
- tuple count: `8`;
- operator-label tuple count: `1`;
- `|Inn(Y)|`: `1`;
- `exp Inn(Y)`: `1`;
- point-pushing image order: `1`;
- point-pushing image exponent: `1`;
- Hurwitz quotient order: `1`;
- vertical kernel size: `1`;
- vertical kernel exponent: `1`;
- vertical exponent divides `exp Inn(Y)`: `True`;
- verifies checked operator-label extension: `True`.

### trivial_rack_2 arity 3

- braid index: `4`;
- tuple count: `16`;
- operator-label tuple count: `1`;
- `|Inn(Y)|`: `1`;
- `exp Inn(Y)`: `1`;
- point-pushing image order: `1`;
- point-pushing image exponent: `1`;
- Hurwitz quotient order: `1`;
- vertical kernel size: `1`;
- vertical kernel exponent: `1`;
- vertical exponent divides `exp Inn(Y)`: `True`;
- verifies checked operator-label extension: `True`.

### dihedral_rack_3 arity 1

- braid index: `2`;
- tuple count: `9`;
- operator-label tuple count: `9`;
- `|Inn(Y)|`: `6`;
- `exp Inn(Y)`: `6`;
- point-pushing image order: `3`;
- point-pushing image exponent: `3`;
- Hurwitz quotient order: `3`;
- vertical kernel size: `1`;
- vertical kernel exponent: `1`;
- vertical exponent divides `exp Inn(Y)`: `True`;
- verifies checked operator-label extension: `True`.

### dihedral_rack_3 arity 2

- braid index: `3`;
- tuple count: `27`;
- operator-label tuple count: `27`;
- `|Inn(Y)|`: `6`;
- `exp Inn(Y)`: `6`;
- point-pushing image order: `24`;
- point-pushing image exponent: `12`;
- Hurwitz quotient order: `24`;
- vertical kernel size: `1`;
- vertical kernel exponent: `1`;
- vertical exponent divides `exp Inn(Y)`: `True`;
- verifies checked operator-label extension: `True`.

### dihedral_rack_3 arity 3

- braid index: `4`;
- tuple count: `81`;
- operator-label tuple count: `81`;
- `|Inn(Y)|`: `6`;
- `exp Inn(Y)`: `6`;
- point-pushing image order: `648`;
- point-pushing image exponent: `36`;
- Hurwitz quotient order: `648`;
- vertical kernel size: `1`;
- vertical kernel exponent: `1`;
- vertical exponent divides `exp Inn(Y)`: `True`;
- verifies checked operator-label extension: `True`.

## Consequence

The dihedral rack rows show why the whole-image exponent is the
wrong invariant: at arity `3`, `exp Inn(Y)=6` but the
point-pushing image exponent is `36`.  The checked rack invariant
is instead the extension by a vertical kernel whose exponent
divides `exp Inn(Y)`.
