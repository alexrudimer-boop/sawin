# Signed-Affine Active-Fibre Gauge Review

Date: 2026-06-08

This note reviews the proposed signed-affine gauge closure for the last
active non-automorphic six-point residual cases in the linear skew-over-flip
family

```text
X={0,1} x F_3.
```

It is not a new dependency in the main proof ledger.  The whole family is
already closed in

```text
proofs/linear_f3_degenerate_noninvolutive_family_closure.md
```

by the combination of non-subdirect quotient-factor closure, relative
contextual closure for the monolith-`J`-separating rows, and the
gap-corrected quotient invariant for the formal monolith-collision rows.

## Claim Reviewed

The proposed residual slice has quotient letters

```text
Z={F} union {v_a : a in F_3}
```

with

```text
R_Z(F,F)=(F,F),
R_Z(v_a,v_b)=(v_a,v_b),
R_Z(v_a,F)=(F,v_{-a}),
R_Z(F,v_a)=(v_{-a},F).
```

The active fibre over `F` is a three-point solution `W`, with internal rule
one of

```text
R_W(i,j)=(-j,i-j),
R_W(i,j)=(-i+j,-i).
```

Visible transports have signed-affine form

```text
S_a(i)=epsilon i + delta a,
T_a(i)=epsilon i + epsilon delta a,
```

for `epsilon,delta in {1,-1}`.  Hence

```text
S_{-a} T_a = id.
```

Under these hypotheses, the proposed gauge is:

```text
tilde a_r = (-1)^{d_r} a_r,
G_s = S_{tilde a_1} ... S_{tilde a_k},
tilde i_s = G_s(i_s),
```

where `d_r` is the number of `F`-strands between the visible letter `v_{a_r}`
and the tracked `F`-strand.

## Check

The local checks are coherent.

Tracked visible-`F` crossings preserve `tilde i_s` by the identities
`S_a` removes the leftmost gauge factor and `S_{-a}T_a=id` adds the inverse
factor when the tracked strand moves rightward past `v_a`.

Passive crossings of a visible letter across a different `F`-strand preserve
the effective label because the visible label changes by `a -> -a` while the
intervening `F`-count changes by one:

```text
(-1)^{d+1}(-a)=(-1)^d a.
```

For adjacent `F`-strands, if the first gauge is `G(t)=eta t+c`, the second
has gauge `G'(t)=eta t-c`.  The two displayed computations show that both
internal affine rules are transported to the same rule on gauged hidden
values.  Thus the gauged `F`-subword evolves by the ordinary `W` braid action.

Since `Z` is involutive, it is dominated by a finite rack.  Since `W` is
nondegenerate, it is dominated by its derived rack.  With the transparent
extension of the `W` detector, the usual quotient-plus-gauged-fibre argument
gives

```text
ker rho^{Y_Z x Y_W^0}_n <= ker rho^X_n
```

for every `n`, where `Y_Z` may be taken as a rack detector for the involutive
quotient.

## Relation To The Canonical Local Closure

This signed-affine gauge is the special case of the broader gap correction

```text
S_{alpha^g(z)}
```

when the visible quotient transport is `alpha(a)=-a`.  The repo's canonical
gap-corrected proof uses this `alpha^g` normalization for the formal
monolith-collision rows.  The monolith-`J`-separating rows are already closed
by the relative contextual theorem rather than this active-fibre gauge.

So the signed-affine proof is useful intuition and may be a shorter direct
proof for a row subfamily after row IDs are matched, but it does not change
the active frontier.

## Frontier Consequence

The six-point linear `F_3` skew-over-flip family should remain excluded from
future counterexample prompts unless a response explicitly defeats the
audited closures:

```text
80 non-subdirect rows: quotient-factor closure,
32 monolith-J-separating rows: relative contextual quotient closure,
32 formal monolith-J-collision rows: gap-corrected quotient invariant.
```

The next meaningful search class is outside this family: non-linear
six-point solutions, or larger degenerate quotient-rigid non-involutive
solutions.
