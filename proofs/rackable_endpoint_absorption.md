# Rackable Endpoint Absorption

Date: 2026-06-04

This note records the same-chat Pro repair to
`proofs/vertical_kernel_endpoint_refutation.md`, sharpened after asking
whether the rack detector integrates as a marked braid factor.

The flip-marker construction refutes the vertical endpoint lemma as stated,
but it is not a Sawin obstruction.  If the formal endpoint labels are upgraded
to faithful actual finite fibre bisections, YBE forces the Artin/rack
conjugation covariance.  The bisections and the finite fibre then form a
finite rack

```text
Y = Phi x F
```

which is not merely an abstract endpoint observer: it is an equivariant
strand-level marked braid factor for the faithful endpoint-fibre extension.

Thus endpoint-only Brunnian classes are Sawin-relevant only after excluding
faithful bisectional, probe-complete endpoint movement.

## Faithful Bisectional Endpoint Systems

Let `I` be an actual completed-context interval with retained germs `G`.  A
faithful bisectional endpoint system consists of:

1. a finite fibre set `F`;
2. for each retained germ `e in G`, a permutation

```text
phi_e in Sym(F);
```

3. local fibre dynamics over every supported row

```text
B(e,f) = (e',f')
```

of the form

```text
(e,z),(f,w) |-> (e', phi_e(w)), (f', z).
```

Here `f'` is the physical continuation of the strand formerly carrying `e`.
Thus the left strand operator acts on the right strand fibre, and the left
fibre is copied to the right output.

Faithfulness means that every nonidentity endpoint element

```text
u in <phi_e : e in G> <= Sym(F)
```

moves some fibre point `z in F`.

This excludes the artificial endpoint labels from the flip-marker refutation
unless those labels are realized by actual finite fibre movement.

## YBE Forces Covariance

Let

```text
B(e,f) = (e',f').
```

Because `f'` is the physical continuation of `e`, the operator carried by
`f'` is

```text
phi_{f'} = phi_e.                         (1)
```

Now compare the two YBE reductions of a triple with two ordinary germs and one
probe fibre.  The probe fibre is acted on by the same total bisection on both
sides, so

```text
phi_{e'} phi_{f'} = phi_e phi_f.          (2)
```

Combining (1) and (2) gives

```text
phi_{e'} = phi_e phi_f phi_e^-1,
phi_{f'} = phi_e.                         (3)
```

These are exactly the Artin meridian row relations and the rack operator-label
recursion.  Faithful bisectional endpoint labels are therefore not arbitrary
external labels: actual YBE functoriality forces them to transform by
conjugation.

## The Absorbing Product Rack

Let

```text
Phi = <phi_e : e in G> <= Sym(F).
```

Define

```text
Y = Phi x F.
```

For `alpha,beta in Phi` and `z,w in F`, define

```text
(alpha,z) * (beta,w) = (alpha beta alpha^-1, alpha(w)).       (4)
```

The associated rack YBE table is

```text
R_Y((alpha,z),(beta,w))
  =
((alpha beta alpha^-1, alpha(w)), (alpha,z)).
```

For `a=(alpha,z)`, the left translation is

```text
L_a(beta,w) = (alpha beta alpha^-1, alpha(w)).
```

It is bijective because `alpha` acts bijectively on `Phi` by conjugation and
on `F` by its given permutation action.

For self-distributivity, compute

```text
L_(alpha,z) L_(beta,w)(gamma,v)
  =
(alpha beta gamma beta^-1 alpha^-1, alpha beta(v)).
```

On the other hand,

```text
(alpha,z) * (beta,w)
  =
(alpha beta alpha^-1, alpha(w)),
```

so

```text
L_((alpha,z)*(beta,w)) L_(alpha,z)(gamma,v)
  =
(alpha beta gamma beta^-1 alpha^-1, alpha beta(v)).
```

Thus

```text
L_a L_b = L_(a*b) L_a,
```

and `Y` is a finite rack.

## Equivariant Strand-Level Factor

For a residual state

```text
e = (e_1,...,e_n)
```

and a fibre tuple

```text
z = (z_1,...,z_n) in F^n,
```

define

```text
Psi_n(e,z)
  =
((phi_{e_1},z_1),..., (phi_{e_n},z_n)) in Y^n.
```

If a supported crossing at positions `i,i+1` has

```text
B(e_i,e_{i+1}) = (e_i',e_{i+1}'),
```

then (3) gives

