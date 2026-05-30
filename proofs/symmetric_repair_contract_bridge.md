# Symmetric repair-contract bridge

Date: 2026-05-30

This note connects the proof-critic repair contract to the local symmetric
detector dichotomy.  It does not prove the missing descent-separation or
endpoint-longitudinalization theorem.  It proves that any successful finite
repair-contract detector can be replaced by one symmetric group detector.

## Setup

Fix a local-minimal interval

```text
pi : X -> Z
```

with `Z` dominated by a finite rack `Q`, and put

```text
N_n = ker rho_{Q,n}.
```

Suppose the descent-endpoint repair contract has supplied a fixed finite
detector group

```text
H = H(pi,Q)
```

such that, for every braid index `n`,

```text
beta in N_n,
Lambda_{H,n}(beta)=Lambda_{H,n}(1)
    => Delta_n(beta)=1.
```

The group `H` is fixed at the interval level.  It may be a product of Green,
Schutzenberger, atom, known-branch, transport, and endpoint/unit factors, but
it has no braid-index parameter.

## Lemma: the repair detector can be made symmetric

Let

```text
m >= |H|.
```

Then

```text
beta in N_n,
Lambda_{S_m,n}(beta)=Lambda_{S_m,n}(1)
    => Delta_n(beta)=1
```

for every `n`.

Proof.  Embed `H` into `S_m` by the left regular representation on `|H|`
points, fixing the remaining `m-|H|` points if `m>|H|`.

If `Lambda_{S_m,n}(beta)` is trivial, then every assignment

```text
Phi : F_n -> S_m
```

sends every recursive Artin longitude `L_i(beta)` to the identity.  In
particular this holds for assignments of the form

```text
F_n -> H -> S_m.
```

Since the left regular embedding is injective, every assignment

```text
phi : F_n -> H
```

sends every `L_i(beta)` to the identity in `H`.  Hence

```text
Lambda_{H,n}(beta)=Lambda_{H,n}(1).
```

The supplied repair-contract implication for `H` now gives
`Delta_n(beta)=1`.  QED.

## Consequence

The positive side of the local symmetric dichotomy can be stated in the same
language as the repair contract:

```text
construct a fixed interval-level repair detector H(pi,Q)
```

is equivalent, for domination purposes, to

```text
construct a fixed symmetric degree m(pi,Q)=|H(pi,Q)|.
```

Larger degrees also work by symmetric tower monotonicity:

```text
K_{S_M}(n) subset K_{S_m}(n)    for M >= m.
```

Thus a successful repair package supplies the local rack

```text
Q x A_{S_m}.
```

The sharp obstruction theorem applies because

```text
ker rho_{A_{S_m},n}=K_{S_m}(n).
```

## What this does not prove

This note only bridges detector formats after the repair contract has already
been proved.  It does not construct:

1. the fixed descent-separating readout;
2. the faithful residual decomposition;
3. the fixed endpoint/unit groups;
4. the all-`n` witnesses that every routed endpoint lies in `V_beta(H_s)`.

Those four items remain the missing uniform descent-endpoint theorem for the
`bi_free_universal_corridor_bottleneck` branch.

## Executable audit

The helper

```text
symmetric_repair_contract_bridge_audit(...)
```

records this bridge for supplied certificates.  It returns
`proves_symmetric_detector_from_repair_contract` exactly when:

1. the supplied `descent_endpoint_repair_contract_audit(...)` passes;
2. the detector group order is positive;
3. the chosen symmetric degree is at least the detector group order.

When no degree is supplied, the helper uses the left-regular degree

```text
m = |H(pi,Q)|.
```

The helper deliberately does not discover the missing repair-contract
witnesses.  It only prevents ambiguity between the product-detector repair
language and the symmetric-detector fork: once a fixed finite repair detector
is valid, a fixed symmetric detector is valid too.
