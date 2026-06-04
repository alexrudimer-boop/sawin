# Inert Observer Rack-Factor Audit

This generated audit isolates the simplest observer-factor
rackification theorem: a pointwise active rack factor plus inert
observer coordinates.

## Theorem

If maps o:X->I and q:X->Y to a finite rack Y satisfy o(u)=o(x), o(v)=o(y), and (q(u),q(v))=r_Y(q(x),q(y)) for every r_X(x,y)=(u,v), and x->(o(x),q(x)) is injective, then X^n is B_n-isomorphic to a B_n-invariant subset of Y^n x I^n with I^n fixed pointwise.  If the map is bijective onto Y x I on one letters, then ker rho^X_n = ker rho^Y_n for all n.

## Rows

| model | expectation | finite conditions | observer failure | rack failure | injectivity collision |
| --- | --- | --- | --- | --- | --- |
| `observer_product_s3_conjugation` | `passes: the S_3 rack coordinate is active and the E coordinate is inert` | `True` | `None` | `None` | `None` |
| `size4_affine_type_a_naive_pointwise` | `fails: Type A needs a sequential prefix-dependent gauge, not a pointwise rack factor` | `False` | `None` | `{'left': '(0, 0)', 'right': '(0, 0)', 'expected': '(1, 0)', 'actual': '(0, 1)'}` | `None` |
| `size4_type_b_flip_across_naive_tag` | `fails: mixed flip-across crossings route the tag observer rather than fixing it pointwise` | `False` | `{'left': "('T', 0)", 'right': "('P', 0)", 'expected': "('T', 'P')", 'actual': "('P', 'T')"}` | `{'left': "('T', 0)", 'right': "('T', 0)", 'expected': '(1, 0)', 'actual': '(0, 0)'}` | `None` |

## Conclusion

The inert observer theorem is a strict positive branch.  It covers the E x S_3 derived-route boundary example but is too narrow for Type A sequential gauges and Type B flip-across routing.  Those require the existing active-factor/transducer certificate framework.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-size5-6-everywhere-singular-core-search_ask_now.md`.
