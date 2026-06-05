# Finite-Index Contextual Rigidity Prompt

Status: answered / GPT-5.5 Pro response recorded on 2026-06-05.

Follow-up status:

GPT-5.5 Pro concluded that finite-index contextual rigidity is not derivable
from the listed residual-rigid hypotheses.  The obstruction is a missing
compactness/noetherianity principle:

```text
pointwise finite separation of each fixed context
does not imply
finite-index contextual behavior over all arities.
```

The response sharpened the boundary in four ways.

First, finite right-separation in the structure monoid is stricter than
ordinary residual finiteness.  For `p,q in L_X`, the profinite equalizer

```text
E(p,q)={ahat in profinite L_X : ahat p = ahat q}
```

is empty exactly when one finite quotient separates the right translations by
`p` and `q` at every finite state.  Residual finiteness separates only fixed
elements.

Second, YBE origin and even nondegeneracy do not rule out right scattering.
The constant-action solution on `{0,1}`,

```text
r(i,j)=(j,1-i),
```

is bijective and nondegenerate, but its left structure monoid has
`lambda_0 lambda_0 = lambda_0 lambda_1` while `lambda_0 != lambda_1`.

Third, bounded bad witnesses are not obtained merely from braid locality,
deleting strands, Fadell-Neuwirth forgetting, or product observers, because
long observer words can be essential to the prefix/suffix states that create a
contextual collapse.

Fourth, pointwise stabilizer separability is not enough.  Uniform separation
of an infinite transporter family is stronger, as shown abstractly by the
factorial sequence `T={n!:n>=1}` in `Z` accumulating at the trivial stabilizer
in every finite quotient.

The remaining target is therefore a sharper theorem:

```text
Residual-rigid X
=> finite-index, crossing-compatible, uniformly stabilizer-separable
   contextual behavior.
```

This is still conditional and strictly smaller than Sawin, but it is not yet
proved by the current route.

Prompt:

```text
Please answer self-containedly and mathematically. Do not give only a bounded
computation. We are working on Sawin's finite rack-domination problem:

    For every finite bijective set-theoretic YBE solution X, does there exist
    a finite rack Y such that ker rho_n^Y <= ker rho_n^X for every n?

Write r_X(x,y)=(L_x(y),R_y(x)).

Current route.

The finite-state contextual tower gives a valid detector.  Let

    L_X=<lambda_x | lambda_x lambda_y=lambda_u lambda_v
          whenever r_X(x,y)=(u,v)>

be the positive left structure monoid.  For a finite quotient theta:L_X->M,
define C_M(X) with generators d_{a,x,b}, a,b in M, x in X, and relations

    d_{a,u,lambda_v b}=d_{a lambda_x,y,b},
    d_{a lambda_u,v,b}
      =
    d_{a lambda_x,y,b} triangleright d_{a,x,lambda_y b}.

The labels Theta_n^M are braid-equivariant.  If one finite M and one finite
rack quotient phi:C_M(X)->Y make phi^n Theta_n^M injective on every braid
orbit in every arity, then ker rho_n^Y <= ker rho_n^X for all n.

Known facts.

1. L_X is residually finite by length-truncation quotients because its
   presentation is homogeneous of degree 2.

2. Residual finiteness separates fixed context words but does not give one
   finite quotient for all arities.

3. Pointwise tower separation does not imply a uniform finite M.  One needs
   finite-index contextual behavior, or equivalently a bounded bad-witness /
   finite Myhill-Nerode theorem.

4. For p,q in L_X, profinite right scattering is controlled by

       E(p,q)={ahat in profinite L_X : ahat p = ahat q}.

   E(p,q)=empty is equivalent to finite right-separation: some finite quotient
   theta:L_X->M satisfies m theta(p) != m theta(q) for every m in M.
   Ordinary residual finiteness does not imply this.

5. For fixed M, finite-rack residual equivalence in C_M(X) is controlled by
   stabilizer coset closure in As(C_M(X)).  Uniform separation of an infinite
   family of transporters is stronger than pointwise stabilizer separability.

6. Infinite contextual tower failure does not automatically yield an active
   factor.  To extract one, the limiting contextual equivalences must factor
   through finitely many states and define a total finite bijective YBE
   solution Z via maps pi_{a,b}:X->Z satisfying

       r_Z(pi_{a,lambda_y b}(x), pi_{a lambda_x,b}(y))
       =
       (pi_{a,lambda_v b}(u), pi_{a lambda_u,b}(v)).

Exact missing lemma.

Finite-index contextual rigidity:

    For residual-rigid X, every orbit-relevant profinite contextual collapse
    factors through one finite quotient of L_X, and the resulting finite
    contextual collapse is crossing-compatible and finite-rack separable.

Task.

1. Try to prove the finite-index contextual rigidity lemma.  Look for
   noetherianity, bounded braid-locality, Green/Rees structure, cancellativity,
   automaticity, regular-language, or finite-state properties forced by YBE and
   residual rigidity.

2. If the lemma is false or unsupported, isolate a realizable obstruction:
   - an infinite sequence of same-orbit bad pairs requiring finer and finer
     finite quotients M;
   - a profinite right-scattering state in L_X that survives residual-rigid
     reductions;
   - a nonregular contextual Myhill-Nerode relation of infinite index;
   - or a uniformly nonseparable transporter family in As(C_M(X)).

3. Analyze right-separation in L_X.  Which YBE hypotheses imply
   E(p,q)=empty for active p!=q?  Does right-nondegeneracy, right
   cancellativity, group embeddability, or residual rigid core structure rule
   out all orbit-relevant right scattering?  If not, give a table pattern.

4. Analyze bounded bad witnesses.  Can every same-orbit contextual bad pair be
   reduced to a bounded arity subconfiguration using braid locality, deletion,
   Fadell-Neuwirth-style arguments, or product observers?  If not, explain why
   long context is essential.

5. Analyze active-factor extraction.  Given a profinite contextual collapse,
   when does it define a finite crossing-compatible state-dependent YBE factor
   Z?  Can residual rigidity force that finite-index compatibility?  If not,
   isolate the obstruction.

6. Analyze uniform stabilizer separation.  For orbit-relevant transporter
   families T in As(C_M(X)), can one prove closure(T) avoids closure(H) in a
   finite quotient?  Or can the factorial-sequence phenomenon in Z be realized
   by contextual rack transporters?

7. Compare with escape holonomy.  Can escape-holonomy data provide the missing
   finite-index contextual states and uniform stabilizer separation, or does it
   retain transporter/coset data beyond finite rack-determined states?

8. State the strongest valid theorem.  Useful outcomes include:
   - finite-index contextual rigidity => Sawin;
   - no right-scattering + bounded witnesses + uniform stabilizer separation
     => Sawin;
   - tower failure => active factor;
   - a realizable infinite-index obstruction;
   - or a sharper missing lemma strictly smaller than Sawin.

Important:

- Do not claim product observers alone prove domination.
- Do not confuse pointwise residual separation with one finite detector for all
  arities.
- Do not use ordinary quotients as active factors unless ker rho_n^Z <=
  ker rho_n^X is proved.
- Do not replace profinite monoid/group separation with finite closure.
- A useful answer should either prove finite-index contextual rigidity, refute
  it with a realizable obstruction, or reduce it to a sharper theorem.
```
