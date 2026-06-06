theoretical_asknow

This is a self-contained theoretical prompt.  Do not ask for code,
repository access, or further computations.  Try to resolve the remaining
mathematical problem.

Problem, due to Will Sawin.

Let X be a finite bijective set-theoretic solution of the Yang-Baxter
equation, with braid actions

  rho^X_n : B_n -> Sym(X^n).

A finite rack Y is viewed as the set-theoretic solution

  R_Y(a,b) = (a*b, a).

Question.  Does every finite bijective set-theoretic YBE solution X admit a
finite rack Y, independent of n, such that

  ker rho^Y_n <= ker rho^X_n

for every n?

Do not spend the answer reproving the standard nondegenerate case.  That case
is closed: for every finite one-sided nondegenerate solution, the derived
rack/guitar construction gives kernel equality in all arities.  Involutive
solutions, product closures, and braided quotients of already dominated
solutions are also closed.

The remaining problem is genuinely degenerate finite bijective solutions.

Known failed shortcuts for degenerate X.

1. Nondegenerate cover shortcut fails.
   If p:Z -> X is a finite surjective braided-set morphism and Z is
   left-nondegenerate, then X is left-nondegenerate; similarly on the right.
   Hence a genuinely degenerate X cannot be solved by taking a finite
   nondegenerate cover Z and pushing the derived-rack domination down.

2. Coordinatewise rack quotient shortcut fails.
   A coordinatewise quotient from a rack switch R_Y(a,b)=(a*b,a) to X forces
   the copied coordinate in X to be unchanged.  With this convention it forces
   rho_y(x)=x for all x,y; with the opposite convention it forces the left
   action to be trivial.  Thus a proof for degenerate X must use contextual
   readouts, finite-state decoders, or a kernel-theoretic detector, not an
   ordinary coordinatewise rack quotient.

3. One-braid obstruction fails.
   No individual braid is invisible to all finite racks.  If beta in B_n is
   nontrivial, the faithful Artin action on F_n and residual finiteness of
   F_n produce a finite quotient G such that the conjugation rack of G detects
   beta.

Equivalent uniform formulation.

For fixed finite X and each X-visible braid beta in B_n, let d_X(n,beta) be
the least size of a finite rack detecting beta.  Then X is dominated by a
finite rack if and only if

  sup_{rho^X_n(beta) != 1} d_X(n,beta) < infinity.

If this supremum is infinite, then, for an enumeration R_1,R_2,... of finite
rack isomorphism classes and P_m=R_1 x ... x R_m, there must be cofinal
witnesses:

  for every m there exist n_m and beta_m in B_{n_m}
  such that rho^{P_m}_{n_m}(beta_m)=1
  but rho^X_{n_m}(beta_m) != 1.

Moreover fixed-arity rack cofinality means a genuine counterexample cannot be
confined to bounded arity: for every m and every cutoff N, there must be such
a witness with n_m>N.

Possible positive route.

A contextual rack detector schema has the form

  (M,Q,alpha),       alpha : M x X x M -> Q,

where M is a finite quotient of the structure monoid and Q is a finite rack.
The local contextual T- and R-relations imply all-arity braid-equivariant
readouts

  Phi_n(x_1,...,x_n)_i =
    alpha([x_1...x_{i-1}], x_i, [x_{i+1}...x_n]).

If finitely many such schemas separate every nontrivial detector-kernel
motion of X^n in every arity, the product of their finite rack targets
dominates X.

The missing bounded-core implication is:

  beta in ker rho^Y_n and rho^X_n(beta) != 1
    =>
  some moved orbit contains a bounded contextual endpoint core separated by a
  finite rack detector.

Potential negative route.

Brunnian or high-context pure braid elements can have all bounded deletion
shadows trivial while remaining nontrivial.  But a negative answer requires
more than one Brunnian miss against one detector: it requires the cofinal
rack-prefix obstruction sequence above for one explicit finite degenerate X.

Your task.

Give the strongest rigorous answer you can for the genuinely degenerate case.
Do one of the following:

A. Prove Sawin's statement for all finite bijective degenerate X by giving a
   finite-state/contextual rack detector theorem, a bounded-core theorem, or a
   different construction of one finite rack Y independent of n.

B. Give an explicit finite degenerate bijective YBE table X and prove no finite
   rack dominates it by constructing the cofinal rack-prefix obstruction
   sequence.  It is not enough to defeat one chosen rack or one detector
   product.

C. If neither A nor B can be proved, give only proof-grade progress: a precise
   theorem that strictly narrows the degenerate case, together with the exact
   remaining unproved implication.  Clearly separate theorem/proof from finite
   evidence, heuristic, and unsupported claims.

Avoid returning only the nondegenerate/guitar theorem, the involutive theorem,
or the fact that Brunnian elements are plausible.  Those are already known and
do not resolve the degenerate case.
