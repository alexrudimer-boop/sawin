# Vertical-Kernel Endpoint Lemma Refutation

Date: 2026-06-04

This note records the same-chat Pro refutation of the vertical-kernel endpoint
lemma from `proofs/vertical_kernel_endpoint_lemma.md`.  The refutation is an
actual endpoint-labelled interval, not a formal partial row system, but it
does not refute Sawin's finite-rack domination problem because the underlying
YBE solution is the involutive flip solution and is already rack-dominated.

The lesson is that arbitrary actual endpoint-labelled intervals are too broad:
finite endpoint labels can create nonabelian vertical Brunnian endpoint
classes even when the underlying solution is harmless.

## Actual Interval

Let `T={a,b,c}` be the three transpositions in `S_3`, let `m` be a marker, and
set

```text
X = T sqcup {m}.
```

Use the flip YBE table

```text
r(x,y) = (y,x).
```

This is finite, bijective, involutive, and satisfies YBE.

Let

```text
C = {0,1,bot}.
```

For every `t in T`, set `tau_t=id_C`.  Define

```text
tau_m(0)=1,
tau_m(1)=bot,
tau_m(bot)=bot.
```

The flip table requires `tau_x tau_y = tau_y tau_x`; this holds because all
old colors have identity context maps and `tau_m` commutes with itself.

Define retained germs

```text
G = {(0,t): t in T} union {(0,m)} union {(1,t): t in T}.
```

There is no retained germ `(1,m)` and no retained germ over `bot`.  Hence a
retained word contains at most one marker.

The supported rows are exactly

```text
(0,t),(0,m) -> (0,m),(1,t)          for t in T,
(0,m),(1,t) -> (0,t),(0,m)          for t in T.
```

These are actual flip rows, and `G` is closed under them and their inverse
rows.  Old-old pairs are unsupported.

There are no fully supported YBE cubes: in a triple such as `(t,m,t')`, after
one supported crossing an old-old adjacent pair appears, which is unsupported.
There are also no distant-commutation obstructions, since every supported
crossing involves the unique marker.  Thus the endpoint cube conditions are
vacuous.

## Endpoint Labels

Let

```text
U = S_3.
```

Use the same symbols `a,b,c` for the three transpositions.  For positive rows,
set

```text
eta((0,t),(0,m)) = t,
eta((0,m),(1,t)) = 1.
```

Inverse rows get inverse labels.  Since transpositions are self-inverse, the
inverse label of the first row is again `t`, and the inverse label of the
second row is `1`.

This gives an actual finite endpoint-labelled interval.

## Artin Readout

Write

```text
M = (0,m),       t_0=(0,t),       t_1=(1,t).
```

For the row

```text
(t_0,M) -> (M,t_1),
```

the Artin row relations include

```text
a_M = a_{t_0} a_M a_{t_0}^{-1},
l_M = a_{t_0} l_M,
a_{t_1} = a_{t_0},
l_{t_1} = l_{t_0}.
```

The relation `l_M=a_{t_0}l_M` forces `a_{t_0}=1`, hence `a_{t_1}=1`.

For the row

```text
(M,t_1) -> (t_0,M),
```

the relation

```text
l_{t_0}=a_M l_{t_1}
```

together with `l_{t_1}=l_{t_0}` forces `a_M=1`.

Thus every meridian generator `a_e` is trivial in `Art_I`.  With all
`a_e=1`, supported rows only swap longitude symbols.  Therefore every pure
branch loop has trivial terminal Artin readout:

```text
alpha_n(zeta)=1.
```

Consequently `q_s alpha_n(zeta)=1` for every finite quotient degree `s`.

## Vertical Generator Endpoints

Fix `K>=2` and `n=K+1`.  Use a base word

```text
(t_1,t_2,...,t_K,m),          t_i in T.
```

For the last-strand point-pushing generator

```text
A_{i,n}
  =
  sigma_{n-1} ... sigma_{i+1} sigma_i^2
  sigma_{i+1}^{-1} ... sigma_{n-1}^{-1},
```

the only moving strand is the marker, and every crossing is supported.  Its
endpoint contribution is

