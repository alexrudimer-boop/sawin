# Review: Fiber-Monodromy Quotient Failure

Date: 2026-06-07

Verdict: no A/B.

This response did not prove Sawin's finite-rack domination statement and did
not construct a fixed finite counterexample.  It gave a concrete finite
example showing why a quotient-to-nondegenerate strategy is not enough:
nontrivial pure-braid monodromy can live entirely in degenerate fibers and be
lost by the quotient.

## Locally Checked Example

Let

```text
X={0,1} x {0,1}.
```

For `x=(a,i)` and `y=(b,j)`, define

```text
R((a,i),(b,j))=((b,I),(a,J)),
```

where

```text
(I,J)=(i,j)     if (a,b)=(0,0),
(I,J)=(j,i)     if (a,b)=(0,1) or (1,0),
(I,J)=(j,1-i)   if (a,b)=(1,1).
```

I checked this example directly in the workspace:

```text
bijective True
YBE True
sigma1sq_moved_count 4
```

It is left-degenerate: for example, the first-coordinate map for `(0,0)` is
not bijective.  The projection to the first coordinate is the two-point flip
solution.  Nevertheless, `sigma_1^2` moves all four fiber points over the base
pair `(1,1)`:

```text
((1,0),(1,0)) -> ((1,1),(1,1))
((1,0),(1,1)) -> ((1,1),(1,0))
((1,1),(1,0)) -> ((1,0),(1,1))
((1,1),(1,1)) -> ((1,0),(1,0))
```

Thus a nondegenerate quotient can kill pure-braid monodromy that remains
visible in the total degenerate solution.

## Consequence

The example blocks a tempting positive route:

```text
take a finite nondegenerate quotient of X, use its derived rack, and hope the
quotient detector controls X.
```

That strategy cannot prove domination in general, because quotient domination
does not preserve kernel information upward through the fibers.  A positive
proof still needs a finite rack construction that records fiber monodromy
uniformly in all arities.

## Negative Route

The response again did not freeze the varying alternating-group construction
into one fixed finite target.  It notes that once `X` is fixed, local pure
orders and finite local monodromy data are fixed, while a rack detector can be
chosen with compatible pure orders.  No fixed finite degenerate solution with
cofinal rack-prefix-invisible witnesses was constructed.

