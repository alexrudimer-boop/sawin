# Non-permutation size-three higher-arity frontier

Date: 2026-06-06

This note records the post-q=5 frontier for the non-permutation
\(|X|=3\) branch.  It started from the reported closure of the arity-3
endpoint gate in `proofs/nonperm3_arity3_q5_resolution.md`; the full local
detector-basis reconstruction and later arity-4 stabilizer audit are recorded
below.

## Status after q=5

Finite endpoint-gate result:

```text
non-permutation |X|=3, arity 3
principal bad endpoint pairs:       37692
finite rack separated:              37692
remaining unresolved candidates:        0
```

Together with the arity-2 checkpoint, this closes the fixed-arity
endpoint-gate batches through arity 3 for non-permutation size-three
solutions.  The local reconstruction now provides the full arity-2, arity-3
q<=4, and q=5-only detector-basis certificates listed later in this note.
This still does not, by itself, prove all-arity finite-rack domination.

## What arity 3 gives

Each verified contextual detector schema \((M,Q,\alpha)\) is reusable in every
arity where the same evaluated contextual endpoint pattern occurs: the
contextual \(T\)- and \(R\)-relations are checked in \(M\times X\times M\),
not in a single tuple orbit.

Thus the q=5 closure is useful beyond the literal finite count.  It supplies a
finite list of endpoint readouts that can separate any higher-arity endpoint
pair whose prefix and suffix contexts evaluate to one of the same separated
patterns.

What is not proved is the bounded-core assertion:

```text
every higher-arity bad endpoint pair has a detector-separated core of
arity at most 3.
```

That assertion is a new theorem.  Without it, a higher arity could contain a
Brunnian or high-context kernel-fiber monodromy: all arity-2 and arity-3
shadows are harmless, while the full \(n\)-strand action still moves \(X^n\).

## Width-3 propagation target

The most concrete all-arity bridge is a width-3 relative parabolic generation
statement.

For a fixed non-permutation size-three table \(X\), let \(Y_X\) be the
componentwise product of the distinct finite rack targets appearing in the
verified arity-2 and arity-3 endpoint detector schemas for \(X\).  This product
should be represented by its component actions rather than physically expanded.

For each arity \(n\), write

```text
K^Y_n = ker(B_n -> Sym(Y_X^n))
H^X_n = ker(B_n -> Sym(X^n)).
```

Finite-rack domination by this detector product is:

```text
K^Y_n <= H^X_n for every n.
```

Let \(J^Y_{3,n}\) be the normal closure in \(B_n\) of all consecutive
parabolic copies of \(K^Y_k\) for \(k\le3\).  A sufficient all-arity theorem is:

```text
rho^X_n(K^Y_n) = rho^X_n(J^Y_{3,n}) for every n.
```

The stronger rack-side version \(K^Y_n=J^Y_{3,n}\) would also suffice, but the
relative \(X\)-realized equality is the actual requirement.

If this statement holds, then the arity-2 and arity-3 endpoint closures
propagate to every arity for this \(X\).

## Next computations

1. Import the q=5 artifacts:

```text
proofs/nonperm3_arity3_q5_resolution_certificate.json
proofs/nonperm3_arity3_q5_resolution_verifier.py
expected reported sha256:
376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75
```

The verifier should recompute the 55 non-permutation tables, all 37,692
arity-3 bad endpoint pairs, the 22 new q=5 schemas, the 216 new coverages, and
`remaining_unresolved_candidates 0`.

2. Build a detector-product index for each of the 55 non-permutation tables:

```text
table X
  distinct target rack tables Q used by arity-2 and arity-3 detector schemas
  monoid/alpha endpoint schemas attached to each Q
  component action representation for Y_X = product(Q_i)
```

3. Directly verify the base kernel inclusions:

```text
K^Y_2 <= H^X_2
K^Y_3 <= H^X_3
```

These should follow from the endpoint gate, but a direct joint-image
certificate is a cleaner bridge from endpoint separation to braid-kernel
domination.

4. Run the first relative cross-effect audit:

```text
C^{X,Y}_{3,4} = rho^X_4(K^Y_4) / rho^X_4(J^Y_{3,4})
```

Then attempt \(n=5\) and \(n=6\) as feasible.  A trivial quotient is evidence
for width-3 propagation.  A nontrivial quotient supplies a concrete
higher-arity witness:

