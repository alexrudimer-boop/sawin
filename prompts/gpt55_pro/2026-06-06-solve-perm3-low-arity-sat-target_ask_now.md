# Solve the first perm3 low-arity finite-rack SAT target

The \(|X|=3\) permutation-form branch is now reduced:

- for every \(r_{\sigma,\tau}(x,y)=(\sigma(y),\tau(x))\) with
  \(\sigma\tau=\tau\sigma\), every principal bad endpoint pair in arity
  \(n\ge4\) is separated by the explicit \(q=3\) detector
  \(D_{\sigma,\tau}\);
- invisible pairs for this detector family occur only in finite low arity;
- the shortest invisible pair occurs in arity \(2\).

Do not reprove the high-arity theorem. Attack the finite SAT target.

## Target instance

Use:

```text
X = {0,1,2}
YBE table = [3,6,0,4,7,1,5,8,2]
partition = [0,0,0]
arity n = 2
start word = [0,0]
end word = [0,0]
start position = 0
end position = 1
endpoint e  = [epsilon,0,0]
endpoint e' = [0,0,epsilon]
```

This pair is quotient-equivalent for the indiscrete partition and not
endpoint-\(T\)-equivalent in \(X\). It is invisible to the high-arity detector
\(D_{\sigma,\tau}\), whose endpoint values are both \(0\).

## Task

Run or solve the full finite-rack SAT detector problem for this endpoint pair.

Return one of:

1. A positive finite rack detector certificate:

```json
{
  "type": "finite_rack_detector",
  "ybe_table": [3,6,0,4,7,1,5,8,2],
  "endpoint_pair": {
    "e": {"prefix": [], "letter": 0, "suffix": [0]},
    "eprime": {"prefix": [0], "letter": 0, "suffix": []}
  },
  "monoid_quotient": {
    "size": "K",
    "identity": "id",
    "mul": [[ "... multiplication table ..." ]],
    "generator_images": ["m0", "m1", "m2"]
  },
  "rack": {
    "size": "q",
    "table": [[ "... rack operation table ..." ]]
  },
  "alpha": [
    {"p": "p", "x": "x", "s": "s", "value": "q_element"}
  ],
  "endpoint_values": ["alpha_e", "alpha_eprime"],
  "separates": true
}
```

2. A bounded negative certificate:

```json
{
  "type": "bounded_no_detector",
  "bounds": {
    "monoid_size_max": "K",
    "rack_size_max": "qmax"
  },
  "monoid_catalog_hash": "...",
  "rack_catalog_hash": "...",
  "unsat_proofs": [
    {
      "monoid_id": "...",
      "rack_size": "q",
      "proof_format": "LRAT/DRAT/SMT/parity-DSU",
      "proof": "..."
    }
  ],
  "classification": "bounded_no_detector_not_residual"
}
```

3. A parametric collapse proof, if one exists.

Do not call a bounded negative result residual collapse. A true residual
collapse proof must quantify over every finite rack detector.
