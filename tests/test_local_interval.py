import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    LocalInterval,
    continuation_congruence_audit,
    continuation_seed_pair_closure_audits,
    continuation_seed_pair_closure_failures,
    continuation_seed_pairs,
    continuation_seed_readout_propagation_audits,
    continuation_seed_readout_propagation_failures,
    continuation_seed_rows,
    continuation_seed_universal_derivation_audits,
    continuation_seed_universal_derivation_failures,
    coordinate_kernel_pair_closure_audits,
    coordinate_kernel_pair_closure_failures,
    local_minimal_seed_saturation_dichotomy_audit,
    partition_readout_labels,
    product_readout_descent_separation_audit,
    product_readout_descent_separation_failures,
    product_readout_kernel_audit,
    product_readout_labels,
    quotient_interval_by_family,
    readout_descent_separation_audit,
    readout_descent_separation_failures,
    readout_kernel_audit,
    readout_kernel_family,
    readout_kernel_quotient_interval,
    readout_seed_saturation_audit,
)


def family_key(family):
    return tuple(sorted((color, family[color]) for color in family))


def one_color_flip_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): (y, x)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def two_color_identity_interval():
    colors = ("a", "b")
    fibres = {"a": (0, 1), "b": (0, 1)}
    base_R = {(x, y): (x, y) for x in colors for y in colors}
    T = {
        (a, b, x, y): (x, y)
        for a in colors
        for b in colors
        for x in fibres[a]
        for y in fibres[b]
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_identity_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): (x, y)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def size_three_affine_interval():
    points = (0, 1, 2)
    values = [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 2),
        (0, 2),
        (1, 2),
        (1, 1),
        (2, 1),
        (0, 1),
    ]
    return LocalInterval(
        colors=("*",),
        fibres={"*": points},
        base_R={("*", "*"): ("*", "*")},
        T={
            ("*", "*", x, y): value
            for (x, y), value in zip(
                ((x, y) for x in points for y in points),
                values,
            )
        },
    )


def two_color_swap_interval():
    colors = ("a", "b")
    fibres = {"a": (0, 1), "b": (0, 1)}
    base_R = {(x, y): (x, y) for x in colors for y in colors}
    T = {
        (a, b, x, y): (y, x)
        for a in colors
        for b in colors
        for x in fibres[a]
        for y in fibres[b]
    }
    return LocalInterval(colors, fibres, base_R, T)


