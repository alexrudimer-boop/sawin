# Everywhere-Singular Rigid-Core Theory Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-04.

Prompt:

```text
Please answer self-containedly and mathematically. Do not propose another
bounded computation or implementation plan unless it is only a small check of a
theorem you prove. The goal is to make real theoretical progress on Sawin's
finite-rack domination problem.

Problem:

Let X be a finite bijective set-theoretic Yang-Baxter solution. Write

    r(x,y) = (L_x(y), R_y(x)).

Sawin's question asks whether every such finite X is dominated by a finite rack:
does there exist a finite rack Y such that, for every n,

    ker rho^Y_n <= ker rho^X_n

as braid group representations?

Current rigorous reductions:

1. One-sided nondegenerate solutions are rack-dominated by the
   Lebed-Vendramin / guitar / derived-rack branch.
2. Involutive solutions are dominated by the flip rack.
3. Proper quotient, subsolution, flip-across/twisted-union, transport/monodromy
   rackification, and periodic observer-rack factor certificates give positive
   closure mechanisms.
4. Fixed-arity rack cofinality holds: for each fixed n and each finite quotient
   representation B_n -> H, some finite conjugation rack Y has

       ker rho^Y_n <= ker(B_n -> H).

   Hence a genuine no-rack counterexample must defeat every finite rack prefix
   at arbitrarily large arities, not merely at one bounded arity.
5. If X is a minimal counterexample outside the one-sided nondegenerate branches
   and has no nonempty proper crossing-closed subsolution, then every coordinate
   map L_x and R_y is singular. This follows because the set of x for which L_x
   is bijective is crossing-closed, and similarly on the right.

Therefore the remaining theoretical endpoint is an asymptotically
rack-invisible rigid core: a finite bijective YBE solution X that is

    everywhere singular,
    non-involutive,
    quotient-rigid,
    subsolution-rigid,
    observer-rigid,
    not flip-across/twisted-union,
    without a proper active rack/observer factor,
    and with unbounded rack-prefix kernel pressure.

The key finite identities are

    L_{L_x(y)} L_{R_y(x)} = L_x L_y,                         (Y1)

    R_z R_y = R_{R_z(y)} R_{L_y(z)},                         (Y3)

plus the middle mixed identity from the Yang-Baxter equation.

Task:

Try to resolve the remaining theoretical endpoint. Specifically, answer one of
the following, with proof-level detail:

A. Prove a structural theorem ruling out everywhere-singular rigid cores.

   A useful target would be:

       If X is finite, bijective, YBE, and every L_x and R_y is singular, then
       X has a nontrivial YBE quotient, a nonempty proper crossing-closed
       subsolution, a nonconstant invariant observer, or a finite observer-rack
       factorization.

   It is acceptable to prove a sharper theorem under an explicit condition that
   every minimal counterexample must satisfy.

B. Prove a semigroup-theoretic decomposition theorem using the transformation
   semigroups

       S_L = <L_x : x in X>,       S_R = <R_y : y in X>.

   In particular, analyze the minimal-rank ideals, Green/Rees structure, and
   kernel/image systems. Does (Y1), (Y3), and bijectivity force a proper
   crossing-closed subset, quotient congruence, invariant observer, or rack
   active factor?

   A concrete desired lemma:

       Let I_L be the minimal ideal of S_L. If all L_x are singular, then the
       image/kernel structure of I_L is YBE-invariant enough to produce a
       nontrivial quotient, subsolution, or observer unless X is already
       rack-factorable.

   Prove this or give a precise obstruction.

C. Refute the proposed structural route by constructing a purely mathematical
   obstruction pattern, not just a search plan: a finite set of transformation
   semigroup data satisfying all formal consequences of (Y1)/(Y3) and
   bijectivity while having no evident quotient/subsolution/observer. Explain
   exactly which missing YBE consequence would still need to be checked.

D. Find a different theoretical route to Sawin-positive that does not rely on
   enumerating rigid cores. For example, show that every finite bijective YBE
   action is a factor or extension of a finite Artin/conjugation-rack action plus
   fixed observer channels, or prove a finite-state transducer/rackification
   theorem that is genuinely weaker than active-factor observability but still
   implies domination.

Important constraints:

- Do not answer only "this is open." If no proof is available, identify the
  exact first unproved lemma and give either a counter-lemma or a proof strategy
  precise enough to be audited.
- Do not give a computational next step as the main result.
- Use the YBE coordinate identities and finite transformation semigroup theory
  explicitly.
- Separate statements that would prove Sawin from statements that merely give a
  new positive branch.
- If you propose a theorem, include a proof or a precise obstruction at the
  first nontrivial step.
```
