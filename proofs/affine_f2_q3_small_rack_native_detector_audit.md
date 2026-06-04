# Affine F2^3 Small Rack Native Detector Audit

This generated audit tests individual small rack representatives
against the affine `F_2^3` survivor using tuple permutations on the
rack side and native affine transformations on the `X` side.

- max rack size: `4`;
- arity: `5`;
- state limit: `250000`;
- rack representatives: `28`;
- rejected by two-strand order: `20`;
- viable by two-strand order: `8`;
- obstructed viable rows: `6`;
- truncated viable rows: `1`;
- unobstructed nontruncated viable rows: `1`.

| rack index | size | order R | explored | detector image | X image | obstruction | truncated | word length |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |
| 8 | 3 | 3 | 154504 | 51840 | 77760 | True | False | 25 |
| 9 | 3 | 6 | 82941 | 12995 | 10047 | True | False | 12 |
| 12 | 4 | 6 | 87212 | 28530 | 10047 | True | False | 12 |
| 17 | 4 | 6 | 250000 | 250001 | 17192 | False | True | None |
| 18 | 4 | 6 | 87212 | 28530 | 10047 | True | False | 12 |
| 22 | 4 | 6 | 82941 | 12995 | 10047 | True | False | 12 |
| 23 | 4 | 6 | 87212 | 28530 | 10047 | True | False | 12 |
| 24 | 4 | 3 | 77760 | 77760 | 77760 | False | False | None |

## Promising Size-4 Rack

- rack index: `24`;
- rack size: `4`;
- kernel inclusion holds through checked arities: `True`;
- image orders match through checked arities: `True`.

Rack operation table rows:

```text
[0, 2, 3, 1]
[3, 1, 0, 2]
[1, 3, 2, 0]
[2, 0, 1, 3]
```

| n | joint image | detector image | X image | obstruction | truncated |
| ---: | ---: | ---: | ---: | --- | --- |
| 2 | 3 | 3 | 3 | False | False |
| 3 | 24 | 24 | 24 | False | False |
| 4 | 648 | 648 | 648 | False | False |
| 5 | 77760 | 77760 | 77760 | False | False |

## Conclusion

Among rack representatives of size at most 4, only those whose two-strand crossing order is divisible by 3 can possibly dominate the affine F_2^3 candidate. This audit tests the viable individual racks at arity 5 using native affine state for X. Obstructed rows give concrete detector-kernel braid words; unobstructed rows need larger arity or an all-n proof.
