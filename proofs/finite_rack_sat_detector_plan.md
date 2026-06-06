# Finite rack SAT detector plan

## Verdict

The associated-group route is dead as a general mechanism, but the finite rack
detector route remains executable. The next rigorous step is not another
separability audit. It is a finite certificate search over contextual endpoint
racks.

For a finite quotient \(M\) of the structure monoid \(L_X\), the contextual
endpoint rack \(C_M(X)\) has generators

\[
[p,x,s]\qquad p,s\in M,\ x\in X,
\]

and relations, for \(r(x,y)=(x',y')\),

\[
[p,x,\bar y s]=[p\bar{x'},y',s],
\]

\[
[p,x,\bar y s]\triangleright[p\bar x,y,s]=[p,x',\bar{y'}s].
\]

A finite rack detector certificate for endpoints \(e,e'\) is exactly:

- a finite rack table \(Q\);
- an assignment \(\alpha:M\times X\times M\to Q\);
- verification of every contextual relation above;
- the strict inequality \(\alpha(e)\ne \alpha(e')\).

This is a complete finite certificate format. It does not factor through the
associated group and therefore sees non-idempotent rack distinctions such as
the two-element constant-action rack example.

## Implementation target

The first implementation should expose a small exact core:

- enumerate finite rack tables up to a small size bound;
- collapse all contextual \(T\)-relations by union-find;
- reduce \(R\)-relations to partial rack equations between \(T\)-classes;
- solve the finite assignment CSP for a candidate rack table;
- emit a checkable `RackDetector` certificate.

The first smoke test is the counterexample to associated-group separation:

\[
X=\{0,1\},\qquad r(i,j)=(1-j,i),\qquad M=1.
\]

In \(C_1(X)\), the endpoint generators \(c_0=[1,0,1]\) and
\(c_1=[1,1,1]\) satisfy

\[
c_x\triangleright c_y=c_{1-y}.
\]

The finite rack \(Q=\{0,1\}\) with \(a\triangleright b=1-b\) separates
\(c_0\) from \(c_1\). The detector core must find this certificate with
\(|Q|=2\).

## Status

This does not solve Target A yet. It converts the next obstruction into an
exact bounded finite search with machine-checkable positive certificates.
The remaining proof work is to connect the detector core to:

- enumeration of finite quotients \(M\);
- principal bad-triple generation from \(K_n(P_X)\);
- bounded or unbounded coverage theorems.

The aggressive next prompt should ask for a proof or counterexample produced
from the finite detector program, not another restatement of endpoint
residuality.
