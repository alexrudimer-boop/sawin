# Descent-endpoint repair contract

Date: 2026-05-30

This note is the repair target after the proof-critic gap audit.  It does not
prove Sawin finite-rack domination.  It states the exact theorem package whose
proof would repair the failed positive assembly in
`proofs/master_local_residual_positive_closure.md`.

The point is to separate the missing work into checkable hypotheses:

1. a fixed finite readout whose kernel descends the local table and kills
   non-strand-continuing seeds;
2. a faithful residual decomposition through that readout plus externally
   routed endpoint factors;
3. fixed-factor recursive-longitude witnesses for every group-like endpoint.

If those three hypotheses are supplied uniformly for every local-minimal
`bi_free_universal_corridor_bottleneck` interval, the Master Local-Minimal
Residual Theorem follows.  Conversely, any failure of these hypotheses is the
precise seed that must be upgraded to a normalized-law counterexample.

## Setup

Let

```text
pi : X -> Z
```

be a local-minimal interval in the bi-free universal-corridor branch.  Assume
the base has been put in the rack-side convention

```text
R_Z(a,b) = (a*b, a).
```

Let the local row be

```text
T_{a,b}(x,y) = (u,v),
```

with `x,v in A_a`.  The non-strand-continuing seed for this row is

```text
x ~ v.
```

Let `Q` dominate `Z`, let

```text
N_n = ker rho_{Q,n},
```

and let

```text
delta_{n,z}:N_n -> Sym(X_z)
```

be the residual action.

## Fixed readout system

A fixed descent readout is a finite family of maps

```text
r_a : A_a -> E_a
```

depending only on the interval and the quotient detector, not on braid index.
Its kernel family is

```text
x K^r_a y  iff  r_a(x)=r_a(y).
```

The readout is descent-separating if:

1. `K^r` is an admissible local congruence family;
2. every continuation seed satisfies `x K^r_a v`;
3. after quotienting by `K^r`, the remaining lower row is strand-continuing.

The third item follows from the first two by
`proofs/readout_descent_separation_certificate.md`, but it is listed here as
the operational consequence.

## External endpoint routing

The readout quotient may intentionally forget lower information.  A fixed
external endpoint routing consists of:

- finitely many fixed finite groups `H_s`;
- for every residual braid action, finitely many endpoint components

  ```text
  h_e(beta,z,x) in H_s;
  ```

- a faithful reconstruction rule saying that if the readout quotient is fixed
  and all routed endpoint components are identity, then the original residual
  output coordinate equals the input coordinate.

The groups `H_s` may depend on the interval and quotient detector, but not on
`n`.  The endpoint components and the assignments used to certify them may
depend on `n`, `beta`, `z`, `x`, the output coordinate, and finite corridor
state.

## Longitude witness condition

Each routed endpoint component must satisfy

```text
h_e(beta,z,x) in V_beta(H_s),
```

where

```text
V_beta(H_s) =
< phi(L_i(beta)) : phi:F_n -> H_s, 1 <= i <= n >.
```

Equivalently, the endpoint may be displayed as a finite signed product of
evaluated recursive Artin longitudes in `H_s`, or by any of the certified
forms already recorded in the repository:

- a literal endpoint-longitude expression;
- a product endpoint witness;
- a chart-conjugate witness, using normality of `V_beta(H_s)`;
- an Artin-defect display;
- an abelian matrix-longitude witness in finite abelian quotients, followed by
  a kernel witness for the lift.

## Repair theorem

Theorem.  Suppose every local-minimal
`bi_free_universal_corridor_bottleneck` interval admits:

1. a fixed descent-separating readout `r`;
2. fixed external endpoint groups `H_s`;
3. a faithful residual decomposition through the readout quotient and the
   routed endpoint components;
4. `V_beta(H_s)` witnesses for every routed endpoint component, uniformly for
   every `n`, `beta in N_n`, base tuple `z`, and fibre tuple `x`.

Then the interval has a finite detector group

```text
H(pi,Q)
```

independent of `n` such that

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
    => Delta_n(beta)=1
```

for all `n` and `beta in N_n`.

Proof.  Since `K^r` is admissible and kills every continuation seed, the
quotient local table is strand-continuing.  The transport-state rackification
theorem applies to that quotient: the finite readout states form a finite rack
after adjoining the lower transport state, and the inner group

```text
H_transport = Inn(transport-state rack)
```

is a finite detector factor independent of `n`.  By the Artin detector-lift
criterion, identity finite-`H_transport` longitude data fixes the quotient
transport state for every residual braid.

Let

```text
H_endpoint = product_s H_s
```

be the finite product of all external endpoint groups, and set

```text
H(pi,Q) =
H_transport x H_endpoint x H_known
```

where `H_known` denotes the fixed quotient, Green, Schutzenberger, atom, and
closed-branch factors already needed by the interval.  This group is finite
and has no braid-index parameter.

Assume

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1).
```

Projection to `H_transport` fixes the quotient transport state.  Projection to
each endpoint factor `H_s` makes `V_beta(H_s)={1}`.  The endpoint witness
condition therefore kills every routed endpoint component.  Projection to the
known branch factors kills the quotient, atom, Green, Schutzenberger, and
closed-branch components covered by their respective all-`n` detector
lemmas.

The faithful residual decomposition now applies: the quotient readout is
fixed and all routed endpoints are identity, so each residual output
coordinate equals the input coordinate.  Thus

```text
delta_{n,z}(beta)=1
```

for every `z`, hence `Delta_n(beta)=1`.  QED.

## Exact missing theorem

The proof-critic gap is therefore equivalent to the following construction
problem.

```text
Uniform descent-endpoint theorem.
For every local-minimal bi_free_universal_corridor_bottleneck interval,
construct the fixed descent-separating readout, fixed external endpoint
groups, faithful reconstruction rule, and all-n V_beta endpoint witnesses
listed in the repair theorem.
```

This is stronger than finite subgroup membership at a fixed braid index.  It
is a symbolic all-`n` theorem.

## Exact B seed if the theorem fails

A failure of the repair contract has one of the following finite shapes:

1. no fixed interval-level readout kernel is admissible and kills the
   continuation seeds;
2. the quotient after any such readout is not strand-continuing;
3. the readout quotient plus routed endpoint components is not faithful;
4. a routed group-like endpoint has no `V_beta` witness in its fixed factor.

None of these finite failures is itself outcome B.  To prove B, one must
choose an explicit finite YBE solution realizing such a failure and upgrade it
to braid words

```text
beta_j in B_{q_j},     q_j -> infinity,
```

whose recursive Artin-longitude data is eventually trivial in every finite
group while the residual action still moves an explicit tuple.

Thus the repair contract is also the normalized-law counterexample extraction
target.
