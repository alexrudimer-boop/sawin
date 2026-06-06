# Size-two bounded finite rack SAT experiment

## Result

The finite rack detector program was run for

\[
|X|\le 2,\qquad 2\le n\le 5,\qquad |M|\le 4,\qquad |Q|\le 4.
\]

The reported bounded result is:

\[
\boxed{\text{No residual-collapse candidate appears in this bound.}}
\]

More strongly, every bad endpoint pair found in the bound is separated by a
rack of size \(2\). No \(q=3\) or \(q=4\) rack is needed.

The reported certificate hash is:

```text
59bf0bf2957d57ff2d231bc31c799ebb9d50182d833190b3c1a4c9a8e808b3cf
```

The reported standalone verifier output is:

```text
OK 6 solutions, 18544 bad endpoint pairs, 9 detectors
```

The raw certificate JSON and verifier script were reported by GPT-5.5 Pro but
are not present in the local attachment/workspace files at this checkpoint.

## Enumerated solutions

For \(|X|=1\), the unique table is:

```text
[0]
```

For \(|X|=2\), using pair encoding \((x,y)\mapsto 2x+y\), the complete
labeled bijective YBE list is:

```text
[0, 1, 2, 3]
[0, 2, 1, 3]
[1, 3, 0, 2]
[2, 0, 3, 1]
[3, 1, 2, 0]
```

## Bounded counts

The run reports the following aggregate counts:

```text
principal bad triples:     1668688
unique bad endpoint pairs:   18544
separated endpoint pairs:    18544
unresolved endpoint pairs:       0
```

Detector distribution:

```text
q=2 identity-action rack T[a,b]=b:      3376 pairs
q=2 flip-action rack T[a,b]=1-b:       15168 pairs
```

First successful monoid sizes:

```text
|M|=1:  9264 pairs
|M|=2:  9264 pairs
|M|=4:    16 pairs
```

Thus the bounded theorem is:

\[
\boxed{
\text{For } |X|\le2,\ n\le5,\text{ every principal bad endpoint pair is }
\text{separated with } |Q|=2,\ |M|\le4.
}
\]

No strong-collapse derivation was needed in the run.

## Corrected endpoint T-closure

The endpoint T-equivalence graph must include context-only moves. For a word
\(\mathbf{x}\in X^n\), adjacent position \(j\), and
\[
r(x_j,x_{j+1})=(a,b),
\]
let \(\mathbf{x}'\) be obtained by replacing the adjacent pair by \((a,b)\).
For endpoint nodes \((\mathbf{x},i)\), add:

- if \(i<j\) or \(i>j+1\), union \((\mathbf{x},i)\sim(\mathbf{x}',i)\);
- if \(i=j\), union \((\mathbf{x},j)\sim(\mathbf{x}',j+1)\);
- if \(i=j+1\), add no direct edge.

The first rule is essential: a YBE move wholly inside the prefix or suffix
does not change the selected endpoint generator \([p,x,s]\).

## q=2 detector schemas

There are exactly two racks on two points.

Identity-action rack:

\[
T[a,b]=b.
\]

Each contextual equation \(u\triangleright v=w\) becomes
\[
\alpha(v)=\alpha(w).
\]

Flip-action rack:

\[
T[a,b]=1-b.
\]

Each contextual equation becomes
\[
\alpha(v)\oplus \alpha(w)=1.
\]

Endpoint separation is \(\alpha(e)\oplus\alpha(e')=1\).

The bounded run found that these two q=2 schemas cover all 18,544 bad endpoint
pairs through arity 5.

## What this proves

This is a finite theorem certificate for the stated bounds, not an unbounded
proof of Target A. It substantially narrows the next unbounded task:

\[
\boxed{
\text{For } |X|=2,\text{ prove or refute that the 9 detected q=2 schemas }
\text{cover all arities.}
}
\]

The direct falsification search is:

```text
load the 9 detector schemas from the certificate
for n = 6,7,...
    enumerate principal bad endpoint pairs for each |X|=2 YBE table
    test the 9 schemas
    stop on the first endpoint pair invisible to all 9 schemas
```

The first invisible output would be the next genuine obstruction candidate.
If no such output exists and the schema coverage is proved inductively, the
\(|X|=2\) Target A branch closes.
