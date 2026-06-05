# Stage B GAC Frontier Next-Step Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-04.

Prompt:

```text
Please answer self-containedly. We are working on Sawin's finite-rack domination problem for finite bijective set-theoretic Yang-Baxter solutions:

    Does every finite bijective solution X admit a finite rack Y with
    ker rho^Y_n <= ker rho^X_n for every braid group B_n?

Current endpoint:

- Known positive branches handle one-sided nondegenerate solutions, involutive solutions, flip-across/twisted unions, total quotient or active-factor certificates, periodic observer-rack factorizations, and several small/affine pressure examples.
- Fixed-arity rack cofinality is known: for fixed n, any finite B_n quotient is refined by a finite conjugation rack detector. Therefore a genuine no-rack counterexample must have rack-prefix failures at arbitrarily large arities.
- A minimal counterexample outside the known branches and with no proper crossing-closed subsolution must be everywhere singular:

      every L_x and every R_y is non-bijective,

  where r(x,y)=(L_x(y),R_y(x)).

We are implementing an exhaustive size 5/6 search for an everywhere-singular rigid core using coordinate arrays:

    U[x,y]=L_x(y),
    V[x,y]=R_y(x),
    r(x,y)=(U[x,y],V[x,y]).

The YBE identities are:

    (Y1) U[U[x,y], U[V[x,y],z]] = U[x, U[y,z]]

    (Y2) V[U[x,y], U[V[x,y],z]]
         = U[V[x,U[y,z]], V[y,z]]

    (Y3) V[V[x,y], z]
         = V[V[x,U[y,z]], V[y,z]]

Stage A U-only gate:

1. Each row L_x is singular.
2. U is globally balanced: every symbol u occurs exactly d times among all U[x,y].
3. U is canonical under simultaneous relabelling.
4. U satisfies the Y1+bijection multiset factorization law:

      for every u,

      multiset{ L_x L_y : L_x(y)=u }
        =
      multiset{ L_u L_v : v in X }.

Equivalently, for every transformation P:X->X:

    C(u,P) = { (x,y) : L_x(y)=u and L_x L_y=P },
    B(u,P) = { v : L_u L_v=P },

and Stage A requires

    |C(u,P)| = |B(u,P)|

for all u,P.

Stage B now treats W_xy=V[x,y] as finite-domain variables:

    D_xy = B(U[x,y], L_x L_y).

For each bucket (u,P), the variables W_c for c in C(u,P) must form a bijection C(u,P)->B(u,P). We enforce exact Hall filtering inside each bucket.

For each triple (x,y,z), write:

    A = W_xy,
    B = W_{x,U[y,z]},
    C = W_yz,
    u = U[x,y].

Then candidate values A=a, B=b, C=c imply:

    (Y2-imp) W_{u,U[a,z]} = U[b,c],
    (Y3-imp) W_{a,z} = W_{b,c}.

We implemented exact generalized arc consistency for these dynamic triple constraints:

For every triple, every dynamically referenced cell r, and every value s in D_r, keep r=s only if there exist

    a in D_xy,
    b in D_{x,U[y,z]},
    c in D_yz,
    t0 in X

such that the assignments

    W_xy=a,
    W_{x,U[y,z]}=b,
    W_yz=c,
    W_{u,U[a,z]}=U[b,c],
    W_{a,z}=t0,
    W_{b,c}=t0

are all domain-consistent and assign r either to s or not at all. If no such support exists, delete s.

Current regression facts:

- Identity solution on 3 points: GAC leaves 9 variables with domain size 3.
- Dihedral rack on 3 points: GAC forces all 9 V-values and verifies Y2/Y3.
- Size-4 affine Type A pressure row: Stage A gives 8 two-cell buckets. GAC leaves all domains of size 2, and exact Stage B has exactly one non-involutive completion, the known rack-dominated affine table.
- Exact size-3 row-catalogue Stage A has one canonical MF-valid U and no non-involutive Stage B completion.
- A small budgeted size-4 Stage A sample currently only hits an identity-type U; the known affine Type A table is added separately as a regression.

Task:

Give the next decisive narrowing after exact Stage B GAC. I want something that can become code/tests or a finite theorem. Avoid broad roadmaps.

Please provide one of the following:

A. A stronger U-only or bucket-only consequence of Y2/Y3 plus bucket bijections, analogous to the Stage A multiset factorization law, so we can reject U arrays before GAC/backtracking.

B. A theorem about GAC fixed points: for example, conditions under which a non-singleton GAC fixed point forces a proper quotient, proper crossing-closed subsolution, invariant observer, involutivity, or an observer-rack factorization.

C. A proof that no size-5 everywhere-singular, MF-valid, GAC-consistent U can admit a non-involutive V completion.

D. An exact branching/search invariant that makes the Stage B GAC backtracking dramatically smaller for d=5,6, with a correctness argument.

E. An explicit finite candidate U or full table X of size 5 or 6 that should be tested next, ideally everywhere singular, non-involutive, quotient/subsolution/observer rigid, and not obviously rackified.

If none of A-E is currently provable, state the sharpest implementable next computation and explain what output would be decisive.
```
