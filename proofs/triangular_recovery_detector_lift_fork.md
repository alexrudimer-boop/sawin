# Triangular recovery detector-lift fork

Date: 2026-05-31

This note follows `proofs/triangular_recovery_unit_observer.md`.  It does not
prove the remaining nonlinear branch.  It converts the `U_tri` endpoint
longitudinalization target into the same finite detector-lift row check used
elsewhere in the repository.

## Setup

The triangular recovery unit observer gives one fixed finite group:

```text
U_tri = < triangular recovery row permutations >.
```

The remaining A-route target is:

```text
For every residual braid beta in the quotient kernel, every triangular
recovery endpoint composite lies in V_beta(U_tri).
```

The endpoint-composite audit

```text
triangular_recovery_longitude_route_audit(...)
```

checks this condition for one supplied braid word by subgroup enumeration.
For an all-`n` proof, enumeration is not enough.  The symbolic route is the
Artin detector-lift criterion.

## Detector-lift sufficient condition

[Conditional] Suppose the triangular recovery observer can be enriched so
that each live strand carries labels

```text
(m_k,u_k) in U_tri x U_tri
```

and every local positive/negative crossing row used by the recovery endpoint
has the active Artin detector form:

```text
sigma_i:
(m_i,u_i),(m_{i+1},u_{i+1})
  -> (m_i m_{i+1} m_i^-1, m_i u_{i+1}), (m_i,u_i),
```

```text
sigma_i^-1:
(m_i,u_i),(m_{i+1},u_{i+1})
  -> (m_{i+1},u_{i+1}), (m_{i+1}^-1 m_i m_{i+1}, m_{i+1}^-1 u_i).
```

Then every terminal triangular recovery endpoint which is a signed product of
terminal `u_k` labels lies in `V_beta(U_tri)`.

Proof.  This is `proofs/artin_detector_lift_criterion.md` applied to the
fixed finite group `U_tri`.  The detector-lift induction proves

```text
u_k(beta) = phi(L_k(beta))
```

for the input-dependent assignment `phi(x_k)=m_k(1)`.  A signed product of
terminal `u_k` labels is therefore a word in evaluated recursive longitudes,
so it lies in `V_beta(U_tri)`.  QED.

## Executable hooks

The specialized helpers are:

```text
triangular_recovery_detector_lift_transition_audit(...)
triangular_recovery_detector_lift_braid_audit(...)
```

The transition helper checks one supplied local row against the active Artin
detector update in `U_tri`.  The braid helper runs the global detector-lift
induction in `U_tri` and verifies that terminal endpoint labels agree with
recursive Artin longitude evaluations.

These helpers do not discover the missing enrichment or prove that the
triangular recovery endpoint rows satisfy the active detector form.  They make
the remaining proof obligation finite and explicit once such row data is
supplied.

The direct supplied-expression certificate is now recorded separately in
`proofs/triangular_recovery_longitude_expression_certificate.md`.  Its helper

```text
triangular_recovery_longitude_expression_audit(...)
```

checks that a recovery endpoint word is an explicit product of evaluated
recursive longitudes in `U_tri`, without subgroup enumeration.  A successful
detector-lift induction supplies exactly this kind of expression certificate.

The System U endpoint family also has a keyed symmetric-detector fork in
`proofs/triangular_recovery_symmetric_endpoint_fork.md`.  A supplied positive
fork proves that one symmetric degree `S_M`, with `M >= |U_tri|`, kills the
finite routed `U_tri` endpoint family.  This is weaker than constructing the
actual endpoint-longitude expressions, but it is still a valid fixed
finite-detector certificate when the covered endpoint keys match the routed
System U keys exactly.

## Derived-series alternative

The detector-lift route is not the only finite `U_tri` route.  The companion
note `proofs/triangular_recovery_derived_series_fork.md` splits `U_tri` by its
derived series.  The specialized helpers

```text
triangular_recovery_derived_series_lift_audit(...)
triangular_recovery_perfect_residual_audit(...)
```

turn a triangular recovery endpoint into a sequence of abelian quotient
witnesses plus one final `P_tri` witness in the stable perfect residual.  This
also proves membership in `V_beta(U_tri)` when the supplied witnesses pass,
and it localizes any nonsolvable finite miss to `P_tri`.

## Final fork

[Open] The exact remaining nonlinear obstruction is now:

```text
a local-minimal bi-free universal-corridor interval whose triangular recovery
unit group U_tri has a residual endpoint composite for which no Artin
detector-lift row enrichment, endpoint longitude expression, derived-series
lift plus P_tri witness, or direct V_beta(U_tri) membership proof has been
supplied uniformly in braid index.
```

To prove `[Resolution: A]`, prove the detector-lift row enrichment, or another
equivalent endpoint-longitude expression theorem, for every such interval.

To prove `[Resolution: B]`, construct one such interval and upgrade a
detector-lift or `V_beta(U_tri)` failure to a normalized-law sequence invisible
to every finite group while moving a residual tuple.

A finite transition-row failure or fixed-word miss is not outcome B by itself;
it only identifies the exact finite row that must be diagonalized into the
normalized-law certificate.
