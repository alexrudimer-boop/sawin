# Bounded Bad Witness Or Obstruction Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-05.

Prompt:

```text
Please answer self-containedly and mathematically. Do not give only a bounded
computation. We are working on Sawin's finite rack-domination problem:

    For every finite bijective set-theoretic YBE solution X, does there exist
    a finite rack Y such that ker rho_n^Y <= ker rho_n^X for every n?

Write r_X(x,y)=(L_x(y),R_y(x)).

Current route.

The finite-state contextual tower is valid.  Let

    L_X=<lambda_x | lambda_x lambda_y=lambda_u lambda_v
          whenever r_X(x,y)=(u,v)>

be the positive left structure monoid.  For a finite quotient theta:L_X->M,
define C_M(X) with generators

    d_{a,x,b}        (a,b in M, x in X)

and relations

    d_{a,u,lambda_v b}=d_{a lambda_x,y,b},
    d_{a lambda_u,v,b}
      =
    d_{a lambda_x,y,b} triangleright d_{a,x,lambda_y b}.

The labels Theta_n^M are braid-equivariant.  If for one finite M and one
finite rack quotient phi:C_M(X)->Y, the labels phi^n Theta_n^M separate all
distinct points inside every braid orbit in every arity, then

    ker rho_n^Y <= ker rho_n^X       for all n.

Known obstruction.

Pointwise tower separation is not enough.  If B_M is the set of same-orbit bad
pairs not separated by C_M(X), refinement gives B_{M'} subset B_M, but

    intersection_M B_M = empty

does not imply

    exists M with B_M = empty.

Sawin needs one finite M and one finite rack quotient for all arities.

Useful positive fact.

The monoid L_X is residually finite because its presentation is homogeneous of
degree 2.  The length-truncation quotients T_N separate any fixed pair of
contexts.  But they do not give one finite quotient for all arities, since
context length is unbounded.

Current possible obstructions.

1. Unbounded bad witnesses:
   an infinite sequence of same-orbit bad pairs requiring finer and finer M.

2. Profinite scattering states:
   a profinite state ahat in the completion of L_X with, for example,

       ahat lambda_s = ahat lambda_x = ahat lambda_u,

   while

       r_X(s,y)=(x,y),   r_X(x,y)=(u,y),   u != x.

   This makes the local crossing invisible in every finite M at some growing
   prefix state.

3. Nonclosed stabilizer cosets:
   for fixed M, finite-rack residual equivalence in C_M(X) is controlled by
   stabilizer coset closure in As(C_M(X)).

4. Active-factor extraction failure:
   contextual collapses are state-dependent and do not automatically define a
   finite YBE solution Z with maps pi_{a,b}:X->Z satisfying

       r_Z(pi_{a,lambda_y b}(x), pi_{a lambda_x,b}(y))
       =
       (pi_{a,lambda_v b}(u), pi_{a lambda_u,b}(v)).

Task.

1. Try to prove a bounded bad-witness theorem:

       For residual rigid X with no proper domination-reducing active factor,
       there exists N=N(X) such that every contextual tower bad pair has a bad
       subconfiguration of arity <= N.

   If true, explain how it yields one finite M and one finite rack detector.
   If false or unsupported, isolate the obstruction.

2. Analyze whether profinite scattering states can exist for YBE-origin
   left structure monoids L_X after residual rigid reductions.  Are such states
   ruled out by cancellativity, regularity, Green structure, minimal ideals, or
   other YBE constraints?  Or can they be constructed?

3. Try to turn an infinite sequence of bad pairs requiring finer M into a
   domination-reducing active factor.  If possible, construct the finite YBE
   solution Z, the maps Pi_n, and inert observers eta_n.  If impossible, state
   the precise context-dependence obstruction.

4. Analyze the stabilizer side.  For the sequence of finite quotients M needed
   to separate longer contexts, can one choose M so that all orbit-relevant
   stabilizer cosets in As(C_M(X)) are profinitely separated?  Or can
   nonclosed cosets persist uniformly?

5. Compare with finite automaton contextual detectors C_{P,Q}(X).  Does a
   Myhill-Nerode/minimal automaton argument give a finite state system for all
   orbit-relevant labels, or can the required automaton have infinitely many
   states?

6. Compare with escape-holonomy.  Does escape-holonomy separation produce a
   finite-state, rack-determined label system under residual rigidity?  If not,
   identify the exact extra object data beyond finite two-sided states.

7. State the strongest valid next theorem.  Useful outcomes include:
   - bounded bad witness => Sawin via contextual tower;
   - no profinite scattering states plus stabilizer separability => Sawin;
   - tower failure => active factor;
   - a concrete realizable obstruction to uniform contextual tower separation;
   - or a sharper finite/profinite lemma strictly smaller than Sawin.

Important:

- Do not claim product observers alone prove domination.
- Do not confuse pointwise residual separation with one finite detector for all
  arities.
- Do not use ordinary quotients as active factors unless the kernel-reflecting
  direction is proved.
- Do not replace profinite monoid/group separability with finite closure.
- A useful answer should either prove a bounded/uniformity theorem, refute it
  with a realizable obstruction, or isolate the exact next missing lemma.
```

