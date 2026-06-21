from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proofs" / "finite_group_brunnian_fan_evaluation_basis_criterion.md"


class FiniteGroupBrunnianFanEvaluationBasisCriterionTest(unittest.TestCase):
    def test_note_states_basis_definition_and_domination_conclusion(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Finite-group Brunnian fan evaluation basis criterion", text)
        self.assertIn("Brunnian fan-evaluation basis", text)
        self.assertIn("rho_m^X(w) != 1", text)
        self.assertIn("w(h_1,...,h_{m-1}) != 1", text)
        self.assertIn("dominated by a finite conjugation rack", text)

    def test_note_constructs_detector_from_regular_modules(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("C_reg(H_i) = F_2[H_i] semidirect H_i", text)
        self.assertIn("G_X = C_2 x C_reg(H_1) x ... x C_reg(H_s)", text)
        self.assertIn("K_n(G_X^conj) <= K_n(X)", text)
        self.assertIn("fan-only regular-module theorem", text)
        self.assertIn("two-element trivial rack", text)

    def test_note_states_diagonal_ghost_converse(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Converse in obstruction form", text)
        self.assertIn("diagonal\nBrunnian fan ghost", text)
        self.assertIn("m_j -> infinity", text)
        self.assertIn("eventually a law on every fixed finite\ngroup", text)
        self.assertIn("Uniform Brunnian Fan-Evaluation Basis Lemma", text)


if __name__ == "__main__":
    unittest.main()
