# Bucket-Permutation Stage B Frontier Prompt

Status: answered / GPT-5.5 Pro answered on 2026-06-04.

Answer summary:

- Use exact canonical bucket-permutation branching modulo Aut(U).
- Build the remaining constraint hypergraph after bucket-GAC.
- Decompose independent components before branching.
- Add exact bucket-domain column-singularity feasibility.
- Add exact bucket-domain non-involutivity feasibility.
- Use canonical augmentation: branch on bucket orbits under the current stabilizer and value orbits under the selected bucket stabilizer.
- The current implementation incorporated exact bucket column feasibility, exact non-involutivity feasibility, and global Aut(U) state rejection; component decomposition and full stabilizer-orbit branching remain the next target.

Prompt:

```text
Please answer self-containedly. We are working on Sawin's finite-rack domination problem for finite bijective set-theoretic Yang-Baxter solutions:

    Does every finite bijective solution X admit a finite rack Y with
    ker rho^Y_n <= ker rho^X_n for every braid group B_n?

Current endpoint:

- Known positive branches handle one-sided nondegenerate solutions, involutive solutions, flip-across/twisted unions, total quotient or active-factor certificates, periodic observer-rack factorizations, and several small/affine pressure examples.
- Fixed-arity rack cofinality is known, so a genuine no-rack counterexample must have rack-prefix failures at arbitrarily large arities.
- A minimal counterexample outside the known branches and without proper crossing-closed subsolutions must be everywhere singular: every coordinate map L_x and R_y is non-bijective.

We are implementing an exhaustive size 5/6 search for an everywhere-singular rigid core using coordinate arrays:

    U[x,y]=L_x(y),
    V[x,y]=R_y(x),
    r(x,y)=(U[x,y],V[x,y]).

YBE in U,V is:

    (Y1) U[U[x,y], U[V[x,y],z]] = U[x, U[y,z]]

    (Y2) V[U[x,y], U[V[x,y],z]]
         = U[V[x,U[y,z]], V[y,z]]

    (Y3) V[V[x,y], z]
         = V[V[x,U[y,z]], V[y,z]]

Stage A U-only gate:

1. every row L_x is singular;
2. U is globally balanced: every symbol appears exactly d times among all U[x,y];
3. U is canonical under simultaneous relabelling;
4. U satisfies the Y1+bijection multiset factorization law:

      for every u,

      multiset{ L_x L_y : L_x(y)=u }
        =
      multiset{ L_u L_v : v in X }.

Equivalently, for every transformation P:

    C(u,P) = { (x,y) : L_x(y)=u and L_x L_y=P },
    B(u,P) = { v : L_u L_v=P },

and Stage A requires |C(u,P)|=|B(u,P)|.

We implemented two Stage B solvers after this MF checkpoint.

1. Cell-level GAC:

Variables W_xy=V[x,y] with domains

    D_xy = B(U[x,y], L_x L_y).

Bucket Hall filtering enforces the bijections C(u,P)->B(u,P). Dynamic Y2/Y3 support GAC uses:

    W_xy=a, W_{x,U[y,z]}=b, W_yz=c

implies

    W_{U[x,y],U[a,z]}=U[b,c],
    W_{a,z}=W_{b,c}.

2. Bucket-permutation GAC:

For each bucket b=(u,P), introduce one variable Pi_b whose domain is Bij(C_b,B_b).
Compile every triple (x,y,z) into support patterns over bucket permutations:

    (x,y)->a,
    (x,U[y,z])->b,
    (y,z)->c,
    (U[x,y],U[a,z])->U[b,c],
    (a,z)->t0,
    (b,c)->t0.

Discard inconsistent patterns. A triple is satisfied iff the chosen bucket permutations extend at least one remaining pattern. We enforce generalized arc consistency over whole bucket-permutation domains, then branch on bucket permutations.

Current regression facts from the implementation:

- identity_3:
    bucket domains product 216 -> 1;
    bucket-permutation GAC forces the unique V completion;
    it is involutive, so no non-involutive candidate.

- dihedral rack_3:
    bucket domains product 1 -> 1;
    it is non-involutive but not column-singular, so it is not an everywhere-singular Stage B candidate.

- size-4 affine Type A pressure row:
    bucket domains product 256 -> 256 under bucket-GAC;
    bucket-permutation branching recovers the unique column-singular non-involutive completion in 3 nodes;
    Aut(U) has order 2 and canonical-state rejection rejects 0 branches on this regression;
    that completion is the known rack-dominated affine Type A table.

- exact size-3 row-catalogue Stage A has one canonical MF-valid U and no non-involutive Stage B completion.

- row-catalogue size-4 budget tests up to 1,000,000 Stage A nodes still hit only the identity-type MF-valid canonical U before truncation; the known affine Type A U is included separately as a regression.

Task:

Give the next decisive narrowing after bucket-permutation GAC. I want something that can become code/tests or a finite theorem. Avoid broad roadmaps.

Please provide one of the following:

A. A stronger Stage A U-only constraint beyond multiset factorization, derived from Y2/Y3 plus bijectivity but not requiring V search.

B. A bucket-permutation-level theorem: for example, a condition under which a non-singleton bucket-GAC fixed point forces a quotient, subsolution, observer, involutivity, or observer-rack factorization.

C. A stronger canonicalization/automorphism pruning method beyond the current Aut(U) orbit-minimal bucket-domain-state rejection, with precise correctness, suitable for d=5,6.

D. A proof that no size-5 everywhere-singular MF-valid U can have a column-singular non-involutive Stage B completion.

E. A concrete size-5 or size-6 U or full X table that should be tested next and why it is a serious rigid-core candidate.

F. If none of these is currently provable, state the sharpest implementable next computation, including exact stopping criteria and what output would be decisive.
```
