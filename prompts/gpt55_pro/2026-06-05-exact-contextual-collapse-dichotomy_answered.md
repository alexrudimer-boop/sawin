# Exact Contextual Collapse Dichotomy Prompt

Status: answered / GPT-5.5 Pro response recorded on 2026-06-05.

Follow-up status:

GPT-5.5 Pro confirmed that the fixed-`M` endpoint issue is finite.  After
separating the finite endpoint set `S_M`, fixed-`M` badness is exactly:

```text
x != x',
x' in B_n.x,
Theta_n^M(x)=Theta_n^M(x')
```

inside `C_M(X)^n`.

The label-equality side is finite-state.  For fixed `M`, define

```text
E_M subset (M x X x M)^2
```

by equality of contextual generators in `C_M(X)`.  Then
`Theta_n^M(x)=Theta_n^M(x')` is recognized by finite state annotations of left
and right context products.  Thus the exact label-collision relation is a
regular relation over `X x X`.

The hard part is the braid-orbit condition `x' in B_n.x`.  For a general
finite bijective YBE solution, the current hypotheses do not imply that this
reachability relation is regular, automatic, noetherian, or bounded by finite
semigroup data.  Even if it were regular, regularity alone would not give one
finite detector for all arities without a finite-index detector equivalence.

The sharp missing lemma remains:

```text
Every harmful unbounded exact contextual collapse is either finite-index /
rack-absorbed or finite-active-factor extractable.
```

Prompt:

```text
Please answer self-containedly and mathematically.  We are working on Sawin's
finite rack-domination problem:

    For every finite bijective set-theoretic YBE solution X, does there exist
    a finite rack Y such that ker rho_n^Y <= ker rho_n^X for every n?

Current route: finite contextual rack detectors.

For a finite quotient theta:L_X->M, let

    S_M={d_{a,x,b}:a,b in M, x in X} subset C_M(X).

Once S_M is separated by one finite rack quotient, a fixed-M same-orbit pair is
bad exactly when its contextual label tuples are identical:

    Theta_n^M(x)=Theta_n^M(x').

Hidden stabilizer/path holonomy can explain why labels stay equal, but it is
not visible to endpoint-label finite rack detection once endpoints are equal.

Thus the remaining obstruction is not fixed-M factorial endpoint holonomy.
It is:

    fixed-M exact contextual-label collisions in unbounded arity

or

    state-refinement escape through finer and finer quotients of L_X.

For state refinement, define for each finite M:

    E_M subset (M x X x M)^2,
    (a,x,b) E_M (a',x',b') iff
    d_{a,x,b}=d_{a',x',b'} in C_M(X).

Let K=hat{L_X} x X x hat{L_X}.  Define

    E_infty = intersection_M (q_M x q_M)^(-1)(E_M).

The finite-index condition needed is that, on orbit-relevant contextual
letters, E_infty is already pulled back from some finite M0.

Task.

1. Try to prove bounded fixed-M exact witnesses:
   for a fixed finite M, if exact Theta^M-label collisions occur inside braid
   orbits, must one occur in arity <= N(M,X)?  If yes, prove it.  If no,
   construct or outline a finite YBE example with exact fixed-M collisions in
   unbounded arity and no bounded bad core.

2. Analyze fixed-M exact collisions as a finite automaton/language problem.
   Since Theta^M uses finite context states, is the set of same-orbit exact
   collisions regular, automatic, noetherian, or bounded by finite semigroup
   data?  Does braid reachability defeat such a finite-state argument?

3. Analyze state-refinement escape.  Can E_infty fail to be pulled back from
   any finite quotient on orbit-relevant contexts?  If yes, describe the
   profinite obstruction.  If no, prove finite-index contextual Myhill-Nerode
   behavior.

4. Try to construct a harmful ultrafilter of either type:
   - fixed-M exact collisions in unbounded arity surviving all detectors;
   - state-refinement escape where every fixed M is defeated.
   If construction fails, identify the precise theorem preventing it.

5. Analyze active-factor extraction from exact contextual collapse.  Given a
   finite or profinite contextual equivalence, when does it produce finite maps
   pi_{a,b}:X->Z such that the induced relation on Z^2 is functional, total,
   bijective, satisfies YBE on all triples, gives braid-equivariant Pi_n, and
   satisfies ker rho_n^Z <= ker rho_n^X?

6. Analyze hidden reachable escape holonomy after endpoint equality.  Can
   stabilizer/path holonomy make exact Theta^M-collisions harmful even though
   finite rack endpoint labels cannot see it?  Does escape holonomy give a
   finite detector, a finite active factor, or only a profinite diagnostic?

7. Analyze product/padding and known positive branches.  Are all obvious
   sources of exact contextual collisions either rack-absorbed or proper
   domination-equivalent active factors?

8. State the strongest valid theorem.  Useful outcomes include:
   - bounded fixed-M exact witnesses => finite detector;
   - finite-index contextual Myhill-Nerode => finite detector;
   - active extraction from exact contextual collapse => residual-rigid Sawin;
   - explicit harmful unbounded exact-collapse obstruction;
   - or a sharper missing lemma strictly smaller than Sawin.

Guardrails:

- Do not treat hidden stabilizer holonomy as endpoint-label detection after
  Theta^M endpoints are equal.
- Do not assume fixed-M exact collisions require finer M; unbounded arity at
  fixed M is a separate possibility.
- Do not claim pointwise separation gives one finite state quotient.
- Do not use ordinary quotients as active factors without proving
  ker rho_n^Z <= ker rho_n^X.
- Do not assume a finite contextual equivalence defines a total bijective YBE
  solution without checking functionality, totality, YBE, and kernel
  reflection.
```
