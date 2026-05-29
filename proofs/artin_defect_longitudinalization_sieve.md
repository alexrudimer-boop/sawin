# Artin-defect longitudinalization sieve

Date: 2026-05-29

This note records the next proof-side reduction for the remaining
`bi_free_universal_corridor_bottleneck` branch.  It does not prove the Master
Local-Minimal Residual Theorem, and it does not prove either final outcome A or
B.  It replaces the last open search for arbitrary endpoint-longitude
expressions by a sharper target: display every elementary group-like
Green/corridor endpoint generator as a finite product of Artin permutation
defect values in one of the fixed detector factors.

The value of this step is that Artin permutation defects are automatically
longitude-visible for every finite target group.  Thus a displayed endpoint
factorization through these defects gives a non-enumerative certificate that
the endpoint lies in the longitude-value subgroup required by the sharp
obstruction theorem.

## Setup

Let

```text
F_n = <x_1,...,x_n>
```

and let `beta in B_n`.  The repository uses the recursive Artin-longitude
convention

```text
beta(x_j) = L_j(beta) x_{p_beta(j)} L_j(beta)^-1,
```

where `p_beta` is the Artin strand permutation.  For a finite group `K`, set

```text
V_beta(K) =
  < phi(L_i(beta)) : phi:F_n -> K, 1 <= i <= n >.
```

The sharp detector construction needs endpoint labels to land in this subgroup.
If `Lambda_{K,n}(beta)=Lambda_{K,n}(1)`, then the Artin permutation is trivial
and `V_beta(K)={1}`.

Define the Artin-defect normal subgroup

```text
D_beta = << L_1(beta),...,L_n(beta) >>_{F_n}.
```

For a word `w in F_n`, write `p_beta(w)` for the word obtained by replacing
each generator `x_j` by `x_{p_beta(j)}`.

## Lemma 1: normal Artin defects evaluate into V_beta

Lemma.  For every finite group `K`, every homomorphism `phi:F_n -> K`, and
every `d in D_beta`,

```text
phi(d) in V_beta(K).
```

Proof.  Since `d` lies in the normal closure, write

```text
d = product_m u_m L_{i_m}(beta)^{epsilon_m} u_m^-1,
```

with `u_m in F_n` and `epsilon_m in {+1,-1}`.  For each factor define

```text
psi_m:F_n -> K,
psi_m(x_j)=phi(u_m x_j u_m^-1).
```

Then

```text
phi(u_m L_{i_m}(beta)^{epsilon_m} u_m^-1)
  = psi_m(L_{i_m}(beta))^{epsilon_m}.
```

Each factor is a generator of `V_beta(K)` or the inverse of such a generator.
Their product is therefore in `V_beta(K)`.  QED.

## Lemma 2: Artin permutation defects lie in D_beta

Lemma.  For every word `w in F_n`,

```text
beta(w) p_beta(w)^-1 in D_beta.
```

Proof.  In the quotient `F_n/D_beta`, every longitude `L_j(beta)` is trivial.
Thus

```text
beta(x_j) = x_{p_beta(j)}
```

for every generator.  Since both sides extend multiplicatively to words,
`beta(w)=p_beta(w)` in `F_n/D_beta`.  Hence
`beta(w) p_beta(w)^-1` lies in `D_beta`.  QED.

## Endpoint sieve criterion

Fix a target interval and its fixed detector product

```text
H(pi,Q) = product_s H_s.
```

Let a remaining group-like endpoint factor be

```text
h_e(beta,z,x) in H_s.
```

It is enough to display, inside the fixed factor `H_s`,

```text
h_e(beta,z,x)
  = product_m phi_m(beta(w_m) p_beta(w_m)^-1)^{epsilon_m},
```

where each `phi_m:F_n -> H_s` may depend on the braid, base tuple, input fibre
tuple, output coordinate, and finite corridor state, while the target group
`H_s` is fixed by the interval and does not depend on `n`.

By Lemmas 1 and 2, each factor

```text
phi_m(beta(w_m) p_beta(w_m)^-1)
```

lies in `V_beta(H_s)`.  Therefore `h_e(beta,z,x)` lies in `V_beta(H_s)`.
The direct-product witness calculus in
`proofs/bifree_corridor_endpoint_factorization.md` then assembles these
factorwise witnesses into one witness in

```text
V_beta(H(pi,Q)).
```

