from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proofs" / "uniform_brunnian_fan_evaluation_frontier.md"


class UniformBrunnianFanEvaluationFrontierTest(unittest.TestCase):
    def test_states_single_group_frontier(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Uniform Brunnian fan-evaluation frontier", text)
        self.assertIn("Uniform Brunnian Fan-Evaluation Group Lemma", text)
        self.assertIn("there exists a finite group `H_X`", text)
        self.assertIn("rho_m^X(w) != 1", text)
        self.assertIn("w(h_1,...,h_{m-1}) != 1", text)

    def test_records_conjugation_rack_consequence(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("C_reg(H_X) = F_2[H_X] semidirect H_X", text)
        self.assertIn("(C_2 x C_reg(H_X))^conj", text)
        self.assertIn("K_n((C_2 x C_reg(H_X))^conj) subset K_n(X)", text)
        self.assertIn("fan-only\nregular-module theorem", text)

    def test_records_diagonal_ghost_and_not_pointwise_ghost(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("The negation is a diagonal law ghost", text)
        self.assertIn("w_j is eventually a law", text)
        self.assertIn("No individual nontrivial\nfan word is invisible", text)
        self.assertIn("free groups are residually\nfinite", text)

    def test_prompt_names_next_attack(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Marked Fan-Image Variety Bound", text)
        self.assertIn("finite recurrent transition type", text)
        self.assertIn("Prompt for the next proof attempt", text)


if __name__ == "__main__":
    unittest.main()
