import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    LocalInterval,
    LostEdgeExternalRoutingAudit,
    MissingTriangularCoordinateUnitRoutingAudit,
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
    latin_triangular_ybe_audit,
    local_minimal_descent_readout_collapse_audit,
    local_minimal_seed_saturation_dichotomy_audit,
    lost_edge_external_routing_audit,
    missing_triangular_coordinate_unit_routing_audit,
    missing_triangular_left_rack_cardinality_audit,
    missing_triangular_partial_constant_closure_audit,
    missing_triangular_partial_constant_continuation_route_audit,
    missing_triangular_row_profile_audit,
    one_color_latin_triangular_collapse_audit,
    partition_readout_labels,
    product_readout_descent_separation_audit,
    product_readout_descent_separation_failures,
    product_readout_kernel_audit,
    product_readout_labels,
    rack_kink_latin_triangular_collapse_audit,
    quotient_interval_by_family,
    readout_descent_separation_audit,
    readout_descent_separation_failures,
    readout_kernel_audit,
    readout_kernel_family,
    readout_kernel_quotient_interval,
    readout_seed_saturation_audit,
    right_rack_kink_latin_triangular_collapse_audit,
    section_kernel_companion_audit,
    section_rank_profile_collapse_audit,
    section_unit_row_audits,
    side_opposite_local_interval,
    triangular_bundle_audit,
    triangular_column_collapse_audit,
    triangular_constant_kernel_recovery_route_audit,
    triangular_latin_defect_closure_audit,
    triangular_recovery_audit,
    two_sided_unit_collapse_audit,
    universal_continuation_identity_routing_audit,
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


def one_color_singleton_identity_interval():
    colors = ("*",)
    fibres = {"*": (0,)}
    base_R = {("*", "*"): ("*", "*")}
    T = {("*", "*", 0, 0): (0, 0)}
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


def one_color_mixed_unit_bijection_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", 0, 0): (0, 0),
        ("*", "*", 0, 1): (1, 1),
        ("*", "*", 1, 0): (1, 0),
        ("*", "*", 1, 1): (0, 1),
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_proper_rank_loss_interval():
    colors = ("*",)
    fibres = {"*": (0, 1, 2)}
    base_R = {("*", "*"): ("*", "*")}
    values = {
        (0, 0): (0, 0),
        (0, 1): (0, 1),
        (0, 2): (1, 0),
        (1, 0): (1, 1),
        (1, 1): (1, 2),
        (1, 2): (2, 0),
        (2, 0): (2, 1),
        (2, 1): (2, 2),
        (2, 2): (0, 2),
    }
    return LocalInterval(
        colors,
        fibres,
        base_R,
        {
            ("*", "*", x, y): value
            for (x, y), value in values.items()
        },
    )


def two_color_nontrivial_triangular_bundle_interval():
    colors = ("a", "b")
    fibres = {"a": (0, 1, 2, 3), "b": ("p", "q")}
    base_R = {(left, right): (right, left) for left in colors for right in colors}
    T = {}
    for left in colors:
        for right in colors:
            for x in fibres[left]:
                for y in fibres[right]:
                    T[(left, right, x, y)] = (y, x)

    alpha = {0: "p", 1: "p", 2: "q", 3: "q"}
    beta = {
        0: {"p": 0, "q": 1},
        1: {"p": 2, "q": 3},
        2: {"p": 0, "q": 1},
        3: {"p": 2, "q": 3},
    }
    for x in fibres["a"]:
        for y in fibres["b"]:
            T[("a", "b", x, y)] = (alpha[x], beta[x][y])
    return LocalInterval(colors, fibres, base_R, T)


def two_color_partial_constant_missing_triangular_interval():
    colors = ("a", "b")
    fibres = {"a": (0, 1, 2), "b": ("p", "q")}
    base_R = {(left, right): (right, left) for left in colors for right in colors}
    T = {}
    for left in colors:
        for right in colors:
            for x in fibres[left]:
                for y in fibres[right]:
                    T[(left, right, x, y)] = (y, x)

    T[("a", "b", 0, "p")] = ("p", 0)
    T[("a", "b", 0, "q")] = ("p", 1)
    T[("a", "b", 1, "p")] = ("p", 2)
    T[("a", "b", 1, "q")] = ("q", 0)
    T[("a", "b", 2, "p")] = ("q", 1)
    T[("a", "b", 2, "q")] = ("q", 2)
    return LocalInterval(colors, fibres, base_R, T)


