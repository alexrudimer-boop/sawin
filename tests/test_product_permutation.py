import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    LocalInterval,
    apply_product_permutation_action,
    artin_longitudes,
    artin_longitude_row_column_sums,
    branch_tags,
    bounded_words,
    direct_product_coboundary_audit,
    direct_product_cocycle_failures,
    direct_product_action,
    direct_product_label_group,
    direct_product_label_pair_closure_audits,
    direct_product_label_pair_closure_failures,
    direct_product_witness,
    direct_product_label_word_action,
    direct_product_holonomy_summary,
    evaluate_direct_product_label_word,
    identity_solution,
    identity_base_direct_reduction,
    identity_base_swapped_reduction,
    is_nondegenerate,
    local_master_bottleneck_summary,
    one_color_swapped_label_exponent_action,
    first_nonidentity_product_closed_label,
    product_closed_label_blind_movers,
    product_closed_label_common_longitude_assignments,
    product_closed_label_exact_audit,
    product_closed_label_longitude_subgroup_audit,
    product_closed_label_longitude_subgroup_failures,
    product_closed_label_longitude_route_audit,
    product_closed_label_longitude_witnesses,
    product_closed_label_permutations,
    product_permutation_action,
    product_coboundary_transport_is_identity,
    product_coboundary_transport_map,
    product_holonomy_closed_label_permutations,
    product_holonomy_exact_audit,
    product_holonomy_groups,
    product_holonomy_label_permutation,
    product_holonomy_longitude_subgroup_audit,
    product_holonomy_longitude_subgroup_failures,
    product_label_permutation_image,
    product_label_word_permutation,
    rack_solution,
    evaluate_swapped_product_label_word,
    sharp_kernel_implication_failures,
    solution_from_local_interval,
    swapped_product_coboundary_audit,
    swapped_product_cocycle_failures,
    swapped_product_label_group,
    swapped_product_label_pair_closure_audits,
    swapped_product_label_pair_closure_failures,
    swapped_product_holonomy_summary,
    swapped_product_invariant_families,
    swapped_product_label_word_action,
    direct_product_invariant_families,
)
from ybe_domination.finite_group import cyclic_group
from ybe_domination.finite_group import symmetric_group
from ybe_domination.product_permutation import _compose_maps, _invert_map


def one_color_permutation_interval():
    points = (0, 1, 2)
    left = {0: 1, 1: 2, 2: 0}
    right = {0: 0, 1: 2, 2: 1}
    return LocalInterval(
        colors=("*",),
        fibres={"*": points},
        base_R={("*", "*"): ("*", "*")},
        T={("*", "*", x, y): (left[y], right[x]) for x in points for y in points},
    )


def one_color_flip_interval():
    points = (0, 1, 2)
    return LocalInterval(
        colors=("*",),
        fibres={"*": points},
        base_R={("*", "*"): ("*", "*")},
        T={("*", "*", x, y): (y, x) for x in points for y in points},
    )


def one_color_commuting_swapped_interval():
    points = (0, 1, 2)
    cycle = {0: 1, 1: 2, 2: 0}
    return LocalInterval(
        colors=("*",),
        fibres={"*": points},
        base_R={("*", "*"): ("*", "*")},
        T={("*", "*", x, y): (cycle[y], cycle[x]) for x in points for y in points},
    )


def one_color_prime_cycle_interval():
    points = (0, 1, 2, 3, 4)
    cycle = {point: (point + 1) % 5 for point in points}
    identity = {point: point for point in points}
    return LocalInterval(
        colors=("*",),
        fibres={"*": points},
        base_R={("*", "*"): ("*", "*")},
        T={("*", "*", x, y): (cycle[y], identity[x]) for x in points for y in points},
    )


def one_color_klein_regular_interval():
    points = (0, 1, 2, 3)
    flip_low_bit = {point: point ^ 1 for point in points}
    flip_high_bit = {point: point ^ 2 for point in points}
    return LocalInterval(
        colors=("*",),
        fibres={"*": points},
        base_R={("*", "*"): ("*", "*")},
        T={
            ("*", "*", x, y): (flip_low_bit[y], flip_high_bit[x])
            for x in points
            for y in points
        },
    )


