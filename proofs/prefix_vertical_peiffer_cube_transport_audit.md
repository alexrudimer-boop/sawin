# Prefix vertical Peiffer cube-transport audit

Date: 2026-06-03

This generated audit checks the first cube-level transport law for
vertical Peiffer square boundaries.  It fixes source point-pushing
arity `5`.  For each deleted triple `T` and each pair face
`F subset T`, it compares

```text
delete_{T-F} after Peiffer_F
=
Peiffer_T(F) after delete_{T-F}.
```

This is a low-dimensional cubical coherence check for the normalized
deletion two-cocycle described by the external theoretical pressure
test: it is not yet the quotient by section gauge or by pullback from
a fixed finite operator-label Hurwitz base.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- source point-pushing arity: `5`;
- row count: `30`;
- all Peiffer boundaries transportable: `True`;
- all Peiffer transports commute: `True`;
- all pair Peiffer boundaries identity: `True`;
- all triple Peiffer boundaries identity: `True`;
- total mismatch count: `0`;
- total pair Peiffer moved tuple count: `0`;
- total triple Peiffer moved tuple count: `0`;
- Peiffer order-pair spectrum: `((1, 1),)`;
- verifies cube transport audit: `True`.

Triple summaries:

- `(1, 2, 3)`: rows `3`, pairs `((1, 2), (1, 3), (2, 3))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 2, 4)`: rows `3`, pairs `((1, 2), (1, 4), (2, 4))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 2, 5)`: rows `3`, pairs `((1, 2), (1, 5), (2, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 3, 4)`: rows `3`, pairs `((1, 3), (1, 4), (3, 4))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 3, 5)`: rows `3`, pairs `((1, 3), (1, 5), (3, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 4, 5)`: rows `3`, pairs `((1, 4), (1, 5), (4, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(2, 3, 4)`: rows `3`, pairs `((2, 3), (2, 4), (3, 4))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(2, 3, 5)`: rows `3`, pairs `((2, 3), (2, 5), (3, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(2, 4, 5)`: rows `3`, pairs `((2, 4), (2, 5), (4, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(3, 4, 5)`: rows `3`, pairs `((3, 4), (3, 5), (4, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.

Cube transport rows:

- triple `(1, 2, 3)`, pair `(1, 2)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 3)`, pair `(1, 3)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 3)`, pair `(2, 3)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 4)`, pair `(1, 2)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 4)`, pair `(1, 4)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 4)`, pair `(2, 4)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 5)`, pair `(1, 2)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 5)`, pair `(1, 5)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 5)`, pair `(2, 5)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 4)`, pair `(1, 3)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 4)`, pair `(1, 4)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 4)`, pair `(3, 4)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 5)`, pair `(1, 3)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 5)`, pair `(1, 5)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 5)`, pair `(3, 5)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 4, 5)`, pair `(1, 4)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 4, 5)`, pair `(1, 5)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 4, 5)`, pair `(4, 5)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 4)`, pair `(2, 3)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 4)`, pair `(2, 4)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 4)`, pair `(3, 4)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 5)`, pair `(2, 3)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 5)`, pair `(2, 5)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 5)`, pair `(3, 5)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 4, 5)`, pair `(2, 4)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 4, 5)`, pair `(2, 5)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 4, 5)`, pair `(4, 5)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(3, 4, 5)`, pair `(3, 4)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(3, 4, 5)`, pair `(3, 5)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(3, 4, 5)`, pair `(4, 5)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.

### degenerate_identity_peiffer_cube_transport

- element count: `2`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- source point-pushing arity: `5`;
- row count: `30`;
- all Peiffer boundaries transportable: `True`;
- all Peiffer transports commute: `True`;
- all pair Peiffer boundaries identity: `True`;
- all triple Peiffer boundaries identity: `True`;
- total mismatch count: `0`;
- total pair Peiffer moved tuple count: `0`;
- total triple Peiffer moved tuple count: `0`;
- Peiffer order-pair spectrum: `((1, 1),)`;
- verifies cube transport audit: `True`.

Triple summaries:

- `(1, 2, 3)`: rows `3`, pairs `((1, 2), (1, 3), (2, 3))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 2, 4)`: rows `3`, pairs `((1, 2), (1, 4), (2, 4))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 2, 5)`: rows `3`, pairs `((1, 2), (1, 5), (2, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 3, 4)`: rows `3`, pairs `((1, 3), (1, 4), (3, 4))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 3, 5)`: rows `3`, pairs `((1, 3), (1, 5), (3, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(1, 4, 5)`: rows `3`, pairs `((1, 4), (1, 5), (4, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(2, 3, 4)`: rows `3`, pairs `((2, 3), (2, 4), (3, 4))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(2, 3, 5)`: rows `3`, pairs `((2, 3), (2, 5), (3, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(2, 4, 5)`: rows `3`, pairs `((2, 4), (2, 5), (4, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.
- `(3, 4, 5)`: rows `3`, pairs `((3, 4), (3, 5), (4, 5))`, mismatches `0`, Peiffer orders `((1, 1),)`, pair moved `0`, triple moved `0`.

Cube transport rows:

- triple `(1, 2, 3)`, pair `(1, 2)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 3)`, pair `(1, 3)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 3)`, pair `(2, 3)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 4)`, pair `(1, 2)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 4)`, pair `(1, 4)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 4)`, pair `(2, 4)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 5)`, pair `(1, 2)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 5)`, pair `(1, 5)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 2, 5)`, pair `(2, 5)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 4)`, pair `(1, 3)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 4)`, pair `(1, 4)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 4)`, pair `(3, 4)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 5)`, pair `(1, 3)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 5)`, pair `(1, 5)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 3, 5)`, pair `(3, 5)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 4, 5)`, pair `(1, 4)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 4, 5)`, pair `(1, 5)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(1, 4, 5)`, pair `(4, 5)`, extra `1`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 4)`, pair `(2, 3)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 4)`, pair `(2, 4)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 4)`, pair `(3, 4)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 5)`, pair `(2, 3)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 5)`, pair `(2, 5)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 3, 5)`, pair `(3, 5)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 4, 5)`, pair `(2, 4)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 4, 5)`, pair `(2, 5)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(2, 4, 5)`, pair `(4, 5)`, extra `2`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(3, 4, 5)`, pair `(3, 4)`, extra `5`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(3, 4, 5)`, pair `(3, 5)`, extra `4`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.
- triple `(3, 4, 5)`, pair `(4, 5)`, extra `3`: pair/triple Peiffer orders `(1, 1)`, transport commutes `True`, mismatches `0`, witness `none`.

## Meaning

For the nondegenerate prefix witness, all `30` cube-transport
rows commute.  The transported pair Peiffer boundaries and the
direct triple-face Peiffer boundaries are all identity.

For the degenerate identity row, the same cube-transport checks are
trivial for the identity-defect reason.

This eliminates the first cubical coherence obstruction for the
current prefix surface.  The remaining pressure test is the
section-change/gauge quotient and the pullback test against one
fixed finite operator-label Hurwitz base.
