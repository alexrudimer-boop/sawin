# Two-strand symmetric detector gate

Date: 2026-05-28

This note makes the two-strand obstruction to the direct
`G_X = Sym(X)` route exact.  It is not a proof of Sawin finite-rack
domination, and it is not a counterexample.  It is a symbolic gate: any
direct symmetric-detector proof must pass it, and any direct symmetric-
detector counterexample can already be detected on two strands if this gate
fails.

The companion note `proofs/two_strand_cyclic_detector.md` records the
opposite guardrail: for every finite solution, some finite cyclic group
detects the two-strand crossing action.  Thus two-strand failures can refute
a proposed detector, but they cannot by themselves prove outcome B.

## Exact `B_2` longitude period

Let `G` be a finite group.  Since `B_2` is infinite cyclic with generator
`sigma_1`, define

```text
P_G = { k in Z : Lambda_{G,2}(sigma_1^k) = Lambda_{G,2}(1) }.
```

Then

```text
P_G = 2 exp(G) Z.
```

Proof.  If `k` is odd, the Artin permutation of `sigma_1^k` is the
transposition of the two strands, so the full finite-G longitude signature is
not the identity.

It remains to consider `k=2m`.  Let `A=sigma_1^2` and let
`c=x_0 x_1` in the free group `F_2`.  The Artin action of `A` is simultaneous
conjugation by `c`:

```text
A(x_i) = c x_i c^{-1},      i=0,1.
```

Therefore `A^m` is simultaneous conjugation by `c^m`.  In the longitude
normalization used by the code, one may take

```text
L_0(A^m) = (x_0 x_1)^m x_0^{-m},
L_1(A^m) = (x_0 x_1)^{m-1} x_0 x_1^{-(m-1)}
```

for `m >= 1`; the case `m=0` is the identity braid.

If `m` is divisible by `exp(G)`, then for every assignment
`x_0 -> a`, `x_1 -> b`, both `(ab)^m`, `a^m`, and `b^m` are identity after the
obvious cancellations above, so both longitude values are identity.

Conversely, if `m` is not divisible by `exp(G)`, choose `g in G` with
`g^m != 1` and evaluate at `x_0 -> g`, `x_1 -> 1`.  Then
`L_1(A^m)` evaluates to `g^m`, so the finite-G longitude signature is not the
identity.  Hence `A^m` is invisible exactly when `m` is divisible by
`exp(G)` for `m >= 0`.  Negative powers follow by inversion, so
`sigma_1^k` is invisible exactly when `k` is divisible by `2 exp(G)`.

## Consequence for a detector group

Let `X` be a finite bijective YBE solution and let `r_X` be the order of the
crossing permutation

```text
R_X : X^2 -> X^2.
```

The finite rack `A_G` dominates the two-strand action of `X` exactly when

```text
r_X divides 2 exp(G).
```

Indeed, the kernel of the `A_G` action on `B_2` is `2 exp(G) Z`, while the
kernel of the `X` action on `B_2` is `r_X Z`.  Kernel containment
`ker rho_{A_G,2} subset ker rho_{X,2}` is therefore precisely the divisibility
above.

For the direct symmetric detector candidate `G_X=Sym(X)`, this becomes

```text
ord(R_X) divides 2 lcm(1,...,|X|).
```

This divisibility is an exact necessary condition for the shortcut
`Y_X=A_{Sym(X)}`.  It is also sufficient for the two-strand part of that
shortcut.  It says nothing by itself about `n>=3`, where the current
factorization problem remains open.

## Relation to outcome B

A finite solution with

```text
ord(R_X) not dividing 2 lcm(1,...,|X|)
```

would disprove the direct `A_{Sym(X)}` route immediately.  It would not yet
be outcome B for Sawin's problem, because a larger finite group might still
detect the two-strand crossing and might still dominate all braid degrees.

To become B, such an example would still need the normalized-law sequence
that defeats every finite group, as required by the sharp obstruction
theorem.

More generally, for any fixed finite group `G` with

```text
ord(R_X) not dividing 2 exp(G),
```

the braid

```text
beta_G = sigma_1^(2 exp(G))
```

is an explicit `G`-longitude-invisible mover on two strands.  Its
invisibility follows from the exact `B_2` period above, and its motion follows
because its exponent is not in the kernel `ord(R_X) Z` of the two-strand
crossing action.  This defeats that one candidate detector group.  It becomes
evidence for outcome B only if such failures can be organized against every
finite group in the normalized-law sense.

## Executable layer

The helper functions are:

```text
two_strand_longitude_period(G) = 2 exp(G),
two_strand_symmetric_longitude_period(|X|) = 2 lcm(1,...,|X|),
two_strand_crossing_order(X),
two_strand_group_detector_covers_solution(X,G),
two_strand_group_detector_failure_certificate(X,G),
two_strand_cyclic_detector_certificate(X),
two_strand_symmetric_detector_covers_solution(X),
two_strand_symmetric_detector_failure_certificate(X).
```

The tests verify exactness for `C_1`, `C_2`, `C_3`, and `S_3`, and record the
two-strand gate for the three-point dihedral rack and the size-three affine
commutator stress row.  A regression also records the explicit obstruction
for the three-point dihedral rack against the too-small detector `C_2`:
`sigma_1^4` is invisible to `C_2` but moves a tuple because the crossing order
is `3`.