def two_color_direct_product_interval():
    colors = (0, 1)
    points = (0, 1)
    fibres = {0: points, 1: points}
    base_R = {(a, b): (b, a) for a in colors for b in colors}
    gauge = {
        0: {0: 0, 1: 1},
        1: {0: 1, 1: 0},
    }

    def inverse(mapping):
        return {value: key for key, value in mapping.items()}

    def compose(left, right):
        return {key: left[right[key]] for key in right}

    table = {}
    for a, b in product(colors, repeat=2):
        c, d = base_R[(a, b)]
        left_map = compose(inverse(gauge[c]), gauge[a])
        right_map = compose(inverse(gauge[d]), gauge[b])
        for x in points:
            for y in points:
                table[(a, b, x, y)] = (left_map[x], right_map[y])
    return LocalInterval(colors, fibres, base_R, table)


def two_color_swapped_coboundary_interval():
    colors = (0, 1)
    points = (0, 1)
    fibres = {0: points, 1: points}
    base_R = {(a, b): (a, b) for a in colors for b in colors}
    gauge = {
        0: {0: 0, 1: 1},
        1: {0: 1, 1: 0},
    }

    def inverse(mapping):
        return {value: key for key, value in mapping.items()}

    def compose(left, right):
        return {key: left[right[key]] for key in right}

    table = {}
    for a, b in product(colors, repeat=2):
        c, d = base_R[(a, b)]
        left_map = compose(inverse(gauge[c]), gauge[b])
        right_map = compose(inverse(gauge[d]), gauge[a])
        for x in points:
            for y in points:
                table[(a, b, x, y)] = (left_map[y], right_map[x])
    return LocalInterval(colors, fibres, base_R, table)


def two_color_identity_base_cyclic_interval():
    colors = (0, 1)
    points = (0, 1, 2)
    fibres = {0: points, 1: points}
    cycle = {0: 1, 1: 2, 2: 0}
    identity = {point: point for point in points}
    base_R = {(a, b): (a, b) for a in colors for b in colors}
    left = {
        (0, 0): identity,
        (0, 1): cycle,
        (1, 0): identity,
        (1, 1): identity,
    }
    right = {
        key: _compose_maps(cycle, _invert_map(mapping))
        for key, mapping in left.items()
    }
    table = {}
    for a, b in product(colors, repeat=2):
        for x, y in product(points, repeat=2):
            table[(a, b, x, y)] = (left[(a, b)][y], right[(a, b)][x])
    return LocalInterval(colors, fibres, base_R, table)


def two_color_identity_base_direct_interval(nontrivial=False):
    colors = (0, 1)
    points = (0, 1)
    fibres = {0: points, 1: points}
    base_R = {(a, b): (a, b) for a in colors for b in colors}
    identity = {0: 0, 1: 1}
    flip = {0: 1, 1: 0}
    table = {}
    for a, b in product(colors, repeat=2):
        left = flip if nontrivial and (a, b) == (0, 1) else identity
        right = identity
        for x, y in product(points, repeat=2):
            table[(a, b, x, y)] = (left[x], right[y])
    return LocalInterval(colors, fibres, base_R, table)


def two_color_product_known_nondegenerate_failure_interval():
    colors = (0, 1)
    points = (0, 1)
    fibres = {0: points, 1: points}
    base_R = {
        (0, 0): (0, 1),
        (0, 1): (1, 1),
        (1, 0): (0, 0),
        (1, 1): (1, 0),
    }
    rows = [
        ((0, 0, 0, 0), (0, 0)),
        ((0, 0, 0, 1), (1, 0)),
        ((0, 0, 1, 0), (0, 1)),
        ((0, 0, 1, 1), (1, 1)),
        ((0, 1, 0, 0), (0, 0)),
        ((0, 1, 0, 1), (1, 0)),
        ((0, 1, 1, 0), (0, 1)),
        ((0, 1, 1, 1), (1, 1)),
        ((1, 0, 0, 0), (0, 1)),
        ((1, 0, 0, 1), (1, 1)),
        ((1, 0, 1, 0), (0, 0)),
        ((1, 0, 1, 1), (1, 0)),
        ((1, 1, 0, 0), (0, 1)),
        ((1, 1, 0, 1), (1, 1)),
        ((1, 1, 1, 0), (0, 0)),
        ((1, 1, 1, 1), (1, 0)),
    ]
    return LocalInterval(colors, fibres, base_R, dict(rows))


def family_key(family):
    return tuple(sorted((repr(color), repr(partition)) for color, partition in family.items()))


