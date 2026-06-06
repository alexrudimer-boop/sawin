theoretical_asknow

This is a self-contained theoretical prompt.  Do not ask for code,
repository access, or further computations.  Be aggressive: try to fully
resolve Will Sawin's problem, not merely restate known partial routes.

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

Known closed cases and reductions.

1. If X is finite one-sided nondegenerate, the derived rack/guitar
   construction gives a finite rack with kernel equality in every arity.
   Do not spend the answer reproving this case except as a sublemma.

2. Involutive solutions, finite products of already dominated solutions, and
   braided quotients of already dominated solutions are dominated.

3. A genuinely degenerate solution cannot be solved by taking a finite
   nondegenerate braided cover: if Z -> X is a finite surjective braided-set
   morphism and Z is left-nondegenerate, then X is left-nondegenerate.
   Similarly on the right.

4. A coordinatewise quotient from a rack switch R_Y(a,b)=(a*b,a) to a general
   YBE solution forces the copied coordinate of X to be unchanged.  Thus a
   proof for genuinely degenerate X must use contextual readouts,
   finite-state decoders, or kernel-theoretic domination, not an ordinary
   coordinatewise rack quotient.

5. No single braid is a universal rack-invisible witness.  For every
   nontrivial beta in B_n, the faithful Artin action on F_n and residual
   finiteness of F_n produce a finite quotient G such that the conjugation
   rack of G detects beta.

Uniform formulation.

For a fixed finite X and every X-visible braid beta in B_n, let d_X(n,beta)
be the least size of a finite rack detecting beta.  Then X is dominated by
one finite rack if and only if

  sup_{rho^X_n(beta) != 1} d_X(n,beta) < infinity.

Equivalently, if no finite rack dominates X, then for an enumeration
R_1,R_2,... of finite rack isomorphism classes and P_m=R_1 x ... x R_m,
there must be cofinal witnesses:

  for every m there are n_m and beta_m in B_{n_m}
  with rho^{P_m}_{n_m}(beta_m)=1 but rho^X_{n_m}(beta_m) != 1.

Fixed-arity rack cofinality is available: for each fixed k and each finite
quotient representation theta:B_k -> H, there exists a finite rack Z such
that ker rho^Z_k <= ker theta.  Therefore a counterexample cannot live in
bounded arity; it must force failures at unbounded braid index.

Transparent deletion-core criterion.

For a rack Y, define Y^0=Y sqcup {0} by

  a*b = old a*b  for a,b in Y,
  0*b = b,
  a*0 = 0,
  0*0 = 0.

This is a rack.  Let T_2 be the two-element trivial rack, so ker rho^{T_2}_n
is the pure braid group P_n.  For beta in P_n and I subset {1,...,n}, write
partial_I beta for the braid obtained by deleting all strands outside I.

Deletion lemma: if beta in ker rho^{Y^0}_n, then

  partial_I beta in ker rho^Y_|I|

for every I.  Diagrammatically, strands outside I are colored by the
transparent color and then deleted.

Relative bounded-deletion theorem: suppose there exist a finite rack Y_0 and
an integer N such that, for every n and every

  beta in ker rho^{Y_0^0 x T_2}_n,

the implication

  rho^X_n(beta) != 1
    =>
  there is I with 2 <= |I| <= N and rho^X_|I|(partial_I beta) != 1

holds.  Then X is dominated by a finite rack.  Indeed, choose finite racks
Z_k for 2<=k<=N with ker rho^{Z_k}_k <= ker rho^X_k by fixed-arity
cofinality; then

  Y = Y_0^0 x T_2 x prod_{k=2}^N Z_k^0

dominates X.

Contrapositive target.  Therefore, if Sawin's statement is false for a
finite degenerate X, then for every finite rack prefix P_m and every deletion
cutoff N there must be a pure braid beta in some P_n such that

  rho^{P_m^0 x T_2}_n(beta)=1,
  rho^X_n(beta) != 1,

but every bounded X-deletion shadow is trivial:

  rho^X_|I|(partial_I beta)=1
  for every I with 2 <= |I| <= N.

Your task.

Try to resolve the full problem from this point.  Do one of the following.

A. Prove Sawin's statement for every finite bijective degenerate X.  The
   cleanest route would be to prove the bounded-deletion core criterion:
   for every finite degenerate X there exist Y_0 and N as above.  But you may
   use any other finite-state/contextual or kernel-theoretic construction of
   one finite rack dominator.

B. Give an explicit finite degenerate bijective YBE table X and prove no
   finite rack dominates it by constructing the cofinal rack-prefix,
   unbounded-deletion-support obstruction sequence above.  It is not enough
   to defeat one rack, one detector product, or one fixed deletion cutoff.

C. If neither A nor B can be proved, give only proof-grade progress: a
   theorem that strictly narrows the remaining degenerate case, with a proof
   and the exact remaining unproved implication.  Clearly separate theorem
   and proof from finite evidence, heuristic, and unsupported claims.

Avoid returning only the nondegenerate theorem, contextual equivariance, or
"Brunnian braids might matter."  Those are already known.  The goal is to
settle the bounded-deletion/core obstruction or replace it by a stronger
complete route.
