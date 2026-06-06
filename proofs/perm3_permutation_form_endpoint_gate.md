# Permutation-form size-three endpoint gate

## Theorem

For every permutation-form \(|X|=3\) solution

\[
r_{\sigma,\tau}(x,y)=(\sigma(y),\tau(x)),
\qquad \sigma,\tau\in S_3,\qquad \sigma\tau=\tau\sigma,
\]

every principal bad endpoint pair in arity \(n\ge 4\) is separated by an
explicit \(q=3\) finite rack detector.

There are \(18\) labeled solutions in this branch, one for each commuting pair
\((\sigma,\tau)\in S_3^2\). The remaining bad pairs invisible to this detector
family occur only in arity \(2\) or \(3\), and are recognized by a finite table.
The shortest invisible bad pair occurs in arity \(2\). This is not a
residual-collapse claim; it is the next finite SAT target.

## YBE condition

For \(r(x,y)=(\sigma(y),\tau(x))\),

\[
r_{12}r_{23}r_{12}(x,y,z)
  =(\sigma^2z,\tau\sigma y,\tau^2x),
\]

while

\[
r_{23}r_{12}r_{23}(x,y,z)
  =(\sigma^2z,\sigma\tau y,\tau^2x).
\]

Thus the Yang-Baxter equation holds exactly when

\[
\sigma\tau=\tau\sigma.
\]

The flat table encoding is

```text
T[3x+y] = 3*sigma(y) + tau(x).
```

## Detector schema

Let

\[
\rho=\tau\sigma=\sigma\tau,\qquad o=\operatorname{ord}(\tau).
\]

Use the monoid

\[
M=C_o
\]

with every generator \(m_x=1\). Use the constant-action rack

\[
Q_\rho=X,\qquad a\triangleright b=\rho(b).
\]

Define

\[
\alpha([p,x,s])=\tau^{-p}(x).
\]

For \(r(x,y)=(x',y')=(\sigma(y),\tau(x))\), the contextual \(T\)-relation is

\[
[p,x,\bar y s]=[p\bar{x'},y',s].
\]

Since every generator maps to \(1\),

\[
\alpha([p,x,\bar y s])=\tau^{-p}x
\]

and

\[
\alpha([p+1,\tau(x),s])=\tau^{-(p+1)}\tau(x)=\tau^{-p}x.
\]

The contextual \(R\)-relation is

\[
[p,x,\bar y s]\triangleright[p\bar x,y,s]=[p,x',\bar{y'}s].
\]

The left side evaluates to

\[
\rho(\tau^{-(p+1)}y)
=\tau\sigma\tau^{-(p+1)}y
=\tau^{-p}\sigma(y),
\]

which is exactly the right side.

So \(D_{\sigma,\tau}=(M,Q_\rho,\alpha)\) is a finite rack detector. For an
arity-\(n\) endpoint \((w,i)\), its value is

\[
D_{\sigma,\tau}(w,i)=\tau^{-i}(w_i).
\]

Call this value \(z_i\).

## Coordinate reduction

Set

\[
z_i=\tau^{-i}(w_i).
\]

In \(z\)-coordinates, a braid generator at positions \(i,i+1\) becomes

\[
S_i(z_i,z_{i+1})=(\rho(z_{i+1}),z_i).
\]