def one_color_latin_unit_triangular_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): (x, (x + y) % 2)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_right_latin_unit_triangular_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): ((x + y) % 2, y)
        for x in fibres["*"]
        for y in fibres["*"]
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

    def test_side_opposite_local_interval_is_involutive_and_preserves_ybe(self):
        interval = one_color_flip_interval()
        opposite = side_opposite_local_interval(interval)
        roundtrip = side_opposite_local_interval(opposite)

        self.assertTrue(opposite.is_colored_ybe())
        self.assertEqual(roundtrip.base_R, interval.base_R)
        self.assertEqual(roundtrip.T, interval.T)

    def test_side_opposite_turns_right_triangular_rows_left_triangular(self):
        interval = one_color_right_latin_unit_triangular_interval()
        opposite = side_opposite_local_interval(interval)

        self.assertEqual(opposite.T, one_color_latin_unit_triangular_interval().T)
        column = triangular_column_collapse_audit(opposite)
        self.assertEqual(
            tuple((row.side, row.left_color, row.right_color) for row in column.latin_unit_rows),
            (("left", "*", "*"),),
        )

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

    def test_two_sided_unit_collapse_accepts_strand_continuing_rack_row(self):
        interval = one_color_flip_interval()

        audit = two_sided_unit_collapse_audit(interval)

        self.assertTrue(audit.colored_ybe)
        self.assertTrue(audit.strand_continuing_case)
        self.assertTrue(audit.all_rows_two_sided_unit)
        self.assertTrue(audit.locally_nondegenerate_closed_branch)
        self.assertFalse(audit.mixed_unit_context_recovery_remaining)
        self.assertEqual(audit.only_mixed_unit_obstruction_rows, ())

    def test_two_sided_unit_collapse_detects_nonunit_continuation_row(self):
        interval = one_color_identity_interval()

        row_audit = section_unit_row_audits(interval)[0]
        audit = two_sided_unit_collapse_audit(interval)

        self.assertFalse(row_audit.all_left_sections_bijective)
        self.assertFalse(row_audit.all_right_sections_bijective)
        self.assertEqual(row_audit.left_nonunit_inputs, (0, 1))
        self.assertEqual(row_audit.right_nonunit_inputs, (0, 1))
        self.assertFalse(row_audit.row_has_unit_section)
        self.assertTrue(row_audit.row_has_nonunit_section)
        self.assertFalse(row_audit.row_is_mixed_unit)
        self.assertFalse(audit.all_rows_two_sided_unit)
        self.assertFalse(audit.locally_nondegenerate_closed_branch)
        self.assertFalse(audit.mixed_unit_context_recovery_remaining)
        self.assertEqual(audit.non_two_sided_rows, audit.row_audits)
        self.assertEqual(audit.only_mixed_unit_obstruction_rows, ())

    def test_two_sided_unit_collapse_closes_non_strand_two_sided_unit_row(self):
        interval = two_color_swap_interval()

        audit = two_sided_unit_collapse_audit(interval)

        self.assertTrue(audit.colored_ybe)
        self.assertFalse(audit.strand_continuing_case)
        self.assertTrue(audit.all_rows_two_sided_unit)
        self.assertTrue(audit.two_sided_unit_closed_branch)
        self.assertTrue(audit.locally_nondegenerate_closed_branch)
        self.assertFalse(audit.mixed_unit_context_recovery_remaining)

    def test_section_kernel_companion_audit_records_recovered_collisions(self):
        interval = one_color_identity_interval()

        audit = section_kernel_companion_audit(interval)

        self.assertTrue(audit.has_section_kernel)
        self.assertEqual(len(audit.left_section_collision_rows), 2)
        self.assertEqual(len(audit.right_section_collision_rows), 2)
        self.assertTrue(audit.every_collision_companion_separated)
        self.assertTrue(all(row.companion_outputs_distinct for row in audit.collision_rows))

        rack_interval = one_color_flip_interval()
        rack_audit = section_kernel_companion_audit(rack_interval)
        self.assertFalse(rack_audit.has_section_kernel)
        self.assertTrue(rack_audit.every_collision_companion_separated)

    def test_section_kernel_companion_audit_exposes_mixed_unit_seed_shape(self):
        interval = one_color_mixed_unit_bijection_interval()

        row_audit = section_unit_row_audits(interval)[0]
        companion = section_kernel_companion_audit(interval)

        self.assertTrue(row_audit.row_is_mixed_unit)
        self.assertTrue(row_audit.all_left_sections_bijective)
        self.assertFalse(row_audit.all_right_sections_bijective)
        self.assertEqual(row_audit.right_nonunit_inputs, (0, 1))
        self.assertEqual(companion.left_section_collision_rows, ())
        self.assertEqual(len(companion.right_section_collision_rows), 2)
        self.assertTrue(companion.every_collision_companion_separated)

    def test_section_rank_profile_collapse_splits_constant_and_proper_kernels(self):
        constant_interval = one_color_identity_interval()
        constant_audit = section_rank_profile_collapse_audit(constant_interval)

        self.assertEqual(len(constant_audit.nonunit_rows), 4)
        self.assertEqual(len(constant_audit.constant_section_rows), 4)
        self.assertEqual(constant_audit.proper_kernel_rows, ())
        self.assertTrue(constant_audit.hidden_kernel_rows_are_constant)
        self.assertEqual(
            constant_audit.hidden_kernel_rows_after_proper_profiles_removed,
            constant_audit.constant_section_rows,
        )

        proper_interval = one_color_proper_rank_loss_interval()
        proper_audit = section_rank_profile_collapse_audit(proper_interval)

        self.assertTrue(proper_audit.proper_kernel_rows)
        self.assertTrue(
            all(row.kernel_kind == "proper" for row in proper_audit.proper_kernel_rows)
        )
        self.assertTrue(any(row.rank == 2 for row in proper_audit.proper_kernel_rows))

    def test_section_rank_profile_collapse_separates_two_sided_unit_rows(self):
        interval = one_color_flip_interval()

        audit = section_rank_profile_collapse_audit(interval)

        self.assertEqual(audit.nonunit_rows, ())
        self.assertEqual(audit.constant_section_rows, ())
        self.assertEqual(audit.proper_kernel_rows, ())
        self.assertTrue(all(row.is_bijective for row in audit.rows))

    def test_triangular_bundle_audit_records_bijective_bundle_partition(self):
        interval = two_color_nontrivial_triangular_bundle_interval()

        audit = triangular_bundle_audit(interval)
        row = next(
            row
            for row in audit.left_triangular_rows
            if row.left_color == "a" and row.right_color == "b"
        )

        self.assertTrue(row.bundle_partition_identity_holds)
        self.assertFalse(row.constant_map_is_bijective)
        self.assertEqual(len(row.nontrivial_bundle_fibres), 2)
        self.assertTrue(all(fibre.blocks_partition_companion_codomain for fibre in row.bundle_fibres))
        self.assertEqual(
            {fibre.output_value: fibre.block_sizes for fibre in row.bundle_fibres},
            {"p": (2, 2), "q": (2, 2)},
        )

    def test_triangular_bundle_audit_identifies_permutation_triangular_rows(self):
        interval = one_color_identity_interval()

        audit = triangular_bundle_audit(interval)

        self.assertEqual(len(audit.left_triangular_rows), 1)
        self.assertEqual(len(audit.right_triangular_rows), 1)
        self.assertTrue(audit.every_bundle_partition_identity_holds)
        self.assertEqual(audit.rows_with_nontrivial_bundles, ())
        self.assertTrue(all(row.constant_map_is_bijective for row in audit.row_audits))

    def test_triangular_recovery_audit_inverts_nontrivial_bundle_row(self):
        interval = two_color_nontrivial_triangular_bundle_interval()

        audit = triangular_recovery_audit(interval)
        row = next(
            row
            for row in audit.row_audits
            if row.side == "left" and row.left_color == "a" and row.right_color == "b"
        )

        self.assertTrue(row.recovery_formula_bijective)
        self.assertEqual(row.missing_or_ambiguous_outputs, ())
        recovered = {
            (entry.output_left, entry.output_right):
            (entry.recovered_left_input, entry.recovered_right_input)
            for entry in row.entries
        }
        self.assertEqual(recovered[("p", 0)], (0, "p"))
        self.assertEqual(recovered[("p", 3)], (1, "q"))
        self.assertEqual(recovered[("q", 0)], (2, "p"))
        self.assertEqual(recovered[("q", 3)], (3, "q"))

    def test_triangular_recovery_audit_inverts_permutation_triangular_rows(self):
        interval = one_color_identity_interval()

        audit = triangular_recovery_audit(interval)

        self.assertEqual(len(audit.row_audits), 2)
        self.assertTrue(audit.every_recovery_formula_bijective)
        self.assertEqual(audit.rows_with_recovery_failures, ())

    def test_triangular_column_collapse_identifies_product_rows(self):
        interval = one_color_identity_interval()

        audit = triangular_column_collapse_audit(interval)

        self.assertEqual(len(audit.row_audits), 2)
        self.assertEqual(len(audit.product_collapse_rows), 2)
        self.assertEqual(audit.latin_unit_rows, ())
        self.assertTrue(
            all(
                row.constant_map_is_bijective
                and row.companion_sections_bijective
                and row.opposite_sections_all_constant
                and row.has_hidden_nonunit_opposite_section
                and row.hidden_nonunit_opposite_forces_product_verified
                for row in audit.product_collapse_rows
            )
        )
        self.assertEqual(audit.hidden_nonunit_opposite_without_product_rows, ())

    def test_triangular_column_collapse_identifies_latin_unit_rows(self):
        interval = one_color_latin_unit_triangular_interval()

        audit = triangular_column_collapse_audit(interval)

        self.assertEqual(len(audit.row_audits), 1)
        row = audit.row_audits[0]
        self.assertTrue(row.latin_unit_triangular)
        self.assertFalse(row.product_collapse_for_hidden_nonunit)
        self.assertTrue(row.opposite_sections_all_bijective)
        self.assertEqual(audit.latin_unit_rows, (row,))
        self.assertEqual(audit.product_collapse_rows, ())
        self.assertTrue(row.companion_nonbijective_requires_constant_kernel)
        self.assertFalse(row.has_hidden_nonunit_opposite_section)

    def test_triangular_column_collapse_records_constant_map_kernel_type(self):
        interval = two_color_nontrivial_triangular_bundle_interval()

        audit = triangular_column_collapse_audit(interval)

        row = audit.row_audits[0]
        self.assertEqual((row.side, row.left_color, row.right_color), ("left", "a", "b"))
        self.assertTrue(row.constant_map_surjective)
        self.assertFalse(row.constant_map_is_bijective)
        self.assertEqual(row.constant_kernel_kind, "proper")
        self.assertEqual(row.constant_kernel_blocks, ((0, 1), (2, 3)))
        self.assertTrue(row.constant_map_has_proper_kernel)
        self.assertFalse(row.constant_map_is_constant)
        self.assertTrue(
            all(section.is_injective_non_surjective for section in row.companion_sections)
        )
        self.assertTrue(row.companion_sections_injective)
        self.assertFalse(row.companion_sections_have_kernel)
        self.assertTrue(row.companion_nonbijective_requires_constant_kernel)
        self.assertEqual(audit.constant_map_non_surjective_rows, ())
        self.assertEqual(audit.companion_kernel_rows, ())
        self.assertEqual(audit.companion_nonbijective_without_constant_kernel_rows, ())

    def test_triangular_latin_defect_closure_records_generated_seed_kinds(self):
        interval = two_color_nontrivial_triangular_bundle_interval()

        audit = triangular_latin_defect_closure_audit(interval)

        constant_rows = tuple(
            row for row in audit.rows if row.defect == "constant_map_kernel"
        )
        self.assertEqual(
            tuple(row.collapsed_inputs for row in constant_rows),
            ((0, 1), (2, 3)),
        )
        self.assertTrue(audit.all_kernel_edges_force_universal_closure)
        self.assertEqual(audit.proper_closure_rows, ())
        self.assertEqual(len(audit.universal_closure_rows), len(audit.rows))

    def test_triangular_constant_kernel_recovery_routes_universal_edges(self):
        interval = two_color_nontrivial_triangular_bundle_interval()

        audit = triangular_constant_kernel_recovery_route_audit(interval)

        self.assertEqual(len(audit.rows), 2)
        self.assertTrue(audit.all_universal_constant_kernel_edges_route_to_recovery)
        self.assertEqual(audit.unrouted_universal_rows, ())
        self.assertEqual(
            tuple(row.collapsed_inputs for row in audit.rows),
            ((0, 1), (2, 3)),
        )
        self.assertTrue(
            all(row.recovery_separates_kernel_edge for row in audit.rows)
        )
        first = audit.rows[0]
        self.assertEqual(
            first.witness_output_pairs,
            (
                (0, (("p", 0), ("p", 1))),
                (1, (("p", 2), ("p", 3))),
            ),
        )

    def test_missing_triangular_row_profile_explains_nonconstant_sides(self):
        affine = missing_triangular_row_profile_audit(size_three_affine_interval())

        self.assertEqual(len(affine.rows), 2)
        self.assertTrue(
            all(
                row.explanation == "coordinate_side_unit_not_triangular"
                for row in affine.rows
            )
        )
        self.assertEqual(affine.coordinate_unit_rows, affine.rows)
        self.assertEqual(affine.proper_kernel_rows, ())

        rank_loss = missing_triangular_row_profile_audit(
            one_color_proper_rank_loss_interval()
        )
        self.assertEqual(
            tuple(row.explanation for row in rank_loss.rows),
            ("proper_section_kernel_visible", "proper_section_kernel_visible"),
        )
        self.assertEqual(rank_loss.proper_kernel_rows, rank_loss.rows)

    def test_missing_triangular_row_profile_identifies_partial_constant_mixed_unit(self):
        interval = two_color_partial_constant_missing_triangular_interval()

        audit = missing_triangular_row_profile_audit(interval)

        row = next(
            row
            for row in audit.rows
            if (row.side, row.left_color, row.right_color) == ("left", "a", "b")
        )
        self.assertEqual(row.explanation, "partial_constant_hidden_rank_loss")
        self.assertEqual(row.constant_section_inputs, (0, 2))
        self.assertEqual(row.unit_section_inputs, (1,))
        self.assertEqual(row.nonunit_section_inputs, (0, 2))
        self.assertTrue(row.partial_constant_mixed_unit_context)
        self.assertIn(row, audit.partial_constant_mixed_unit_rows)
        self.assertEqual(audit.nonconstant_hidden_rows, ())
        self.assertEqual(audit.unclassified_rows, ())
        self.assertTrue(audit.finite_map_classification_exhaustive)

    def test_missing_triangular_left_rack_cardinality_closes_injective_profiles(self):
        interval = two_color_partial_constant_missing_triangular_interval()

        audit = missing_triangular_left_rack_cardinality_audit(interval)

        self.assertTrue(audit.base_rows_are_left_rack_form)
        self.assertTrue(audit.all_section_domains_match_codomain)
        self.assertEqual(audit.unequal_section_rows, ())
        self.assertEqual(audit.injective_non_surjective_rows, ())
        self.assertTrue(audit.injective_non_surjective_rows_eliminated)
        self.assertEqual(audit.nonconstant_hidden_rows, ())
        self.assertEqual(audit.unclassified_rows, ())
        self.assertTrue(
            audit.proves_left_rack_missing_triangular_cardinality_closure
        )

    def test_missing_triangular_partial_constant_closure_records_seed_edges(self):
        interval = two_color_partial_constant_missing_triangular_interval()

        audit = missing_triangular_partial_constant_closure_audit(interval)

        self.assertEqual(len(audit.rows), 2)
        self.assertTrue(audit.all_partial_constant_edges_force_universal_closure)
        self.assertEqual(audit.proper_closure_rows, ())
        self.assertEqual(audit.universal_closure_rows, audit.rows)
        self.assertEqual(
            tuple(
                (
                    row.side,
                    row.left_color,
                    row.right_color,
                    row.fixed_input,
                    row.domain_color,
                    row.collapsed_inputs,
                    row.closure_kind,
                )
                for row in audit.rows
            ),
            (
                ("left", "a", "b", 0, "b", ("p", "q"), "universal"),
                ("left", "a", "b", 2, "b", ("p", "q"), "universal"),
            ),
        )

    def test_missing_triangular_partial_constant_routes_to_continuation_seed(self):
        interval = two_color_partial_constant_missing_triangular_interval()

        audit = missing_triangular_partial_constant_continuation_route_audit(
            interval
        )

        self.assertEqual(len(audit.rows), 2)
        self.assertTrue(audit.all_partial_constant_edges_route_to_continuation)
        self.assertEqual(audit.unrouted_rows, ())
        self.assertEqual(audit.universal_continuation_rows, audit.rows)
        self.assertEqual(
            tuple(
                (
                    row.fixed_input,
                    row.collapsed_inputs,
                    row.companion_outputs,
                    row.continuation_seed_closure_kinds,
                    row.partial_edge_contained_in_seed_closure,
                    row.status,
                    tuple(
                        (
                            witness.left_input,
                            witness.right_input,
                            witness.continuing_output,
                        )
                        for witness in row.continuation_seed_witnesses
                    ),
                )
                for row in audit.rows
            ),
            (
                (
                    0,
                    ("p", "q"),
                    (0, 1),
                    ("universal",),
                    True,
                    "routed_to_universal_continuation_seed",
                    ((0, "q", 1),),
                ),
                (
                    2,
                    ("p", "q"),
                    (1, 2),
                    ("universal",),
                    True,
                    "routed_to_universal_continuation_seed",
                    ((2, "p", 1),),
                ),
            ),
        )

    def test_missing_triangular_coordinate_unit_routing_closes_affine_pair(self):
        audit = missing_triangular_coordinate_unit_routing_audit(
            size_three_affine_interval()
        )

        self.assertTrue(audit.colored_ybe)
        self.assertTrue(audit.locally_nondegenerate_closed_branch)
        self.assertEqual(len(audit.rows), 1)
        row = audit.rows[0]
        self.assertEqual(row.coordinate_unit_sides, ("left", "right"))
        self.assertEqual(row.left_explanation, "coordinate_side_unit_not_triangular")
        self.assertEqual(row.right_explanation, "coordinate_side_unit_not_triangular")
        self.assertEqual(row.status, "two_sided_unit_pair")
        self.assertEqual(audit.mixed_unit_context_rows, ())
        self.assertEqual(audit.unrouted_rows, ())
        self.assertTrue(audit.all_coordinate_unit_rows_routed)

    def test_missing_triangular_coordinate_unit_routing_finds_mixed_partner(self):
        interval = two_color_partial_constant_missing_triangular_interval()

        audit = missing_triangular_coordinate_unit_routing_audit(interval)

        row = next(
            row
            for row in audit.rows
            if (row.left_color, row.right_color) == ("a", "b")
        )
        self.assertEqual(row.coordinate_unit_sides, ("right",))
        self.assertEqual(row.left_explanation, "partial_constant_hidden_rank_loss")
        self.assertEqual(row.right_explanation, "coordinate_side_unit_not_triangular")
        self.assertEqual(row.status, "mixed_unit_context")
        self.assertIn(row, audit.mixed_unit_context_rows)
        self.assertEqual(audit.unrouted_rows, ())

    def test_coordinate_unit_routing_ledger_is_not_vacuous(self):
        audit = MissingTriangularCoordinateUnitRoutingAudit(
            colored_ybe=True,
            locally_nondegenerate_closed_branch=True,
            rows=(),
        )

        self.assertFalse(audit.all_coordinate_unit_rows_routed)
        self.assertFalse(audit.proves_coordinate_unit_routing_ledger)

    def test_latin_triangular_ybe_audit_accepts_singleton_ybe_row(self):
        interval = one_color_singleton_identity_interval()

        audit = latin_triangular_ybe_audit(interval)

        self.assertEqual(len(audit.latin_left_rows), 1)
        self.assertEqual(len(audit.triple_audits), 1)
        self.assertTrue(audit.all_alpha_cocycles_hold)
        self.assertTrue(audit.all_companion_equations_hold)
        self.assertTrue(audit.all_equations_hold)

    def test_latin_triangular_ybe_audit_exposes_endpoint_shear_failure(self):
        interval = one_color_latin_unit_triangular_interval()

        audit = latin_triangular_ybe_audit(interval)

        self.assertEqual(len(audit.triple_audits), 1)
        self.assertTrue(audit.all_alpha_cocycles_hold)
        self.assertFalse(audit.all_companion_equations_hold)
        self.assertFalse(audit.all_equations_hold)
        self.assertTrue(audit.triples_with_endpoint_shear_failures)

    def test_one_color_latin_triangular_collapse_routes_identity_to_product(self):
        interval = one_color_identity_interval()

        audit = one_color_latin_triangular_collapse_audit(interval)[0]

        self.assertTrue(audit.colored_ybe)
        self.assertTrue(audit.alpha_is_identity)
        self.assertTrue(audit.companion_sections_are_identity)
        self.assertFalse(audit.row_is_latin_unit_triangular)
        self.assertTrue(audit.one_color_latin_obstruction_eliminated)

    def test_one_color_latin_triangular_collapse_rejects_latin_shear_ybe(self):
        interval = one_color_latin_unit_triangular_interval()

        audit = one_color_latin_triangular_collapse_audit(interval)[0]

        self.assertFalse(audit.colored_ybe)
        self.assertTrue(audit.row_is_latin_unit_triangular)
        self.assertTrue(audit.companion_identity_failures)
        self.assertFalse(audit.nontrivial_latin_unit_ybe_candidate)
        self.assertTrue(audit.one_color_latin_obstruction_eliminated)

    def test_rack_kink_latin_triangular_collapse_accepts_singletons(self):
        interval = one_color_singleton_identity_interval()

        audit = rack_kink_latin_triangular_collapse_audit(interval)

        self.assertTrue(audit.base_is_finite_rack)
        self.assertTrue(audit.theorem_hypotheses_hold)
        self.assertTrue(audit.kink_cancellation_verified)
        self.assertTrue(audit.all_latin_fibres_forced_singleton)
        self.assertEqual(audit.non_singleton_latin_colors, ())

    def test_rack_kink_latin_triangular_collapse_rejects_non_ybe_shear(self):
        interval = one_color_latin_unit_triangular_interval()

        audit = rack_kink_latin_triangular_collapse_audit(interval)

        self.assertTrue(audit.base_is_finite_rack)
        self.assertTrue(audit.latin_rows_present_for_all_pairs)
        self.assertFalse(audit.latin_ybe_equations_hold)
        self.assertTrue(audit.kink_column_constancy_failures)
        self.assertTrue(audit.nontrivial_latin_obstruction_eliminated)

    def test_right_rack_kink_latin_triangular_collapse_accepts_singletons(self):
        interval = side_opposite_local_interval(one_color_singleton_identity_interval())

        audit = right_rack_kink_latin_triangular_collapse_audit(interval)

        self.assertTrue(audit.base_is_finite_right_rack)
        self.assertTrue(audit.theorem_hypotheses_hold)
        self.assertTrue(audit.diagonal_cancellation_verified)
        self.assertTrue(audit.all_latin_fibres_forced_singleton)
        self.assertEqual(audit.non_singleton_latin_colors, ())

    def test_right_rack_kink_latin_triangular_collapse_rejects_non_ybe_shear(self):
        interval = side_opposite_local_interval(
            one_color_right_latin_unit_triangular_interval()
        )

        audit = right_rack_kink_latin_triangular_collapse_audit(interval)

        self.assertTrue(audit.base_is_finite_right_rack)
        self.assertTrue(audit.latin_rows_present_for_all_pairs)
        self.assertFalse(audit.latin_ybe_equations_hold)
        self.assertTrue(audit.diagonal_column_constancy_failures)
        self.assertTrue(audit.nontrivial_latin_obstruction_eliminated)

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

    def test_local_minimal_descent_readout_collapse_keeps_equality_no_seed_case(self):
        interval = one_color_flip_interval()
        labels = {"*": {0: "zero", 1: "one"}}

        audit = local_minimal_descent_readout_collapse_audit(interval, labels)

        self.assertTrue(audit.interval_is_local_minimal)
        self.assertEqual(audit.readout_kind, "equality")
        self.assertFalse(audit.has_nontrivial_continuation_seed)
        self.assertTrue(audit.equality_case_is_strand_continuing)
        self.assertFalse(audit.universal_case_needs_external_recovery)
        self.assertTrue(audit.nontrivial_seed_forces_universal)
        self.assertTrue(audit.proves_local_minimal_descent_readout_collapse)

    def test_local_minimal_descent_readout_collapse_flags_universal_seed_case(self):
        interval = one_color_identity_interval()
        labels = {"*": {0: "same", 1: "same"}}

        audit = local_minimal_descent_readout_collapse_audit(interval, labels)

        self.assertTrue(audit.interval_is_local_minimal)
        self.assertEqual(audit.readout_kind, "universal")
        self.assertTrue(audit.has_nontrivial_continuation_seed)
        self.assertFalse(audit.equality_case_is_strand_continuing)
        self.assertTrue(audit.universal_case_needs_external_recovery)
        self.assertTrue(audit.nontrivial_seed_forces_universal)
        self.assertTrue(audit.proves_local_minimal_descent_readout_collapse)

    def test_local_minimal_descent_readout_collapse_rejects_nonminimal_interval(self):
        interval = two_color_identity_interval()
        labels = {
            "a": {0: "zero", 1: "one"},
            "b": {0: "zero", 1: "one"},
        }

        audit = local_minimal_descent_readout_collapse_audit(interval, labels)

        self.assertFalse(audit.interval_is_local_minimal)
        self.assertFalse(audit.proves_local_minimal_descent_readout_collapse)

    def test_lost_edge_external_routing_records_routed_collapse_edges(self):
        interval = one_color_identity_interval()
        descent_labels = {"*": {0: "zero", 1: "one"}}
        routing_labels = {"*": {0: "left", 1: "right"}}

        audit = lost_edge_external_routing_audit(
            interval,
            descent_labels,
            routing_labels,
        )

        self.assertTrue(audit.forced_collapse_requires_routing)
        self.assertEqual(len(audit.lost_edges), 1)
        self.assertEqual(set(audit.routed_edges), set(audit.lost_edges))
        self.assertEqual(audit.unrouted_edges, ())
        self.assertTrue(audit.has_required_lost_edges)
        self.assertTrue(audit.lost_edges_match_saturation)
        self.assertTrue(audit.routed_unrouted_edges_partition_lost_edges)
        self.assertTrue(audit.routed_edges_are_distinguished)
        self.assertTrue(audit.unrouted_edges_are_not_distinguished)
        self.assertTrue(audit.all_lost_edges_routed)
        self.assertTrue(audit.proves_external_routing_ledger)

    def test_lost_edge_external_routing_rejects_empty_forced_ledger(self):
        interval = one_color_identity_interval()
        real = lost_edge_external_routing_audit(
            interval,
            {"*": {0: "zero", 1: "one"}},
            {"*": {0: "left", 1: "right"}},
        )
        forged = LostEdgeExternalRoutingAudit(
            dichotomy=real.dichotomy,
            routing_labels=real.routing_labels,
            routing_kernel=real.routing_kernel,
            lost_edges=(),
            routed_edges=(),
            unrouted_edges=(),
        )

        self.assertTrue(forged.forced_collapse_requires_routing)
        self.assertFalse(forged.has_required_lost_edges)
        self.assertFalse(forged.lost_edges_match_saturation)
        self.assertTrue(forged.routed_unrouted_edges_partition_lost_edges)
        self.assertFalse(forged.all_lost_edges_routed)
        self.assertFalse(forged.proves_external_routing_ledger)

    def test_lost_edge_external_routing_reports_unrouted_collapse_edges(self):
        interval = one_color_identity_interval()
        descent_labels = {"*": {0: "zero", 1: "one"}}
        routing_labels = {"*": {0: "same", 1: "same"}}

        audit = lost_edge_external_routing_audit(
            interval,
            descent_labels,
            routing_labels,
        )

        self.assertTrue(audit.forced_collapse_requires_routing)
        self.assertEqual(len(audit.lost_edges), 1)
        self.assertEqual(audit.routed_edges, ())
        self.assertEqual(set(audit.unrouted_edges), set(audit.lost_edges))
        self.assertFalse(audit.all_lost_edges_routed)
        self.assertFalse(audit.proves_external_routing_ledger)

    def test_universal_continuation_identity_routing_is_canonical_lost_edge_ledger(self):
        interval = two_color_partial_constant_missing_triangular_interval()

        audit = universal_continuation_identity_routing_audit(interval)

        self.assertTrue(audit.equality_descent_readout)
        self.assertTrue(audit.saturation_is_universal)
        self.assertTrue(audit.has_nontrivial_continuation_seed)
        self.assertTrue(audit.identity_routing_is_admissible)
        self.assertTrue(audit.routes_all_saturation_lost_edges)
        self.assertTrue(audit.proves_identity_routed_universal_continuation)
        self.assertEqual(audit.routing.unrouted_edges, ())
        self.assertEqual(
            audit.routing.lost_edges,
            (
                ("a", 0, 1),
                ("a", 0, 2),
                ("a", 1, 2),
                ("b", "p", "q"),
            ),
        )

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
