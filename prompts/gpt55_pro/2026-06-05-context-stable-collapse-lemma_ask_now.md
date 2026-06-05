# Context-Stable Collapse Lemma Prompt

Status: ask now / awaiting GPT-5.5 Pro response.

Prompt:

```text
Please answer self-containedly and mathematically.  We are working on Sawin's
finite rack-domination problem:

    For every finite bijective set-theoretic YBE solution X, does there exist
    a finite rack Y such that ker rho_n^Y <= ker rho_n^X for every n?

Current route: finite contextual rack detectors.

For a finite quotient theta:L_X->M, define

    Theta_n^M(x)_i=d_{a_i,x_i,b_i}

with

    a_i=theta(lambda_{x_1}...lambda_{x_{i-1}}),
    b_i=theta(lambda_{x_{i+1}}...lambda_{x_n}).

For fixed finite M, the endpoint issue is settled.  Let

    Sbar_M={d_{a,x,b}:a,b in M, x in X} subset C_M(X)

as actual elements of C_M(X).  If every distinct pair in Sbar_M is separated
by some finite rack quotient, then one finite product quotient is injective on
Sbar_M.  After that, fixed-M badness is exactly

    x != x',
    x' in B_n.x,
    Theta_n^M(x)=Theta_n^M(x')

inside C_M(X)^n.

For fixed M, exact label equality is regular: using

    E_M subset (M x X x M)^2,
    (a,x,b) E_M (a',x',b') iff
    d_{a,x,b}=d_{a',x',b'} in C_M(X),

one recognizes Theta_n^M(x)=Theta_n^M(x') by finite prefix/suffix state
annotations.

But the braid-orbit relation is not regular in general.  The flip rack
r(x,y)=(y,x) on {0,1} gives braid orbits equal to Parikh classes; intersecting
the convolution orbit relation with (0,1)^*(1,0)^* gives

    {(0,1)^n(1,0)^n:n>=0},

which is nonregular.  Thus ordinary regularity/automaticity of braid orbits
is not available in general.

Also, weak Higman boundedness is not enough.  A long bad pair may contain a
short bad subsequence, but deleting observer strands changes the contextual
states a_i,b_i, so a detector separating the short standalone pair need not
separate the long pair.

The useful missing theorem must be context-stable:

    every harmful long exact contextual collapse contains a bounded bad core
    whose separation is stable under arbitrary surrounding observers.

Task.

1. Formulate a precise context-stable bounded core lemma.  What exactly should
   a "core" be so that a detector separating the core also separates every
   occurrence of that core inside arbitrary left/right observer contexts?
   Give a mathematically clean definition using contextual triples

       (a,x,b) in M x X x M

   or profinite triples

       (ahat,x,bhat) in hat{L_X} x X x hat{L_X}.

2. Determine whether such a context-stable bounded core lemma follows from
   any standard well-quasi-ordering argument, such as Higman's lemma, after
   enriching letters by contexts.  If yes, prove it.  If no, explain exactly
   where wqo fails: changing prefix/suffix states, braid reachability, hidden
   state refinement, or non-hereditary orbit data.

3. Analyze whether the flip rack nonregularity is harmless because the rack
   branch Y=X absorbs it.  More generally, can every nonregular orbit
   phenomenon in a solved branch be separated from genuinely harmful
   contextual collapse by an active-factor/rack-absorption argument?

4. Study fixed-M exact collisions.  Can there exist a fixed finite M and a
   harmful ultrafilter of same-orbit pairs with exact

       Theta_n^M(x)=Theta_n^M(x')

   in unbounded arity, after Sbar_M has been endpoint-separated?  Try to
   construct one or prove that it implies a finite rack detector or proper
   finite active factor.

5. Study state-refinement escape.  Let

       K=hat{L_X} x X x hat{L_X},
       E_infty=intersection_M (q_M x q_M)^(-1)(E_M).

   Can harmful orbit-relevant E_infty fail to be pulled back from any finite
   quotient M0?  If yes, describe an explicit profinite mechanism.  If no,
   prove a finite-index contextual Myhill-Nerode theorem.

6. Revisit the observer-corridor mechanism:

       lambda_o^k remains distinguishable in L_X,
       finite quotients see long periods,
       active letters p,q collapse at prefix lambda_o^k,
       a braid corridor realizes o^k p (...) -> o^k q (...),
       k=n! defeats fixed finite quotients.

   Is the visible color periodicity obstruction enough to rule this out, or
   can prefix monoid/context data still carry unbounded information?  Identify
   the exact YBE identity, if any, that blocks such a corridor.

7. Analyze whether hidden stabilizer/path holonomy after exact endpoint
   equality can be converted into a finite enriched detector.  What uniform
   separability condition on reachable holonomy groupoids is required?  When
   does holonomy remain only profinite diagnostic data?

8. Analyze active-factor extraction from a context-stable or profinite
   collapse.  Give the exact conditions under which maps

       pi_{a,b}:X->Z

   define a total bijective YBE solution on Z, satisfy YBE on all triples,
   give braid-equivariant Pi_n, and prove

       ker rho_n^Z <= ker rho_n^X
       for all n.

9. State the strongest valid next theorem.  Choose between:

       context-stable bounded harmful witnesses,
       finite-index contextual Myhill-Nerode,
       uniform reachable holonomy separation,
       active-factor extraction from unbounded exact contextual collapse,

   or formulate a sharper combined lemma.

Guardrails.

- Do not use ordinary regularity of braid orbits; it is false in general.
- Do not use weak subsequence-minimal boundedness unless it is stable under
  surrounding contextual states.
- Do not treat hidden stabilizer holonomy as endpoint-label detection.
- Do not treat an ordinary quotient as a domination-reducing active factor
  without proving ker rho^Z <= ker rho^X.
- Do not assume contextual equivalence classes automatically define a total
  bijective YBE solution.

Goal.

Find the precise theorem, strictly smaller than Sawin, that bridges the gap
from unbounded exact contextual collapse to either finite rack absorption or
proper finite active-factor extraction.
```
