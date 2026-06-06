# Perm3 low-arity SAT detector

## Result

The first low-arity permutation-form \(|X|=3\) SAT target is resolved
positively. It is not a bounded negative and not a residual-collapse candidate.

The target pair was the shortest endpoint pair invisible to the high-arity
detector \(D_{\sigma,\tau}\):

```text
YBE table = [3,6,0,4,7,1,5,8,2]
partition = [0,0,0]
arity n = 2
start word = [0,0]
end word = [0,0]
start position = 0
end position = 1
e  = [epsilon,0,0]
e' = [0,0,epsilon]
```

The solution is

\[
r(x,y)=(y+1,x)\pmod 3.
\]

A \(q=2\) identity-action rack separates the endpoint pair using a
5-element finite monoid quotient.

Reported verifier output:

```text
OK finite rack detector certificate verified
```

Reported certificate SHA256:

```text
f92cd18f73fad0e75c25e54034390f7170ec12aeb37a60a8fda9ad957e092bea
```

The linked full certificate/verifier are not present in the local workspace at
this checkpoint, so the compact certificate below is recorded and verified by
repo tests.

## Monoid quotient

Use

```text
M = {e,z,a0,a1,a2}
0 = e
1 = z
2 = a0
3 = a1
4 = a2
```

with identity \(e=0\), generator images

```text
m0 = a0 = 2
m1 = a1 = 3
m2 = a2 = 4
```

and multiplication table

```text
[
  [0,1,2,3,4],
  [1,1,1,1,1],
  [2,1,1,1,1],
  [3,1,1,1,1],
  [4,1,1,1,1]
]
```

Equivalently, \(eu=ue=u\), and \(uv=z\) for all nonidentity \(u,v\).

This satisfies the structure-monoid relations for \(r(x,y)=(y+1,x)\), since

\[
m_xm_y=z=m_{y+1}m_x.
\]

## Rack

Use the two-element identity-action rack

```text
Q={0,1},   u ▷ v = v
rack table = [[0,1],[0,1]]
```

## Assignment

Define \(\alpha([p,x,s])=1\) exactly on:

```text
(e, 0, a2)
(e, 1, a0)
(e, 2, a1)
(a0, 0, e)
(a1, 1, e)
(a2, 2, e)
```

In numeric form:

```text
(0,0,4)
(0,1,2)
(0,2,3)
(2,0,0)
(3,1,0)
(4,2,0)
```

All other triples have value `0`.

Equivalently, with indices mod \(3\),

\[
\alpha([p,x,s])=1
\]

iff either \(p=a_x,s=e\), or \(p=e,s=a_{x-1}\).

## Endpoint separation

The endpoint

```text
e = [epsilon,0,0]
```

maps in \(M\) to \([e,0,a_0]\), so \(\alpha(e)=0\).

The endpoint

```text
e' = [0,0,epsilon]
```

maps in \(M\) to \([a_0,0,e]\), so \(\alpha(e')=1\).

Thus

\[
\alpha(e)\ne\alpha(e').
\]

## Relation verification

For this solution, the contextual \(T\)-relation is

\[
[p,x,m_y s]=[p m_{y+1},x,s].
\]

The contextual \(R\)-relation is

\[
[p,x,m_y s]\triangleright[p m_x,y,s]=[p,y+1,m_xs].
\]

Since the rack is identity-action, \(u\triangleright v=v\), so \(R\) reduces
to

\[
\alpha([p m_x,y,s])=\alpha([p,y+1,m_xs]).
\]

The \(T\)-relation holds because both sides are \(1\) exactly when

```text
p=e, s=e, y=x-1.
```

The \(R\)-relation holds because both sides are \(1\) exactly when

```text
p=e, s=e, x=y.
```

Therefore this is a genuine finite rack detector certificate.

## Classification

```text
resolved_by_positive_finite_rack_detector
|M| = 5
|Q| = 2
```

No associated-group detector is used.
