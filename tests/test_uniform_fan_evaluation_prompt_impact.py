from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proofs" / "uniform_fan_evaluation_prompt_impact.md"


class UniformFanEvaluationPromptImpactTest(unittest.TestCase):
    def test_positive_answer_resolves_sawin_by_conjugation_rack(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Positive outcome", text)
        self.assertIn("resolves Sawin", text)
        self.assertIn("finite-conjugation-rack form", text)
        self.assertIn("C_reg(H_X)=F_2[H_X] semidirect H_X", text)
        self.assertIn("K_n((C_2 x C_reg(H_X))^conj) subset K_n(X)", text)

    def test_negative_finite_group_answer_is_not_full_sawin_counterexample(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Negative outcome", text)
        self.assertIn("diagonal finite-group law\nghost", text)
        self.assertIn("not by\nitself a counterexample to Sawin", text)
        self.assertIn("finite pointed rack", text)
        self.assertIn("pointed-rack Brunnian ghost", text)

    def test_records_asymmetric_fork_and_upgrade_needed(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Correct fork", text)
        self.assertIn("positive answer", text)
        self.assertIn("negative finite-group answer", text)
        self.assertIn("finite-group law ghost\n    =>\npointed-rack Brunnian ghost", text)
        self.assertIn("row-15 image of order `51840`", text)

    def test_rank4_pressure_is_not_overclaimed(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("nonperm3_rank4_fan_image_representative_probe.md", text)
        self.assertIn("rank 4, row 15 hard image order = 51840", text)
        self.assertIn("only pressure", text)
        self.assertIn("Large order and large exponent do not imply", text)
        self.assertIn("remaining nontrivial on the marked row-15 fan tuple", text)


if __name__ == "__main__":
    unittest.main()
