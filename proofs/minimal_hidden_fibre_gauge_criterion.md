# Minimal hidden-fibre rack gauge criterion

This note records the guardrail for the proposed "minimal hidden-fibre rack
gauge" route.

Let `pi:X -> Z` be a finite YBE quotient.  Suppose `Z` is already dominated by
a finite rack detector.  A second finite rack `S` would close the hidden-fibre
motion over `Z` if

```text
ker(rho^Z_n) cap ker(rho^S_n) <= ker(rho^X_n)       for every n.
```

Then the product of a rack dominating `Z` with `S` dominates `X`.

This condition is exact but too broad to be a new induction lemma.  If "finite
fibre gauge" means an arbitrary finite rack `S`, then the criterion is
equivalent to Sawin's original problem for `X`: any rack `Y` dominating `X`
itself can be used as `S`, since

```text
ker(rho^Z_n) cap ker(rho^Y_n) <= ker(rho^Y_n) <= ker(rho^X_n).
```

Thus the unrestricted hidden-fibre rack-gauge lemma is not a smaller missing
lemma.

## Relative negative sequence

Failure of the exact criterion for every finite rack `S` gives the relative
normalized-law obstruction over the quotient `Z`.  Enumerate finite racks
`S_1,S_2,...`.  For each `m`, choose a braid

```text
beta_m in ker(rho^Z_{n_m})
         cap ker(rho^{S_1}_{n_m})
         cap ...
         cap ker(rho^{S_m}_{n_m})
```

with

```text
rho^X_{n_m}(beta_m) != 1.
```

After passing to an unbounded/stabilized sequence of arities, this is the
relative version of a Sawin-negative normalized-law sequence: every fixed
finite rack detector is eventually blind while the hidden fibre over `Z` still
moves in `X`.

Conversely, such a relative sequence rules out every finite rack gauge over
`Z`.

## Meaningful restricted target

The useful positive theorem must restrict the allowed gauge `S` to something
constructive and checkable from the quotient, fibres, and extension cocycle:
for example a finite transducer, finite monoidal holonomy, finite group/rack
extension, or bounded-width endpoint detector.  Failure of one such restricted
construction is only an induction gap.  Failure of the unrestricted finite-rack
criterion above is equivalent to the Sawin-negative branch.

Therefore the next genuine target is:

```text
For every actual minimal hidden-fibre extension pi:X->Z, construct a finite
checkable rack/transducer gauge S(pi) such that

ker(rho^Z_n) cap ker(rho^{S(pi)}_n) <= ker(rho^X_n)

for all n.
```

This is precisely where the endpoint-language and finite-transducer criteria
meet the quotient/fibre decomposition approach.
