# Stabilizer Component Solver Prompt

Status: answered / GPT-5.5 Pro answered on 2026-06-04.

Answer summary:

- Compile Y2/Y3, column singularity, and non-involutivity into bucket-pattern relations.
- Include column-singularity hyperedges and non-involutivity witness hyperedges; component decomposition is unsound without them.
- Compute the current stabilizer Gamma(D) at each branch state.
- Branch by component orbit, then bucket orbit inside the chosen component, then value orbit under the selected bucket stabilizer.
- Component-local solutions can be combined by product, with the only global condition that at least one component realizes a non-involutivity witness.

Implementation response:

- The current repository now has compiled relation hypergraph auditing and current-stabilizer branch auditing.
- The affine Type A regression has one component of size 8 and root stabilizer order 2; the selected bucket is 0 with value representatives (0, 1).
- Full component-local solution enumeration and integration into Stage B branching remain the next implementation target.

Prompt:

```text
Please answer self-containedly. We are working on Sawin's finite-rack domination problem for finite bijective set-theoretic Yang-Baxter solutions:

    Does every finite bijective solution X admit a finite rack Y with
    ker rho^Y_n <= ker rho^X_n for every braid group B_n?

Current endpoint:

- Known positive branches handle one-sided nondegenerate solutions, involutive solutions, flip-across/twisted unions, total quotient or active-factor certificates, periodic observer-rack factorizations, and several small/affine pressure examples.
- Fixed-arity rack cofinality is known, so a no-rack counterexample must have rack-prefix failures at arbitrarily large arities.
- A minimal counterexample outside the known branches and without proper crossing-closed subsolutions must be everywhere singular: every L_x and R_y is non-bijective.

We are implementing an exhaustive size 5/6 search for an everywhere-singular rigid core using coordinate arrays:

    U[x,y]=L_x(y),
    V[x,y]=R_y(x),
    r(x,y)=(U[x,y],V[x,y]).

Stage A U-only gate:

1. every row L_x is singular;
2. U is globally balanced;
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
   For each triple (x,y,z), compile patterns:

      (x,y)->a,
      (x,U[y,z])->b,
      (y,z)->c,
      (U[x,y],U[a,z])->U[b,c],
      (a,z)->t0,
      (b,c)->t0.

   A triple is satisfied iff selected bucket permutations extend at least one compiled pattern.

3. Bucket-permutation GAC.
   It deletes whole bucket permutations with no support in some triple.

4. Exact bucket-domain column-singularity feasibility.
   For each column y, use bucket-domain DP to test whether some compatible column assignment has a repeated value.

5. Exact bucket-domain non-involutivity feasibility.
   Test whether some compatible cell assignment can witness r^2 != id.

6. Aut(U) global state canonical rejection.
   Compute Aut(U) exactly. It acts on buckets and bucket permutations. Reject a bucket-domain state D if its code is not minimal in its Aut(U)-orbit.

7. Compiled relation hypergraph audit.
   After bucket-GAC, compile:

   - surviving Y2/Y3 triple patterns;
   - exact column-singularity patterns;
   - exact non-involutivity witness patterns.

   Build hyperedges from these relation scopes on unresolved buckets and compute connected components.

Regression facts:

- identity_3:
    bucket product 216 -> 1;
    column-singularity possible true;
    non-involutivity possible false;
    compiled relation hypergraph locally_consistent false.

- dihedral_rack_3:
    bucket product 1 -> 1;
    column-singularity possible false;
    non-involutivity possible true;
    compiled relation hypergraph locally_consistent false.

- size4 affine Type A:
    bucket product 256 -> 256 after bucket-GAC;
    Aut(U) order 2;
    compiled relation counts YBE/column/noninv = 156/16/24;
    hypergraph edge counts YBE/column/noninv = 19/4/4;
    hypergraph has one connected component of size 8;
    bucket branching recovers the unique column-singular non-involutive completion in 3 nodes;
    known rack-dominated table.

Remaining missing layer:

- implement the actual component solver using the compiled relation hypergraph;
- compute current stabilizer Gamma(D) at each branch state;
- branch by component orbit, bucket orbit, and bucket-permutation value orbit;
- combine component solutions while preserving the global OR condition for non-involutivity.

Task:

Give the next implementable algorithm and test plan for this exact current frontier.

Please provide one of:

A. A concrete component-local solver protocol that consumes compiled relation pattern lists and bucket domains, emits local solution representatives plus a noninv flag, and combines components exactly.

B. A precise current-stabilizer canonical augmentation algorithm in code-level terms: state representation, Gamma(D), component orbits, bucket orbits, value orbits, and child-domain construction.

C. A minimal first implementation slice that improves the current solver while being easy to test on identity_3, dihedral_rack_3, and affine Type A.

D. A warning that the current compiled-relation hypergraph audit is still too coarse for sound component solving, with the corrected relation scope.

Avoid broad roadmaps. Give pseudocode and invariants suitable for direct implementation in Python for d=5,6.
```