```text
g_i = P_i t_i P_i^{-1},
P_i = t_K t_{K-1} ... t_{i+1}.
```

Since conjugates of transpositions in `S_3` are transpositions, choosing

```text
t_i = P_i^{-1} g_i P_i
```

recursively realizes any prescribed sequence

```text
g_1,...,g_K in T
```

as the endpoint values of the vertical generators

```text
A_{1,n},...,A_{K,n}.
```

## Brunnian Vertical Words

Let

```text
F_K = <x_1,...,x_K>.
```

Define

```text
W_2 = [x_1,x_2],
W_{K+1} = [W_K,x_{K+1}].
```

Each `W_K` is Brunnian: setting any one variable to `1` makes the word
trivial.

Choose two noncommuting transpositions `a,b in S_3`, and let

```text
u = [a,b],
```

a nontrivial 3-cycle.  Choose endpoint generator values

```text
g_1=a,       g_2=b,       g_i=a for i>=3.
```

Then `W_K(g_1,...,g_K)` alternates between the two nontrivial 3-cycles, so for
one parity of `K` it equals the fixed nonidentity element `u`.

For a requested deletion bound `N`, choose `K>N` with this parity, set
`n=K+1`, and define

```text
zeta_{s,N} = W_K(A_{1,n},...,A_{K,n}).
```

The word does not depend on `s`; the finite Artin condition is automatic.

Then

```text
epsilon_n(zeta_{s,N}) = u != 1.
```

## Bounded Deletion Shadows

Let `J subset {1,...,n}` with `|J|<=N`.

If the marker strand `n` is not in `J`, then every vertical generator
`A_{i,n}` deletes to identity.

If the marker strand is in `J`, then `K>N` implies some old strand `i` is
missing from `J`.  The generator `A_{i,n}` deletes to identity, so the deleted
word is the Brunnian word `W_K` with at least one variable set to `1`.

Thus

```text
d_J zeta_{s,N} = 1
```

for every `|J|<=N`, and hence all deleted endpoint and finite Artin readouts
are trivial.

## Consequence

For every pair `(s,N)`, this actual interval supplies a vertical loop with

```text
q_s^{T_n} alpha_n(zeta_{s,N}) = 1,
epsilon_n(zeta_{s,N}) = u != 1,
(q_s^{T_J} alpha_J(d_J zeta_{s,N}), epsilon_J(d_J zeta_{s,N})) = (1,1)
for every |J|<=N.
```

Equivalently,

```text
u in H^vert_{I,s,N,n,c}
```

for cofinally all `(s,N)`.  Therefore the vertical-kernel endpoint lemma is
false as stated.

This does not produce a Sawin counterexample: the underlying `X` is an
involutive flip solution, dominated by the two-point flip rack.  It only
refutes this endpoint-separation lemma as a route to Sawin.

The repair/upgrade analysis is recorded in
`proofs/rackable_endpoint_absorption.md`.  If these external endpoint labels
are made faithful as actual finite marker-fibre bisections, YBE forces either
commuting bisections over the old flip table, or conjugation covariance

```text
phi_{p*q} = phi_p phi_q phi_p^-1.
```

In the noncommuting case the bisections assemble into a finite rack
`C sqcup F`, with `C` a finite conjugation-stable set of endpoint bisections
and `F` the endpoint fibre.  The same Brunnian vertical words then move an
actual point of that rack, so they are detected by a finite rack.  Thus the
marker obstruction is endpoint-realizable only in a rack-harmless way.

## Guardrail

The one-germ flip interval does not refute the lemma because its endpoint is
only exponent-sum data.  The refutation needs multiple old germs whose
crossings with the marker realize independently chosen noncommuting endpoint
values, while old-old crossings remain unsupported.

Any endpoint route that remains viable must impose an additional restriction
excluding such artificial endpoint-labelled intervals, or it must tie endpoint
labels to the actual residual action more tightly than the current interval
axioms do.

The tighter admissibility filter is now: endpoint motion must be actual and
not absorbed by a finite conjugation/action rack factor.  Faithful rackable
endpoint movement is automatically Sawin-harmless.
