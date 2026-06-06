# Non-permutation size-three detector-product import gap

Date: 2026-06-06

This note records the local artifact status for the proposed width-3
detector-product cross-effect computation.

## External problem status

Direct recheck of Will Sawin's MathOverflow question on 2026-06-06 still shows
the question with `0` answers:

```text
https://mathoverflow.net/questions/509988/set-theoretic-solutions-to-the-yang-baxter-equations-and-racks
```

Thus there is no posted external solution to import at this checkpoint.

## Intended audit

For each non-permutation size-three YBE table `X`, the proposed detector is:

```text
Y_X = product of all distinct finite rack targets appearing in the verified
      arity-2 and arity-3 endpoint detector schemas for X.
```

The first fixed-arity obstruction group is:

```text
C^{X,Y_X}_{3,4}
  =
rho^X_4(K^Y_4) / rho^X_4(J^Y_{3,4}).
```

The required all-table audit row fields are:

```text
ybe_table
detector_component_count
detector_component_sizes
bound
arity
joint_image_size
kernel_image_size
parabolic_image_size
quotient_size
quotient_nontrivial
seed_count
first_witness_word
first_moved_tuple
first_moved_tuple_image
truncated
```

## New local importer

The helper

```text
tools/run_nonperm3_detector_product_cross_effect_audit.py
```

now imports schema-like records from certificate JSON files.  A record is
accepted when it contains a `ybe_table` and a target rack table in one of:

```text
rack.table
rack
rack_table
```

The helper groups distinct target rack tables by YBE table.  Duplicate target
racks for the same table are merged, while any available schema IDs are
retained in `source_schema_ids`.  The output includes:

```text
kind: nonperm3_width3_componentwise_cross_effect_audit_v1
branch: nonpermutation_size3
detector_index:
  - ybe_table
    detectors:
      - rack_table
        source_schema_ids
```

With `--run-audit`, it converts those components into the componentwise
product detector and calls:

```text
ybe_domination.componentwise_realized_parabolic_cross_effect_audit
```

This prepares the exact arity-4, bound-3 computation once the full arity-2 and
arity-3 detector schema certificates are available locally.

## Current compact artifacts are insufficient

Running the importer against the two local compact certificates:

```text
python tools/run_nonperm3_detector_product_cross_effect_audit.py \
  --certificate proofs/nonperm3_arity2_endpoint_gate_certificate.json \
  --certificate proofs/nonperm3_arity3_endpoint_gate_checkpoint_certificate.json \
  --bound 3 \
  --arity 4 \
  --output proofs/nonperm3_detector_product_import_gap.json
```

produces:

```text
kind: nonperm3_width3_componentwise_cross_effect_audit_v1
schema_like_detector_records: 1
nonpermutation_ybe_tables: 55
tables_with_detector_components: 1
missing_table_count: 54
incomplete_detector_basis: true
run_audit: false
```

This is not mathematical evidence for or against width-3 propagation.  It only
means the locally present compact artifacts do not contain the detector schema
lists needed to build `Y_X`.

In particular:

- `proofs/nonperm3_arity2_endpoint_gate_certificate.json` records the arity-2
  theorem and one example detector, but not all `2064` positive detector
  schemas.
- `proofs/nonperm3_arity3_endpoint_gate_checkpoint_certificate.json` records
  the q<=4 checkpoint counts, but not the `320` positive schema records.
- `proofs/nonperm3_arity3_q5_resolution.md` records reported q=5 verifier
  output, but the q=5 JSON certificate and verifier are still absent.

## Decision consequence

Until the full schema certificates are imported, the intended full audit:

```text
for each of the 55 non-permutation |X|=3 tables:
  compute C^{X,Y_X}_{3,4}
```

cannot be run locally.  The correct next computational step is to import:

```text
proofs/nonperm3_arity3_q5_resolution_certificate.json
proofs/nonperm3_arity3_q5_resolution_verifier.py
```

and the corresponding full arity-2 / q<=4 schema certificates if they are
separate from the compact summary JSON files.

After import, rerun the helper with all schema certificates and `--run-audit`.
If all `55` tables have detector components and all rows are untruncated with
`quotient_size = 1`, then arity 4 has no realized width-3 obstruction for
this detector product.  This would still be finite fixed-arity evidence, not
the required all-arity proof.
