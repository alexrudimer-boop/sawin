# Finish the perm3 low-arity finite-rack SAT table

The permutation-form \(|X|=3\) branch is reduced as follows:

- every arity \(n\ge4\) principal bad endpoint pair is separated by the
  \(q=3\) detector \(D_{\sigma,\tau}\);
- invisible pairs for that detector occur only in arity \(2\) or \(3\);
- the first arity-2 target for
  `ybe_table=[3,6,0,4,7,1,5,8,2]`,
  `e=[epsilon,0,0]`, `e'=[0,0,epsilon]`
  is resolved by a positive finite rack detector with \(|M|=5\), \(|Q|=2\).

Do not reprove the high-arity theorem or the first detector certificate.

## Task

Finish the finite low-arity table for the permutation-form \(|X|=3\) branch.

For all commuting pairs \((\sigma,\tau)\in S_3^2\), all rack-admissible
partitions \(P\), and arities \(n=2,3\):

1. enumerate the principal bad endpoint pairs invisible to
   \(D_{\sigma,\tau}\);
2. deduplicate endpoint pairs under symmetry where sound;
3. for each remaining pair, give a positive finite rack detector certificate
   or a bounded negative certificate.

Positive certificates must include:

```json
{
  "type": "finite_rack_detector",
  "ybe_table": "...",
  "endpoint_pair": "...",
  "monoid_quotient": "...",
  "rack": "...",
  "alpha": "...",
  "endpoint_values": ["...", "..."],
  "separates": true
}
```

Bounded negatives must include catalog hashes and unsat proofs. Do not call a
bounded negative result residual collapse without a parametric proof over all
finite rack detectors.

## Desired outcome

Either:

- close the entire permutation-form \(|X|=3\) endpoint gate by finite rack
  detectors; or
- produce the smallest unresolved low-arity obstruction candidate with full
  verifier-level data.