The corrected endpoint \(T\)-closure preserves the marked value \(z_i\). Thus
the detector separates every bad pair with different marked \(z\)-value.
Invisible bad pairs must satisfy \(z_i=z'_j\).

## Endpoint T-class classification

After moving the marked endpoint to position \(0\), an endpoint is represented
as

\[
(a;u_1,\ldots,u_m),\qquad m=n-1,
\]

where \(a\) is the marked value and \(u\) is the unmarked context word.

There are three cycle types for \(\rho\in S_3\).

### \(\rho=\mathrm{id}\)

The context action is ordinary adjacent swapping. Context orbits are exactly
multisets. Since the full word braid orbit preserves the multiset of all
\(z\)-letters, two endpoints in the same braid orbit with the same marked value
have the same context multiset. Hence they are endpoint-\(T\)-equivalent.

So \(D_{\sigma,\tau}\) separates every principal bad pair in every arity.

### \(\rho\) a transposition

Let \(c\) be the fixed point of \(\rho\). For \(m\ge2\), the context action is
transitive on words with the same number of \(c\)'s. Fixed letters can be moved
through the word, and on the two-letter orbit the local action is

\[
S(u,v)=(1-v,u),
\]

whose squares toggle adjacent pairs. Adjacent pair toggles generate the
even-parity subspace, and one \(S\)-move changes parity.

Thus invisible bad pairs can occur only when \(m=1\), i.e. \(n=2\). In
particular, all \(n\ge4\) cases are closed.

### \(\rho\) a 3-cycle

Identify \(X=\mathbb Z/3\mathbb Z\) and \(\rho(x)=x+1\). Then

\[
S(u,v)=(v+1,u).
\]

For \(m\ge3\), the context action is transitive on \(X^m\). The linear part
generates coordinate permutations, and \(S_i^2\) gives translations
\(e_i+e_{i+1}\). Conjugating gives \(e_i+e_j\) for all \(i\ne j\), and for
distinct \(i,j,k\),

\[
2(e_i+e_j)+2(e_i+e_k)+(e_j+e_k)=e_i
\]

over \(\mathbb Z/3\mathbb Z\). Hence all translations are generated.

Thus for \(m\ge3\), i.e. \(n\ge4\), same marked value implies endpoint
\(T\)-equivalence.

## High-arity closure

Combining the three cycle types:

\[
\boxed{
\text{For every } |X|=3 \text{ permutation-form solution, every principal bad
endpoint pair in arity } n\ge4 \text{ is separated by }D_{\sigma,\tau}.
}
\]

This is independent of the rack-admissible partition \(P\). It proves the
stronger statement that if two endpoints are in the same original braid orbit
and are not endpoint-\(T\)-equivalent, then \(D_{\sigma,\tau}\) separates them
for \(n\ge4\).

## Shortest invisible low-arity pair

For the constant-action 3-cycle solution

\[
\tau=\mathrm{id},\qquad \sigma=\rho=(012),
\]

we have

\[
r(x,y)=(y+1,x)\pmod 3.
\]

The flat YBE table is

```text
[3, 6, 0, 4, 7, 1, 5, 8, 2].
```

Use the indiscrete partition \(P=[0,0,0]\), arity \(n=2\), the empty braid
word, the word \(w=w'=(0,0)\), and endpoint positions \(i=0,j=1\). Then

```text
e  = [epsilon, 0, 0]
e' = [0, 0, epsilon].
```

The quotient endpoints are equivalent, but the corrected endpoint
\(T\)-closure in \(X\) does not identify them. The only \(T\)-edge from
`((0,0),0)` is

```text
((0,0),0) ~ ((1,0),1).
```

The detector \(D_{\sigma,\tau}\) has \(M=1\), \(Q=X\) with
\(a\triangleright b=b+1\), and \(\alpha([p,x,s])=x\). Therefore both endpoints
have detector value \(0\). This is the shortest principal bad endpoint pair
invisible to the high-arity \(q=3\) detector schema.

It is not a residual-collapse candidate. It is the next finite low-arity
endpoint pair for the full finite rack SAT detector.

## Next executable target

Run full finite-rack SAT on:

```text
X = {0,1,2}
YBE table = [3,6,0,4,7,1,5,8,2]
partition = [0,0,0]
arity n = 2
e  = [epsilon,0,0]
e' = [0,0,epsilon]
```

A positive result should include a finite monoid quotient, finite rack table,
assignment \(\alpha\), and unequal endpoint values. A negative bounded result
must include monoid/rack catalog hashes and unsat certificates, and should be
called bounded no-detector, not residual collapse.