```text
phi_{e_i'}     = phi_{e_i} phi_{e_{i+1}} phi_{e_i}^-1,
phi_{e_{i+1}'} = phi_{e_i}.
```

The fibre update is

```text
(z_i,z_{i+1}) |-> (phi_{e_i}(z_{i+1}), z_i).
```

Therefore the `Y` colours update as

```text
((phi_{e_i},z_i),(phi_{e_{i+1}},z_{i+1}))
  |->
((phi_{e_i} phi_{e_{i+1}} phi_{e_i}^-1, phi_{e_i}(z_{i+1})),
 (phi_{e_i},z_i)),
```

which is exactly the rack crossing `R_Y`.

Hence, for every actual supported branch word `beta`,

```text
Psi_n(rho^I_n(beta)(e,z)) = rho^Y_n(beta) Psi_n(e,z).          (5)
```

This is the needed marked braid factor: the rack detector integrates with the
actual endpoint-fibre tower, not just with the final endpoint value.

## Kernel Implication

Suppose an actual residual branch `gamma` has endpoint

```text
u in Phi,       u != 1.
```

By faithfulness, choose `z in F` with `u(z) != z`.  Put `z` in the relevant
terminal fibre coordinate and choose arbitrary compatible fibre values in the
other coordinates.

By equivariance (5), the rack action changes that coordinate from `z` to
`u(z)`.  Hence

```text
rho^Y_n(gamma) != 1.
```

Equivalently,

```text
rho^Y_n(gamma)=1  =>  epsilon_n(gamma)=1.                     (6)
```

Thus no branch with faithful nontrivial endpoint can be invisible to the
finite rack `Y=Phi x F`.  Even if its bounded deletion shadows vanish and its
other Artin readouts are trivial, this rack detects the endpoint directly.

## Artin Quotient

The same covariance defines a finite quotient of the Artin meridian part.
Send the Artin row generator `a_e` to `phi_e`.  The Artin relations

```text
a_{e'} = a_e a_f a_e^-1,
a_{f'} = a_e
```

are exactly (3).  Hence faithful bisectional endpoint movement is already
visible in a finite Artin quotient

```text
Art_I -> Phi.
```

It cannot be profinitely Artin-null.

## The Marker Obstruction Becomes Harmless

The refutation in `proofs/vertical_kernel_endpoint_refutation.md` used the
involutive flip table on

```text
X = T sqcup {m},
```

where `T` is the set of transpositions in `S_3`.  The endpoint labels were
external `S_3` labels attached to marker crossings.  They produced Brunnian
vertical point-pushing words with nontrivial endpoint and trivial Artin and
bounded deletion shadows.

If those labels are made faithful as actual finite fibre bisections while
old-old crossings remain literal flips, then for old colours `p,q`

```text
B(p,q) = (q,p).
```

The covariance (3) gives

```text
phi_q = phi_p phi_q phi_p^-1,
```

so `phi_p` and `phi_q` commute.  Thus the noncommuting `S_3` Brunnian
mechanism is impossible over old-old flip.

If one changes the old-old crossing so noncommuting bisections are allowed,
then covariance forces

```text
phi_{p*q} = phi_p phi_q phi_p^-1,
```

and the product rack `Phi x F` above detects every nontrivial endpoint.

So the marker obstruction has only two faithful outcomes:

```text
commuting endpoint action, so the nonabelian Brunnian endpoint dies;
```

or

```text
noncommuting endpoint action, so a finite rack detector appears.
```

It cannot yield a normalized-law no-rack sequence.

## Correct Admissibility Filter

Endpoint-only Brunnian classes are not enough for outcome B.  A candidate
negative sequence must involve residual movement that is not representable as

```text
(z,w) |-> (phi_e(w), z)
```

with `phi_e in Sym(F)` satisfying the actual YBE covariance (3).

Equivalently, a genuine negative example must exhibit at least one of:

1. non-bisectional fibre movement, where local movement is not by
   permutations of one fixed finite endpoint fibre;
2. non-probe-complete movement, where the alleged endpoint cannot be tested by
   adjoining an actual finite probe fibre closed under YBE cubes;
3. higher-arity nonlocal movement, where the moved datum is not carried by a
   single strand/fibre and cannot be localized into finite operator labels.

The flip-marker refutation fails the first condition before repair, and after
faithful repair it is rack-detected by `Phi x F`.  It is therefore a guardrail
against an overbroad endpoint lemma, not evidence for a Sawin-negative
solution.