```text
table X
arity n >= 4
braid beta in K^Y_n
moved tuple x with beta.x != x in X^n
proof beta is not generated, as an X-action, by width <= 3 detector-kernel
relations
```

This would not yet be a Sawin counterexample.  It would be a failure of the
current finite detector product and would need to be promoted to a cofinal
rack-prefix obstruction.

5. In parallel, run the endpoint-pattern extension scan at arity 4:

```text
enumerate principal bad endpoint pairs in arity 4;
evaluate all imported arity-2 and arity-3 schemas on their M-contexts;
count separated pairs and misses;
classify misses by monoid context pattern.
```

No misses in arity 4 and 5 would be strong finite evidence.  It would still
not replace the symbolic width-3 or bounded-core theorem.

## Smoke audit

As a quick check, the displayed q=5 rack for the first arity-3 candidate was
tested as a single detector rack against that same \(X\) using the existing
componentwise cross-effect helper.

```text
X = [0,3,6,1,4,7,5,2,8]
Y = displayed q=5 rack from nonperm3_arity3_q5_resolution.md
state_limit = 200000

n=2:
  joint_image_size = 12
  kernel_image_size = 1
  parabolic_image_size = 1
  quotient_size = 1
  quotient_nontrivial = False
  truncated = False

n=3:
  truncated = True

n=4:
  truncated = True
```

This is not a detector-product certificate.  It only shows that naive
joint-image closure for even one q=5 component becomes too large at arity 3
under the generic closure algorithm.  The higher-arity plan therefore needs
the imported detector-product index plus stronger compression, or a symbolic
parabolic-generation argument.

The implementation hook for the product-index version is:

```text
ybe_domination.componentwise_realized_parabolic_cross_effect_audit
tools/run_componentwise_cross_effect_audit.py
```

It stores the detector side as a tuple of component rack permutation images,
which is equivalent to the Cartesian product detector but avoids constructing
the product rack state set.

The full-table importer/wrapper added for this target is:

```text
tools/run_nonperm3_detector_product_cross_effect_audit.py
```

The original compact local certificates were not enough to reconstruct `Y_X`.
At that stage, the generated import audit
`proofs/nonperm3_detector_product_import_gap.json` recorded:

```text
schema_like_detector_records: 1
tables_with_detector_components: 1
missing_table_count: 54
incomplete_detector_basis: true
```

This was an artifact gap only.  It was not mathematical evidence against
width-3 propagation.

The detector-basis gap has now been closed by deterministic local
reconstruction:

```text
proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json
proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json
proofs/nonperm3_arity3_q5_resolution_certificate.json
```

The arity-2 certificate now contains 456 reconstructed exact schema records
covering all 2064 arity-2 principal bad endpoint pairs.

The arity-3 q<=4 certificate records the archived schema count and the
reconstructed schema count separately:

```text
archived_positive_detector_schemas 320
reconstructed_positive_detector_schemas 600
positive_detector_coverages 37476
unresolved_obstruction_candidates 216
```

The q=5-only certificate records:

```text
new_positive_detector_coverages 216
new_positive_detector_schemas 22
combined_positive_detector_coverages 37692
remaining_unresolved_candidates 0
```

The complete detector-product import index is:

```text
proofs/nonperm3_detector_product_full_import_audit.json
```

It passes:

```text
python tools/verify_nonperm3_width3_cross_effect_audit.py \
  proofs/nonperm3_detector_product_full_import_audit.json \
  --require-complete-basis

OK nonperm3 width-3 audit verification
detector_index_rows 55
audit_rows 0
incomplete_detector_basis False
```

The identity table has no arity-2 or arity-3 principal bad endpoint pairs and
is represented by an explicit empty detector product.  The product-index
component-count distribution is:

```text
{0: 1, 1: 12, 2: 12, 3: 24, 4: 6}
```

The next computation was therefore the intended 55-row product audit, not
additional detector import.  A first full run with the generic BFS
componentwise closure and `state_limit=1000000` timed out after approximately
904 seconds before producing a final JSON payload.  The bottleneck was the
full joint-image enumeration for rows with q=5 detector components; a
representative `[2,3,5]` detector row already exceeded 100,000 detector states.

The audit wrapper supports row-level JSONL progress:

