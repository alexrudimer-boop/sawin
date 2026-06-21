# Framed C2 versus S3 arity-3 cover probe

The S3 conjugation rack covers the framed C2 Artin detector in arities 2 and 3 under the residual-image audit.  This strengthens the two-strand sanity check, but it remains finite evidence only; the Framed-to-Conjugation Cover Lemma still requires an all-arity proof.

## Setup

- solution: `A_C2`;
- detector: `S3^conj`;
- arities checked: `[2, 3]`;
- proves all-arity cover: `False`;

## Residual-image rows

| n | joint image | solution image | detector image | kernel size | kernel contains nonidentity | truncated | containment certified |
| ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| 2 | 12 | 4 | 12 | 1 | False | False | True |
| 3 | 279936 | 48 | 279936 | 1 | False | False | True |

## Boundary

This proves the containment

```text
K_n(S3^conj) subset K_n(A_C2)
```

for arity 2 and 3 only.  It does not prove the all-arity
Framed-to-Conjugation Cover Lemma.
