# Production Component Stage B Size 5/6 Prompt

Status: partially_answered / implemented locally as the production component
Stage B frontier audit; no longer the prompt to answer now.

Prompt:

```text
Please answer self-containedly. We are working on Sawin's finite-rack domination problem for finite bijective set-theoretic Yang-Baxter solutions:

    Does every finite bijective solution X admit a finite rack Y with
    ker rho^Y_n <= ker rho^X_n for every braid group B_n?

Current endpoint:

- Known positive branches handle one-sided nondegenerate solutions, involutive solutions, flip-across/twisted unions, quotient/active-factor certificates, periodic observer-rack factorizations, and several small/affine pressure examples.
- Fixed-arity rack cofinality is known, so a no-rack counterexample must have rack-prefix failures at arbitrarily large arities.
- A minimal counterexample outside known branches and without proper crossing-closed subsolutions must be everywhere singular: every L_x and R_y is non-bijective.

Implemented search layers:

Stage A:
- enumerate singular balanced U rows;
- canonicalize under relabelling;
- impose Y1+bijection multiset factorization:

      multiset{ L_x L_y : L_x(y)=u }
        =
      multiset{ L_u L_v : v in X }.

Stage B:
- bucket-permutation variables Pi_b in Bij(C_b,B_b);
- compiled Y2/Y3 support patterns;
- bucket-permutation GAC over YBE relations;
- exact compiled column-singularity relations;
- relation-level GAC over YBE + column relations;
- exact non-involutivity witness patterns as a global OR;
- exact relation hypergraph from YBE, column, and noninv witness scopes;
- current-stabilizer branch audit using Gamma(D), component orbits, bucket orbits, and bucket-permutation value orbits;
- component-local solver audit that enumerates each connected component and combines components by product with the global noninv OR.

Regression facts:

- identity_3:
    relation-GAC reduces bucket product 216 -> 1;
    column singularity possible true;
    non-involutivity witness impossible;
    component solver accepted count 0 for rigid-core search.

- dihedral_rack_3:
    relation-GAC sees 0 column patterns;
    locally_consistent false for everywhere-singular Stage B;
    component solver accepted count 0.

- size4 affine Type A:
    relation-GAC product 256 -> 256;
    YBE/column pattern counts 156/16;
    exact noninv witness count 24;
    one component of size 8;
    component solver local solution counts (2), noninv counts (1);
    global solution count 2, global noninv count 1, accepted count 1;
    bucket search finds the unique column-singular non-involutive completion in 3 nodes.

Remaining implementation gap:

- The component-local solver is currently an audit. It counts local solutions and noninv flags, but production Stage B enumeration still uses global recursive bucket branching.
- The size 5/6 frontier has not yet been run with the component solver as the production engine.

Task:

Give the next exact implementation step.

Please provide one of:

A. A code-level algorithm to turn the component solver audit into production Stage B enumeration that emits V completions, with max-node/max-example truncation semantics.

B. A safe bounded size-5/6 execution plan using the current component solver audit before full V emission, including stopping criteria and artifact format.

C. A stronger component-local canonicalization method: solve each component modulo its setwise stabilizer and combine representatives without losing full-table isomorphism classes.

D. A warning that the component solver audit still misses some relation coupling, with a concrete counterexample pattern and the corrected scope.

Avoid broad roadmaps. Give pseudocode and invariants suitable for direct implementation in the existing Python bucket-domain representation.
```