```text
--row-output-jsonl proofs/nonperm3_width3_arity4_cross_effect_rows.jsonl
--resume-row-output-jsonl
--start-index N
--only-table-index N
--stop-after-new-rows N
```

A two-row smoke run with row-level output checked the identity row and the
first nontrivial row; both were untruncated with `quotient_size = 1`.
The resume path now deduplicates completed rows by table, rejects conflicting
duplicate rows, and emits final rows in detector-index order.

## Arity-4 width-3 product audit

The full arity-4, bound-3 product audit is now completed by a stabilizer
method:

```text
ybe_domination.componentwise_stabilizer_realized_parabolic_cross_effect_audit
tools/run_nonperm3_detector_product_cross_effect_audit.py --method stabilizer
```

The stabilizer method embeds all detector component actions and the X-action
in one disjoint-union permutation action, computes the pointwise stabilizer of
every detector point using SymPy Schreier-Sims, restricts stabilizer generators
to the X block to obtain `rho^X_n(K^Y_n)`, and normal-closes the lower-width
parabolic kernel images inside the finite X-action image.  It is an exact
replacement for full joint-image enumeration when the detector image is too
large to enumerate directly.

Command:

```text
python tools/run_nonperm3_detector_product_cross_effect_audit.py \
  --certificate proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json \
  --certificate proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json \
  --certificate proofs/nonperm3_arity3_q5_resolution_certificate.json \
  --bound 3 \
  --arity 4 \
  --state-limit 1000000 \
  --method stabilizer \
  --require-all-55 \
  --run-audit \
  --row-output-jsonl proofs/nonperm3_width3_arity4_cross_effect_rows_stabilizer.jsonl \
  --output proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json
```

Certificate:

```text
proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json
proofs/nonperm3_width3_arity4_cross_effect_rows_stabilizer.jsonl
```

Verifier:

```text
python tools/verify_nonperm3_width3_cross_effect_audit.py \
  proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json \
  --require-complete-basis \
  --require-run-audit \
  --require-untruncated-trivial

OK nonperm3 width-3 audit verification
detector_index_rows 55
audit_rows 55
incomplete_detector_basis False
```

Summary:

```text
truncated rows:                  0
quotient_nontrivial rows:        0
quotient_size distribution:      {1: 55}
kernel_image_size distribution:  {1: 55}
max joint_image_size:            3454279995636458717184
```

Thus the first possible finite cross-effect obstruction is absent for this
detector product: every non-permutation size-three table has trivial realized
detector-kernel image on `X^4`.  This is finite arity-4 evidence only.  It is
not an all-arity theorem.

The audit verifier has been hardened for final-result use.  With
`--require-run-audit`, it now requires exactly one row for each detector-index
table, rejects duplicate row tables, and checks that row tables match the
detector index.  Empty detector rows are also independently checked: the
verifier recomputes that there are no arity-2 or arity-3 principal bad endpoint
candidates for the table and verifies that the X-action in the audited arity
is trivial with the expected all-one image sizes.

The stabilizer row arithmetic is now also independently checkable in the
trivial-kernel case:

```text
python tools/verify_nonperm3_stabilizer_rows.py \
  proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json \
  --arity 4 \
  --require-complete-basis \
  --require-run-audit \
  --require-trivial-kernel-image
```

This verifier recomputes the detector pointwise stabilizer for each row,
restricts stabilizer generators to the `X^4` block, closes the resulting
kernel image in `Sym(X^4)`, and checks that the recomputed kernel image is
trivial.  Since every arity-4 row has `kernel_image_size = 1`, this certifies
the row arithmetic needed for the stronger finite conclusion
`rho^X_4(K^{Y_X}_4)=1` without recomputing the parabolic normal closures.

The stabilizer cross-effect helper now asserts that every embedded lower-width
parabolic seed lies both in the full `X`-action image and in the recomputed
detector-kernel `X` image before normal closure.  This is a defensive invariant
for future higher-arity runs.

## Arity-5 partial probes

The arity-5 stabilizer computation has been probed but not completed.  The
following partial certificates are finite evidence only:

```text
proofs/nonperm3_width3_arity5_component_count_le2_stabilizer_probe.json
proofs/nonperm3_width3_arity5_component_count_le2_rows_stabilizer_probe.jsonl
```

