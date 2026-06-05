# Component Canonical Branching Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-04.

Prompt:

```text
Please answer self-containedly. We are working on Sawin's finite-rack domination problem for finite bijective set-theoretic Yang-Baxter solutions:

    Does every finite bijective solution X admit a finite rack Y with
    ker rho^Y_n <= ker rho^X_n for every braid group B_n?

Current endpoint:

- Known positive branches handle one-sided nondegenerate solutions, involutive solutions, flip-across/twisted unions, total quotient or active-factor certificates, periodic observer-rack factorizations, and several small/affine pressure examples.
- Fixed-arity rack cofinality is known, so a no-rack counterexample must have rack-prefix failures at arbitrarily large arities.
- A minimal counterexample outside the known branches and without proper crossing-closed subsolutions must be everywhere singular: every L_x and R_y is non-bijective.

We search for a size 5/6 everywhere-singular rigid core using coordinate arrays:

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

Equivalently, with

    C(u,P) = { (x,y) : L_x(y)=u and L_x L_y=P },
    B(u,P) = { v : L_u L_v=P },

Stage A requires |C(u,P)|=|B(u,P)|.

Stage B implemented so far:

1. Bucket-permutation variables.
   For each bucket b=(u,P), one variable Pi_b ranges over Bij(C_b,B_b).

2. Y2/Y3 support-pattern compilation.
   For each triple (x,y,z), enumerate patterns:

      (x,y)->a,
      (x,U[y,z])->b,
      (y,z)->c,
      (U[x,y],U[a,z])->U[b,c],
      (a,z)->t0,
      (b,c)->t0.

   Discard inconsistent patterns. A triple is satisfied iff selected bucket permutations extend at least one pattern.

3. Bucket-permutation GAC.
   It deletes whole bucket permutations with no support in some triple.

4. Exact bucket-domain column-singularity feasibility.
   For each column y, use DP over touched bucket permutations to test whether some compatible column assignment has a repeated value. If not, every completion makes that V-column bijective, so reject.

5. Exact bucket-domain non-involutivity feasibility.
   For each cell (x,y), with u=U[x,y], test whether some compatible value v=W_xy either has U[u,v] != x, or has U[u,v]=x and can force W_{u,v} != y. If no such witness is compatible anywhere, reject as forced involutive.

6. Aut(U) global state canonical rejection.
   Compute Aut(U) exactly. It acts on buckets and bucket permutations. A bucket-domain state D is rejected if its code is not minimal in its Aut(U)-orbit.

Regression facts:

- identity_3:
    bucket product 216 -> 1;
    Aut(U) order 6;
    column-singularity possible true;
    non-involutivity possible false;
    no non-involutive completion.

- dihedral_rack_3:
    bucket product 1 -> 1;
    Aut(U) order 6;
    column-singularity possible false;
    non-involutivity possible true;
    no column-singular non-involutive Stage B candidate.

- size4 affine Type A:
    bucket product 256 -> 256 after bucket-GAC;
    Aut(U) order 2;
    column-singularity possible true;
    non-involutivity possible true;
    bucket branching recovers the unique column-singular non-involutive completion in 3 nodes;
    known rack-dominated table.

Remaining missing layer from the previous answer:

- build exact remaining constraint hypergraph after bucket-GAC;
- decompose independent connected components;
- implement canonical augmentation using the current stabilizer Gamma(D), bucket orbits, and value orbits, instead of only global orbit-minimal state rejection.

Task:

Give the next implementable theorem/algorithm after the exact column + non-involutivity feasibility layer.

Please provide one of:

A. A precise construction of the remaining constraint hypergraph from compiled Y2/Y3 support patterns, column-singularity constraints, and non-involutivity witness constraints, including exact component decomposition and what global data must still be tracked across components.

B. A concrete canonical-augmentation algorithm using the current stabilizer Gamma(D): how to compute bucket orbits, selected bucket stabilizers, value orbits, and child states, with proof of completeness modulo Aut(U).

C. An exact component solver protocol for d=5,6: solve each component modulo its stabilizer, combine only component summaries, and preserve the global OR condition for non-involutivity.

D. A stronger exact pruning condition after bucket-GAC that is cheaper than full component decomposition.

E. A warning that component decomposition or stabilizer-orbit branching is not sound in the presence of column/non-involutive global constraints, with the corrected sound formulation.

Please be specific enough to translate into code and tests. Avoid general roadmaps.
```
