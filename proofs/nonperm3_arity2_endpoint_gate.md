# Non-permutation size-three arity-2 endpoint gate

## Result

The non-permutation-form \(|X|=3\), arity-2 endpoint gate is closed.

\[
\boxed{
\text{Every arity-2 principal bad endpoint pair for every non-permutation-form }
|X|=3\text{ bijective YBE table is separated by a finite rack detector with }
|M|=5,\ |Q|\le3.
}
\]

Reported verifier output:

```text
OK nonperm3 arity-2 endpoint gate certificate verified
sha256 9bb0e62c6073d88410fb1b6d846992101aa1ffb396d95b92b00840b55d87c24c
nonpermutation_ybe_tables 55
arity2_bad_endpoint_pairs 2064
positive_detectors 2064
unresolved 0
by_rack_size {'q2': 1200, 'q3': 864}
```

Reported certificate SHA256:

```text
9bb0e62c6073d88410fb1b6d846992101aa1ffb396d95b92b00840b55d87c24c
```

The linked full certificate/verifier are not present in the local workspace at
this checkpoint. This note records the reported compact theorem and verifies
representative certificate mechanics in repo tests.

## Exact bounded theorem

Bounds:

```text
|X| = 3
branch = non-permutation-form tables only
arity = n = 2
|M| = 5
|Q| <= 3
```

Enumeration:

```text
all bijective YBE tables on X^2: 73
permutation-form tables:        18
non-permutation-form tables:    55
```

For the 55 non-permutation-form tables, the verifier enumerates all
rack-admissible partitions \(P\), all principal bad endpoint pairs in arity 2,
and deduplicates endpoint pairs by unordered endpoint-pair equality within the
same `(ybe_table, partition, arity)`.

Final count:

```text
deduplicated arity-2 bad endpoint pairs: 2064
positive finite rack detectors:          2064
bounded negatives:                          0
unresolved:                                 0
```

## Universal monoid

Every detector uses the same 5-element monoid:

```text
M = {e,a0,a1,a2,z}
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
[
  [0,1,2,3,4],
  [1,4,4,4,4],
  [2,4,4,4,4],
  [3,4,4,4,4],
  [4,4,4,4,4]
]
```

Equivalently, \(eu=ue=u\), and every product of two nonidentity elements is
\(z\).

This is a quotient of every quadratic structure monoid in the \(|X|=3\) YBE
enumeration because every relation has the form

\[
m_xm_y=m_{x'}m_{y'},
\]

and both sides map to \(z\).

## Rack catalog

Complete rack enumeration for \(|Q|\le3\):

```text
q=2: 2 racks
q=3: 13 racks
```

Successful detector distribution:

```text
q=2: 1200 endpoint pairs
q=3:  864 endpoint pairs
```

No \(q=4\) rack is used.

Partition distribution:

```text
P = [0,0,0]: 1416 endpoint pairs
P = [0,0,1]:  216 endpoint pairs
P = [0,1,0]:  216 endpoint pairs
P = [0,1,1]:  216 endpoint pairs
P = [0,1,2]:    0 unresolved arity-2 pairs in this batch
```

## Example detector

One positive detector record is:

```text
ybe_table = [0,1,6,3,4,7,2,5,8]
partition = [0,0,0]
arity = 2
e  = word [0,2], position 0 = [epsilon,0,2]
e' = word [0,2], position 1 = [0,2,epsilon]
```

Use the universal 5-element monoid above and the q=2 identity-action rack:

```text
[[0,1],[0,1]]
```

The compact assignment has \(\alpha=1\) exactly on:

```text
(e,2,a0)
(a0,2,e)
```

In numeric form:

```text
(0,2,1)
(1,2,0)
```

All other triples have value `0`.

The endpoints map to:

```text
e  -> (e,0,a2)
e' -> (a0,2,e)
```

so

```text
alpha(e)  = 0
alpha(e') = 1
```

and the detector separates.

## Verification scope

The reported standalone verifier recomputes and checks:

1. all \(9!\) bijective tables on \(X^2\);
2. exactly 73 YBE tables;
3. exactly 18 permutation-form tables;
4. exactly 55 non-permutation-form tables;
5. all rack-admissible partitions of each non-permutation table;
6. corrected endpoint \(T\)-closure for arity 2;
7. every principal bad endpoint pair;
8. exact deduplicated coverage by the certificate;
9. monoid associativity, identity, and generator relations;
10. rack axioms for every \(Q\);
11. every contextual \(T\)-relation;
12. every contextual \(R\)-relation;
13. endpoint inequality.

The contextual relations checked are:

\[
[p,x,\bar y s]=[p\bar{x'},y',s],
\]

\[
[p,x,\bar y s]\triangleright[p\bar x,y,s]=[p,x',\bar{y'}s].
\]

## Classification

Within the stated bound:

```text
resolved by positive finite rack detector: 2064
bounded no-detector:                         0
strong collapse needed:                      0
unresolved:                                  0
```

This is a positive rack-valued detector theorem for the arity-2
non-permutation-form \(|X|=3\) endpoint gate. It does not claim residual
collapse, and it does not use associated groups.
