# Local-minimal Green audit

Date: 2026-05-28

This note moves the Green completed-context audit through the actual
congruence-cover reduction.

For each finite YBE table in the audited size range, the script enumerates
congruences, takes cover intervals, converts each cover

```text
X / lower -> X / upper
```

to a coloured local interval, checks local-minimality, realizes the local
interval as a finite braided set, and runs the bounded Green
completed-context category at depth `2`.

This is still not proof evidence for the global theorem.  It is a candidate
ledger aligned with the required local-minimal reduction: a B-style
counterexample should eventually show a non-known-branch hidden loop inside
one of these local-minimal interval audits, while an A proof must explain why
such loops always collapse or become finite-G measurable.

## Exhaustive small results

The generated report is `proofs/local_minimal_green_audit.json`.

For all size-2 bijective YBE tables:

- YBE tables: `5`;
- congruence covers: `5`;
- local-minimal covers: `5`;
- semisplit cover intervals: `0`;
- semisplit equality/universal candidate mixtures tested: `0`;
- kernel-action nonpermutation intervals: `0`;
- maximum kernel-action group size: `2`;
- output coordinate-kernel closures: `equality: 4`, `universal: 1`;
- universal output-kernel corridor depths: `0: 1`;
- universal output-kernel intervals with depth-2 hidden atom-trivial loops:
  `1`;
- universal output-kernel intervals with depth-2 hidden bijective loops:
  `0`;
- universal output-kernel intervals with mixed source atom projection: `0`;
- universal output-kernel untagged intervals: `0`;
- mixed source atom-projection intervals: `0`;
- local-only Green edge-germ intervals: `0`;
- non-group Schutzenberger action intervals: `0`;
- depth-2 hidden atom-trivial loop intervals: `1`;
- depth-2 hidden bijective loop intervals: `0`;
- untagged hidden loop intervals: `0`;
- hidden loop branch tags: `involutive: 1`, `identity_table: 1`.

For all size-3 bijective YBE tables:

- YBE tables: `73`;
- congruence covers: `134`;
- local-minimal covers: `134`;
- semisplit cover intervals: `0`;
- semisplit equality/universal candidate mixtures tested: `0` after
  singleton-fibre degeneracies are identified with both equality and
  universal;
- kernel-action nonpermutation intervals: `0`;
- maximum kernel-action group size: `6`;
- output coordinate-kernel closures: `equality: 122`, `universal: 12`;
- universal output-kernel corridor depths: `0: 12`;
- universal output-kernel intervals with depth-2 hidden atom-trivial loops:
  `12`;
- universal output-kernel intervals with depth-2 hidden bijective loops:
  `3`;
- universal output-kernel intervals with mixed source atom projection: `6`;
- universal output-kernel untagged intervals: `0`;
- universal output-kernel branch tags: `involutive: 12`, `identity_table: 6`;
- mixed source atom-projection intervals: `6`, all `6` involutive;
- mixed source atom-projection branch tags: `involutive: 6`;
- local-only Green edge-germ intervals: `0`;
- non-group Schutzenberger action intervals: `0`;
- depth-2 hidden atom-trivial loop intervals: `12`;
- depth-2 hidden bijective loop intervals: `3`;
- untagged hidden loop intervals: `0`;
- untagged hidden bijective loop intervals: `0`;
- hidden loop branch tags: `involutive: 12`, `identity_table: 6`;
- hidden bijective loop branch tags: `involutive: 3`.

Thus, after passing to local-minimal congruence-cover intervals, the same
pattern remains: bounded hidden completed-context loops exist in tiny data,
but every such signal is still contained in the known eliminated involutive
branch, and several are literal identity-table intervals.  The sharper
kernel-action refinement finds that every retained label induces a finite
permutation action on the relevant kernel-block quotient, and the
Schutzenberger refinement finds no local-only retained edge-germ and no
non-group stabilizer action in the audited local-minimal intervals.  Thus the
remaining arbitrary-fibre master gap is no longer simply "bounded hidden loops
exist"; it is the symbolic problem of proving that these finite kernel-block
and Schutzenberger actions detect the residual braid action, with mixed source
atom projections falling into already eliminated branches, or else finding a
finite YBE table where this finite-group control fails.

The new corridor cross-tab shows that the universal coordinate-kernel branch
and the Green hidden-loop branch overlap in tiny data, but the overlap is
again entirely known: the size-2 universal-output overlap is the involutive
identity-table interval, and the size-3 universal-output overlaps are all
involutive, with the identity-table tag appearing in half of them.  This is
finite diagnostic evidence only.  It suggests that a symbolic proof should
show either that universal coordinate-kernel corridors force the Green
completed-context hidden loops into known involutive/permutation-style
branches, or that the two-sided symmetric kernel-block and Schutzenberger
groups detect any remaining corridor holonomy.
