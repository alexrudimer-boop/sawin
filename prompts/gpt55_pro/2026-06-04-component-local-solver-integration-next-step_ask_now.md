# Component-Local Solver Integration Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-04.

Prompt:

```text
Please answer self-containedly. We are working on Sawin's finite-rack domination problem for finite bijective set-theoretic Yang-Baxter solutions:

    Does every finite bijective solution X admit a finite rack Y with
    ker rho^Y_n <= ker rho^X_n for every braid group B_n?

Current endpoint:

- Known positive branches handle one-sided nondegenerate solutions, involutive solutions, flip-across/twisted unions, quotient/active-factor certificates, periodic observer-rack factorizations, and several small/affine pressure examples.
- Fixed-arity rack cofinality is known, so a no-rack counterexample must have rack-prefix failures at arbitrarily large arities.
- A minimal counterexample outside the known branches and without proper crossing-closed subsolutions must be everywhere singular: every L_x and R_y is non-bijective.

We are implementing an exhaustive size 5/6 search for an everywhere-singular rigid core using coordinate arrays U,V.

Stage A is implemented:

- enumerate singular balanced U rows;
- impose canonicalization under relabelling;
- impose the U-only Y1+bijection multiset factorization law:

      multiset{ L_x L_y : L_x(y)=u }
        =
      multiset{ L_u L_v : v in X }.

Stage B implemented:

1. Bucket variables:
   For each bucket b=(u,P), Pi_b ranges over Bij(C_b,B_b).

2. Compiled Y2/Y3 triple patterns:

      (x,y)->a,
      (x,U[y,z])->b,
      (y,z)->c,
      (U[x,y],U[a,z])->U[b,c],
      (a,z)->t0,
      (b,c)->t0.

3. Bucket-permutation GAC over the compiled Y2/Y3 relations.

4. Exact bucket-domain column-singularity feasibility.

5. Exact bucket-domain non-involutivity feasibility.

6. Exact compiled relation hypergraph:
   vertices are unresolved buckets; hyperedges come from surviving Y2/Y3 patterns, compiled column-singularity patterns, and compiled non-involutivity witness patterns.

7. Current-stabilizer branch audit:
   compute Aut(U), induced bucket-permutation actions, current stabilizer Gamma(D), component orbits, selected component, selected bucket orbit, and selected bucket-permutation value orbit representatives.

Regression facts:

- identity_3:
    bucket product 216 -> 1;
    column-singularity possible true;
    non-involutivity possible false;
    stabilizer branch audit locally_consistent false.

- dihedral_rack_3:
    bucket product 1 -> 1;
    column-singularity possible false;
    non-involutivity possible true;
    stabilizer branch audit locally_consistent false.

- size4 affine Type A:
    bucket product 256 -> 256 after bucket-GAC;
    compiled relation counts YBE/column/noninv = 156/16/24;
    hypergraph edge counts YBE/column/noninv = 19/4/4;
    one component of size 8;
    Aut(U) order 2;
    current stabilizer order 2;
    selected component is buckets 0..7;
    selected bucket is 0;
    selected bucket orbit size 2;
    selected value representatives are (0,1);
    existing bucket search recovers the unique column-singular non-involutive completion in 3 nodes.

Remaining missing implementation:

- The branch audit computes the next canonical branch but the actual Stage B search still uses simpler smallest-bucket branching plus global canonical rejection.
- There is no component-local solution enumerator yet.
- There is no component-summary combiner with the global OR condition for non-involutivity.

Task:

Give the next implementable step after the current stabilizer branch audit.

Please provide one of:

A. Minimal code-level changes to replace Stage B branching with Gamma(D)-canonical branching while preserving current search outputs.

B. A component-local enumerator design that uses the compiled relation lists and emits local solution representatives plus noninv flags.

C. A safe hybrid: keep global search but choose branches using the stabilizer branch audit and value-orbit representatives, with a proof this remains complete modulo Aut(U).

D. A stricter test plan before changing the search: additional regression U arrays or artificial domain states that verify component orbits and value orbits.

Avoid broad roadmaps. Give pseudocode and invariants suitable for direct implementation in the existing Python bucket-domain representation.
```