This component-count <= 2 probe covers the identity row, the twelve one
q=2-component rows, and the twelve `[3,4]` two-component rows:

```text
audit_rows 25
truncated rows 0
quotient_size distribution {1: 25}
kernel_image_size distribution {1: 25}
```

A separate no-q5 component-count <= 3 probe covers the identity row, the
twelve one q=2-component rows, and the twelve `[2,3,3]` three-component rows:

```text
proofs/nonperm3_width3_arity5_no_q5_component_count_le3_stabilizer_probe.json
proofs/nonperm3_width3_arity5_no_q5_component_count_le3_rows_stabilizer_probe.jsonl

audit_rows 25
truncated rows 0
quotient_size distribution {1: 25}
kernel_image_size distribution {1: 25}
```

A third no-q5 component-count 4 probe covers the six `[2,3,3,3]`
four-component rows:

```text
proofs/nonperm3_width3_arity5_component_count4_no_q5_stabilizer_probe.json
proofs/nonperm3_width3_arity5_component_count4_no_q5_rows_stabilizer_probe.jsonl

audit_rows 6
truncated rows 0
quotient_size distribution {1: 6}
kernel_image_size distribution {1: 6}
```

The independent stabilizer-row verifier recomputes these six row kernels:

```text
python tools/verify_nonperm3_stabilizer_rows.py \
  proofs/nonperm3_width3_arity5_component_count4_no_q5_stabilizer_probe.json \
  --arity 5 \
  --require-complete-basis \
  --require-trivial-kernel-image

OK independent stabilizer-row verification
recomputed_stabilizer_rows 6
trivial_kernel_rows 6
```

Together these partial probes cover 43 of the 55 arity-5 rows, all with
trivial detector-kernel image.  The remaining rows are exactly:

```text
12 rows with detector component sizes [2,3,5]
```

The q=5-component arity-5 rows were then closed by a subproduct certificate:

```text
proofs/nonperm3_width3_arity5_q5_subproduct_trivial_kernel_audit.json

selected rows 12
full detector component sizes [2,3,5]
audited subproduct component sizes [2,3]
subproduct_kernel_image_size distribution {1: 12}
full_product_kernel_image_size distribution {1: 12}
```

The independent verifier recomputes these twelve `[2,3]` subproduct kernels:

```text
python tools/verify_nonperm3_subproduct_trivial_kernel_audit.py \
  proofs/nonperm3_width3_arity5_q5_subproduct_trivial_kernel_audit.json \
  --arity 5 \
  --state-limit 1000000 \
  --require-trivial-full-product

OK nonperm3 subproduct trivial-kernel audit verification
recomputed_rows 12
trivial_subproduct_rows 12
```

This proves the full-product conclusion because if a detector subproduct
`Y'` already has `rho^X_5(K^{Y'}_5)=1`, then any larger detector product
`Y=Y' x Y''` satisfies `K^Y_5 <= K^{Y'}_5`, hence also has trivial realized
kernel image on `X^5`.

Combining the direct stabilizer rows and the subproduct certificate gives:

```text
arity 5 rows certified 55 / 55
direct full-product stabilizer rows 43
subproduct-certified q=5 rows 12
truncated rows 0
full_product_kernel_image_size distribution {1: 55}
full_product_quotient_size distribution {1: 55}
```

This is proof-grade fixed-arity evidence that there is no arity-5 realized
cross-effect obstruction for the current detector product.  It is not an
all-arity theorem.

A consolidated certificate packages the 43 direct rows and the 12 subproduct
rows into one auditable fixed-arity conclusion:

```text
proofs/nonperm3_width3_arity5_certified_trivial_kernel_combined.json

row_count 55
certification_method_counts {
  "direct_full_product_stabilizer": 43,
  "subproduct_trivial_kernel": 12
}
full_product_kernel_image_size_distribution {"1": 55}
full_product_quotient_size_distribution {"1": 55}
```

Verifier:

```text
python tools/verify_nonperm3_certified_trivial_kernel_audit.py \
  proofs/nonperm3_width3_arity5_certified_trivial_kernel_combined.json \
  --arity 5 \
  --require-all-55 \
  --require-trivial-full-product

OK nonperm3 combined trivial-kernel audit verification
rows 55
methods {'direct_full_product_stabilizer': 43, 'subproduct_trivial_kernel': 12}
```

