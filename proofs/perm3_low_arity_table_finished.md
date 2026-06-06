# Perm3 low-arity table finished

## Result

The permutation-form \(|X|=3\) low-arity endpoint gate is closed for
\(n=2,3\). Combined with the already-established \(n\ge4\) detector theorem,
the full permutation-form \(|X|=3\) branch now has no unresolved endpoint-gate
cases.

Reported verifier output:

```text
OK perm3 low-arity endpoint gate certificate verified
sha256 ecb66dc5461106b6a816ff9780424fd05c8ce78b36a577559eaa6891557c0b4e
invisible_dedup_pairs 3132
positive_detectors 216
strong_collapse_witnesses 2916
```

Reported certificate SHA256:

```text
ecb66dc5461106b6a816ff9780424fd05c8ce78b36a577559eaa6891557c0b4e
```

The linked full JSON certificate and standalone verifier are not present in
the local workspace at this checkpoint. This note records the reported compact
classification and the shared certificate structures.

## Classification

For all commuting pairs \((\sigma,\tau)\in S_3^2\), all rack-admissible
partitions \(P\), and arities \(n=2,3\), the program finds:

```text
deduplicated D_{sigma,tau}-invisible bad endpoint pairs: 3132
resolved by positive finite rack detector:                 216
resolved by strong left-cancellation collapse:            2916
unresolved:                                                  0
bounded negative certificates:                               0
```

No bounded negative result is used. No residual-collapse claim is made.

The low-arity branch splits cleanly:

```text
n = 2:
    every invisible bad endpoint pair is separated by a positive finite rack detector.
n = 3:
    every invisible bad endpoint pair has a parametric strong-collapse
    certificate by rack left-cancellation.
```

Thus:

\[
\boxed{
\text{Every low-arity }D_{\sigma,\tau}\text{-invisible bad endpoint pair is
either finite-rack separated or strongly collapsed.}
}
\]

## Detector side: arity 2

All 216 deduplicated arity-2 invisible bad endpoint pairs are separated using
the same size-5 monoid quotient:

```text
M = {e, a0, a1, a2, z}
0 = e
1 = a0
2 = a1
3 = a2
4 = z
```

Generator images:

```text
m0 = a0 = 1
m1 = a1 = 2
m2 = a2 = 3
```

Multiplication:

```text
e*u = u*e = u
u*v = z for all nonidentity u,v
```

Table:

```text
[
  [0,1,2,3,4],
  [1,4,4,4,4],
  [2,4,4,4,4],
  [3,4,4,4,4],
  [4,4,4,4,4]
]
```

This is a quotient of every permutation-form structure monoid because every
length-2 product collapses to \(z\), so every relation

\[
m_xm_y=m_{\sigma(y)}m_{\tau(x)}
\]

holds.

Rack distribution for the 216 positive detectors:

```text
q=2 identity-action rack: 168 endpoint pairs
q=3 rack:                  48 endpoint pairs
```

The q=2 rack is:

```text
[
  [0,1],
  [0,1]
]
```

The q=3 rack used is:

```text
[
  [0,1,2],
  [0,1,2],
  [1,0,2]
]
```

The full certificate reportedly includes the complete
\(\alpha:M\times X\times M\to Q\) table for every positive detector, and the
verifier checks every contextual \(T\)-relation, every contextual \(R\)-relation,
and the endpoint inequality.

## Collapse side: arity 3

All 2916 arity-3 invisible bad endpoint pairs are strongly collapsed by the
same proof pattern.

Each certificate consists of two contextual \(R\)-relations:

\[
A\triangleright B=C,\qquad A'\triangleright B'=C',
\]

where the corrected endpoint \(T\)-closure verifies:

\[
A\sim_T A',\qquad C\sim_T C',\qquad B\sim_T e,\qquad B'\sim_T e'.
\]

The two equations therefore become:

\[
A\triangleright e=C,\qquad A\triangleright e'=C.
\]

Since every rack left translation is bijective, it is injective, so:

\[
e=e'.
\]

This is a parametric rack proof, not a bounded no-detector result.

## Example collapse witness

For

```text
ybe_table = [3,6,0,4,7,1,5,8,2]
arity = 3
word = [0,0,0]
e  = (word, position 0)
e' = (word, position 1)
```

the two \(R\)-relations are:

```text
[epsilon,0,00] ▷ [0,0,0] = [epsilon,1,00]
[epsilon,0,02] ▷ [0,0,2] = [epsilon,1,02]
```

The corrected endpoint \(T\)-closure verifies:

```text
[epsilon,0,00] ~T [epsilon,0,02]
[epsilon,1,00] ~T [epsilon,1,02]
[0,0,0]        ~T e'
[0,0,2]        ~T e
```

Left cancellation gives \(e=e'\).

## Final branch checkpoint

The permutation-form \(|X|=3\) endpoint gate is now closed:

```text
n >= 4:
    every principal bad endpoint pair is separated by D_{sigma,tau}.
n = 2:
    every D_{sigma,tau}-invisible bad endpoint pair is separated by an
    explicit finite rack detector with |M| = 5 and |Q| <= 3.
n = 3:
    every D_{sigma,tau}-invisible bad endpoint pair has a strong
    left-cancellation collapse certificate.
unresolved low-arity cases:
    0
```

No associated-group detector is used. No bounded negative is promoted to
residual collapse.
