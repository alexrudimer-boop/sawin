# Rank-profile collapse of mixed-unit continuation

Date: 2026-05-30

This note follows `proofs/mixed_unit_companion_separation.md`.  It does not
prove the Master Local-Minimal Residual Theorem.  It removes another false
mixed-unit obstruction: proper nontrivial section-kernel profiles are
Green/Schutzenberger-visible.  The only hidden section-kernel collapse left in
the constant-observer case is rank-one, i.e. constant-section triangular.

## Setup

Work in the remaining constant-observer universal-continuation case

```text
Theta^cont = Nabla,
K^O = Nabla.
```

Thus continuation changes generate the whole local congruence, while every
currently certified Green, Schutzenberger, atom, quotient, known-branch, and
endpoint/unit observer is fibrewise constant.

Let a lower local row be

```text
T_{a,b}(x,y)=(u,v),
x in A_a, y in A_b, u in A_{a*b}, v in A_a
```

in the side convention used for the continuation corridor.  Define coordinate
sections

```text
L_x^{a,b}: A_b -> A_{a*b},   L_x^{a,b}(y)=u,
R_y^{a,b}: A_a -> A_a,       R_y^{a,b}(x)=v.
```

The previous note shows that if one of these sections collapses two inputs,
the companion output separates those inputs because the full row `T_{a,b}` is
bijective.

## Rank-profile lemma

Suppose a noninjective coordinate section survives the certified
Green/Schutzenberger readout without being detected.  Then its kernel profile
cannot be proper nontrivial.  Hence its kernel is universal and the section is
constant.

Proof.  A noninjective finite map has a nontrivial kernel partition of its
domain.  If this kernel partition is proper nontrivial, it defines a
nontrivial Green kernel-block profile for the coordinate-action observer.  The
fixed detector product in the bottleneck branch explicitly includes symmetric
groups on Green kernel-block quotients and Schutzenberger action groups.  Such
a proper kernel profile is therefore visible in the certified
Green/Schutzenberger readout.

In the remaining case `K^O=Nabla`, every certified observer is fibrewise
constant.  Thus no proper nontrivial section-kernel profile can remain hidden.
The only nontrivial kernel type left is universal.  A universal kernel means
all inputs of the section have the same output, so the section has rank one.
QED.

When the raw coloured fibres of a section have unequal cardinalities, a map
can be injective but not surjective.  That is not a section-kernel
context-recovery collapse: no input distinction is lost.  The executable audit
records such injective non-surjective sections separately so they are not
silently grouped with hidden rank-loss.

## Consequence: triangular rank-one residue

After proper kernel profiles have been routed through the fixed
Green/Schutzenberger readouts, every hidden rank-losing section is constant:

```text
L_x^{a,b}(y)=alpha_{a,b}(x)  for all y,
```

or dually

```text
R_y^{a,b}(x)=gamma_{a,b}(y)  for all x.
```

Therefore the final mixed-unit obstruction is narrower than arbitrary context
recovery.  It has triangular rank-one form, for example

```text
T_{a,b}(x,y) =
  (alpha_{a,b}(x), beta_{a,b,x}(y)),
```

or the side-dual form

```text
T_{a,b}(x,y) =
  (lambda_{a,b,y}(x), gamma_{a,b}(y)).
```

The companion-separation lemma says that the nonconstant companion coordinate
must carry the distinctions lost by the constant section.

## Updated positive theorem target

The remaining A-route statement is now:

```text
No constant-section triangular bottleneck theorem.
```

In every local-minimal interval reaching the
`bi_free_universal_corridor_bottleneck`, a constant-section triangular lower
row must route to one of the already closed branches: product/permutation,
affine or product holonomy, locally nondegenerate/guitar after quotienting, or
strand-continuing transport-rack after descent.

If this theorem is proved, the A-route closes:

1. strand-continuing rows are detected by transport-state rackification;
2. two-sided unit rows are closed by the nondegenerate/guitar branch;
3. proper-rank mixed-unit rows are Green/Schutzenberger-visible;
4. constant-section triangular rows route to a closed branch;
5. all residual endpoint components have fixed-factor longitude certificates;
6. product-longitude calculus assembles one finite `H(pi,Q)`;
7. the sharp obstruction theorem supplies `Q x A_H`;
8. congruence-chain induction gives a finite rack independent of braid index.

## Updated B seed

A counterexample can no longer use:

- a raw non-strand-continuing row;
- a nonunit section of proper intermediate kernel profile;
- a Green or Schutzenberger row defect;
- a reset-like nonunit label;
- a bounded finite detector miss.

The only remaining seed in this channel is an explicit local-minimal
bottleneck interval whose hidden continuation motion is carried by rank-one
triangular sections, and whose resulting context recovery can be upgraded to
a normalized-law sequence invisible to every finite group while still moving a
residual tuple.

## Executable audit

The helper

```text
section_rank_profile_collapse_audit(interval)
```

records every left and right coordinate section with:

- domain size and codomain size;
- rank;
- kernel blocks and image;
- kernel kind: equality, proper, or universal;
- whether the section is bijective, constant, or injective non-surjective.

The audit exposes:

```text
proper_kernel_rows
constant_section_rows
injective_non_surjective_rows
hidden_kernel_rows_after_proper_profiles_removed
hidden_kernel_rows_are_constant
```

It is a finite row-profile ledger, not a finite-search proof of the global
theorem.  Its role is to make the final obstruction exact: classify
constant-section triangular YBE rows in the local-minimal bottleneck branch,
or turn one into the required normalized-law counterexample.
