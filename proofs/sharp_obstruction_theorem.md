# Sharp obstruction theorem

Date: 2026-05-28

This note records the precise proof that the finite-group longitude detector
produces the rack domination step used in the reduction program.

## Detector rack kernel

For a finite group `G`, let

```text
A_G = T_2 x (G x G)
```

with rack operation on the active coordinates

```text
(a,u) ▷ (b,v) = (a b a^{-1}, a v).
```

The `T_2` factor is the two-element trivial rack.  Its braid action is the
ordinary permutation of coordinates, so it detects the Artin permutation part
of a braid.  Equivalently, `ker rho_{T_2,n}` is the pure braid group `P_n`.
This purity stabilization is what permits local branch arguments to use
pure-braid formulas after the full `A_G` kernel condition is imposed.  The
active `G x G` factor tracks the recursive Artin image and
longitude convention:

```text
starting from (g_i,e), the final active coordinates are
( eval(beta(x_i)), eval(L_i(beta)) ).
```

More generally, if the second active coordinates start as arbitrary `u_i`,
then the final second coordinate is

```text
eval(L_i(beta)) u_{p(i)}.
```

Therefore

```text
rho_{A_G,n}(beta)=1
```

if and only if

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1).
```

The forward implication is obtained by evaluating on all tuples with second
coordinates `e`, and the `T_2` factor forces the permutation to be identity.
The reverse implication uses the displayed formula: identity permutation and
identity longitude evaluations make both active coordinates and the trivial
`T_2` coordinates fixed for every input tuple.

## Kernel form gives domination

Let

```text
pi : X -> Z
```

be a quotient of finite braided sets.  Suppose `Z` is dominated by a finite
rack `Q`, so

```text
ker rho_{Q,n} subset ker rho_{Z,n}
```

for every `n`.  Put

```text
N_n = ker rho_{Q,n}.
```

Assume a finite group `G` satisfies the residual kernel implication

```text
beta in N_n and Lambda_{G,n}(beta)=Lambda_{G,n}(1)
  => Delta_n(beta)=1
```

for every braid degree `n`.

Then the finite rack

```text
Y = Q x A_G
```

dominates `X`.

Indeed, if `beta in ker rho_{Y,n}`, then beta lies in
`ker rho_{Q,n}=N_n` and in `ker rho_{A_G,n}`.  By the detector-kernel
equivalence, the latter condition is exactly

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1).
```

The residual implication gives `Delta_n(beta)=1`.  Since `beta in N_n` and
`Q` dominates `Z`, beta fixes every base tuple in `Z^n`; since the residual
action is identity over every fixed base tuple, beta fixes every point of
`X^n`.  Hence

```text
beta in ker rho_{X,n}.
```

Thus

```text
ker rho_{Q x A_G,n} subset ker rho_{X,n}
```

for every `n`.

## Collision form

The equivalent collision formulation says that for all
`beta,gamma in N_n`,

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(gamma)
  => Delta_n(beta)=Delta_n(gamma).
```

This is equivalent to the kernel form.  If the collision form holds, take
`gamma=1`.  Conversely, if the kernel form holds and the two longitude
signatures are equal, then

```text
rho_{A_G,n}(beta gamma^{-1}) = 1.
```

Also `beta gamma^{-1} in N_n`.  The kernel form gives
`Delta_n(beta gamma^{-1})=1`, hence `Delta_n(beta)=Delta_n(gamma)`.

## Role in the global induction

In a congruence chain

```text
Delta_X = kappa_0 < ... < kappa_m = Nabla_X,
```

apply the theorem to each local-minimal interval
`X/kappa_i -> X/kappa_{i+1}`.  If the interval detector is `G_i` and
`Q_{i+1}` dominates the quotient, define

```text
Q_i = Q_{i+1} x A_{G_i}.
```

The kernel inclusion above proves that `Q_i` dominates `X/kappa_i`.  Since the
chain is finite and every `G_i` is finite and independent of braid degree,
the final rack `Q_0` is finite and independent of `n`.

## Executable checks

The test

```text
test_detector_rack_kernel_matches_longitude_signature
```

checks the detector-kernel equivalence on a bounded set of braid words for
`G=C_2`.  This is only a convention check; the proof above supplies the
all-degree argument.

The constructor

```text
sharp_obstruction_rack(Q,G)
```

now builds the rack `Q x A_G` explicitly.  It requires `Q` to be in rack form,
uses the Cartesian product braided-set construction, and returns a finite rack
with `|Q| * 2 * |G|^2` elements.  The generic helper
`is_rack_solution()` verifies the rack form `R(a,b)=(a▷b,a)`, while
`product_solution()` supplies the finite Cartesian product.  Regression tests
check that `sharp_obstruction_rack(Q,G)` is a YBE rack and that, on small
words,

```text
ker rho_{Q x A_G,n}
  =
ker rho_{Q,n} cap ker rho_{A_G,n}.
```

The congruence-chain wrapper

```text
assemble_congruence_chain_rack(Q_m, groups)
```

now iterates this same constructor along a supplied finite list of local
detector groups.  Its audit rows record the formal multiplication
`|Q_i|=|Q_{i+1}|*2*|G_i|^2`, so the executable artifact matches the induction
step `Q_i=Q_{i+1} x A_{G_i}` exactly.  This wrapper does not prove the local
detector theorem; it verifies that once the fixed interval groups are known,
the assembled rack is a finite object independent of braid degree.

Again this executable check is not the theorem; it is the concrete artifact
matching the proof above and the rack used in the congruence-chain induction.
