# Theoretical Review: Context-Signature Quotient Failure

Date: 2026-06-08.

## Verdict

The canonical quotient

```text
x -> (m_x,r_x)
```

is not automatically braided.  The proposed induction route through the
coarsest quotient whose fibres have identical two-sided context maps fails in
general.

This does not prove B, because the supplied failure is nondegenerate and is
therefore already covered by the derived-rack/guitar theorem.  It does,
however, remove one plausible canonical quotient strategy for A.

## Verified Local Certificate

The example is recorded and checked by:

```text
tools/run_context_signature_quotient_failure_certificate.py
proofs/context_signature_quotient_failure_certificate.json
proofs/context_signature_quotient_failure_certificate.md
```

The generated certificate verifies:

```text
YBE = True;
left_nondegenerate = True;
right_nondegenerate = True;
nondegenerate = True;
context-signature braided congruence = False.
```

The solution is the six-point linear skew-over-flip solution on

```text
X={0,1} x F_3
```

with matrices

```text
M_00 = [[0,1],[2,2]]
M_01 = [[0,1],[2,0]]
M_10 = [[0,2],[1,0]]
M_11 = [[0,2],[1,2]]
```

over `F_3`.

The certificate confirms:

```text
e_0 ~ctx f_0,
R(e_0,e_1) = (e_1,e_2),
R(f_0,e_1) = (e_2,f_0),
e_1 not ~ctx e_2.
```

Therefore `~ctx` is not a braided congruence.

## Consequence

The extension theorem remains useful when a suitable braided quotient
`pi:X->Z` is given, but `Z` cannot be chosen universally as
`X/~ctx`.

The next quotient-layer target is:

```text
replace ~ctx by the largest braided congruence contained in ~ctx,
then test whether that quotient gives a useful dominated layer while P_X
separates the remaining fibres.
```

## Related Correction: Active-Lift Pruning

The previously recorded "greatest fixed point" pruning operator for active
lifts is not a valid canonical existence theorem as stated.  The operator

```text
T(C)_p = {g in C_p :
  for all q in D_p and all h in C_q,
  g h g^{-1} in C_{lambda_p(q)}}
```

is not monotone with respect to inclusion of families `C_p`: enlarging
neighbour fibres adds compatibility obligations and can delete elements, while
shrinking fibres can make obligations disappear.  Therefore iterating from all
extensions can delete a lift that would be valid inside a smaller active
system.

The active-lift problem is still a finite constraint problem.  In the audited
families it is solved by a stronger explicit certificate: identity-extension
translations form singleton active sets.  The repo now records these as
active-lift existence certificates, not as proofs of nonempty fibres in a
canonical greatest fixed point.