Consequently, if

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1),
```

then every endpoint factor displayed by this Artin-defect criterion is killed.
If the finite endpoint/readout decomposition is faithful, the corresponding
residual coordinate is fixed.  If this is done for every residual coordinate
and every residual row, the sharp obstruction theorem supplies the local rack

```text
Q x A_{H(pi,Q)}.
```

## Nonunit collapse cannot be the final obstruction

The corridor branch is a residual permutation problem.  A finite product of
total transformations whose final residual action is a permutation cannot use a
nonunit/reset-like factor as an unavoidable final obstruction: the unit
factorization gate has already isolated the group-like part that remains after
telescoping.  Thus the serious remaining obstruction is not a raw aperiodic
collapse.  It must live in one of the fixed group factors: Green kernel-block
symmetric groups, Schutzenberger action groups, atom-inner groups, quotient or
known-branch detector factors, or fixed endpoint-unit groups.

## Exact remaining local statement

The endpoint-longitude burden is now the following sharper statement.

```text
Artin-defect endpoint lemma.
In every local-minimal interval with verdict
bi_free_universal_corridor_bottleneck, every elementary group-like
Green/corridor endpoint generator is a finite product of Artin permutation
defect values in one fixed factor of H(pi,Q).
```

More explicitly, for each elementary coordinate-kernel corridor generator `e`,
prove inside one of the fixed groups

```text
Sym(Green kernel blocks),
Sch(C),
Inn(atom quotient),
U(M),
or a fixed quotient/known-branch detector factor
```

an identity of the form

```text
u_e(beta,z,x)
  = product_m phi_m(beta(w_m) p_beta(w_m)^-1)^{epsilon_m}.
```

If this boxed local lemma is proved, then the positive route closes:

1. each endpoint factor lies in `V_beta(H_s)`;
2. the factor witnesses assemble into `V_beta(H(pi,Q))`;
3. identity `Lambda_{H(pi,Q),n}` kills all group-like corridor endpoints;
4. the faithful residual readout makes `delta_{n,z}(beta)` trivial;
5. the sharp obstruction theorem gives the local rack `Q x A_{H(pi,Q)}`;
6. congruence-chain induction multiplies the local racks into one global finite
   rack independent of `n`.

If the Artin-defect endpoint lemma fails, that failure is still not a final B
outcome.  A B proof must upgrade it to an explicit finite local-minimal target
interval and a normalized-law sequence whose endpoint units remain nonidentity
while every finite group has identity recursive Artin-longitude data.

## Factor audit checklist

A proof of the Artin-defect endpoint lemma should check, uniformly in `n`:

1. Kernel-block factors.  Each left and right Green kernel-block residual
   permutation is a product of Artin permutation defect values in the fixed
   symmetric group on that block quotient.
2. Schutzenberger factors.  Each regular Green-class coordinate is either
   killed by the atom quotient or displayed as an Artin-defect value product in
   the fixed Schutzenberger action group.
3. Atom quotient factors.  Total rack-like atom layers are handled by their
   fixed inner groups; any information lost under descent-closed coarsening is
   pushed to lower endpoint/unit factors.
4. Lower unit factors.  Every remaining lower section or endpoint composite is
   a unit in one fixed finite monoid and is displayed as an Artin-defect value
   product in the unit group.
5. Product assembly.  All factor displays use fixed interval-level groups.
   Multiplication into `H(pi,Q)` introduces no detector depending on the braid
   index.

This is strictly stronger than finite subgroup-membership at a bounded braid
degree: it asks for the symbolic Artin-defect identities that force membership
in the longitude-value subgroup for all braid indices.

## Executable certificate layer

The code now contains a supplied-certificate checker for this sieve.

```text
artin_permutation_defect_word(n,beta,w)
artin_permutation_defect_longitude_witness(G,n,beta,assignment,w)
artin_permutation_defect_witness_audit(G,n,beta,assignment,w)
endpoint_artin_defect_audit(G,n,beta,endpoint,terms)
endpoint_product_artin_defect_audit(groups,n,beta,endpoints,terms_by_factor)
```

The witness helper expands

```text
beta(w) p_beta(w)^-1
```

into a literal word in generators of `V_beta(G)` by changing assignments to
absorb the normal conjugators.  The endpoint helpers then check that a supplied
product of Artin-defect values equals the endpoint and, factorwise or in a
direct product, evaluates to the same literal longitude-subgroup witness.

As with the earlier endpoint expression audits, these helpers do not find the
missing Green/corridor displays.  They verify the final algebraic handoff once
a symbolic proof supplies those displays.
