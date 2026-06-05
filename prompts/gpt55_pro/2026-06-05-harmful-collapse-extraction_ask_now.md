# Harmful Contextual Collapse Extraction Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-05.

Prompt:

```text
Please answer self-containedly and mathematically.  We are working on Sawin's
finite rack-domination problem:

    For every finite bijective set-theoretic YBE solution X, does there exist
    a finite rack Y such that ker rho_n^Y <= ker rho_n^X for every n?

Write r_X(x,y)=(L_x(y),R_y(x)).  The current route is the finite-state
contextual tower.

For the positive left structure monoid

    L_X=<lambda_x | lambda_x lambda_y=lambda_u lambda_v
          whenever r_X(x,y)=(u,v)>,

and a finite quotient theta:L_X->M, define the contextual rack C_M(X) with
generators d_{a,x,b}, a,b in M, x in X, and relations

    d_{a,u,lambda_v b}=d_{a lambda_x,y,b},

    d_{a lambda_u,v,b}
      =
    d_{a lambda_x,y,b} triangleright d_{a,x,lambda_y b}.

The labels Theta_n^M are braid-equivariant.  If one finite M and one finite
rack quotient phi:C_M(X)->Y make phi^n Theta_n^M injective on every braid
orbit in every arity, then ker rho_n^Y <= ker rho_n^X for all n.

Current correction.

Residual rigidity should not be expected to imply finite right-separation for
all active pairs in L_X.  Right scattering can be harmless.  Example:

    X={0,1}, r(i,j)=(j,1-i).

This is nondegenerate and has actual right scattering

    lambda_0 lambda_0 = lambda_0 lambda_1, lambda_0 != lambda_1,

but it is itself a rack solution under j triangleright i=1-i, so it is
dominated by itself.  The trivial contextual state M=1 also gives an injective
detector.

Therefore the missing theorem is not "no scattering".  It is:

    Harmful contextual collapse dichotomy.
    Every orbit-relevant profinite contextual collapse either
      (i) is absorbed by a finite contextual rack detector, or
      (ii) descends to a finite-index, crossing-compatible active factor Z
           satisfying ker rho_n^Z <= ker rho_n^X for every n.

Residual rigidity would exclude (ii), and (i) gives Sawin.

Definitions and known obstructions.

1. For p,q in L_X,

       E(p,q)={ahat in profinite L_X : ahat p = ahat q}.

   E(p,q)=empty iff p,q are finitely right-separated: some finite quotient
   theta:L_X->M has m theta(p) != m theta(q) for every m in M.
   This is useful but too strong globally.

2. A contextual collapse yields an active factor only if it factors through
   finite states and maps pi_{a,b}:X->Z such that the relation

       r_Z(pi_{a,lambda_y b}(x), pi_{a lambda_x,b}(y))
       =
       (pi_{a,lambda_v b}(u), pi_{a lambda_u,b}(v))

   is functional, total, bijective, satisfies YBE on all of Z^3, and gives
   orbit-injective equivariant maps Pi_n:X^n->Z^n.

3. For fixed M, finite rack separation in C_M(X) is controlled by stabilizer
   cosets in As(C_M(X)).  Uniform separation of a family T from a stabilizer H
   requires closure(T) cap closure(H)=empty, not merely pointwise separability.
   The factorial sequence in Z is the model obstruction.

4. Escape holonomy records transporter/stabilizer-coset data.  It becomes a
   finite contextual rack detector only if this holonomy is finite-state,
   crossing-compatible, and uniformly separated from stabilizers.

Task.

1. Try to prove the harmful contextual collapse dichotomy.  Start from an
   orbit-relevant profinite contextual collapse that is not absorbed by any
   finite contextual rack detector.  Can one extract a finite-index,
   crossing-compatible active factor Z with ker rho_n^Z <= ker rho_n^X?

2. Make precise what "harmful" must mean.  Give a definition in terms of
   same-orbit bad pairs, tower bad sets B_M, profinite contexts, or transporter
   families.  The definition should exclude harmless examples like the
   constant-action rack above.

3. Give necessary and sufficient conditions for a finite-index contextual
   collapse pi_{a,b}:X->Z to define a valid active YBE factor.  In particular,
   audit functionality, totality, cofunctionality, YBE on unreached triples,
   braid equivariance, and orbit-injectivity.

4. Determine whether non-absorption by finite contextual rack detectors forces
   those active-factor conditions.  If not, isolate the exact obstruction:
   infinite-index behavior, nonfunctional crossing relation, partiality,
   nonbijectivity, YBE failure on unreached triples, or loss of orbit-injectivity.

5. Analyze uniform stabilizer separation.  Can orbit-relevant transporter
   families in As(C_M(X)) have factorial accumulation while remaining harmful
   and not yielding an active factor?  If impossible, prove the YBE-specific
   reason.  If possible, formulate it as an obstruction.

6. Analyze whether escape holonomy closes the gap.  Does every harmful
   contextual collapse produce finite escape-holonomy data that is rack
   determined and uniformly separated?  Or can escape holonomy remain
   genuinely profinite/non-finite-state?

7. State the strongest valid theorem at the end.  Useful outcomes include:
   - harmful collapse dichotomy => Sawin for residual-rigid X;
   - finite rack absorption or finite active-factor extraction under explicit
     extra hypotheses;
   - a counterexample to the dichotomy at the level of contextual racks;
   - or a sharper missing lemma strictly smaller than Sawin.

Guardrails:

- Do not claim all right scattering is bad.
- Do not claim finite right-separation follows from residual rigidity.
- Do not use ordinary quotients as active factors unless the kernel direction
  ker rho_n^Z <= ker rho_n^X is proved.
- Do not replace uniform transporter separation by pointwise stabilizer
  separability.
- Do not assume a partial contextual crossing relation extends to a total
  bijective YBE solution without proof.
- If an obstruction is absorbed by a rack detector, classify it as harmless.
```

