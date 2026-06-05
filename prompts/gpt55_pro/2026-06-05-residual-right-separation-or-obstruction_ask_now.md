# Residual Right-Separation Or Obstruction Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-05.

Prompt:

```text
Please answer self-containedly and mathematically.  We are working on Sawin's
finite rack-domination problem:

    For every finite bijective set-theoretic YBE solution X, does there exist
    a finite rack Y such that ker rho_n^Y <= ker rho_n^X for every n?

Write r_X(x,y)=(L_x(y),R_y(x)).  The current route is the finite-state
contextual tower.

Let

    L_X=<lambda_x | lambda_x lambda_y=lambda_u lambda_v
          whenever r_X(x,y)=(u,v)>

be the positive left structure monoid.  For a finite quotient theta:L_X->M,
the contextual rack C_M(X) has generators d_{a,x,b}, a,b in M, x in X, and
relations

    d_{a,u,lambda_v b}=d_{a lambda_x,y,b},

    d_{a lambda_u,v,b}
      =
    d_{a lambda_x,y,b} triangleright d_{a,x,lambda_y b}.

The labels Theta_n^M are braid-equivariant.  If one finite M and one finite
rack quotient phi:C_M(X)->Y make phi^n Theta_n^M injective on every braid
orbit in every arity, then ker rho_n^Y <= ker rho_n^X for every n.

Current obstruction.

Finite-index contextual rigidity is not proved.  Pointwise finite separation
of fixed contexts does not imply one finite detector over all arities.  The
missing principle is:

    residual-rigid X
    => finite-index, crossing-compatible, uniformly stabilizer-separable
       contextual behavior.

In particular:

1. For p,q in L_X, define

       E(p,q)={ahat in profinite L_X : ahat p = ahat q}.

   E(p,q)=empty is equivalent to finite right-separation: some finite quotient
   theta:L_X->M has m theta(p) != m theta(q) for every m in M.
   This is stronger than ordinary residual finiteness.

2. YBE origin and nondegeneracy do not eliminate right scattering.  For

       X={0,1},  r(i,j)=(j,1-i),

   the solution is bijective and nondegenerate, but the left structure monoid
   has lambda_0 lambda_0 = lambda_0 lambda_1 while lambda_0 != lambda_1.

3. Bounded bad witnesses are not obtained just by deleting observer strands or
   by braid locality, because contextual labels depend on the full left and
   right observer states.

4. Pointwise stabilizer separability in As(C_M(X)) is not enough.  Uniform
   separation of an infinite transporter family T from a stabilizer H requires
   closure(T) cap closure(H)=empty, not just t notin closure(H) for each t.

5. A profinite contextual collapse gives a finite active factor only if it is
   finite-index, crossing-compatible, and extends to a total bijective YBE
   solution Z.

Task.

1. Determine whether residual-rigid hypotheses can imply finite
   right-separation for all orbit-relevant active pairs p!=q in L_X.  If yes,
   prove it precisely.  If no, identify the exact additional hypothesis needed.

2. Analyze the nondegenerate constant-action example r(i,j)=(j,1-i).  Is it
   already covered by a known positive branch or an explicit finite rack
   detector?  What guardrail does it impose on any attempted residual-rigid
   theorem?  Does its right scattering become harmless, and why?

3. Try to construct or rule out a residual-rigid obstruction with
   orbit-relevant actual or profinite right scattering, no proper
   domination-reducing active factor, and no finite contextual rack detector.
   If construction is impossible, isolate the theorem that makes it impossible.

4. Investigate bounded bad witnesses again under stronger assumptions such as
   finite right-separation, cancellativity, group embeddability of L_X,
   finite Green/Rees depth, or residual-rigid minimality.  Does any combination
   yield an N(X) such that all contextual bad pairs have bad subconfigurations
   of arity <= N(X)?

5. Analyze active-factor extraction.  Given a finite-index contextual collapse
   on states (a,b) and maps pi_{a,b}:X->Z, give necessary and sufficient
   conditions for the formula

       r_Z(pi_{a,lambda_y b}(x), pi_{a lambda_x,b}(y))
       =
       (pi_{a,lambda_v b}(u), pi_{a lambda_u,b}(v))

   to define a finite bijective YBE solution Z with
   ker rho_n^Z <= ker rho_n^X.  Can residual-rigid failure of contextual
   separation force these conditions?

6. Analyze uniform stabilizer separation for contextual racks.  For fixed M,
   can orbit-relevant transporter families in As(C_M(X)) be uniformly separated
   from stabilizers using YBE-specific structure?  Or can a factorial-sequence
   accumulation phenomenon be realized in contextual rack transporters?

7. Compare with escape holonomy.  Can escape-holonomy transporter/coset data
   be compressed into a finite contextual rack state system under reasonable
   residual-rigid hypotheses?  Or does it retain genuinely non-finite-state
   data?

8. State the strongest valid theorem at the end.  Useful outcomes include:
   - finite right-separation + bounded bad witnesses + uniform stabilizer
     separation => Sawin;
   - residual-rigid failure => proper domination-reducing active factor;
   - an explicit finite or profinite obstruction to contextual rigidity;
   - or a sharper missing lemma strictly smaller than Sawin.

Important guardrails:

- Do not claim pointwise residual finiteness gives one finite detector.
- Do not use ordinary quotients as active factors unless the kernel direction
  ker rho_n^Z <= ker rho_n^X is proved.
- Do not erase context dependence by adding inert observers; inert observers
  are constant inside a braid orbit.
- Do not replace uniform transporter separation by pointwise stabilizer
  separability.
- If a proposed obstruction is not residual-rigid, say exactly which branch
  removes it and what remains after removal.
```

