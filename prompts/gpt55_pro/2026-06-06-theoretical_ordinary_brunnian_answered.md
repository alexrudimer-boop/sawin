theoretical_answered

Status: answered on 2026-06-06.  Reviewed in
`proofs/2026_06_06_theoretical_ordinary_brunnian_response_review.md`; the
valid extracted progress is recorded in
`proofs/ordinary_brunnian_sharpening.md`.

This is a self-contained theoretical prompt.  Do not ask for code,
repository access, or further computations.  Be aggressive: try to fully
resolve Will Sawin's problem from the Brunnian-core reduction below.

Problem, due to Will Sawin.

Let X be a finite bijective set-theoretic solution of the Yang-Baxter
equation.  Thus each braid group B_n acts on X^n by

  rho^X_n : B_n -> Sym(X^n).

A finite rack Y is viewed as the set-theoretic solution

  R_Y(a,b) = (a*b, a).

Question.  Does every finite bijective set-theoretic YBE solution X admit a
single finite rack Y, independent of n, such that

  ker rho^Y_n <= ker rho^X_n

for every n?

Known closed cases and guardrails.

1. Finite one-sided nondegenerate solutions are closed by the derived
   rack/guitar construction, with kernel equality in every arity.

2. Involutive solutions, finite products of dominated solutions, and braided
   quotients of dominated solutions are dominated.

3. Genuinely degenerate X cannot be solved by a finite nondegenerate braided
   cover: a finite surjective image of a left-nondegenerate solution is
   left-nondegenerate.  Similarly on the right.

4. A coordinatewise quotient from a rack switch R_Y(a,b)=(a*b,a) is too
   restrictive.  A proof for degenerate X must use contextual readouts,
   finite-state decoders, or kernel-theoretic domination.

5. No single braid is invisible to all finite racks.  Artin faithfulness plus
   residual finiteness of free groups gives a finite conjugation rack
   detecting any fixed nontrivial braid.

6. Fixed-arity rack cofinality is available: for each fixed k and each finite
   quotient representation theta:B_k -> H, there exists a finite rack Z with

   ker rho^Z_k <= ker theta.

   Hence any counterexample must force failures at unbounded braid index.

Transparent extension and exact support.

For a rack Y define Y^0=Y sqcup {0} by

  a*b = old a*b  for a,b in Y,
  0*b = b,
  a*0 = 0,
  0*0 = 0.

This is a rack.  Let T_2 be the two-element trivial rack, so ker rho^{T_2}_n
is the pure braid group P_n.

For I subset {1,...,n}, let partial_I beta be the braid obtained by deleting
all strands outside I.  If iota_I colors the strands in I by elements of Y
and all other strands by 0, then for every beta in B_n,

  rho^{Y^0}_n(beta) iota_I(c)
    =
  iota_{pi_beta(I)}(rho^Y_|I|(partial_I beta)c),

where pi_beta is the braid permutation.  In particular, for pure beta,

  beta in ker rho^{Y^0}_n
    iff
  partial_I beta in ker rho^Y_|I| for every I.

Fully Brunnian-core reduction.

For a finite rack Y, set

  Q = Y^0 x T_2.

For n>=2 define

  B_{X,Y}(n) =
  {
    beta in ker rho^Q_n :
    rho^X_|I|(partial_I beta)=1
    for every proper I subsetneq {1,...,n}
  }.

Then Q dominates X if and only if

  rho^X_n(beta)=1

for every n and every beta in B_{X,Y}(n).

Proof sketch: if Q fails to dominate X, choose a Q-invisible, X-visible
witness of minimal arity.  The T_2 factor makes it pure.  Exact transparent
support shows every proper deletion remains Q-invisible; minimality forces
every proper deletion to be X-trivial.

Cofinal negative target.

Let R_1,R_2,... enumerate finite rack isomorphism classes, let

  P_m = R_1 x ... x R_m,
  Q_m = P_m^0 x T_2.

If no finite rack dominates X, then for every m there are n_m and beta_m with

  beta_m in ker rho^{Q_m}_{n_m},
  rho^X_{n_m}(beta_m) != 1,
  rho^X_|I|(partial_I beta_m)=1
    for every proper I subsetneq {1,...,n_m}.

Moreover n_m -> infinity by fixed-arity rack cofinality.

Thus the remaining counterexample target is very sharp: one explicit finite
degenerate X must have a cofinal sequence of rack-prefix-invisible,
X-visible, fully deletion-minimal pure braids.

Your task.

Resolve the problem from this Brunnian-core boundary if possible.

A. Prove Sawin's statement for every finite bijective degenerate X by proving
   Brunnian-core annihilation: for each finite X, construct one finite rack
   Y_0 such that every beta in B_{X,Y_0}(n) is X-trivial for all n.  You may
   instead give any other construction of one finite rack dominator.

B. Give an explicit finite degenerate bijective YBE table X and prove no
   finite rack dominates it by constructing the cofinal sequence above.  It is
   not enough to defeat one rack prefix, one detector product, bounded arity,
   or bounded deletion depth.

C. If neither A nor B can be proved, give only proof-grade progress: a
   theorem that strictly narrows the fully Brunnian-core case, with proof and
   exact remaining implication.  Clearly separate theorem/proof from finite
   evidence, heuristic, and unsupported claims.

Avoid returning only the nondegenerate theorem, contextual equivariance,
bounded-deletion reduction, or the statement that Brunnian braids are
plausible.  Those are already known.  The target is the fully
deletion-minimal X-Brunnian core.
