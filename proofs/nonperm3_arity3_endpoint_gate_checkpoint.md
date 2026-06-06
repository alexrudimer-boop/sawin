# Non-permutation size-three arity-3 endpoint gate checkpoint

## Result

Update: this q<=4 checkpoint is now superseded by the reported q=5 resolution
recorded in `proofs/nonperm3_arity3_q5_resolution.md`, which resolves the
216 candidates left open here.  This file remains the q<=4 checkpoint record.

The non-permutation-form \(|X|=3\), arity-3 endpoint gate is not closed yet,
but the q<=4 detector pass resolves almost all of it and extracts a finite
frontier of obstruction candidates.

\[
\boxed{
\text{For non-permutation-form }|X|=3,\ n=3,\text{ the current detector catalog
separates }37{,}476\text{ of }37{,}692\text{ bad endpoint pairs, leaving }216
\text{ unresolved candidates.}
}
\]

Reported verifier output:

```text
OK nonperm3 arity-3 q4 checkpoint verified
sha256 bdd034c1c1fd665054818b58a76249bc009a0532dec33fea404063d61a82fee8
nonpermutation_ybe_tables 55
arity3_bad_endpoint_pairs 37692
positive_detector_coverages 37476
positive_detector_schemas 320
unresolved_obstruction_candidates 216
by_rack_size {'q2': 16416, 'q3': 20736, 'q4': 324}
by_monoid {'truncated_structure_monoid_length_1': 15309, 'truncated_structure_monoid_length_2': 22167}
```

Reported certificate SHA256:

```text
bdd034c1c1fd665054818b58a76249bc009a0532dec33fea404063d61a82fee8
```

The linked full checkpoint certificate/verifier are not present in the local
workspace at this checkpoint. This note records the reported compact theorem,
the detector families, and the first unresolved candidate. Repo tests verify
the reusable finite mechanics and the displayed candidate directly.

## Exact checkpoint

Bounds and branch:

```text
|X| = 3
branch = non-permutation-form tables only
arity = n = 3
rack sizes searched in the detector catalog: q <= 4
monoids used:
  truncated_structure_monoid_length_1, size 5
  truncated_structure_monoid_length_2, size <= 14
```

Enumeration:

```text
all bijective YBE tables on X^2: 73
permutation-form tables:        18
non-permutation-form tables:    55
```

Classification:

```text
principal bad endpoint pairs:      37692
positive finite rack detectors:    37476
positive detector schemas:           320
unresolved obstruction candidates:   216
bounded no-detector certificates:       0
residual-collapse claims:              0
```

This is deliberately not a bounded negative result: no unsat proofs are
attached for the unresolved candidates. It is also not a residual-collapse
claim.

## Monoid families

### M1: truncated length-1 monoid

The first monoid is the universal 5-element monoid used in the arity-2
checkpoint:

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
\(z\). This is a quotient of every quadratic structure monoid on three
letters because every relation has the form \(m_xm_y=m_{x'}m_{y'}\), and both
sides map to \(z\).

### M2(r): truncated length-2 structure monoid

For each YBE table \(r\), the second monoid keeps:

- the empty word;
- length-1 words;
- length-2 words modulo \(xy=x'y'\) when \(r(x,y)=(x',y')\);
- one absorbing element \(z\) for all words of length at least 3.

The reported sizes satisfy:

```text
8 <= |M2(r)| <= 14
```

The verifier checks associativity, identity, generator generation, and every
structure relation

\[
m_xm_y=m_{x'}m_{y'}
\]

for every \(r(x,y)=(x',y')\).

## Rack catalog

The detector catalog uses complete rack enumeration through q=4:

```text
q=2:   2 racks
q=3:  13 racks
q=4: 114 racks
```

Successful detector distribution:

```text
q=2: 16416 endpoint pairs
q=3: 20736 endpoint pairs
q=4:   324 endpoint pairs
```

So \(q=4\) is genuinely needed for this checkpoint: 324 arity-3 pairs were
not covered by \(q\le3\) with these two monoid families.

## Positive detector records

Each positive detector schema in the checkpoint JSON has the shape:

```text
id: D...
type: finite_rack_detector_schema
ybe_table: ...
monoid_quotient:
  construction: truncated_structure_monoid_length_1 or
                truncated_structure_monoid_length_2
  size: ...
  identity: 0
  generator_images: [1,2,3]
  mul: ...
rack:
  size: 2, 3, or 4
  table: ...
alpha: full assignment M x X x M -> Q
```

Each coverage record points to a schema and records the endpoint values. The
verifier checks every contextual relation

\[
[p,x,\bar y s]=[p\bar{x'},y',s],
\]

\[
[p,x,\bar y s]\triangleright[p\bar x,y,s]=[p,x',\bar{y'}s],
\]

for all \(p,s\in M\) and all \(x,y\in X\), plus the endpoint inequality.

## First unresolved obstruction candidate

The first unresolved candidate is:

```text
solution_index = 5
ybe_table = [0,3,6,1,4,7,5,2,8]
partition = [0,0,0]
arity = 3
braid_word = [1,0]
e  = word [0,0,2], position 2 = [00,2,epsilon]
e' = word [2,0,0], position 0 = [epsilon,2,00]
```

This table is rack-form:

\[
r(x,y)=(x\triangleright y,x),
\]

with operation:

```text
0 ▷ y = y
1 ▷ y = y
2 ▷ 0 = 1
2 ▷ 1 = 0
2 ▷ 2 = 2
```

The braid word check is:

```text
(0,0,2) --sigma_1--> (0,2,0) --sigma_0--> (2,0,0)
```

The indiscrete partition \(P=[0,0,0]\) makes the endpoints quotient-equivalent.
The corrected endpoint \(T\)-closure in \(X\) does not identify them. Thus it
is a genuine principal bad endpoint pair for the endpoint gate.

For this exact YBE table, the current positive detector catalog contains four
detector schemas, all invisible on the candidate:

```text
D4: q=3, M=truncated length 1, endpoint values [2,2]
D5: q=2, M=truncated length 1, endpoint values [1,1]
D6: q=3, M=truncated length 2, endpoint values [0,0]
D7: q=3, M=truncated length 2, endpoint values [1,1]
```

No known detector schema in the current catalog separates this pair.

## Unresolved distribution

The 216 unresolved candidates are concentrated in 12 YBE tables:

```text
12 tables x 18 unresolved pairs each = 216
```

Partition distribution:

```text
P = [0,0,0]: 108
P = [0,0,1]:  36
P = [0,1,0]:  36
P = [0,1,1]:  36
P = [0,1,2]:   0
```

## Current frontier

The non-permutation \(|X|=3\), arity-3 gate now stands at:

```text
total bad endpoint pairs:       37692
positive finite rack detectors: 37476
unresolved candidates:            216
```

The next exact target is the displayed candidate

\[
e=[00,2,\epsilon],
\qquad
e'=[\epsilon,2,00],
\]

for

```text
ybe_table = [0,3,6,1,4,7,5,2,8]
partition = [0,0,0]
arity = 3
```

To turn it into a bounded negative, one needs exhaustive monoid/rack catalogs
and unsat proofs. To turn it into a positive result, one needs a finite rack
detector outside the current catalog, or a parametric strong-collapse proof.