class LocalIntervalTests(unittest.TestCase):
    def test_one_color_flip_is_colored_ybe_and_local_minimal(self):
        interval = one_color_flip_interval()
        self.assertTrue(interval.is_colored_ybe())
        self.assertEqual(interval.semisplit_families(), [])
        self.assertTrue(interval.is_local_minimal())

    def test_semisplit_family_is_detected(self):
        interval = two_color_identity_interval()
        self.assertTrue(interval.is_colored_ybe())
        self.assertTrue(interval.semisplit_families())
        self.assertFalse(interval.is_local_minimal())

    def test_semisplit_audit_agrees_with_full_admissibility_enumeration(self):
        interval = two_color_identity_interval()
        admissible = {family_key(family) for family in interval.admissible_congruence_families()}
        semisplit = {family_key(family) for family in interval.semisplit_families()}
        self.assertTrue(semisplit)
        self.assertTrue(semisplit.issubset(admissible))

    def test_pair_generated_local_minimality_agrees_with_enumeration(self):
        local_minimal = one_color_flip_interval()
        nonminimal = two_color_identity_interval()

        self.assertTrue(local_minimal.is_local_minimal())
        self.assertEqual(local_minimal.pair_generated_local_minimality_failures(), [])

        self.assertFalse(nonminimal.is_local_minimal())
        failures = nonminimal.pair_generated_local_minimality_failures()
        self.assertTrue(failures)
        self.assertTrue(all(failure.generated.kind != "universal" for failure in failures))

    def test_coordinate_kernel_pair_closures_certify_universal_corridor(self):
        local_minimal_degenerate = one_color_identity_interval()
        audits = coordinate_kernel_pair_closure_audits(local_minimal_degenerate)

        self.assertTrue(local_minimal_degenerate.is_local_minimal())
        self.assertEqual(len(audits), 1)
        self.assertEqual(audits[0].generated.kind, "universal")
        self.assertEqual(coordinate_kernel_pair_closure_failures(local_minimal_degenerate), ())

        nonminimal = two_color_identity_interval()
        failures = coordinate_kernel_pair_closure_failures(nonminimal)
        self.assertTrue(failures)
        self.assertTrue(all(failure.generated.kind != "universal" for failure in failures))

        nondegenerate = one_color_flip_interval()
        self.assertEqual(coordinate_kernel_pair_closure_audits(nondegenerate), ())

    def test_semisplit_boolean_constraints_match_relation_audit(self):
        interval = two_color_identity_interval()
        rows = interval.semisplit_constraint_rows()
        assignments = interval.semisplit_boolean_assignments()

        self.assertEqual(len(rows), 4)
        self.assertEqual(len(assignments), 2)
        self.assertEqual(
            {tuple(assignment[color] for color in interval.colors) for assignment in assignments},
            {(0, 1), (1, 0)},
        )
        self.assertEqual(
            {family_key(family) for family in interval.semisplit_families()},
            {
                family_key(
                    {
                        color: interval._semisplit_partition(color, assignment[color])
                        for color in interval.colors
                    }
                )
                for assignment in assignments
            },
        )

    def test_semisplit_audit_records_failure_witness(self):
        interval = two_color_swap_interval()
        audits = interval.semisplit_audits()
        self.assertEqual(len(audits), 2)
        self.assertFalse(any(audit.admissible for audit in audits))
        self.assertTrue(all(audit.failure is not None for audit in audits))
        self.assertIn(audits[0].failure.side, {"transported_not_target", "target_not_transported"})
        self.assertEqual(interval.semisplit_boolean_assignments(), [])

    def test_singleton_fibres_do_not_create_fake_semisplit_families(self):
        colors = ("a", "b")
        fibres = {"a": (0,), "b": (1,)}
        base_R = {(x, y): (x, y) for x in colors for y in colors}
        T = {
            (a, b, x, y): (x, y)
            for a in colors
            for b in colors
            for x in fibres[a]
            for y in fibres[b]
        }
        interval = LocalInterval(colors, fibres, base_R, T)
        self.assertEqual(interval.semisplit_audits(), [])
        self.assertEqual(interval.semisplit_boolean_assignments(), [])
        self.assertTrue(interval.is_local_minimal())

    def test_generated_congruence_derivation_rows_record_seed_and_transport(self):
        interval = size_three_affine_interval()
        audit = next(
            row
            for row in interval.pair_generated_local_minimality_audits()
            if row.left == 0 and row.right == 1
        ).generated

        self.assertEqual(audit.kind, "universal")
        self.assertEqual(audit.stable_depth, 1)
        self.assertEqual(audit.edge_count_rows, (("*", 3),))
        self.assertEqual(audit.derivation_count_rows, audit.edge_count_rows)
        self.assertEqual(audit.derivation_rows[0].source, "seed")
        self.assertEqual(audit.derivation_rows[0].depth, 0)
        self.assertTrue(
            any(
                row.depth == 1 and row.source != "seed" and row.crossing == ("*", "*")
                for row in audit.derivation_rows
            )
        )
        self.assertTrue(
            all(row.source_pairs or row.source == "seed" for row in audit.derivation_rows)
        )

    def test_continuation_congruence_detects_strand_continuing_rows(self):
        interval = one_color_flip_interval()

        audit = continuation_congruence_audit(interval)

        self.assertEqual(continuation_seed_rows(interval), ())
        self.assertEqual(continuation_seed_pairs(interval), {"*": ()})
        self.assertEqual(continuation_seed_pair_closure_audits(interval), ())
        self.assertEqual(continuation_seed_pair_closure_failures(interval), ())
        self.assertEqual(continuation_seed_universal_derivation_audits(interval), ())
        self.assertEqual(continuation_seed_universal_derivation_failures(interval), ())
        self.assertTrue(audit.base_rows_are_left_rack_form)
        self.assertTrue(audit.is_strand_continuing_on_the_nose)
        self.assertEqual(audit.generated.kind, "equality")
        self.assertTrue(audit.proves_transport_or_universal_dichotomy)

    def test_continuation_congruence_universal_for_local_minimal_flip_gap(self):
        interval = one_color_identity_interval()

        audit = continuation_congruence_audit(interval)

        self.assertEqual(audit.nontrivial_seed_count, 2)
        self.assertTrue(audit.base_rows_are_left_rack_form)
        self.assertFalse(audit.is_strand_continuing_on_the_nose)
        self.assertEqual(audit.generated.kind, "universal")
        self.assertTrue(audit.continuation_closure_is_universal)
        self.assertTrue(audit.proves_transport_or_universal_dichotomy)

        pair_audits = continuation_seed_pair_closure_audits(interval)
        self.assertEqual(len(pair_audits), 1)
        self.assertEqual(pair_audits[0].color, "*")
        self.assertEqual(pair_audits[0].generated.kind, "universal")
        self.assertEqual(pair_audits[0].generated.seed_pair_count, 1)
        self.assertEqual(len(pair_audits[0].seed_rows), 2)
        self.assertEqual(continuation_seed_pair_closure_failures(interval), ())

        derivation_audits = continuation_seed_universal_derivation_audits(interval)
        self.assertEqual(len(derivation_audits), 1)
        self.assertTrue(derivation_audits[0].closure_is_universal)
        self.assertTrue(derivation_audits[0].every_edge_has_derivation)
        self.assertEqual(derivation_audits[0].missing_derivation_count_rows, (("*", 0),))
        self.assertTrue(derivation_audits[0].proves_single_seed_universal_derivation)
        self.assertEqual(continuation_seed_universal_derivation_failures(interval), ())

    def test_continuation_universal_derivation_records_positive_depth_edges(self):
        interval = size_three_affine_interval()

        audits = continuation_seed_universal_derivation_audits(interval)

        self.assertEqual(len(audits), 1)
        self.assertEqual(audits[0].seed_closure.generated.stable_depth, 1)
        self.assertEqual(audits[0].edge_count_rows, (("*", 3),))
        self.assertEqual(audits[0].derivation_count_rows, (("*", 3),))
        self.assertEqual(audits[0].missing_derivation_count_rows, (("*", 0),))
        self.assertTrue(audits[0].proves_single_seed_universal_derivation)
        self.assertTrue(
            any(
                row.depth == 1 and row.source != "seed"
                for row in audits[0].seed_closure.generated.derivation_rows
            )
        )

    def test_continuation_seed_readout_propagates_admissible_universal_readout(self):
        interval = one_color_identity_interval()
        readout = {"*": (frozenset({0, 1}),)}

        audits = continuation_seed_readout_propagation_audits(interval, readout)

        self.assertEqual(len(audits), 1)
        self.assertTrue(audits[0].readout_is_admissible)
        self.assertTrue(audits[0].seed_contained)
        self.assertTrue(audits[0].generated_contained)
        self.assertEqual(audits[0].missing_generated_edges, ())
        self.assertTrue(audits[0].proves_readout_propagation)
        self.assertTrue(audits[0].forces_universal_readout)
        self.assertEqual(continuation_seed_readout_propagation_failures(interval, readout), ())

    def test_continuation_seed_readout_reports_missing_seed_and_edges(self):
        interval = one_color_identity_interval()
        readout = {"*": (frozenset({0}), frozenset({1}))}

        audits = continuation_seed_readout_propagation_audits(interval, readout)

        self.assertEqual(len(audits), 1)
        self.assertTrue(audits[0].readout_is_admissible)
        self.assertFalse(audits[0].seed_contained)
        self.assertFalse(audits[0].generated_contained)
        self.assertEqual(audits[0].missing_generated_edges, (("*", 0, 1),))
        self.assertFalse(audits[0].proves_readout_propagation)
        self.assertFalse(audits[0].forces_universal_readout)
        self.assertEqual(
            continuation_seed_readout_propagation_failures(interval, readout),
            audits,
        )

    def test_readout_kernel_audit_accepts_admissible_readout_labels(self):
        interval = one_color_identity_interval()
        labels = {"*": {0: "same", 1: "same"}}

        family = readout_kernel_family(interval, labels)
        audit = readout_kernel_audit(interval, labels)
        propagation = continuation_seed_readout_propagation_audits(
            interval,
            audit.family,
        )

        self.assertEqual(family, {"*": (frozenset({0, 1}),)})
        self.assertEqual(audit.family, family)
        self.assertEqual(audit.kind, "universal")
        self.assertEqual(audit.label_count_rows, (("*", 1),))
        self.assertEqual(audit.block_count_rows, (("*", 1),))
        self.assertTrue(audit.admissible)
        self.assertIsNone(audit.failure)
        self.assertTrue(audit.proves_readout_kernel_admissible)
        self.assertTrue(propagation[0].proves_readout_propagation)

    def test_readout_kernel_audit_rejects_nonadmissible_readout_labels(self):
        interval = two_color_swap_interval()
        labels = {
            "a": {0: "same", 1: "same"},
            "b": {0: "zero", 1: "one"},
        }

        audit = readout_kernel_audit(interval, labels)

        self.assertEqual(audit.kind, "semisplit_or_mixed")
        self.assertEqual(audit.label_count_rows, (("a", 1), ("b", 2)))
        self.assertEqual(audit.block_count_rows, (("a", 1), ("b", 2)))
        self.assertFalse(audit.admissible)
        self.assertFalse(audit.proves_readout_kernel_admissible)
        self.assertIsNotNone(audit.failure)
        self.assertEqual(audit.failure.side, "transported_not_target")

    def test_readout_descent_separation_certifies_strand_continuing_quotient(self):
        interval = one_color_identity_interval()
        labels = {"*": {0: "same", 1: "same"}}

        audit = readout_descent_separation_audit(interval, labels)

        self.assertTrue(audit.readout_is_admissible)
        self.assertEqual(audit.continuation.nontrivial_seed_count, 2)
        self.assertTrue(audit.continuation.base_rows_are_left_rack_form)
        self.assertEqual(audit.surviving_seed_rows, ())
        self.assertTrue(audit.all_continuation_seeds_killed)
        self.assertTrue(audit.all_seed_closures_propagate)
        self.assertTrue(audit.quotient_is_strand_continuing)
        self.assertTrue(audit.proves_descent_separation_readout)
        self.assertEqual(readout_descent_separation_failures(interval, labels), ())
        self.assertIsNotNone(audit.quotient_interval)
        self.assertIsNotNone(audit.quotient_continuation)
        self.assertEqual(audit.quotient_continuation.nontrivial_seed_count, 0)
        self.assertTrue(audit.quotient_continuation.is_strand_continuing_on_the_nose)

    def test_readout_kernel_quotient_interval_descends_local_table(self):
        interval = one_color_identity_interval()
        labels = {"*": {0: "same", 1: "same"}}

        quotient = readout_kernel_quotient_interval(interval, labels)
        family_quotient = quotient_interval_by_family(
            interval,
            readout_kernel_family(interval, labels),
        )

        self.assertEqual(quotient.fibres, family_quotient.fibres)
        self.assertTrue(quotient.is_colored_ybe())
        self.assertEqual(len(quotient.fibres["*"]), 1)
        block = quotient.fibres["*"][0]
        self.assertEqual(quotient.T[("*", "*", block, block)], (block, block))
        self.assertTrue(continuation_congruence_audit(quotient).is_strand_continuing_on_the_nose)

    def test_readout_seed_saturation_is_minimal_coarsening_that_kills_seeds(self):
        interval = one_color_identity_interval()
        labels = {"*": {0: "zero", 1: "one"}}

        audit = readout_seed_saturation_audit(interval, labels)

        self.assertEqual(audit.readout_kernel.kind, "equality")
        self.assertEqual(audit.saturation.kind, "universal")
        self.assertTrue(audit.saturation_contains_readout_kernel)
        self.assertFalse(audit.saturation_adds_no_new_edges)
        self.assertEqual(len(audit.original_surviving_seed_rows), 2)
        self.assertEqual(audit.saturated_readout_kernel.family, audit.saturation.family)
        self.assertEqual(audit.saturated_readout_kernel.kind, "universal")
        self.assertTrue(audit.saturated_descent.all_continuation_seeds_killed)
        self.assertTrue(audit.proves_admissible_seed_saturation)
        self.assertTrue(audit.proves_saturated_descent_separation)

        labels_from_saturation = partition_readout_labels(
            interval,
            audit.saturation.family,
        )
        self.assertEqual(labels_from_saturation, audit.saturated_labels)

    def test_readout_seed_saturation_adds_no_edges_when_no_seeds_survive(self):
        interval = one_color_flip_interval()
        labels = {"*": {0: "zero", 1: "one"}}

        audit = readout_seed_saturation_audit(interval, labels)

        self.assertEqual(audit.readout_kernel.kind, "equality")
        self.assertEqual(audit.saturation.kind, "equality")
        self.assertTrue(audit.saturation_adds_no_new_edges)
        self.assertEqual(audit.original_surviving_seed_rows, ())
        self.assertEqual(audit.new_saturation_edges, ())
        self.assertTrue(audit.proves_admissible_seed_saturation)
        self.assertTrue(audit.proves_saturated_descent_separation)

    def test_local_minimal_seed_saturation_dichotomy_records_universal_collapse(self):
        interval = one_color_identity_interval()
        labels = {"*": {0: "zero", 1: "one"}}

        audit = local_minimal_seed_saturation_dichotomy_audit(interval, labels)

        self.assertTrue(audit.interval_is_local_minimal)
        self.assertEqual(audit.expected_saturation_kind, "universal")
        self.assertTrue(audit.readout_kernel_has_local_minimal_kind)
        self.assertTrue(audit.saturation_has_local_minimal_kind)
        self.assertTrue(audit.forced_universal_collapse)
        self.assertTrue(audit.needs_external_routing_after_collapse)
        self.assertTrue(audit.proves_local_minimal_seed_saturation_dichotomy)

    def test_local_minimal_seed_saturation_dichotomy_keeps_rack_equality(self):
        interval = one_color_flip_interval()
        labels = {"*": {0: "zero", 1: "one"}}

        audit = local_minimal_seed_saturation_dichotomy_audit(interval, labels)

        self.assertTrue(audit.interval_is_local_minimal)
        self.assertEqual(audit.expected_saturation_kind, "equality")
        self.assertFalse(audit.forced_universal_collapse)
        self.assertFalse(audit.needs_external_routing_after_collapse)
        self.assertTrue(audit.proves_local_minimal_seed_saturation_dichotomy)

    def test_local_minimal_seed_saturation_dichotomy_rejects_nonminimal_interval(self):
        interval = two_color_identity_interval()
        labels = {
            "a": {0: "zero", 1: "one"},
            "b": {0: "zero", 1: "one"},
        }

        audit = local_minimal_seed_saturation_dichotomy_audit(interval, labels)

        self.assertFalse(audit.interval_is_local_minimal)
        self.assertFalse(audit.proves_local_minimal_seed_saturation_dichotomy)

    def test_product_readout_kernel_is_meet_of_factor_kernels(self):
        interval = two_color_identity_interval()
        collapse_a = {
            "a": {0: "same", 1: "same"},
            "b": {0: "zero", 1: "one"},
        }
        collapse_b = {
            "a": {0: "zero", 1: "one"},
            "b": {0: "same", 1: "same"},
        }

        labels = product_readout_labels(interval, collapse_a, collapse_b)
        audit = product_readout_kernel_audit(interval, collapse_a, collapse_b)

        self.assertEqual(labels["a"][0], ("same", "zero"))
        self.assertEqual(labels["b"][1], ("one", "same"))
        self.assertEqual(audit.product_audit.kind, "equality")
        self.assertTrue(audit.product_family_is_factor_meet)
        self.assertTrue(audit.all_factors_admissible)
        self.assertTrue(audit.product_audit.admissible)
        self.assertTrue(audit.proves_product_readout_kernel_admissible)
        self.assertEqual(audit.product_audit.family, audit.meet_family)

    def test_product_readout_kernel_records_nonadmissible_factor(self):
        interval = two_color_swap_interval()
        nonadmissible = {
            "a": {0: "same", 1: "same"},
            "b": {0: "zero", 1: "one"},
        }
        equality_labels = {
            "a": {0: "zero", 1: "one"},
            "b": {0: "zero", 1: "one"},
        }

        audit = product_readout_kernel_audit(interval, nonadmissible, equality_labels)

        self.assertFalse(audit.factor_audits[0].admissible)
        self.assertTrue(audit.factor_audits[1].admissible)
        self.assertTrue(audit.product_family_is_factor_meet)
        self.assertTrue(audit.product_audit.admissible)
        self.assertFalse(audit.all_factors_admissible)
        self.assertFalse(audit.proves_product_readout_kernel_admissible)

    def test_product_readout_descent_separation_requires_all_factors_to_kill_seed(self):
        interval = one_color_identity_interval()
        universal_left = {"*": {0: "same", 1: "same"}}
        universal_right = {"*": {0: "again", 1: "again"}}

        audit = product_readout_descent_separation_audit(
            interval,
            universal_left,
            universal_right,
        )

        self.assertTrue(audit.product_kernel.proves_product_readout_kernel_admissible)
        self.assertTrue(audit.product_survival_is_factor_union)
        self.assertTrue(audit.all_factor_seed_rows_killed)
        self.assertEqual(audit.product_surviving_seed_rows, ())
        self.assertEqual(audit.factor_survival_union, ())
        self.assertTrue(audit.descent.proves_descent_separation_readout)
        self.assertTrue(audit.proves_product_descent_separation)
        self.assertEqual(
            product_readout_descent_separation_failures(
                interval,
                universal_left,
                universal_right,
            ),
            (),
        )

    def test_product_readout_descent_separation_reports_factor_seed_survival(self):
        interval = one_color_identity_interval()
        universal_labels = {"*": {0: "same", 1: "same"}}
        equality_labels = {"*": {0: "zero", 1: "one"}}

        audit = product_readout_descent_separation_audit(
            interval,
            universal_labels,
            equality_labels,
        )

        self.assertTrue(audit.product_kernel.proves_product_readout_kernel_admissible)
        self.assertTrue(audit.product_survival_is_factor_union)
        self.assertEqual(audit.factor_surviving_seed_rows[0][1], ())
        self.assertEqual(len(audit.factor_surviving_seed_rows[1][1]), 2)
        self.assertEqual(
            set(audit.product_surviving_seed_rows),
            set(audit.factor_survival_union),
        )
        self.assertFalse(audit.all_factor_seed_rows_killed)
        self.assertFalse(audit.descent.proves_descent_separation_readout)
        self.assertFalse(audit.proves_product_descent_separation)

    def test_readout_descent_separation_reports_surviving_seed_rows(self):
        interval = one_color_identity_interval()
        labels = {"*": {0: "zero", 1: "one"}}

        audit = readout_descent_separation_audit(interval, labels)

        self.assertTrue(audit.readout_is_admissible)
        self.assertEqual(len(audit.surviving_seed_rows), 2)
        self.assertFalse(audit.all_continuation_seeds_killed)
        self.assertFalse(audit.all_seed_closures_propagate)
        self.assertFalse(audit.quotient_is_strand_continuing)
        self.assertFalse(audit.proves_descent_separation_readout)
        self.assertIsNotNone(audit.quotient_interval)
        self.assertIsNotNone(audit.quotient_continuation)
        self.assertEqual(audit.quotient_continuation.nontrivial_seed_count, 2)
        self.assertEqual(
            readout_descent_separation_failures(interval, labels),
            audit.surviving_seed_rows,
        )

    def test_readout_descent_separation_rejects_non_rack_base_rows(self):
        interval = two_color_identity_interval()
        labels = {
            "a": {0: "same", 1: "same"},
            "b": {0: "same", 1: "same"},
        }

        audit = readout_descent_separation_audit(interval, labels)

        self.assertTrue(audit.readout_is_admissible)
        self.assertFalse(audit.continuation.base_rows_are_left_rack_form)
        self.assertEqual(audit.surviving_seed_rows, ())
        self.assertFalse(audit.quotient_is_strand_continuing)
        self.assertFalse(audit.proves_descent_separation_readout)

    def test_continuation_congruence_records_non_rack_base_rows(self):
        interval = two_color_identity_interval()

        audit = continuation_congruence_audit(interval)

        self.assertFalse(audit.base_rows_are_left_rack_form)
        self.assertTrue(audit.non_rack_base_rows)
        self.assertFalse(audit.proves_transport_or_universal_dichotomy)

    def test_continuation_seed_pair_closure_exposes_nonminimal_rows(self):
        interval = two_color_identity_interval()

        self.assertFalse(interval.is_local_minimal())
        failures = continuation_seed_pair_closure_failures(interval)

        self.assertTrue(failures)
        self.assertTrue(all(failure.generated.kind != "universal" for failure in failures))
        self.assertTrue(continuation_seed_universal_derivation_failures(interval))


if __name__ == "__main__":
    unittest.main()