### Arity 6 initial probe

The first arity-6 stabilizer probe covers the identity row and the twelve
one-component q=2 detector rows:

```text
proofs/nonperm3_width3_arity6_component_count_le1_stabilizer_probe.json
proofs/nonperm3_width3_arity6_component_count_le1_rows_stabilizer_probe.jsonl

audit_rows 13
detector component size distribution {[]: 1, [2]: 12}
truncated rows 0
kernel_image_size distribution {1: 13}
quotient_size distribution {1: 13}
```

The independent stabilizer-row verifier recomputes the twelve non-empty
detector rows:

```text
python tools/verify_nonperm3_stabilizer_rows.py \
  proofs/nonperm3_width3_arity6_component_count_le1_stabilizer_probe.json \
  --arity 6 \
  --require-complete-basis \
  --require-trivial-kernel-image

OK independent stabilizer-row verification
recomputed_stabilizer_rows 12
trivial_kernel_rows 12
```

This is proof-grade fixed-arity evidence only for this low-component slice.
It does not imply anything for the remaining arity-6 rows or for all arities.

After the trivial-kernel early return in the stabilizer cross-effect audit,
the no-q5 component-count <= 3 slice also closes:

```text
proofs/nonperm3_width3_arity6_no_q5_component_count_le3_stabilizer_probe.json
proofs/nonperm3_width3_arity6_no_q5_component_count_le3_rows_stabilizer_probe.jsonl

audit_rows 25
detector component size distribution {[]: 1, [2]: 12, [2, 3, 3]: 12}
truncated rows 0
kernel_image_size distribution {1: 25}
quotient_size distribution {1: 25}
elapsed_seconds total 66.362072
```

The structural verifier checks the complete 55-table detector index and the
25 audited rows:

```text
python tools/verify_nonperm3_width3_cross_effect_audit.py \
  proofs/nonperm3_width3_arity6_no_q5_component_count_le3_stabilizer_probe.json \
  --require-complete-basis

OK nonperm3 width-3 audit verification
detector_index_rows 55
audit_rows 25
incomplete_detector_basis False
```

The independent stabilizer-row verifier recomputes the 24 non-empty rows:

```text
python tools/verify_nonperm3_stabilizer_rows.py \
  proofs/nonperm3_width3_arity6_no_q5_component_count_le3_stabilizer_probe.json \
  --arity 6 \
  --require-complete-basis \
  --require-trivial-kernel-image

OK independent stabilizer-row verification
recomputed_stabilizer_rows 24
trivial_kernel_rows 24
```

This remains partial arity-6 evidence.  It certifies the identity, q=2
one-component, and q=2/q=3/q=3 component rows.  It does not certify rows with
q=4 or q=5 detector components.

The expanded no-q5 full-product stabilizer probe certifies the remaining
q<=3 component rows:

```text
proofs/nonperm3_width3_arity6_no_q5_component_count_le4_stabilizer_probe.json
proofs/nonperm3_width3_arity6_no_q5_component_count_le4_rows_stabilizer_probe.jsonl

audit_rows 31
detector component size distribution {[]: 1, [2]: 12, [2, 3, 3]: 12, [2, 3, 3, 3]: 6}
truncated rows 0
kernel_image_size distribution {1: 31}
quotient_size distribution {1: 31}
```

The structural and independent stabilizer-row verifiers report:

```text
OK nonperm3 width-3 audit verification
detector_index_rows 55
audit_rows 31
incomplete_detector_basis False

OK independent stabilizer-row verification
arity 6
recomputed_stabilizer_rows 30
trivial_kernel_rows 30
```

The q=4/q=5 rows are certified by subproduct triviality.  For each `(3,4)`
row the q=3 component alone has trivial realized detector-kernel image; for
each `(2,3,5)` row the `(2,3)` subproduct has trivial realized
detector-kernel image.  Since the full product kernel is a subgroup of the
subproduct kernel, the full product also has trivial X-image:

```text
proofs/nonperm3_width3_arity6_q4_q5_subproduct_size_le3_trivial_kernel_audit.json

row_count 24
full component size distribution {[3, 4]: 12, [2, 3, 5]: 12}
audited subproduct size distribution {[3]: 12, [2, 3]: 12}
omitted component size distribution {[4]: 12, [5]: 12}
subproduct_kernel_image_size distribution {1: 24}
full_product_kernel_image_size distribution {1: 24}
```