class ProductPermutationTests(unittest.TestCase):
    def test_decomposition_matches_total_action(self):
        interval = one_color_permutation_interval()
        qmap = solution_from_local_interval(interval)
        base = ("*", "*", "*")
        words = [
            tuple(),
            (1,),
            (1, 2, 1),
            (2, -1, 2, 1),
            (1, 1, -2, 1),
        ]
        for word in words:
            action = product_permutation_action(interval, base, word)
            for fibre_tuple in product(interval.fibres["*"], repeat=3):
                total_tuple = tuple(("*", point) for point in fibre_tuple)
                image = qmap.total.braid_action(word, total_tuple)
                self.assertEqual(
                    tuple(point for _color, point in image),
                    apply_product_permutation_action(action, fibre_tuple),
                )

    def test_swapped_label_words_evaluate_to_coordinate_maps(self):
        interval = two_color_identity_base_cyclic_interval()
        base = (0, 1, 0, 1)
        words = [
            tuple(),
            (1,),
            (1, 2, 1),
            (2, -1, 3, 2, 1),
            (1, 1, -2, 3, -1, 2),
        ]
        initial_colors = tuple(base)
        for word in words:
            action = product_permutation_action(interval, base, word)
            label_action = swapped_product_label_word_action(interval, base, word)
            self.assertEqual(label_action.final_colors, action.final_colors)
            self.assertEqual(label_action.dependency, action.dependency)
            for index, label_word in enumerate(label_action.label_words):
                source_color = initial_colors[label_action.dependency[index]]
                target_color, mapping = evaluate_swapped_product_label_word(
                    interval, source_color, label_word
                )
                self.assertEqual(target_color, action.final_colors[index])
                self.assertEqual(mapping, action.coordinate_maps[index])
                label_permutation = product_label_word_permutation(
                    interval,
                    "swapped",
                    label_word,
                )
                for source_point, target_point in mapping:
                    self.assertEqual(
                        product_label_permutation_image(
                            interval,
                            label_permutation,
                            source_color,
                            source_point,
                        ),
                        (target_color, target_point),
                    )

    def test_swapped_product_cocycle_equations(self):
        interval = one_color_flip_interval()
        self.assertTrue(interval.is_colored_ybe())
        self.assertEqual(swapped_product_cocycle_failures(interval), ())
        audit = swapped_product_coboundary_audit(interval)
        self.assertTrue(audit.is_coboundary)
        self.assertTrue(product_coboundary_transport_is_identity(interval, audit, "*"))
        self.assertTrue(swapped_product_holonomy_summary(interval).is_trivial)

    def test_swapped_coboundary_label_words_telescope_to_gauge_transport(self):
        interval = two_color_swapped_coboundary_interval()
        self.assertTrue(interval.is_colored_ybe())
        audit = swapped_product_coboundary_audit(interval)
        self.assertTrue(audit.is_coboundary)
        base = (0, 1, 0, 1)
        for word in [tuple(), (1,), (1, 2, 1), (2, -1, 3, 2, 1), (1, 1, -2, 3, -1, 2)]:
            label_action = swapped_product_label_word_action(interval, base, word)
            for index, label_word in enumerate(label_action.label_words):
                source_color = base[label_action.dependency[index]]
                target_color, mapping = evaluate_swapped_product_label_word(
                    interval,
                    source_color,
                    label_word,
                )
                self.assertEqual(target_color, label_action.final_colors[index])
                self.assertEqual(
                    mapping,
                    product_coboundary_transport_map(
                        interval,
                        audit,
                        source_color,
                        target_color,
                    ),
                )

    def test_swapped_product_cocycle_detects_non_ybe_fixture(self):
        interval = one_color_permutation_interval()
        self.assertFalse(interval.is_colored_ybe())
        self.assertTrue(swapped_product_cocycle_failures(interval))

    def test_swapped_product_coboundary_detects_pairwise_linking_label(self):
        interval = one_color_commuting_swapped_interval()
        self.assertTrue(interval.is_colored_ybe())
        self.assertTrue(interval.is_local_minimal())
        self.assertEqual(swapped_product_cocycle_failures(interval), ())
        audit = swapped_product_coboundary_audit(interval)
        self.assertFalse(audit.is_coboundary)
        self.assertTrue(audit.failures)
        holonomy = swapped_product_holonomy_summary(interval)
        self.assertFalse(holonomy.is_trivial)
        self.assertEqual(holonomy.component_group_sizes, (((0, 1, 2), 3),))
        self.assertEqual(len(swapped_product_invariant_families(interval)), 2)
        self.assertEqual(len(swapped_product_label_group(interval).group.elements), 3)

    def test_one_color_product_local_minimal_for_prime_cycle_only(self):
        prime = one_color_prime_cycle_interval()
        self.assertTrue(prime.is_colored_ybe())
        self.assertTrue(prime.is_local_minimal())
        self.assertEqual(len(swapped_product_invariant_families(prime)), 2)
        prime_failures = sharp_kernel_implication_failures(
            solution_from_local_interval(prime),
            identity_solution((0,)),
            cyclic_group(5),
            3,
            bounded_words(3, 3),
        )
        self.assertEqual(prime_failures, {})

        klein = one_color_klein_regular_interval()
        self.assertTrue(klein.is_colored_ybe())
        self.assertFalse(klein.is_local_minimal())
        self.assertGreater(len(swapped_product_invariant_families(klein)), 2)

    def test_one_color_swapped_exponents_are_longitude_row_column_sums(self):
        for word in bounded_words(3, 4):
            data = artin_longitudes(3, word)
            if data.permutation != (0, 1, 2):
                continue
            action = one_color_swapped_label_exponent_action(3, word)
            self.assertEqual(action.dependency, (0, 1, 2))
            self.assertEqual(
                action.exponents,
                artin_longitude_row_column_sums(3, word),
            )

    def test_one_color_pairwise_linking_detector_matches_residual_action(self):
        interval = one_color_commuting_swapped_interval()
        cycle = {0: 1, 1: 2, 2: 0}

        def cycle_power(exponent):
            mapping = {point: point for point in interval.fibres["*"]}
            for _ in range(exponent % 3):
                mapping = _compose_maps(cycle, mapping)
            return mapping

        pure_words = [
            (1, 1),
            (1, 2, 2, 1),
            (1, -2, -2, 1),
            (-1, 2, 2, -1),
            (1, 2, 1, 1, 2, 1),
        ]
        for word in pure_words:
            self.assertEqual(artin_longitudes(3, word).permutation, (0, 1, 2))
            exponent_action = one_color_swapped_label_exponent_action(3, word)
            residual_action = product_permutation_action(interval, ("*", "*", "*"), word)
            self.assertEqual(residual_action.dependency, (0, 1, 2))
            for index, (left_exp, right_exp) in enumerate(exponent_action.exponents):
                self.assertEqual(
                    dict(residual_action.coordinate_maps[index]),
                    cycle_power(left_exp + right_exp),
                )

    def test_negative_generator_uses_inverse_partial_maps(self):
        interval = one_color_permutation_interval()
        action = product_permutation_action(interval, ("*", "*"), (1, -1))
        self.assertEqual(action.dependency, (0, 1))
        self.assertEqual(
            apply_product_permutation_action(action, (0, 2)),
            (0, 2),
        )

    def test_direct_product_decomposition_matches_total_action(self):
        interval = two_color_direct_product_interval()
        self.assertTrue(interval.is_colored_ybe())
        self.assertIsNotNone(direct_product_witness(interval))
        qmap = solution_from_local_interval(interval)
        base = (0, 1, 0)
        words = [
            tuple(),
            (1,),
            (1, 2, 1),
            (2, -1, 2, 1),
            (1, 1, -2, 1),
        ]
        for word in words:
            action = direct_product_action(interval, base, word)
            self.assertEqual(action.dependency, (0, 1, 2))
            for fibre_tuple in product(interval.fibres[0], repeat=3):
                total_tuple = tuple(zip(base, fibre_tuple))
                image = qmap.total.braid_action(word, total_tuple)
                self.assertEqual(
                    tuple(point for _color, point in image),
                    apply_product_permutation_action(action, fibre_tuple),
                )

    def test_direct_label_words_evaluate_to_coordinate_maps(self):
        interval = two_color_direct_product_interval()
        base = (0, 1, 0, 1)
        words = [
            tuple(),
            (1,),
            (1, 2, 1),
            (2, -1, 3, 2, 1),
            (1, 1, -2, 3, -1, 2),
        ]
        initial_colors = tuple(base)
        for word in words:
            action = direct_product_action(interval, base, word)
            label_action = direct_product_label_word_action(interval, base, word)
            self.assertEqual(label_action.final_colors, action.final_colors)
            self.assertEqual(label_action.dependency, action.dependency)
            for index, label_word in enumerate(label_action.label_words):
                source_color = initial_colors[label_action.dependency[index]]
                target_color, mapping = evaluate_direct_product_label_word(
                    interval, source_color, label_word
                )
                self.assertEqual(target_color, action.final_colors[index])
                self.assertEqual(mapping, action.coordinate_maps[index])
                label_permutation = product_label_word_permutation(
                    interval,
                    "direct",
                    label_word,
                )
                for source_point, target_point in mapping:
                    self.assertEqual(
                        product_label_permutation_image(
                            interval,
                            label_permutation,
                            source_color,
                            source_point,
                        ),
                        (target_color, target_point),
                    )

    def test_direct_product_cocycle_equations(self):
        interval = two_color_direct_product_interval()
        self.assertEqual(direct_product_cocycle_failures(interval), ())
        audit = direct_product_coboundary_audit(interval)
        self.assertTrue(audit.is_coboundary)
        for color in interval.colors:
            self.assertTrue(product_coboundary_transport_is_identity(interval, audit, color))
        self.assertTrue(direct_product_holonomy_summary(interval).is_trivial)
        self.assertEqual(len(direct_product_label_group(interval).group.elements), 2)

    def test_direct_coboundary_label_words_telescope_to_gauge_transport(self):
        interval = two_color_direct_product_interval()
        audit = direct_product_coboundary_audit(interval)
        base = (0, 1, 0, 1)
        for word in [tuple(), (1,), (1, 2, 1), (2, -1, 3, 2, 1), (1, 1, -2, 3, -1, 2)]:
            label_action = direct_product_label_word_action(interval, base, word)
            for index, label_word in enumerate(label_action.label_words):
                source_color = base[index]
                target_color, mapping = evaluate_direct_product_label_word(
                    interval,
                    source_color,
                    label_word,
                )
                self.assertEqual(target_color, label_action.final_colors[index])
                self.assertEqual(
                    mapping,
                    product_coboundary_transport_map(
                        interval,
                        audit,
                        source_color,
                        target_color,
                    ),
                )

    def test_product_holonomy_labels_normalize_coboundaries_to_identity(self):
        interval = two_color_swapped_coboundary_interval()
        self.assertEqual(product_holonomy_groups(interval, "swapped"), ())
        target_color, model_points, permutation = product_holonomy_label_permutation(
            interval,
            "swapped",
            1,
            (("L", 0, 1, 1), ("R", 0, 1, 1)),
        )

        self.assertEqual(target_color, 1)
        self.assertEqual(permutation, tuple(range(len(model_points))))

        closed = product_holonomy_closed_label_permutations(
            interval,
            "swapped",
            (0, 1),
            (1, 1),
        )
        self.assertTrue(closed)
        self.assertTrue(
            all(permutation == tuple(range(len(model))) for model, permutation in closed)
        )
        audit = product_holonomy_longitude_subgroup_audit(
            interval,
            "swapped",
            (0, 1),
            (1, 1),
        )
        self.assertEqual(audit.rows, ())
        self.assertTrue(audit.all_closed_holonomies_detected)
        exact = product_holonomy_exact_audit(
            interval,
            "swapped",
            (0, 1),
            state_limit=1000,
        )
        self.assertFalse(exact.truncated)
        self.assertIsNone(exact.failure)
        self.assertTrue(exact.proves_fixed_tuple_kernel_implication)
        self.assertEqual(exact.holonomy_group_orders, ())

    def test_product_holonomy_labels_record_pairwise_branch_motion(self):
        interval = one_color_commuting_swapped_interval()
        holonomy_groups = product_holonomy_groups(interval, "swapped")
        self.assertEqual(len(holonomy_groups), 1)
        self.assertEqual(holonomy_groups[0].model_points, (0, 1, 2))
        self.assertEqual(len(holonomy_groups[0].group.elements), 3)
        closed = product_holonomy_closed_label_permutations(
            interval,
            "swapped",
            ("*", "*"),
            (1, 1),
        )

        self.assertEqual(closed, (((0, 1, 2), (2, 0, 1)), ((0, 1, 2), (2, 0, 1))))
        audit = product_holonomy_longitude_subgroup_audit(
            interval,
            "swapped",
            ("*", "*"),
            (1, 1),
        )
        self.assertTrue(audit.rows)
        self.assertTrue(audit.all_closed_holonomies_detected)
        self.assertEqual(audit.subgroup_sizes, {(0, 1, 2): 3})
        failures = product_holonomy_longitude_subgroup_failures(
            interval,
            "swapped",
            ("*", "*", "*"),
            bounded_words(3, 3),
        )
        self.assertEqual(failures, ())
        exact = product_holonomy_exact_audit(
            interval,
            "swapped",
            ("*", "*"),
            state_limit=1000,
        )
        self.assertFalse(exact.truncated)
        self.assertIsNone(exact.failure)
        self.assertTrue(exact.proves_fixed_tuple_kernel_implication)
        self.assertEqual(exact.holonomy_group_orders, (3,))
        self.assertGreater(exact.closed_state_count, 0)

    def test_product_holonomy_exact_audit_known_branch_needs_extra_factor(self):
        interval = two_color_product_known_nondegenerate_failure_interval()
        tags = branch_tags(solution_from_local_interval(interval).total)
        self.assertIn("nondegenerate", tags)
        self.assertTrue(is_nondegenerate(FiniteBraidedSet(interval.colors, interval.base_R)))
        self.assertTrue(is_nondegenerate(solution_from_local_interval(interval).total))

        raw = product_holonomy_exact_audit(
            interval,
            "swapped",
            (0, 0),
            state_limit=1000,
        )
        self.assertFalse(raw.truncated)
        self.assertIsNotNone(raw.failure)
        self.assertEqual(raw.failure.braid_word, (1, 1, 1, 1))
        self.assertEqual(raw.holonomy_group_orders, (2,))

        augmented = product_holonomy_exact_audit(
            interval,
            "swapped",
            (0, 0),
            extra_groups=(symmetric_group(4),),
            state_limit=1000,
        )
        self.assertFalse(augmented.truncated)
        self.assertIsNone(augmented.failure)
        self.assertTrue(augmented.proves_fixed_tuple_kernel_implication)
        self.assertEqual(augmented.extra_group_orders, (24,))

    def test_product_invariant_families_match_local_admissibility(self):
        swapped = one_color_flip_interval()
        self.assertEqual(
            {family_key(family) for family in swapped_product_invariant_families(swapped)},
            {family_key(family) for family in swapped.admissible_congruence_families()},
        )

        direct = two_color_direct_product_interval()
        self.assertEqual(
            {family_key(family) for family in direct_product_invariant_families(direct)},
            {family_key(family) for family in direct.admissible_congruence_families()},
        )

    def test_product_label_pair_closures_match_local_minimality(self):
        swapped = one_color_prime_cycle_interval()
        swapped_audits = swapped_product_label_pair_closure_audits(swapped)
        self.assertEqual(len(swapped_audits), 10)
        self.assertEqual(swapped_product_label_pair_closure_failures(swapped), ())
        self.assertTrue(all(audit.generated.kind == "universal" for audit in swapped_audits))
        self.assertEqual(
            swapped_audits[0].generated.derivation_count_rows,
            swapped_audits[0].generated.edge_count_rows,
        )
        self.assertEqual(swapped_audits[0].generated.derivation_rows[0].source, "seed")
        self.assertTrue(
            any(
                row.source in {"label_forward", "label_inverse"} and row.source_pairs
                for row in swapped_audits[0].generated.derivation_rows
            )
        )

        imprimitive = one_color_klein_regular_interval()
        swapped_failures = swapped_product_label_pair_closure_failures(imprimitive)
        self.assertTrue(swapped_failures)
        self.assertFalse(imprimitive.is_local_minimal())

        direct = two_color_direct_product_interval()
        direct_audits = direct_product_label_pair_closure_audits(direct)
        self.assertEqual(len(direct_audits), 2)
        self.assertEqual(direct_product_label_pair_closure_failures(direct), ())
        self.assertTrue(all(audit.generated.kind == "universal" for audit in direct_audits))
        self.assertTrue(
            any(
                row.source == "label_forward" and row.crossing == (0, 1)
                for row in direct_audits[0].generated.derivation_rows
            )
        )

    def test_identity_base_product_branch_reduces_to_cyclic_detector(self):
        interval = two_color_identity_base_cyclic_interval()
        self.assertTrue(interval.is_colored_ybe())
        self.assertTrue(interval.is_local_minimal())
        self.assertEqual(interval.semisplit_families(), [])
        self.assertEqual(len(swapped_product_invariant_families(interval)), 2)

        reduction = identity_base_swapped_reduction(interval)
        self.assertTrue(reduction.satisfies_central_form)
        self.assertFalse(reduction.all_central_maps_identity)
        self.assertEqual(reduction.cycle_lengths, {0: (3,), 1: (3,)})
        self.assertEqual(reduction.prime_cycle_modulus, 3)
        summary = local_master_bottleneck_summary(interval)
        self.assertIn("swapped_identity_base_cyclic", summary.product_holonomy_details)
        self.assertEqual(summary.verdict, "product_finite_g_branch")

        audit = swapped_product_coboundary_audit(interval)
        self.assertFalse(audit.is_coboundary)
        holonomy = swapped_product_holonomy_summary(interval)
        self.assertEqual(holonomy.component_group_sizes, (((0, 1, 2), 3),))

        qmap = solution_from_local_interval(interval)
        failures = sharp_kernel_implication_failures(
            qmap,
            identity_solution((0,)),
            cyclic_group(3),
            3,
            bounded_words(3, 4),
        )
        self.assertEqual(failures, {})

    def test_identity_base_reduction_separates_trivial_and_imprimitive_cases(self):
        trivial = identity_base_swapped_reduction(one_color_flip_interval())
        self.assertTrue(trivial.satisfies_central_form)
        self.assertTrue(trivial.all_central_maps_identity)
        self.assertEqual(trivial.prime_cycle_modulus, 1)

        prime = identity_base_swapped_reduction(one_color_prime_cycle_interval())
        self.assertTrue(prime.satisfies_central_form)
        self.assertEqual(prime.cycle_lengths, {"*": (5,)})
        self.assertEqual(prime.prime_cycle_modulus, 5)

        imprimitive = identity_base_swapped_reduction(one_color_klein_regular_interval())
        self.assertTrue(imprimitive.satisfies_central_form)
        self.assertEqual(imprimitive.cycle_lengths, {"*": (2, 2)})
        self.assertIsNone(imprimitive.prime_cycle_modulus)
        self.assertFalse(one_color_klein_regular_interval().is_local_minimal())

    def test_identity_base_direct_reduction_forces_trivial_labels(self):
        interval = two_color_identity_base_direct_interval()
        self.assertTrue(interval.is_colored_ybe())
        reduction = identity_base_direct_reduction(interval)
        self.assertTrue(reduction.is_trivial)

        nontrivial = two_color_identity_base_direct_interval(nontrivial=True)
        self.assertTrue(direct_product_witness(nontrivial))
        self.assertTrue(direct_product_cocycle_failures(nontrivial))
        reduction = identity_base_direct_reduction(nontrivial)
        self.assertFalse(reduction.is_trivial)
        self.assertEqual(reduction.failures[0].kind, "left_label_nonidentity")

    def test_product_closed_label_permutations_record_closed_holonomy(self):
        interval = two_color_identity_base_cyclic_interval()
        identity = tuple(range(6))

        closed = product_closed_label_permutations(
            interval,
            "swapped",
            (0, 1),
            (1, 1),
        )
        self.assertEqual(len(closed), 2)
        self.assertNotEqual(closed[0], identity)
        self.assertNotEqual(closed[1], identity)

        killed_by_cyclic_detector = product_closed_label_permutations(
            interval,
            "swapped",
            (0, 1),
            (1, 1, 1, 1, 1, 1),
        )
        self.assertEqual(killed_by_cyclic_detector, (identity, identity))

        with self.assertRaises(ValueError):
            product_closed_label_permutations(interval, "swapped", (0, 1), (1,))

    def test_product_closed_label_blind_mover_helper(self):
        interval = two_color_identity_base_cyclic_interval()
        identity = tuple(range(6))
        mover = first_nonidentity_product_closed_label(
            interval,
            "swapped",
            (0, 1),
            (1, 1, 1, 1),
        )
        self.assertIsNotNone(mover)
        self.assertNotEqual(mover[1], identity)

        movers = product_closed_label_blind_movers(
            interval,
            "swapped",
            (cyclic_group(2),),
            (0, 1),
            [(1, 1), (1, 1, 1, 1), (1, 1, 1, 1, 1, 1)],
        )
        self.assertIn((1, 1, 1, 1), movers)
        self.assertNotIn((1, 1), movers)
        self.assertNotIn((1, 1, 1, 1, 1, 1), movers)

    def test_product_closed_label_longitude_witnesses_are_weaker_than_common_assignment(self):
        interval = two_color_identity_base_cyclic_interval()
        braid_word = (1, 2, 2, 1)

        self.assertEqual(
            product_closed_label_common_longitude_assignments(
                interval,
                "swapped",
                (0, 1, 0),
                braid_word,
            ),
            (),
        )

        witnesses = product_closed_label_longitude_witnesses(
            interval,
            "swapped",
            (0, 1, 0),
            braid_word,
        )
        self.assertEqual(tuple(witness.coordinate for witness in witnesses), (0, 1, 2))
        self.assertEqual(tuple(witness.longitude_index for witness in witnesses), (0, 0, 0))

    def test_product_closed_label_route_audit_records_proof_routes(self):
        interval = two_color_identity_base_cyclic_interval()
        audit = product_closed_label_longitude_route_audit(
            interval,
            "swapped",
            (0, 1, 0),
            (1, 2, 2, 1),
        )

        self.assertFalse(audit.has_common_assignment)
        self.assertEqual(audit.common_assignment_count, 0)
        self.assertEqual(tuple(row.coordinate for row in audit.rows), (0, 1, 2))
        self.assertTrue(audit.all_single_witnessed)
        self.assertTrue(audit.all_in_longitude_subgroup)
        self.assertEqual(audit.subgroup_only_rows, ())
        self.assertEqual(audit.failed_rows, ())
        self.assertGreaterEqual(audit.longitude_generator_count, 1)
        self.assertGreaterEqual(audit.longitude_subgroup_size, 2)

    def test_product_closed_labels_lie_in_longitude_value_subgroup_on_fixture(self):
        interval = two_color_identity_base_cyclic_interval()
        audit = product_closed_label_longitude_subgroup_audit(
            interval,
            "swapped",
            (0, 1, 0),
            (1, 2, 2, 1),
        )

        self.assertTrue(audit.rows)
        self.assertTrue(audit.all_closed_labels_detected)
        self.assertGreaterEqual(audit.subgroup_size, 2)

    def test_product_closed_label_subgroup_failure_scan_has_none_on_fixture(self):
        interval = two_color_identity_base_cyclic_interval()
        failures = product_closed_label_longitude_subgroup_failures(
            interval,
            "swapped",
            (0, 1, 0),
            bounded_words(3, 3),
        )

        self.assertEqual(failures, ())

    def test_product_closed_label_exact_audit_finds_too_small_detector(self):
        interval = two_color_identity_base_cyclic_interval()
        audit = product_closed_label_exact_audit(
            interval,
            "swapped",
            (cyclic_group(2),),
            (0, 1),
            state_limit=1000,
        )

        self.assertFalse(audit.truncated)
        self.assertIsNotNone(audit.failure)
        self.assertEqual(audit.failure.braid_word, (1, 1, 1, 1))
        self.assertFalse(audit.proves_fixed_tuple_kernel_implication)

    def test_product_closed_label_exact_audit_accepts_stronger_base_detector(self):
        interval = two_color_identity_base_cyclic_interval()
        base_detector = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        audit = product_closed_label_exact_audit(
            interval,
            "swapped",
            (cyclic_group(2),),
            (0, 1),
            base_detector=base_detector,
            state_limit=1000,
        )

        self.assertFalse(audit.truncated)
        self.assertIsNone(audit.failure)
        self.assertTrue(audit.proves_fixed_tuple_kernel_implication)
        self.assertGreater(audit.base_state_count, 1)

    def test_product_closed_label_exact_audit_closes_for_label_group_detector(self):
        interval = two_color_identity_base_cyclic_interval()
        detector = swapped_product_label_group(interval).group
        audit = product_closed_label_exact_audit(
            interval,
            "swapped",
            (detector,),
            (0, 1),
            state_limit=1000,
        )

        self.assertFalse(audit.truncated)
        self.assertIsNone(audit.failure)
        self.assertTrue(audit.proves_fixed_tuple_kernel_implication)
        self.assertGreater(audit.closed_state_count, 0)

    def test_product_closed_label_exact_audit_known_branch_needs_detector_product(self):
        interval = two_color_product_known_nondegenerate_failure_interval()
        tags = branch_tags(solution_from_local_interval(interval).total)
        self.assertIn("nondegenerate", tags)

        raw_detector = swapped_product_label_group(interval).group
        raw = product_closed_label_exact_audit(
            interval,
            "swapped",
            (raw_detector,),
            (0, 0),
            state_limit=1000,
        )

        self.assertFalse(raw.truncated)
        self.assertIsNotNone(raw.failure)
        self.assertEqual(raw.failure.braid_word, (1, 1, 1, 1))
        self.assertFalse(raw.proves_fixed_tuple_kernel_implication)

        augmented = product_closed_label_exact_audit(
            interval,
            "swapped",
            (raw_detector, symmetric_group(4)),
            (0, 0),
            state_limit=1000,
        )

        self.assertFalse(augmented.truncated)
        self.assertIsNone(augmented.failure)
        self.assertTrue(augmented.proves_fixed_tuple_kernel_implication)
        self.assertGreater(augmented.detector_state_count, raw.detector_state_count)

    def test_product_label_group_detector_has_no_bounded_blind_mover_on_fixture(self):
        interval = two_color_identity_base_cyclic_interval()
        detector = swapped_product_label_group(interval).group
        movers = product_closed_label_blind_movers(
            interval,
            "swapped",
            (detector,),
            (0, 1, 0),
            [
                (1, 1),
                (1, 1, 1, 1),
                (1, 2, 2, 1),
                (1, 2, 2, -1),
            ],
        )

        self.assertEqual(movers, {})


if __name__ == "__main__":
    unittest.main()
