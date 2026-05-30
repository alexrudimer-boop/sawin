# Point-Pushing Abelian-Chief Relation Module

Date: 2026-05-30

This note linearizes the abelian-chief part of the remaining Brunnian
product-prefix obstruction.

It does not prove outcome A or B.  It shows that an abelian-chief first
failure is not an arbitrary solvable quotient: it is exactly a nonzero
quotient of the detector orbit relation module.

## Setup

Fix a finite bijective set-theoretic YBE solution `X`, a product-prefix
detector group `Pi_j`, and a first-failure Brunnian extension row at arity
`k+1`.

Let

```text
D = D_{k+1}(Pi_j),
P = P_{k+1}(X).
```

Arity `k` is already detected, but arity `k+1` fails.  By jump normalization,
the failure can be chosen inside the relative deletion kernel

```text
ker(F_{k+1}->F_k).
```

Let `C_D` be the old suffix detector subgroup, and let

```text
q:C_D -> C_X
```

be the already-existing old marked quotient on the suffix action.  Let `d in D`
be the detector image of the newly added far-left point-push, and let `h in P`
be the corresponding action image.

For each `c in C_D`, define transported detector and action labels

```text
o_c = c d c^{-1},
a_c = q(c) h q(c)^{-1}.
```

Let `F_C` be the free group on generators `t_c` indexed by `c in C_D`, and
define

```text
mu_D:F_C -> N_D=<o_c:c in C_D>,      mu_D(t_c)=o_c.
```

After passing to a finite quotient `H` of the transported action orbit
subgroup, also define

```text
mu_H:F_C -> H,                       mu_H(t_c)=image(a_c).
```

Write

```text
R = ker(mu_D).
```

By the Brunnian orbit criterion, a vertical Brunnian failure in this quotient
is exactly an element `r in R` such that

```text
mu_H(r) != 1.
```

## Minimal Quotient Compression

Choose `H` of minimal order among finite quotients of the transported action
orbit subgroup for which a vertical failure survives.  Let

```text
V = mu_H(R).
```

Then `H` is monolithic, with unique minimal nontrivial normal subgroup `M`, and

```text
1 != V <= M.
```

### Proof

Since `R` is normal in `F_C`, its image `V` is normal in
`H=mu_H(F_C)`.  If `N normal H` is nontrivial and `V` is not contained in `N`,
then the quotient `H/N` still sees a nontrivial image of `V`, contradicting
the minimality of `H`.  Hence `V` is contained in every nontrivial normal
subgroup of `H`.

Therefore `H` has a unique minimal nontrivial normal subgroup.  If two minimal
normal subgroups existed, both would contain the nontrivial subgroup `V`, so
their intersection would be nontrivial; minimality would force them to be
equal.  Call the unique minimal normal subgroup `M`.  Then `1 != V <= M`.
QED.

## Abelian-Chief Linearization

Assume now that the chief layer is abelian:

```text
M ~= C_p^r.
```

Then the failure is a nonzero module quotient of the detector relation module.

Since `mu_H(R)<=M`, the map `mu_H` modulo `M` kills `R` and therefore factors
through `mu_D`:

```text
F_C --mu_D--> N_D --bar_nu--> H/M.
```

Consequently the conjugation action of `F_C` on `M` factors through `N_D`.
Define

```text
tau:R -> M,          tau(r)=mu_H(r).
```

Because `M` is abelian, `tau` is a group homomorphism.  Also, for
`f in F_C` and `r in R`,

```text
tau(f r f^{-1})
  = mu_H(f) tau(r) mu_H(f)^{-1}.
```

If two elements of `F_C` have the same image in `N_D`, their quotient lies in
`R`, and its `mu_H`-image lies in `M`; conjugation by elements of the abelian
group `M` is trivial on `M`.  Thus the action in the displayed formula depends
only on `mu_D(f)`.  The map `tau` is therefore `N_D`-equivariant.

Let

```text
Rel_D = R/[R,R]
```

with its usual `Z[N_D]`-module structure by conjugation.  Since `M` is an
elementary abelian `p`-group, `tau` factors through

```text
Rel_D,p = Rel_D tensor F_p.
```

The induced map

```text
Rel_D,p -> M
```

is nonzero because the row is a vertical failure.  Its image is an
`H`-normal subgroup contained in the minimal normal subgroup `M`.  Hence the
image is all of `M`.

Therefore every abelian-chief first failure produces a surjective
`F_p[N_D]`-module quotient

```text
Rel_D tensor F_p  ->>  M.
```

Conversely, for an actual Brunnian row, a nonzero value of the relation-lift
map `R -> M` is exactly a nontrivial vertical Brunnian failure.  The theorem is
therefore an exact linearization of the abelian chief layer of an actual row.

## Consequence For The Fork

Every product-prefix B tail has a subsequence of one of two forms.

1. **Abelian-chief module tail.**  There are primes `p_j`, arities `k_j`,
   detector orbit groups `N_{D,j}`, and irreducible modules
   `M_j ~= C_{p_j}^{r_j}` such that

   ```text
   Rel_{D,j} tensor F_{p_j} ->> M_j
   ```

   and the corresponding relation-lift value is nonzero.

2. **Nonabelian-chief tail.**  The monoliths are

   ```text
   M_j ~= S_j^{r_j}
   ```

   for nonabelian finite simple `S_j`, and the failure is a nontrivial
   relation lift into that transitive simple-power monolith.

Thus the abelian side of the remaining B route is a finite module-quotient
problem, not a vague solvable quotient problem.  A positive proof may now rule
out abelian relation-module tails and nonabelian simple-power tails.  A
negative proof must construct one explicit infinite tail of one of those two
types, which then right-stabilizes to the normalized-law obstruction sequence
by the product-prefix obstruction theorem.

## Audit Hook

The helper

```text
point_pushing_abelian_chief_relation_module_audit(...)
```

checks the finite-group bookkeeping for an abelian-chief row: the relation
image is nontrivial, normal, contained in the unique minimal abelian normal
subgroup, and therefore equals that chief layer.  It is a guardrail for finite
certificates; the symbolic proof above is the all-arity reduction.
