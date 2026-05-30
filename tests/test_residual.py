import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    QuotientMap,
    braid_action_order,
    bounded_words,
    cyclic_group,
    identity_solution,
    is_identity_action,
    local_normalized_law_prefix_witness_audit,
    local_symmetric_normalized_law_prefix_witness_audit,
    is_nondegenerate,
    product_solution,
    quotient_image_kernel_summary,
    rack_solution,
    residual_coordinate_dependency_summary,
    pure_braid_generator,
    sharp_kernel_implication_failures,
)


class ResidualTests(unittest.TestCase):
    def test_product_solution_preserves_ybe(self):
        left = rack_solution([0, 1], lambda a, b: b)
        right = identity_solution(["x", "y"])
        product = product_solution(left, right)
        self.assertTrue(product.is_ybe())

    def test_product_solution_action_is_coordinatewise_for_braid_words(self):
        left = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        right = FiniteBraidedSet(
            ("x", "y"),
            {
                ("x", "x"): ("x", "x"),
                ("x", "y"): ("y", "x"),
                ("y", "x"): ("x", "y"),
                ("y", "y"): ("y", "y"),
            },
        )
        product = product_solution(left, right)
        word = (1, 2, -1, 1, -2)
        left_tuple = (0, 1, 2)
        right_tuple = ("x", "y", "x")
        product_tuple = tuple(zip(left_tuple, right_tuple))

        image = product.braid_action(word, product_tuple)

        self.assertEqual(
            image,
            tuple(
                zip(
                    left.braid_action(word, left_tuple),
                    right.braid_action(word, right_tuple),
                )
            ),
        )

    def test_quotient_map_validates_homomorphism(self):
        total = identity_solution([(0, "a"), (0, "b"), (1, "a"), (1, "b")])
        quotient = identity_solution([0, 1])
        pi = {x: x[0] for x in total.elements}
        qmap = QuotientMap(total, quotient, pi)
        self.assertTrue(qmap.residual_is_identity(2, [1]))

    def test_quotient_action_is_projection_of_total_action(self):
        total = rack_solution([0, 1, 2], lambda _left, right: right)
        quotient = rack_solution(["a", "b"], lambda _left, right: right)
        pi = {0: "a", 1: "a", 2: "b"}
        qmap = QuotientMap(total, quotient, pi)
        word = (1, 2, -1, 2, 1)
        tup = (0, 2, 1)
        total_image = qmap.total.braid_action(word, tup)
        quotient_tuple = tuple(pi[item] for item in tup)

        self.assertEqual(
            tuple(pi[item] for item in total_image),
            qmap.quotient.braid_action(word, quotient_tuple),
        )

    def test_quotient_of_nondegenerate_solution_is_nondegenerate(self):
        left = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        right = rack_solution(["a", "b"], lambda _left, right: right)
        total = product_solution(left, right)
        qmap = QuotientMap(total, left, {element: element[0] for element in total.elements})

        self.assertTrue(is_nondegenerate(total))
        self.assertTrue(is_nondegenerate(qmap.quotient))

    def test_quotient_map_rejects_non_homomorphism(self):
        total = rack_solution([0, 1], lambda a, b: b)
        quotient = identity_solution([0, 1])
        with self.assertRaises(ValueError):
            QuotientMap(total, quotient, {0: 0, 1: 1})

    def test_residual_detects_fibre_motion_over_identity_base(self):
        elems = ((0, "a"), (0, "b"))
        total = rack_solution(elems, lambda a, b: b)
        quotient = identity_solution([0])
        qmap = QuotientMap(total, quotient, {x: 0 for x in elems})
        self.assertFalse(qmap.residual_is_identity(2, [1]))
        moved = qmap.moved_residual_tuple(2, [1])
        self.assertIsNotNone(moved)

    def test_sharp_implication_failure_found_for_too_small_detector(self):
        elems = ((0, "a"), (0, "b"))
        flip = {elems[0]: elems[1], elems[1]: elems[0]}
        total = rack_solution(elems, lambda a, b: flip[b])
        quotient = identity_solution([0])
        qmap = QuotientMap(total, quotient, {x: 0 for x in elems})
        base_detector = identity_solution(["*"])
        failures = sharp_kernel_implication_failures(
            qmap,
            base_detector,
            cyclic_group(1),
            2,
            bounded_words(2, 2),
        )
        self.assertIn((1, 1), failures)

    def test_identity_action_helper(self):
        solution = identity_solution([0, 1])
        self.assertTrue(is_identity_action(solution, 3, [1, -1, 2, -2]))

    def test_braid_action_order_for_two_point_permutation_fibre(self):
        elems = ((0, "a"), (0, "b"))
        flip = {elems[0]: elems[1], elems[1]: elems[0]}
        total = rack_solution(elems, lambda a, b: flip[b])
        self.assertEqual(braid_action_order(total, 2, [1, 1]), 2)

    def test_quotient_image_kernel_summary_for_trivial_quotient(self):
        elems = ((0, "a"), (0, "b"))
        flip = {elems[0]: elems[1], elems[1]: elems[0]}
        total = rack_solution(elems, lambda a, b: flip[b])
        quotient = identity_solution([0])
        qmap = QuotientMap(total, quotient, {x: 0 for x in elems})

        summary = quotient_image_kernel_summary(qmap, 2)

        self.assertTrue(summary.proves_fixed_n_exact_sequence)
        self.assertEqual(summary.base_image_size, 1)
        self.assertEqual(summary.joint_image_size, summary.kernel_size)
        self.assertTrue(summary.kernel_contains_nonidentity)
        self.assertEqual(summary.first_nonidentity_kernel_word, (1,))

    def test_quotient_image_kernel_summary_has_trivial_kernel_for_identity_cover(self):
        total = identity_solution([(0, "a"), (1, "a")])
        quotient = identity_solution([0, 1])
        qmap = QuotientMap(total, quotient, {x: x[0] for x in total.elements})

        summary = quotient_image_kernel_summary(qmap, 3)

        self.assertTrue(summary.proves_fixed_n_exact_sequence)
        self.assertEqual(summary.kernel_size, 1)
        self.assertFalse(summary.kernel_contains_nonidentity)
        self.assertIsNone(summary.first_nonidentity_kernel_word)

    def test_residual_dependency_summary_for_identity_action(self):
        total = identity_solution([(0, "a"), (0, "b")])
        quotient = identity_solution([0])
        qmap = QuotientMap(total, quotient, {x: 0 for x in total.elements})

        summary = residual_coordinate_dependency_summary(qmap, (0, 0), (1,))

        self.assertEqual(summary.supports, ((0,), (1,)))
        self.assertEqual(summary.max_arity, 1)
        self.assertTrue(summary.is_coordinatewise)

    def test_residual_dependency_summary_detects_multi_input_rack_coordinate(self):
        total = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        quotient = identity_solution([0])
        qmap = QuotientMap(total, quotient, {x: 0 for x in total.elements})

        summary = residual_coordinate_dependency_summary(qmap, (0, 0), (1,))

        self.assertEqual(summary.supports, ((0, 1), (0,)))
        self.assertEqual(summary.max_arity, 2)
        self.assertFalse(summary.is_coordinatewise)

    def test_residual_dependency_summary_rejects_non_base_fixed_word(self):
        quotient = rack_solution([0, 1], lambda a, b: b)
        total = product_solution(quotient, identity_solution(["a"]))
        qmap = QuotientMap(total, quotient, {x: x[0] for x in total.elements})

        with self.assertRaises(ValueError):
            residual_coordinate_dependency_summary(qmap, (0, 1), (1,))

    def test_local_normalized_law_prefix_witness_checks_residual_stabilization(self):
        total = rack_solution([0, 1], lambda _left, right: 1 - right)
        quotient = identity_solution(["*"])
        qmap = QuotientMap(total, quotient, {element: "*" for element in total.elements})
        base_detector = identity_solution(["q"])
        braid = pure_braid_generator(1, 2)

        audit = local_normalized_law_prefix_witness_audit(
            qmap,
            base_detector,
            (cyclic_group(1),),
            2,
            braid,
            ("*", "*"),
            (0, 0),
            extra_strands=2,
            fill_value=0,
        )

        self.assertTrue(audit.source_in_residual_kernel)
        self.assertTrue(audit.target_in_residual_kernel)
        self.assertTrue(audit.product_invisibility_survives_stabilization)
        self.assertEqual(audit.source_image, (1, 1))
        self.assertEqual(audit.stabilized_image, (1, 1, 0, 0))
        self.assertTrue(audit.residual_movement_survives_stabilization)
        self.assertTrue(audit.proves_one_local_prefix_normalized_law_witness)

    def test_local_normalized_law_prefix_witness_rejects_nonmoving_residual_tuple(self):
        total = identity_solution([0, 1])
        quotient = identity_solution(["*"])
        qmap = QuotientMap(total, quotient, {element: "*" for element in total.elements})
        base_detector = identity_solution(["q"])

        audit = local_normalized_law_prefix_witness_audit(
            qmap,
            base_detector,
            (cyclic_group(1),),
            2,
            pure_braid_generator(1, 2),
            ("*", "*"),
            (0, 1),
            extra_strands=1,
            fill_value=0,
        )

        self.assertTrue(audit.source_in_residual_kernel)
        self.assertTrue(audit.target_in_residual_kernel)
        self.assertTrue(audit.product_invisibility_survives_stabilization)
        self.assertFalse(audit.residual_movement_survives_stabilization)
        self.assertFalse(audit.proves_one_local_prefix_normalized_law_witness)

    def test_local_symmetric_normalized_law_prefix_witness_uses_symmetric_tower(self):
        total = rack_solution([0, 1], lambda _left, right: 1 - right)
        quotient = identity_solution(["*"])
        qmap = QuotientMap(total, quotient, {element: "*" for element in total.elements})
        base_detector = identity_solution(["q"])

        audit = local_symmetric_normalized_law_prefix_witness_audit(
            qmap,
            base_detector,
            1,
            2,
            pure_braid_generator(1, 2),
            ("*", "*"),
            (0, 0),
            extra_strands=1,
            fill_value=0,
        )

        self.assertEqual(audit.group_orders, (1,))
        self.assertEqual(audit.product_group_order, 1)
        self.assertTrue(audit.proves_one_local_prefix_normalized_law_witness)


if __name__ == "__main__":
    unittest.main()
