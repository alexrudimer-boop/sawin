# Transport-state rackification detector

Date: 2026-05-29

This note follows `proofs/principal_gauge_extension_detector.md` and removes
the principal-gauge assumption for genuinely strand-continuing lower
endpoint/unit holonomy.  It does not prove the Master Local-Minimal Residual
Theorem.  It proves that every finite strand-continuing transport row is
closed once its remaining lower state is included in the rack state.

The new residual bottleneck is therefore not nonprincipal gauge.  It is
descent separation: prove that every completed Green/corridor readout splits
into Green/Schutzenberger motion plus strand-continuing finite transport
state, with no residual motion outside those readouts.
The next note, `proofs/continuation_congruence_descent_gate.md`, turns this
descent-separation question into a finite local-minimality dichotomy by
closing all continuation-change pairs `x~v` under admissible congruence.
The status note `proofs/descent_separation_transport_rack_closure.md`
separates the proved transport-rack closure from the still-unproved descent
separation theorem.

## Strand-continuing transport row

Let `A` be a finite rack in the left convention

```text
R_A(a,b) = (a*b, a).
```

Let `E` be the finite set of lower endpoint states not seen by the atom
quotient.  A general strand-continuing lower row has the form

```text
R~((a,r),(b,s)) = ((a*b, F_{a,b,r}(s)), (a,r)),
```

where each

```text
F_{a,b,r}: E -> E
```

is a bijection.  This includes the principal case
`F_{a,b,r}(s)=c(a,b)s`, but allows the transition to depend on the continuing
state `r`.

Define

```text
A^ = A x E
```

and

```text
(a,r) ^* (b,s) = (a*b, F_{a,b,r}(s)).
```

Then `R~(x,y)=(x ^* y,x)`.

## Rackification lemma

Lemma.  If the completed strand-continuing row `R~` is a bijective YBE row,
then `A^` is a finite rack.

Proof.  Since `R~(x,y)=(x ^* y,x)`, bijectivity of `R~` is equivalent to
bijectivity of every left translation

```text
L_x:y |-> x ^* y.
```

For a crossing in rack form, the set-theoretic Yang-Baxter equation is exactly
left self-distributivity:

```text
x ^* (y ^* z) = (x ^* y) ^* (x ^* z).
```

Thus the completed YBE row supplies self-distributivity, and bijectivity
supplies the rack left translations.  Therefore `A^` is a finite rack.  QED.

Equivalently, if one starts from explicit finite transition maps, it is enough
to check the finite left-translation bijectivity and the YBE/rack law of the
induced table on `A x E`.

## Detector consequence

Let

```text
W = Inn(A^) <= Sym(A^)
```

be the finite inner group of the transport-state rack.  It depends only on
the local interval data, not on braid index `n`.

Rack self-distributivity gives

```text
L_{x ^* y} = L_x L_y L_x^-1.
```

Therefore the positive crossing row in `W` is the active Artin detector-lift
row

```text
(m_i,u_i),(m_{i+1},u_{i+1})
  |-> (m_i m_{i+1} m_i^-1, m_i u_{i+1}), (m_i,u_i).
```

The inverse row is the negative crossing row.  Hence
`proofs/artin_detector_lift_criterion.md` applies: for every braid word
`beta`, terminal transport-state labels are recursive Artin-longitude
evaluations in the fixed finite group `W`.

Thus identity finite-`W` longitude data kills the strand-continuing lower
transport readout.

## Relation to the principal gauge note

The principal gauge-extension note is the special case in which

```text
F_{a,b,r}(s)=c(a,b)s
```

for a unit-group action on `E=U`.  The transport-state rackification argument
does not need this form.  Nonprincipal dependence on `r` is harmless once the
full finite state `(a,r)` is treated as the rack element.

## Updated corridor target

After the balanced Green decomposition:

1. raw Green/Schutzenberger first-output defects are Artin-visible
   commutators times terminal gauge boundaries;
2. genuinely strand-continuing terminal gauge is a finite transport-state
   rack and is detected by `Inn(A^)`;
3. atom-inner factors are already detected by their rack inner groups after
   atom descent/totality.

The remaining theorem burden is therefore:

```text
Descent separation.
Every local-minimal bi-free corridor readout separates into:
  (i) Green kernel-block/Schutzenberger motion visible in the fixed Green
      factors; and
  (ii) strand-continuing finite transport-state rack motion.
No residual motion remains outside these finite readouts.
```

If descent separation is proved, the local detector is the product of the
fixed Green factors, atom-inner factors, and transport-state inner groups.
The sharp obstruction theorem then gives `Q x A_H`, and congruence-chain
induction gives a finite rack independent of `n`.

If descent separation fails, the failure is a precise B-route seed: a finite
row where lower state changes the identity of the continuing strand without
being visible in the Green/Schutzenberger readout.  It still must be upgraded
to a normalized-law sequence invisible to every finite group before outcome B
is proved.

## Executable audit hooks

The code records this reduction through:

```text
rack_extension_projection_failures(...)
rack_extension_detector_audit(...)
transport_state_left_translation_failures(...)
transport_state_rack(...)
transport_state_rackification_audit(...)
```

`transport_state_rackification_audit(...)` builds the finite rack on `A x E`
when all left translations are bijective, checks the projection to `A`, and
then reuses `rack_inner_detector_lift_audit(...)` for the fixed inner-group
detector.