Verifier:

```text
python tools/verify_nonperm3_subproduct_trivial_kernel_audit.py \
  proofs/nonperm3_width3_arity6_q4_q5_subproduct_size_le3_trivial_kernel_audit.json \
  --arity 6 \
  --require-trivial-full-product

OK nonperm3 subproduct trivial-kernel audit verification
arity 6
recomputed_rows 24
trivial_subproduct_rows 24
```

The consolidated arity-6 certificate is:

```text
proofs/nonperm3_width3_arity6_certified_trivial_kernel_combined.json

row_count 55
certification_method_counts {
  "direct_full_product_stabilizer": 31,
  "subproduct_trivial_kernel": 24
}
full_product_kernel_image_size_distribution {"1": 55}
full_product_quotient_size_distribution {"1": 55}
```

Verifier:

```text
python tools/verify_nonperm3_certified_trivial_kernel_audit.py \
  proofs/nonperm3_width3_arity6_certified_trivial_kernel_combined.json \
  --arity 6 \
  --require-all-55 \
  --require-trivial-full-product

OK nonperm3 combined trivial-kernel audit verification
arity 6
rows 55
methods {'direct_full_product_stabilizer': 31, 'subproduct_trivial_kernel': 24}
```

Thus arity 6, like arities 4 and 5, has no realized detector-kernel X-action
for the current detector products:

```text
rho^X_6(K^{Y_X}_6)=1
```

for all 55 non-permutation size-three tables.  This is proof-grade
fixed-arity evidence only; it is not an all-arity theorem.

### Arity 7

The arity-7 direct stabilizer computation closes all q<=3 component rows:

```text
proofs/nonperm3_width3_arity7_no_q5_component_count_le4_stabilizer_probe.json
proofs/nonperm3_width3_arity7_no_q5_component_count_le4_rows_stabilizer_probe.jsonl

audit_rows 31
detector component size distribution {[]: 1, [2]: 12, [2, 3, 3]: 12, [2, 3, 3, 3]: 6}
truncated rows 0
kernel_image_size distribution {1: 31}
quotient_size distribution {1: 31}
```

Verifier output:

```text
python tools/verify_nonperm3_width3_cross_effect_audit.py \
  proofs/nonperm3_width3_arity7_no_q5_component_count_le4_stabilizer_probe.json \
  --require-complete-basis

OK nonperm3 width-3 audit verification
detector_index_rows 55
audit_rows 31
incomplete_detector_basis False

python tools/verify_nonperm3_stabilizer_rows.py \
  proofs/nonperm3_width3_arity7_no_q5_component_count_le4_stabilizer_probe.json \
  --arity 7 \
  --require-complete-basis \
  --require-trivial-kernel-image

OK independent stabilizer-row verification
arity 7
recomputed_stabilizer_rows 30
trivial_kernel_rows 30
```

The q=4/q=5 rows again close by q<=3 subproduct triviality:

```text
proofs/nonperm3_width3_arity7_q4_q5_subproduct_size_le3_trivial_kernel_audit.json

row_count 24
full component size distribution {[3, 4]: 12, [2, 3, 5]: 12}
audited subproduct size distribution {[3]: 12, [2, 3]: 12}
omitted component size distribution {[4]: 12, [5]: 12}
subproduct_kernel_image_size distribution {1: 24}
full_product_kernel_image_size distribution {1: 24}
```

Verifier:

```text
python tools/verify_nonperm3_subproduct_trivial_kernel_audit.py \
  proofs/nonperm3_width3_arity7_q4_q5_subproduct_size_le3_trivial_kernel_audit.json \
  --arity 7 \
  --require-trivial-full-product

OK nonperm3 subproduct trivial-kernel audit verification
arity 7
recomputed_rows 24
trivial_subproduct_rows 24
```

The consolidated arity-7 certificate is:

```text
proofs/nonperm3_width3_arity7_certified_trivial_kernel_combined.json

row_count 55
certification_method_counts {
  "direct_full_product_stabilizer": 31,
  "subproduct_trivial_kernel": 24
}
full_product_kernel_image_size_distribution {"1": 55}
full_product_quotient_size_distribution {"1": 55}
```

