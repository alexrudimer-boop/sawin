# Artin detector-lift criterion

Date: 2026-05-29

This note records the next finite local reduction for the remaining
Green/corridor endpoint problem.  It does not prove the Master Local-Minimal
Residual Theorem.  It proves that, once a fixed endpoint observer satisfies the
same local row rules as the active `U x U` part of the sharp Artin detector,
the unbounded braid-word recursion is automatically the recursive
Artin-longitude recursion.

Thus the remaining all-`n` corridor work is narrowed again: for each fixed
detector factor, verify finite local detector-lift row identities.  The
induction over arbitrary braid words then needs no new search.

## Setup

Let `U` be one fixed finite group factor of `H(pi,Q)`.  Consider a group-like
endpoint observer whose final readout is an element

```text
h_beta in U.
```

While sweeping a braid word, suppose the observer carries on each live strand
`k` two labels

```text
m_k(w), u_k(w) in U.
```

The label `m_k(w)` is the meridian/image label after the prefix `w`, and
`u_k(w)` is the endpoint or longitude label after that prefix.  Assume the
initial endpoint labels are trivial:

```text
u_k(1)=1.
```

The initial meridian labels define the input-dependent homomorphism

```text
phi:F_n -> U,
phi(x_k)=m_k(1).
```

## Local row identities

For a positive crossing `sigma_i`, require the observer row

```text
(m_i,u_i),(m_{i+1},u_{i+1})
  |->
(m_i m_{i+1} m_i^-1, m_i u_{i+1}), (m_i,u_i).
```

For a negative crossing `sigma_i^-1`, require

```text
(m_i,u_i),(m_{i+1},u_{i+1})
  |->
(m_{i+1},u_{i+1}), (m_{i+1}^-1 m_i m_{i+1}, m_{i+1}^-1 u_i).
```

These are exactly the active `U x U` update rules in the sharp detector rack
`A_U`.  The separate `T_2` coordinate records the Artin strand permutation;
the active `U` coordinates carry the recursive image and longitude data.

## Theorem

If the observer satisfies the two row identities above for every local row it
uses, then for every braid `beta in B_n`,

```text
u_k(beta)=phi(L_k(beta))
```

for every terminal strand `k`, where `L_k(beta)` is the recursive Artin
longitude in the repository convention.  Consequently, every endpoint readout
of the form

```text
h_beta =
  u_{i_1}(beta)^{epsilon_1}
  ...
  u_{i_r}(beta)^{epsilon_r},
epsilon_j in {+1,-1},
```

has the endpoint-longitude expression

```text
h_beta =
  phi(L_{i_1}(beta))^{epsilon_1}
  ...
  phi(L_{i_r}(beta))^{epsilon_r}.
```

Hence `h_beta in V_beta(U)`.

## Proof

Induct on the length of a braid word.

For the empty word, the recursive Artin longitudes are trivial and the
endpoint labels are trivial:

```text
u_k(1)=1=phi(L_k(1)).
```

The meridian labels also agree with the Artin images:

```text
m_k(1)=phi(x_k).
```

Assume both invariants hold after a prefix `w`:

```text
m_k(w)=phi(w(x_k)),
u_k(w)=phi(L_k(w)).
```

For a positive crossing `sigma_i`, the required local row gives

```text
u_i(w sigma_i)=m_i(w)u_{i+1}(w),
u_{i+1}(w sigma_i)=u_i(w),
```

and

```text
m_i(w sigma_i)=m_i(w)m_{i+1}(w)m_i(w)^-1,
m_{i+1}(w sigma_i)=m_i(w).
```

These are exactly the recursive Artin image and longitude updates after
applying `phi`:

```text
x_i     |-> x_i x_{i+1} x_i^-1,
x_{i+1} |-> x_i,
L_i     |-> image_i(w) L_{i+1}(w),
L_{i+1} |-> L_i(w).
```

All other strand labels are unchanged.  Therefore the invariants persist.

For a negative crossing `sigma_i^-1`, the required local row gives

```text
u_i(w sigma_i^-1)=u_{i+1}(w),
u_{i+1}(w sigma_i^-1)=m_{i+1}(w)^-1 u_i(w),
```

and

```text
m_i(w sigma_i^-1)=m_{i+1}(w),
m_{i+1}(w sigma_i^-1)=m_{i+1}(w)^-1 m_i(w) m_{i+1}(w).
```

These are exactly the inverse recursive Artin image and longitude updates
after applying `phi`:

```text
x_i     |-> x_{i+1},
x_{i+1} |-> x_{i+1}^-1 x_i x_{i+1},
L_i     |-> L_{i+1}(w),
L_{i+1} |-> image_{i+1}(w)^-1 L_i(w).
```

Again all other strands are unchanged.  The induction proves
`u_k(beta)=phi(L_k(beta))` for every braid word.

A signed product of terminal `u`-labels is therefore a signed product of
evaluated recursive Artin longitudes under the same assignment `phi`, and so
lies in `V_beta(U)`.  QED.

## Consequence for the corridor branch

This theorem resolves the unbounded braid-word recursion once the finite row
identities are verified.  The remaining corridor problem is the finite local
check:

```text
For every remaining Green/corridor observer row,
verify the two Artin detector-lift identities in its fixed detector factor.
```

The relevant fixed factors are:

```text
Sym(left/right Green kernel blocks),
Sch(left/right regular Green classes),
Inn(rack-like atom quotient),
fixed quotient or known-branch detector groups,
fixed lower endpoint/unit groups.
```

The atom-inner entry is now closed conditionally on atom descent and totality:
`proofs/atom_inner_detector_lift_rows.md` proves that a rack-like atom quotient
automatically satisfies these detector-lift rows in its inner group.  The
remaining unverified row identities are therefore the Green kernel-block,
Schutzenberger, and lower endpoint/unit holonomy rows.

If the row identities hold for every endpoint factor, then every endpoint
factor lies in `V_beta(H_s)`.  The product assembly note
`proofs/bifree_corridor_endpoint_factorization.md` combines these witnesses
into `V_beta(H(pi,Q))`.  Identity finite-`H(pi,Q)` longitude data kills every
endpoint factor, the faithful readout fixes the residual tuple, and the sharp
obstruction theorem supplies the local rack

```text
Q x A_{H(pi,Q)}.
```

The theorem does not verify the Green/corridor rows themselves.  A
counterexample route must now exhibit a concrete row where the detector-lift
identity fails and then upgrade that failure to a normalized-law obstruction;
a bounded row failure or fixed detector miss alone is not outcome B.

## Executable certificate layer

The code exposes the finite row and braid-recursion checks as:

```text
artin_detector_lift_positive_update(G,left,right)
artin_detector_lift_negative_update(G,left,right)
artin_detector_lift_transition_audit(
    G,signed_generator,input_left,input_right,supplied_left,supplied_right
)
artin_detector_lift_state(G,initial_meridians,beta)
artin_detector_lift_braid_audit(
    G,initial_meridians,beta,endpoint_expression
)
```

The transition audit is the finite local row checker.  The braid audit is the
global induction check: it sweeps an arbitrary braid word using the local
rules and compares the terminal meridian and endpoint labels with
`evaluate_artin_images(...)` and `evaluate_artin_longitudes(...)`.  Passing
the braid audit is not the corridor theorem; it verifies that the row rules,
once supplied, produce endpoint-longitude expressions uniformly in braid word
length.
