# Product readout descent-separation certificate

Date: 2026-05-29

This note follows `proofs/product_readout_kernel_assembly.md`.  It does not
prove the Master Local-Minimal Residual Theorem.  It records the exact
interaction between product readouts and continuation seeds in the current
descent-separation target.

The important point is a guardrail: adding more readout factors refines the
kernel.  Therefore a tuple-valued product readout kills a continuation seed
only when every factor kills that seed.

## Setup

Let `pi:X->Z` be a local interval in rack-side convention.  For a row

```text
T_{a,b}(x,y) = (u,v),
```

a continuation seed is the pair

```text
x ~ v
```

whenever the base row has second output colour `a` and `v != x`.

Suppose we have finitely many fixed readout label systems

```text
r^j_a : A_a -> E^j_a,       j=1,...,m.
```

Let `Phi^j` be the kernel of `r^j`, and let the product readout be

```text
r_a(x) = (r^1_a(x),...,r^m_a(x)).
```

Let `Phi` be the product kernel.

## Lemma: product seed survival is the union of factor survival

For every continuation seed `x ~ v` in fibre `A_a`,

```text
x Phi_a v
```

if and only if

```text
x Phi^j_a v    for every j.
```

Equivalently, the seed survives the product quotient if and only if it
survives at least one factor quotient.

Proof.  By the product-kernel assembly lemma, `Phi_a` is the meet of the factor
kernels:

```text
Phi_a = meet_j Phi^j_a.
```

Thus `x` and `v` are equivalent for the product exactly when they are
equivalent for every factor.  Negating the statement gives the survival form:
the product distinguishes `x` and `v` exactly when some factor distinguishes
them.  QED.

## Consequence

The descent-separation certificate for a fixed product readout requires two
separate facts:

1. factorwise admissibility, so the product kernel is an admissible
   congruence by finite-meet stability;
2. factorwise seed killing, so every continuation seed is killed by every
   factor and therefore by the product.

It is not enough for one detector factor to kill a seed.  If any fixed factor
still separates the two endpoints of a continuation seed, the tuple-valued
product separates them too, and the quotient row remains non-strand-continuing.

This is not a new obstruction to the A-route; it is the precise bookkeeping
needed for the descent-separation theorem.  A successful proof must choose the
Green, Schutzenberger, atom, known-branch, and endpoint/unit readouts so that
their product kernel is admissible and kills the representative continuation
seeds.

## Code certificate

The helper

```text
product_readout_descent_separation_audit(interval,*label_families)
```

records:

- the `ProductReadoutKernelAudit`;
- the descent-separation audit of the tuple-valued product labels;
- the continuation seed rows that survive each factor;
- the seed rows that survive the product;
- whether product seed survival equals the union of factor seed survival.

Its property

```text
proves_product_descent_separation
```

is true only when:

1. product-kernel assembly is certified from admissible factors;
2. product seed survival is exactly the factor-survival union;
3. every factor kills every continuation seed;
4. the product readout passes the descent-separation audit.

The failure helper

```text
product_readout_descent_separation_failures(interval,*label_families)
```

returns the continuation seed rows that survive in the product quotient.

## Updated local proof target

The remaining descent-separation theorem can now be stated in factorwise
certificate form:

```text
Construct fixed interval-level readout factors such that each factor kernel is
admissible and each factor kills every representative continuation seed.
```

Then product readout descent separation gives one admissible fixed product
quotient whose lower row is strand-continuing.  Transport-state rackification
then supplies the finite rack detector for the remaining lower gauge.

If this factorwise statement fails for a concrete interval, the failure is
still only a finite B seed.  It must be upgraded to a normalized-law sequence
invisible to every finite group before it can prove outcome B.