Verifier:

```text
python tools/verify_nonperm3_certified_trivial_kernel_audit.py \
  proofs/nonperm3_width3_arity7_certified_trivial_kernel_combined.json \
  --arity 7 \
  --require-all-55 \
  --require-trivial-full-product

OK nonperm3 combined trivial-kernel audit verification
arity 7
rows 55
methods {'direct_full_product_stabilizer': 31, 'subproduct_trivial_kernel': 24}
```

Thus arity 7 also has no realized detector-kernel X-action for the current
detector products:

```text
rho^X_7(K^{Y_X}_7)=1
```

for all 55 non-permutation size-three tables.  This is still proof-grade
fixed-arity evidence only, not an all-arity theorem.

### Arity 8 initial probe

The first arity-8 direct stabilizer probe covers the identity row and the
twelve q=2 one-component rows:

```text
proofs/nonperm3_width3_arity8_component_count_le1_stabilizer_probe.json
proofs/nonperm3_width3_arity8_component_count_le1_rows_stabilizer_probe.jsonl

audit_rows 13
detector component size distribution {[]: 1, [2]: 12}
truncated rows 0
kernel_image_size distribution {1: 13}
quotient_size distribution {1: 13}
elapsed_seconds total 14.055528
```

Verifier output:

```text
python tools/verify_nonperm3_width3_cross_effect_audit.py \
  proofs/nonperm3_width3_arity8_component_count_le1_stabilizer_probe.json \
  --require-complete-basis

OK nonperm3 width-3 audit verification
detector_index_rows 55
audit_rows 13
incomplete_detector_basis False

python tools/verify_nonperm3_stabilizer_rows.py \
  proofs/nonperm3_width3_arity8_component_count_le1_stabilizer_probe.json \
  --arity 8 \
  --require-complete-basis \
  --require-trivial-kernel-image

OK independent stabilizer-row verification
arity 8
recomputed_stabilizer_rows 12
trivial_kernel_rows 12
```

A resumable q=4/q=5 subproduct partial also closes:

```text
proofs/nonperm3_width3_arity8_q4_q5_subproduct_size_le3_rows.jsonl
proofs/nonperm3_width3_arity8_q4_q5_subproduct_size_le3_trivial_kernel_audit.partial.json

row_count 12
full component size distribution {[2, 3, 5]: 8, [3, 4]: 4}
audited subproduct size distribution {[2, 3]: 8, [3]: 4}
omitted component size distribution {[5]: 8, [4]: 4}
subproduct_kernel_image_size distribution {1: 12}
full_product_kernel_image_size distribution {1: 12}
elapsed_seconds total 3882.674988
```

Verifier:

```text
python tools/verify_nonperm3_subproduct_trivial_kernel_audit.py \
  proofs/nonperm3_width3_arity8_q4_q5_subproduct_size_le3_trivial_kernel_audit.partial.json \
  --arity 8 \
  --require-trivial-full-product

OK nonperm3 subproduct trivial-kernel audit verification
arity 8
recomputed_rows 12
trivial_subproduct_rows 12
```

The partial arity-8 combined certificate is:

```text
proofs/nonperm3_width3_arity8_partial_certified_trivial_kernel_combined.json

row_count 25
certification_method_counts {
  "direct_full_product_stabilizer": 13,
  "subproduct_trivial_kernel": 12
}
full_product_kernel_image_size_distribution {"1": 25}
full_product_quotient_size_distribution {"1": 25}
```

Verifier:

```text
python tools/verify_nonperm3_certified_trivial_kernel_audit.py \
  proofs/nonperm3_width3_arity8_partial_certified_trivial_kernel_combined.json \
  --arity 8 \
  --require-trivial-full-product

OK nonperm3 combined trivial-kernel audit verification
arity 8
rows 25
methods {'direct_full_product_stabilizer': 13, 'subproduct_trivial_kernel': 12}
```

This is proof-grade fixed-arity evidence for only 25 of the 55 arity-8 rows.
The q=4/q=5 partial indicates that the subproduct strategy still works at
arity 8, but completing the 24-row q=4/q=5 subproduct batch is now a
multi-hour computation.  The remaining 30 arity-8 rows are not certified by this
probe.

The subproduct audit tool now supports durable row-level progress for that
long batch:

