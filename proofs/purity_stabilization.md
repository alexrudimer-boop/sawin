# Purity stabilization in local detectors

Date: 2026-05-28

This note records a small but important convention in the local reduction.
Some branch proofs, such as the involutive and permutation-form branches, use
formulas that only apply after the Artin permutation is identity.  The local
setup must therefore not silently assume that

```text
beta in ker rho_{Q,n}
```

already implies that `beta` is pure.  It need not.

## Detector Source Of Purity

The sharp obstruction theorem always uses

```text
A_G = T_2 x (G x G),
```

where `T_2` is the two-point trivial rack.  The braid action of `T_2` on
`T_2^n` is the ordinary coordinate-permutation action.  Since there are two
available labels, every nonidentity Artin permutation moves some tuple in
`T_2^n`.  Hence

```text
ker rho_{T_2,n} = P_n.
```

Consequently

```text
rho_{A_G,n}(beta)=1
```

forces the Artin permutation of `beta` to be identity before the active
`G x G` longitude coordinates are considered.

Equivalently, the kernel form

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)
    => Delta_n(beta)=1
```

includes the Artin permutation condition as part of the hypothesis.  A branch
proof may use pure-braid formulas after this hypothesis is imposed, but not
merely from `beta in ker rho_{Q,n}`.

## Harmless Stabilization

If a base rack `Q` does not itself detect the Artin permutation, it may be
replaced by

```text
Q x T_2.
```

This only shrinks the kernel:

```text
ker rho_{Q x T_2,n} = ker rho_{Q,n} cap P_n subset ker rho_{Q,n}.
```

Thus if `Q` dominates a quotient `Z`, then `Q x T_2` also dominates `Z`.
In the actual sharp-obstruction step this stabilization is already present
inside `A_G`, so the final rack

```text
Q x A_G
```

forces both base fixing and Artin-purity for any braid in its kernel.

## Audit Guardrail

The test `test_trivial_two_factor_forces_artin_permutation` checks the
convention in the degenerate case `G=1`: with the `T_2` factor included, the
positive generator `sigma_1` is not in the detector kernel, while
`sigma_1^2` is pure and lies in the `T_2` kernel; without the `T_2` factor,
the one-point active rack would incorrectly miss the Artin permutation.

This is why branch notes should phrase pure-braid formulas as consequences of
the full finite longitude identity, not as consequences of quotient-base
kernel membership alone.
