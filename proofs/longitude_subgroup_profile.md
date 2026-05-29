# Longitude-subgroup visibility profile

Date: 2026-05-28

This note records a compact diagnostic for normalized-law obstruction
attempts and for finite detector comparisons.

## Definition

For a finite group `G`, braid degree `n`, and braid `beta`, define

```text
V_beta(G)
  =
< phi(L_i(beta)) : phi:F_n -> G, 1 <= i <= n > <= G,
```

where `L_i(beta)` are the recursive Artin longitudes.  Then

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)
```

is equivalent to:

1. the Artin permutation of `beta` is the identity; and
2. `V_beta(G)` is the trivial subgroup.

The forward implication is immediate because identity finite-`G` longitude
data kills every generator of `V_beta(G)`.  Conversely, if the permutation is
identity and `V_beta(G)={1}`, then every longitude value under every
assignment is identity.

## Executable profile

The helper

```text
longitude_subgroup_profile(groups, n, beta)
```

returns one row per named finite group:

- group order;
- Artin permutation;
- number of distinct longitude-value generators;
- size of the generated subgroup;
- a Boolean property `identity_longitude_signature`.

For pure-braid law embeddings, the wrapper

```text
law_braid_longitude_subgroup_profile(groups, word, arity)
```

embeds the free word by the standard last-strand pure generators and returns
the same profile.

This profile is logically equivalent to the full finite-group longitude
signature for the yes/no identity question, but it is much smaller to record
in audits.  It should not be confused with a proof that a branch is detected:
a branch proof must still show that every residual holonomy element lies in
the relevant subgroup `V_beta(G)`.

## Mover profiles

The bounded helpers

```text
longitude_subgroup_mover_profiles(X, groups, n, braid_words)
residual_longitude_subgroup_mover_profiles(qmap, Q, groups, n, braid_words)
```

attach an explicit moved tuple to the same subgroup rows.  The first helper
searches moving braid words for a total finite solution `X`.  The residual
helper first requires the word to fix the supplied quotient/base detector and
then records a moved fibre tuple for the quotient map.

With `require_invisible=True`, these helpers keep only words whose listed
finite groups all have identity longitude data.  They are B-candidate
diagnostics: a row says exactly which tuple still moves and which finite
groups, if any, already see the word.  They remain bounded diagnostics only;
they do not replace the symbolic all-finite-group normalized-law proof
required for outcome B.

## Use in A

For a proposed detector group `G(pi,Q)`, the A-route target can be stated as:

> for every residual braid `beta`, every residual holonomy element attached
> to `beta` belongs to `V_beta(G(pi,Q))`.

Then identity finite-`G(pi,Q)` longitude data forces every such holonomy
element to be trivial.  This is the subgroup form of the
input-dependent-longitude criterion and is already specialized to product
labels in `proofs/product_longitude_subgroup_criterion.md`.

## Use in B

A normalized-law obstruction sequence must make this profile trivial for
every fixed finite group eventually, while still moving a tuple in the finite
YBE action.  Equivalently, for every fixed finite group `G`, the sequence must
eventually have identity Artin permutation and `|V_beta_j(G)|=1`.

Thus the profile is a convenient audit table for candidate B words:
nontrivial subgroup size means the listed group already sees the word, while
trivial subgroup size for a growing finite group list is the required
finite-group invisibility side of B.

## Guardrail tests

The test suite checks:

- a positive generator has full longitude-value subgroup in `C_3`;
- a sixth power of the two-strand pure generator has trivial subgroup profile
  on `C_2` and `C_3`;
- the exponent-law pure-braid embedding gives trivial subgroup profiles on
  the corresponding cyclic groups.

These are convention guardrails only.  The master theorem still requires the
all-`n` residual factorization or a symbolic normalized-law escape.