```text
python tools/run_nonperm3_subproduct_trivial_kernel_audit.py \
  --certificate proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json \
  --certificate proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json \
  --certificate proofs/nonperm3_arity3_q5_resolution_certificate.json \
  --arity 8 \
  --bound 3 \
  --state-limit 1000000 \
  --component-size-max 3 \
  --require-all-selected-trivial \
  --include-row-timing \
  --stop-after-new-rows 1 \
  --row-output-jsonl proofs/nonperm3_width3_arity8_q4_q5_subproduct_size_le3_rows.jsonl \
  --resume-row-output-jsonl \
  --output proofs/nonperm3_width3_arity8_q4_q5_subproduct_size_le3_trivial_kernel_audit.partial.json
```

Repeating the same command skips rows already present in the JSONL file and
appends one newly certified row.  Once all 24 rows are present, rerun without
`--stop-after-new-rows` to assemble the complete q=4/q=5 subproduct JSON.

The decision rule for future higher-arity product audits remains:

```text
if any non-permutation size-three table has quotient_nontrivial = True:
  the width-3 propagation lemma is false for that detector product;

if all 55 rows are untruncated and quotient_size = 1:
  there is no obstruction in that arity, but an all-n induction is still needed;

if any row truncates:
  the result is inconclusive, and the closure step needs stronger permutation
  group compression.
```

## Exact missing lemma

For the current non-permutation \(|X|=3\) endpoint route, the missing lemma is:

```text
Width-3 endpoint/rack-kernel propagation.

For every non-permutation size-three YBE table X, let Y_X be the product of
the finite rack targets appearing in the verified arity-2 and arity-3 endpoint
detector basis.  If a braid beta is invisible to Y_X in arity n, then its
action on X^n is generated, as an X-action, by consecutive parabolic copies of
invisible actions in arities 2 and 3.
```

Equivalently:

```text
rho^X_n(K^Y_n) = rho^X_n(J^Y_{3,n}) for all n.
```

For a complete MathOverflow answer, the broader missing theorem is:

```text
Primitive endpoint-change finite-basis theorem.

For every finite bijective YBE solution X, finitely many finite-rack-separable
one-coordinate contextual endpoint-change patterns cover every actual
kernel-fiber bad pair.
```

The q=5 batch is positive finite evidence for this strategy in the
non-permutation size-three arity-3 endpoint gate.  The all-arity bridge remains
the unsolved part.

## Conditional 3-coskeletal route

The current theoretical C-output is the following conditional theorem, not an
unconditional proof.

For each verified contextual detector schema `s = (M,Q,alpha)`, define in
every arity:

```text
Phi^s_n(x_1,...,x_n)_i =
  alpha([x_1...x_{i-1}], x_i, [x_{i+1}...x_n]).
```

The contextual verifier checks the local `T` and `R` relations in
`M x X x M`, so each verified schema gives a braid-equivariant readout
`Phi^s_n : X^n -> Q^n` in every arity.  Hence, if every nontrivial
`Y_X`-invisible motion of `X^n` contains a transported endpoint pair whose
obstruction has an arity-2 or arity-3 principal endpoint core separated by one
of the verified schemas, then `K^{Y_X}_n <= H^X_n` for every `n`.

This additional hypothesis can be called:

```text
3-coskeletal endpoint completeness.
Every beta in K^{Y_X}_n with rho^X_n(beta) != 1 contains a detector-separated
principal endpoint core of arity at most 3.
```

Under that hypothesis, equivariance gives the contradiction: if
`beta in K^{Y_X}_n`, then `beta` fixes every component `Q^n` of `Y_X^n`, so
`Phi^s_n(beta.x) = beta.Phi^s_n(x) = Phi^s_n(x)` for every verified schema
component.  A schema-separated endpoint pair along the moved orbit cannot then
exist.  Thus `beta` fixes `X^n`.

The first unproved implication is exactly the bounded-core assertion:

```text
beta in K^{Y_X}_n and rho^X_n(beta) != 1
  => an arity <= 3 detector-separated endpoint core exists.
```

The arity-4 stabilizer audit supports this route only as finite evidence: in
arity 4 the realized detector-kernel image on `X^4` is already trivial.  No
transition lemma currently proves that this persists, nor that Brunnian or
high-context kernel-fiber monodromy is impossible in higher arity.
