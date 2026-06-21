from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proofs" / "marked_fan_image_variety_bound_frontier.md"


class MarkedFanImageVarietyBoundFrontierTest(unittest.TestCase):
    def test_states_moving_fan_image_tuple_setup(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Marked fan-image variety bound frontier", text)
        self.assertIn("G_m^X = theta_m^X(L_m)", text)
        self.assertIn("g_{m,i} = theta_m^X(y_i)", text)
        self.assertIn("w(g_{m,1},...,g_{m,m-1})", text)

    def test_separates_strong_variety_from_exact_marked_condition(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Strong sufficient condition: fixed variety bound", text)
        self.assertIn("G_m^X in var(H_X)", text)
        self.assertIn("This condition is stronger than necessary", text)
        self.assertIn("Brunnian marked variety bound", text)

    def test_records_detector_consequence_and_diagonal_failure(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Uniform Brunnian Fan-Evaluation Group Lemma", text)
        self.assertIn("(C_2 x C_reg(H_X))^conj", text)
        self.assertIn("diagonal marked variety escape", text)
        self.assertIn("eventually a law on every fixed finite group", text)

    def test_names_false_shortcuts_and_real_counterexample_target(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("False shortcuts", text)
        self.assertIn("Growing group size", text)
        self.assertIn("Central and abelian values", text)
        self.assertIn("Fixed arity", text)
        self.assertIn("current exact negative target", text)

    def test_records_rank2_and_rank3_nonperm3_evidence_as_limited(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Existing finite-prefix evidence", text)
        self.assertIn("nonperm3_rank2_fan_image_structure_audit.md", text)
        self.assertIn("marked-isomorphic to one group `H24`", text)
        self.assertIn("central second-derived layer", text)
        self.assertIn("nonperm3_rank3_fan_image_structure_audit.md", text)
        self.assertIn("marked-isomorphic to one reusable group `F648`", text)
        self.assertIn("first unrecorded place", text)
        self.assertIn("rank `4`", text)
        self.assertIn("nonperm3_rank4_fan_image_representative_probe.md", text)
        self.assertIn("image order `51840`", text)
        self.assertIn("finite pressure point, not a counterexample", text)
        self.assertIn("does not prove the uniform lemma", text)


if __name__ == "__main__":
    unittest.main()
