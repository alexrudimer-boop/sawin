# Regular-module cover candidate probe

The regular-module candidate passes the feasible residual checks for C2 and C3 and the B2 order check for S3.  This is evidence for the candidate only; the regular-module Artin longitude Fox separation lemma remains the proof obligation.

## Scope

- candidate: `C_reg(G)=F_2[G] semidirect G`;
- proves regular-module Fox separation: `False`;
- frontier artifact: `proofs/regular_module_framed_to_conjugation_cover_theorem.md`;

## Rows

### C2 arity 2

- kind: `residual`;
- group order: `2`;
- detector group order: `8`;
- joint image size: `4`;
- solution image size: `4`;
- detector image size: `4`;
- kernel size: `1`;
- kernel contains nonidentity: `False`;
- truncated: `False`;
- containment certified: `True`;

### C2 arity 3

- kind: `residual`;
- group order: `2`;
- detector group order: `8`;
- joint image size: `48`;
- solution image size: `48`;
- detector image size: `48`;
- kernel size: `1`;
- kernel contains nonidentity: `False`;
- truncated: `False`;
- containment certified: `True`;

### C3 arity 2

- kind: `residual`;
- group order: `3`;
- detector group order: `24`;
- joint image size: `12`;
- solution image size: `6`;
- detector image size: `12`;
- kernel size: `1`;
- kernel contains nonidentity: `False`;
- truncated: `False`;
- containment certified: `True`;

### S3 arity 2

- kind: `b2_order`;
- group order: `6`;
- detector group order: `384`;
- solution sigma order: `12`;
- detector sigma order: `24`;
- B2 containment by order: `True`;

## Boundary

This probe does not prove the regular-module cover.  It only pins
small positive instances and keeps the Fox-separation proof
obligation explicit.
