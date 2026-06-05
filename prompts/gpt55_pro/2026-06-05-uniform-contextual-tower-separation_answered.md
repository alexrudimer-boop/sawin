# Uniform Contextual Tower Separation Prompt

Status: answered on 2026-06-05.

Follow-up status:

GPT-5.5 Pro confirmed that the contextual tower is valid but still conditional:
the missing lemma is uniform finite-state contextual separation, not pointwise
residual separation.  It also proved a useful guardrail: the positive left
structure monoid `L_X` is residually finite by length-truncation quotients.
This separates fixed contexts, but does not supply one finite state quotient
working for all arities.

The remaining obstructions are unbounded finite-state context requirements,
profinite scattering states in the completion of `L_X`, and nonclosed
stabilizer cosets in `As(C_M(X))`.  The next active prompt asks whether these
obstructions can be reduced to a bounded bad-witness theorem, an active-factor
extraction theorem, or a realizable counterpattern.

Prompt:

```text
Please answer self-containedly and mathematically. Do not give only a bounded
computation. We are working on Sawin's finite rack-domination problem:

    For every finite bijective set-theoretic YBE solution X, does there exist
    a finite rack Y such that ker rho_n^Y <= ker rho_n^X for every n?

Write r_X(x,y)=(L_x(y),R_y(x)).

Known guardrails:

1. Product observers are inert but kernel-universal by singular padding:
   X=E x Z has ker rho_n^X=ker rho_n^Z.

2. One-coordinate prefix rack labels collapse through evaluation.  The
   two-sided contextual rack C_L(X) is stronger but has scattering collapse
   because it uses S_L^1 rather than word-level structure data.

3. The finite-state contextual tower uses the positive left structure monoid

       L_X=<lambda_x | lambda_x lambda_y=lambda_u lambda_v
             whenever r_X(x,y)=(u,v)>.

   For a finite quotient theta:L_X->M, define C_M(X) with generators

       d_{a,x,b}        (a,b in M, x in X)

   and relations

       d_{a,u,lambda_v b}=d_{a lambda_x,y,b},
       d_{a lambda_u,v,b}
          =
       d_{a lambda_x,y,b} triangleright d_{a,x,lambda_y b}.

   The corresponding contextual labels Theta_n^M are braid-equivariant.

4. Fixed-M theorem:
   If for some finite M, every distinct same-orbit pair w,w' in every X^n is
   separated in some coordinate modulo finite-rack residual equivalence in
   C_M(X), then X is dominated by a finite rack.

5. For fixed M, finite-rack residual equivalence is controlled by stabilizer
   coset closure in

       As(C_M(X)).

   If d_beta=g.d_alpha, then

       alpha ==_{M,fin} beta
       iff
       g in closure_prof(Stab(alpha)).

6. The main new obstruction is uniformity.  Finer M can improve separation,
   but Sawin requires one finite M and one finite rack quotient working for all
   arities.  Pointwise tower separation is not enough.

7. Tower-equivalence can persist for three reasons:
   - monoid profinite collapse in L_X;
   - universal collapse in the full marked-word contextual rack;
   - rack profinite collapse in every finite C_M(X).

8. Contextual scattering cycles do not automatically yield domination-reducing
   active factors.  A state-dependent active factor would require a finite YBE
   solution Z and maps pi_{a,b}:X->Z satisfying

       r_Z(pi_{a,lambda_y b}(x), pi_{a lambda_x,b}(y))
       =
       (pi_{a,lambda_v b}(u), pi_{a lambda_u,b}(v)).

Task.

1. Try to prove the uniform contextual tower lemma:

       If X is residual rigid and has no proper domination-reducing active
       factor, then there exists one finite quotient M of L_X such that C_M(X)
       is orbitwise residually separating on all Theta_n^M labels.

   If this is false or currently unprovable, isolate the exact obstruction.

2. Analyze finite-state uniformity.  Does some compactness, noetherianity,
   finite automaton, bounded-context, or braid-locality argument reduce
   all arities to finitely many orbit-relevant contextual pairs?  Or can one
   build an infinite sequence of same-orbit bad pairs requiring finer and finer
   M?

3. Analyze monoid profinite collapse in L_X.  Are the relevant context and
   escape words residually separated in finite quotients of L_X for YBE-origin
   monoids?  Can nonseparable monoid behavior be realized by finite YBE
   solutions?

4. Analyze the full marked-word contextual rack.  If it is pointwise
   residually finite on orbit labels, can one extract a single finite quotient
   sufficient for all arities?  Does every finite rack quotient factor through
   a finite-state quotient C_M(X), or can finite rack quotients have
   non-finite-state dependence on contexts?

5. Analyze profinite stabilizer obstructions in As(C_M(X)).  Do residual rigid
   hypotheses imply separability of orbit-relevant stabilizer cosets for some
   finite M?  Or can hard subgroup-separability behavior survive throughout
   the tower?

6. Try to turn contextual tower failure into a domination-reducing active
   factor.  If possible, construct the finite YBE solution Z, the maps
   Pi_n:X^n->Z^n, and inert observers eta_n.  If impossible, explain exactly
   why the context dependence blocks active-factor extraction.

7. Compare finite monoid quotients with more general finite automaton
   contextual detectors C_{P,Q}(X), where P and Q are finite left/right state
   sets with L_X actions.  Does allowing arbitrary finite automata remove the
   uniformity obstruction, or merely restate it in a larger tower?

8. Relate this to escape-rack/minimal-ideal holonomy.  Does escape-holonomy
   separation imply finite separation in some C_M(X) or C_{P,Q}(X) under a
   precise finite rack determinacy condition?  If not, what extra object data
   does escape holonomy retain?

9. State the strongest valid reduced theorem.  Useful outcomes include:
   - a proof of the uniform contextual tower lemma;
   - a finite obstruction showing it can fail;
   - a contextual tower failure -> active factor theorem;
   - an escape/finite-automaton determinacy theorem;
   - or an exact new finite/profinite lemma that is strictly smaller than
     Sawin.

Important:

- Do not claim product observers alone prove domination.
- Do not use ordinary quotients as active factors unless ker rho_n^Z <=
  ker rho_n^X is proved.
- Do not confuse pointwise residual separation with one finite detector for
  all arities.
- Do not replace profinite subgroup or monoid separability with finite closure.
- A useful answer should either prove uniform finite-state contextual
  separation, refute it with a realizable obstruction, or reduce it to a
  sharper finite/profinite/active-factor theorem.
```
