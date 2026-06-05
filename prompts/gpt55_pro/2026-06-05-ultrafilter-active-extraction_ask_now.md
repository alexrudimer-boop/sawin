# Ultrafilter Active Extraction Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-05.

Prompt:

```text
Please answer self-containedly and mathematically.  We are working on Sawin's
finite rack-domination problem:

    For every finite bijective set-theoretic YBE solution X, does there exist
    a finite rack Y such that ker rho_n^Y <= ker rho_n^X for every n?

Current route: finite contextual rack detectors.

A finite contextual rack detector is D=(M,phi), where M is a finite quotient of
the positive left structure monoid L_X and phi:C_M(X)->Y is a finite rack
quotient.  Let

    Lambda_n^D = phi^n Theta_n^M:X^n -> Y^n.

Let Omega_n be the set of distinct same-orbit pairs in X^n:

    Omega_n={(x,x') : x!=x', x' in B_n.x},
    Omega=disjoint_union_n Omega_n.

Define

    B_D={(x,x') in Omega : Lambda_n^D(x)=Lambda_n^D(x')}.

Then D proves Sawin for X exactly when B_D=empty.  Detector products satisfy

    B_{D1 x D2}=B_{D1} cap B_{D2}.

Thus, if every finite detector fails, there is an ultrafilter U on Omega with
B_D in U for every finite detector D.  If fixed bad pairs are pointwise
separable, U is nonprincipal and unbounded in arity.

This is the sharp definition of a harmful contextual tower collapse.

There is also a profinite contextual formulation.  Put

    K=hat{L_X} x X x hat{L_X}.

For x=(x_1,...,x_n), let

    kappa_i(x)=(
      lambda_{x_1}...lambda_{x_{i-1}},
      x_i,
      lambda_{x_{i+1}}...lambda_{x_n}
    ) in K.

A closed relation R subset K x K is a profinite contextual collapse.  For a
finite quotient theta:L_X->M, define the thickening R[theta] by projecting to
M x X x M and pulling back.  A detector D absorbs R if, for some theta,

    B_D cap Omega(R,theta)=empty.

Current obstruction.

The desired harmful-collapse dichotomy reduces to a finite extraction lemma:

    Every harmful bad-pair ultrafilter/profinite contextual collapse has a
    finite-index contextual quotient whose induced equivalence is functional,
    total, bijective, YBE-compatible on all triples, and orbit-injective in
    the kernel-reflecting direction.

Equivalently, harmful non-absorption should yield a finite active factor
Z with ker rho_n^Z <= ker rho_n^X for all n.

But this is a quantifier reversal:

    forall finite detectors D, exists bad pair omega_D in B_D

does not formally imply

    exists one finite (M,Z,pi) satisfying all crossing identities.

Known active-factor conditions.

Given finite M, finite Z, and maps pi_{a,b}:X->Z, define Gamma subset Z^2 x Z^2
by

    (A,B) Gamma (C,D)

if, for some a,b,x,y with r_X(x,y)=(u,v),

    A=pi_{a,lambda_y b}(x),
    B=pi_{a lambda_x,b}(y),
    C=pi_{a,lambda_v b}(u),
    D=pi_{a lambda_u,b}(v).

This gives a finite bijective YBE solution Z only if:

1. Gamma is functional;
2. Gamma is total on Z^2;
3. Gamma is cofunctional/bijective;
4. the induced r_Z satisfies YBE on all of Z^3, including unreached triples;
5. the resulting Pi_n:X^n->Z^n are braid-equivariant;
6. Pi_n is orbit-injective, or at least ker rho_n^Z <= ker rho_n^X.

Task.

1. Can the harmful bad-pair ultrafilter U be used to construct any canonical
   limiting object: an ultraproduct rack, a profinite contextual equivalence,
   a partial YBE solution, or a pro-active factor?  State it precisely.

2. Does compactness/Los/ultraproduct reasoning ever force a finite-index
   quotient from U?  If yes, prove the finite-index step.  If no, isolate the
   exact obstruction.

3. Try to prove the finite active extraction lemma.  Starting from harmful
   non-absorption, can one force functionality, totality, bijectivity, YBE on
   unreached triples, and orbit-injectivity for some finite Z?  Where exactly
   does the proof fail?

4. Construct or outline a counterexample to the extraction lemma at the level
   of contextual racks or associated rack groups: a harmful ultrafilter or
   uniformly nonseparable transporter family that is not finite-rack absorbed
   and does not define a finite active factor.

5. Analyze whether residual-rigid hypotheses could rule out the counterexample.
   Which part would residual rigidity remove: infinite-index behavior,
   nonfunctionality, partiality, nonbijectivity, YBE failure on unreached
   triples, or loss of orbit-injectivity?

6. Examine uniform stabilizer separation again.  Can factorial accumulation
   h^{n!} near a stabilizer occur in orbit-relevant transporters of As(C_M(X))
   for YBE-origin contextual racks?  If impossible, prove the YBE-specific
   reason.  If possible, explain why it does not automatically become an
   active factor.

7. Examine escape holonomy.  Does the bad-pair ultrafilter determine a
   holonomy coset ultralimit?  Can that holonomy be compressed to finite rack
   labels, or can it remain genuinely profinite/non-finite-state?

8. State the strongest valid theorem at the end.  Useful outcomes include:
   - finite active extraction lemma => residual-rigid Sawin;
   - bounded harmful witnesses => finite rack detector;
   - uniform stabilizer separation plus finite-index contextual behavior =>
     finite rack detector;
   - a counterexample to extraction at the contextual-rack level;
   - or a sharper missing lemma strictly smaller than Sawin.

Guardrails:

- Do not claim all right scattering is harmful.
- Do not claim pointwise separation gives a uniform finite detector.
- Do not assume an ultraproduct/profinite object has a finite quotient unless
  finite index is proved.
- Do not use ordinary quotients as active factors without proving
  ker rho_n^Z <= ker rho_n^X.
- Do not assume a partial contextual crossing relation extends to a total
  bijective YBE solution.
```

