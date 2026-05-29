# Product closed-label obstruction criterion

Date: 2026-05-28

This note records the exact B-route supplied by the closed-label product
target.  It is not a counterexample.  It says what must be proved once an
explicit product interval is suspected to escape all finite longitude
detectors.

## Detector failure for closed labels

Fix a local product interval over a quotient dominated by `Q`, and let

```text
h_{z,j}(beta) in H_prod
```

be the closed product label from
`proofs/product_closed_label_cocycle.md`, defined whenever
`beta in ker rho_{Q,n}` and the relevant strand dependency is identity.  Say
that a finite group `G` detects the closed labels if, for all `n`, all base
tuples `z`, all coordinates `j`, and all `beta in ker rho_{Q,n}`,

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)
    => h_{z,j}(beta)=1.
```

By the sharp obstruction theorem, such a `G` detects the product residual
branch.

## Diagonal closed-label sequence

Suppose no finite group detects these closed labels.  Enumerate finite groups
up to isomorphism as

```text
G_1, G_2, G_3, ...
```

and set `E_r=G_1 x ... x G_r`.  Since `E_r` also fails to detect, there are
some braid degree `n_r`, base tuple `z_r`, coordinate `j_r`, and braid
`alpha_r in ker rho_{Q,n_r}` such that

```text
Lambda_{E_r,n_r}(alpha_r)=Lambda_{E_r,n_r}(1),
h_{z_r,j_r}(alpha_r) != 1.
```

The direct-product longitude lemma implies that `alpha_r` is invisible to
each `G_i` with `i <= r`.  Stabilize `alpha_r` by adding unused right-hand
strands, choosing `q_r=n_r+r`.  The old closed label survives on the old
coordinate, the new strands have empty longitudes, and the stabilized braid
still lies in the base kernel.  Therefore:

```text
q_r -> infinity,
Lambda_{G,q_r}(beta_r)=Lambda_{G,q_r}(1)
```

eventually for every finite group `G`, while a closed product label remains
nonidentity.

This is exactly the normalized-law obstruction sequence specialized to
product labels.  If the product interval is embedded in a full finite YBE
solution, the nonidentity closed label gives an explicit moved tuple by
choosing a point of the source fibre moved by that label and arbitrary values
on the other coordinates.

## Executable bounded screen

The helper

```text
product_closed_label_blind_movers(interval,branch,groups,z,words)
```

searches a finite word list for this phenomenon relative to a finite list of
detector groups.  It returns words whose Artin-longitude data is identity for
all listed groups but whose closed product label is nonidentity.

This helper is finite search only.  It can disprove a proposed detector or
find a candidate pattern, but outcome B still requires the symbolic
all-finite-group diagonal hypothesis above for an explicit finite YBE
solution.

There is also an exact fixed-degree image audit:

```text
product_closed_label_exact_audit(interval,branch,groups,z)
```

For the one supplied colour tuple `z`, it closes the finite joint image of
the base-detector action, the product-label action, the Artin strand
permutation, and the listed finite-group Artin-longitude detector states.
By default the base detector is the quotient colour solution itself.  The
optional `base_detector` parameter can be set to a stronger finite braided
set, such as the rack `Q` already dominating the quotient in the sharp
obstruction setup.

A failure is a braid with identity base-detector action, identity Artin
permutation, identity finite-group detector state, and a nonidentity closed
product label.  A nontruncated run with no failure proves the closed-label
kernel implication for that fixed `z`, fixed braid degree, base detector, and
detector list without a word-length cutoff.

This exact audit is still fixed-degree evidence only.  It is useful for
certifying or refuting proposed product detectors on concrete finite
subcases, and for producing explicit closed-label movers, but it is not the
all-`n` symbolic product theorem.

This distinction matters.  A quotient-only exact failure need not contradict
the final interval theorem: the actual kernel is `ker rho_{Q,n}`, and a
stronger already-known base rack `Q` may exclude that braid.  The tests record
this on the identity-base cyclic product fixture: `C_2` alone misses
`sigma_1^4`, while adding a three-point rack as base detector removes that
fixed-degree failure.

## Consequence

The product branch now has the same A/B form as the master theorem:

- A-route: construct a finite `G` proving the closed-label implication.
- B-route: prove that every finite `G` fails, then diagonalize as above and
  use `proofs/finite_rack_longitude_quotient.md` to defeat every finite rack.
