# Size-two unbounded q=2 schema coverage

## Theorem

For every two-element finite bijective set-theoretic Yang-Baxter solution
\(X\), there is no unbounded bad triple in the finite-rack SAT endpoint gate.
More strongly, every two-element solution is dominated by a finite rack.

This closes the active \(|X|\le 2\) finite-rack SAT endpoint task. It is not a
global proof of Sawin finite-rack domination for arbitrary finite \(X\).

## Classification

The five labeled bijective YBE solutions on \(\{0,1\}\) are:

```text
X0: [0,1,2,3],  R(x,y)=(x,y)
X1: [0,2,1,3],  R(x,y)=(y,x)
X2: [1,3,0,2],  R(x,y)=(y,t(x))
X3: [2,0,3,1],  R(x,y)=(t(y),x)
X4: [3,1,2,0],  R(x,y)=(t(y),t(x))
```

where \(t=(0\ 1)\) and the pair encoding is \((x,y)\mapsto 2x+y\).

## Domination proof

- \(X0\) has trivial braid action, so it is dominated by the one-point rack.
- \(X1\) is the trivial two-point rack \(x\triangleright y=y\), hence is
  dominated by itself.
- \(X3\) is the two-point constant-action rack \(x\triangleright y=t(y)\),
  hence is dominated by itself.
- \(X4\) is involutive:
  \[
  R^2(x,y)=R(t(y),t(x))=(x,y).
  \]
  Its braid action factors through \(B_n\to S_n\). The two-point trivial rack
  has kernel equal to the pure braid kernel, so its kernel is contained in the
  kernel of \(X4\) for every \(n\).
- \(X2\) is conjugate in every braid degree to the constant-action rack
  \(Q_2\) with \(a\triangleright b=t(b)\). Define
  \[
  F_n(x_1,\ldots,x_n)=(t x_1,x_2,t x_3,x_4,\ldots).
  \]
  Then for adjacent coordinates,
  \[
  F_n Q_{2,i} F_n^{-1}(a,b)=(b,t(a))=X2_i(a,b).
  \]
  Therefore the braid actions of \(X2\) and \(Q_2\) have equal kernels in all
  arities.

Thus no two-point solution can be a finite-rack counterexample.

## Endpoint-gate schema coverage

The nine q=2 detector schemas found in the bounded run cover all arities.
Use the two racks:

```text
Q_id:   u ▷ v = v
Q_flip: u ▷ v = 1-v
```

and three monoids:

```text
M1: one-element monoid
M2: C2, with both generators mapped to 1
M4: {e,z,a0,a1}, with e as identity and every product of two nonidentity
    elements equal to z; generators m0=a0, m1=a1
```

The detector assignment schemas are:

```text
D0: [0,2,1,3], Q_id,   M1, alpha([p,x,s]) = x
D1: [1,3,0,2], Q_id,   M4, alpha=1 on (e,0,a1),(e,1,a0),(a0,0,e),(a1,1,e)
D2: [1,3,0,2], Q_flip, M2, alpha([p,x,s]) = x+p
D3: [1,3,0,2], Q_id,   M4, alpha=1 on (e,0,a0),(e,1,a1),(a0,1,e),(a1,0,e)
D4: [2,0,3,1], Q_id,   M4, same alpha as D1
D5: [2,0,3,1], Q_flip, M1, alpha([p,x,s]) = x
D6: [2,0,3,1], Q_id,   M4, same alpha as D3
D7: [3,1,2,0], Q_id,   M2, alpha=1 on (0,1,1),(1,0,0)
D8: [3,1,2,0], Q_id,   M2, alpha=1 on (0,1,0),(1,0,1)
```

Each schema is checked directly against the contextual \(T/R\)-relations on
\(M\times X\times M\).

## All-arity invariant

For the four non-identity affine tables, write

\[
r_{a,b}(x,y)=(y+a,x+b)
\]

over \(\mathbb F_2\). Define the marked endpoint invariant

\[
\delta(w,i)=w_i+b\,i.
\]

The corrected endpoint \(T\)-closure preserves \(\delta\). With the coordinate
change \(z_i=x_i+b\,i\), the local move becomes

\[
(z_i,z_{i+1})\mapsto(z_{i+1}+c,z_i),
\qquad c=a+b.
\]

If \(c=0\), the action is ordinary swapping in \(z\)-coordinates. Endpoint
\(T\)-classes are determined by the selected \(z\)-letter, so bad endpoint
pairs are separated by the detector reading \(\delta\).

If \(c=1\), the local move \(S(u,v)=(v+1,u)\) is transitive on
\(\{0,1\}^m\) for every \(m\ge 2\). Indeed, \(S_i^2\) adds
\(e_i+e_{i+1}\), the adjacent even-weight generators span the even-weight
subspace, and one use of \(S_0\) changes total parity. Hence for \(n\ge3\),
every endpoint \(T\)-class is again determined by \(\delta\). The arity-2
exception is covered by the finite signature tables for D1/D2/D3 and
D4/D5/D6.

Therefore:

```text
[0,2,1,3]: D0 for every n
[1,3,0,2]: D2 for n >= 3; D1/D2/D3 for n = 2
[2,0,3,1]: D5 for n >= 3; D4/D5/D6 for n = 2
[3,1,2,0]: D7 for even n; D8 for odd n
```

So the q=2 schemas are not bounded artifacts; they cover all arities for
\(|X|=2\).

## Bounded SAT certificate compatibility

The bounded run with

\[
2\le n\le 5,\qquad |M|\le4,\qquad |Q|\le4
\]

reported:

```text
X2: n=2: 12, n=3: 168, n=4: 2880, n=5: 59520; unseparated: 0
X4: n=2: 2,  n=3: 24,  n=4: 264,  n=5: 3120;  unseparated: 0
```

The all-arity symbolic proof explains these finite observations and rules out
any first obstruction in arity \(n\ge6\).
