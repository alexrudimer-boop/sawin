# Terminal gauge Artin-defect target

Date: 2026-05-30

This note records the current smallest positive theorem target.  It does not
prove Sawin finite-rack domination and it does not construct a counterexample.

The proof-critic gap remains the uniform descent-separation and endpoint-
longitudinalization theorem in the `bi_free_universal_corridor_bottleneck`
branch.  The surrounding reductions have narrowed the genuinely unresolved
part to terminal gauge/unit holonomy.

## Statement needed

Let

```text
pi : X -> Z
```

be a local-minimal bi-free universal-corridor interval, let `Q` dominate `Z`,
and put

```text
N_n = ker rho_{Q,n}.
```

Let `U` be one fixed interval-level terminal gauge factor: a lower endpoint
unit group, a Schutzenberger factor, or the remaining fixed unit factor after
Green/Schutzenberger readout.  For a residual braid

```text
beta in N_n
```

write the transported terminal gauge endpoint as

```text
S_beta = g_terminal g_initial^-1 in U.
```

The missing positive lemma is:

```text
Terminal Gauge Artin-Defect Lemma.
Every such S_beta is a product of evaluated Artin permutation defects
beta(w) p_beta(w)^-1 in the fixed group U.
```

Equivalently, there are finitely many words `w_k in F_n`, signs
`epsilon_k in {+1,-1}`, and input-dependent homomorphisms

```text
psi_k : F_n -> U
```

such that

```text
S_beta =
  product_k psi_k(beta(w_k) p_beta(w_k)^-1)^{epsilon_k}.
```

By the Artin-defect sieve, each factor lies in

```text
V_beta(U)=< phi(L_i(beta)) : phi:F_n->U, 1<=i<=n >.
```

Therefore

```text
S_beta in V_beta(U).
```

## Why this closes the positive route

The balanced Green decomposition has already reduced a raw
Green/Schutzenberger first-output defect to

```text
Artin-visible commutator * terminal gauge boundary.
```

The commutator is itself an Artin permutation defect value, hence already
belongs to `V_beta`.  If the terminal gauge endpoint also belongs to
`V_beta(U)`, then identity finite-`U` longitude data kills the entire
Green/Schutzenberger/lower-unit endpoint.

For all fixed factors in

```text
H(pi,Q)
```

the direct-product longitude calculus assembles the factor witnesses into one
product detector.  Thus

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
    => Delta_n(beta)=1.
```

The sharp obstruction theorem then supplies the local rack

```text
Q x A_{H(pi,Q)}.
```

The congruence-chain induction assembles the local racks into one finite rack
independent of braid index.

## Why this is not yet outcome A

The archive proves the certificate calculus around this statement:

1. Artin permutation defects lie in `V_beta(U)`.
2. `V_beta(U)` is normal, so chart conjugates are harmless.
3. Factor witnesses assemble into one fixed product detector.
4. Identity product-longitude data kills supplied endpoint witnesses.

It does not yet prove that every remaining terminal gauge endpoint has the
Artin-defect display above.  That symbolic identity is the missing theorem.

## Exact negative seed if it fails

If this lemma is false, a bounded endpoint miss is still not outcome B.  A
negative proof must exhibit an explicit local-minimal interval and upgrade the
failure to a normalized-law sequence

```text
beta_j in B_{q_j},      q_j -> infinity,
```

such that `beta_j in N_{q_j}`, every finite group eventually has identity
recursive Artin-longitude data on `beta_j`, and the residual action still
moves a fibre tuple.

Thus the fork is now:

```text
prove terminal gauge Artin-defect visibility, or build the normalized-law
obstruction from the first genuine terminal gauge failure.
```
