# Periodic Observer-Rack Factorization Audit

This generated audit records the all-arity positive mechanism
underlying the observer-product and affine tetrahedral examples.

## Theorem

Name: `Periodic observer-rack factorization`.

Data:

- finite bijective YBE solution X;
- finite rack Y;
- period d >= 1;
- finite rack-output state set Q with initial states q_r for r in Z/d;
- finite observer state set P with initial states p_r for r in Z/d;
- transition maps delta:Q x X -> Q and Delta:P x X -> P;
- output maps omega:Q x X -> Y and nu:P x X -> I;

Local equations:

- `delta(delta(q,x),y)=delta(delta(q,u),v)`;
- `r_Y(omega(q,x), omega(delta(q,x),y))=(omega(q,u), omega(delta(q,u),v))`;
- `Delta(Delta(p,x),y)=Delta(Delta(p,u),v)`;
- `(nu(p,x), nu(Delta(p,x),y))=(nu(p,u), nu(Delta(p,u),v))`;

Conclusion: If the left-to-right code Phi_n:X^n -> Y^n x I^n built from the n mod d initial states is injective for every n, then ker rho^Y_n <= ker rho^X_n for every n.  If the Y-output projection is surjective in every arity, then the kernels are equal.

Proof steps:

- The first two local equations give B_n-equivariance of the Y-output coordinate.;
- The last two local equations give B_n-invariance of the observer coordinate.;
- A Y-trivial braid fixes the Y-output and the observer output of every X-word.;
- All-length injectivity of Phi_n forces the braid to fix every X-word.;
- Surjectivity of the Y-output gives the reverse kernel inclusion.;

## Examples

| example | period | rack | observer | status | artifact |
| --- | --- | --- | --- | --- | --- |
| `observer_product_s3_conjugation` | `1` | `S_3 conjugation rack` | `E={0,1} coordinate` | `kernel equality` | `proofs/observer_product_derived_route_boundary.md` |
| `affine_f2_q3_tetrahedral` | `3` | `four-element tetrahedral Alexander rack` | `n invariant F_2 bits r_i=sum_{j<i}(a_j+c_j)+a_i+b_i` | `kernel equality after shifted linear coordinates` | `proofs/affine_f2_q3_full_tetrahedral_conjugacy_audit.md` |
| `inert_observer_pointwise_subcase` | `1` | `arbitrary finite rack Y` | `pointwise observer o:X->I fixed coordinatewise` | `strict subcase of the periodic theorem` | `proofs/inert_observer_rack_factor_audit.md` |

## Relationship To Sawin

Kernel inclusion can hold without a finite symbolic left-to-right reconstruction.  Periodic observer-rack factorization is therefore a positive branch, not an equivalent reformulation of Sawin.

For proposed finite data, the local equations are finite.  All-length injectivity is checked by the usual pair automaton for left-to-right transducer outputs.

## Next Computation

Search sizes 5 and 6 for everywhere-singular rigid-core candidates, applying quotient/subsolution/observer/flip-across/minimal-image filters before any rack-prefix pressure computation.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-size5-6-everywhere-singular-core-search_ask_now.md`.
