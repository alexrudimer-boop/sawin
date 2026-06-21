from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proofs" / "framed_abelian_dihedral_cover_theorem.md"


class FramedAbelianDihedralCoverTheoremTest(unittest.TestCase):
    def test_theorem_states_abelian_conjugation_cover(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Framed finite abelian detectors are covered", text)
        self.assertIn("For every finite abelian group `A`", text)
        self.assertIn("K_n(D_e^conj) <= K_n(A_A)", text)
        self.assertIn("for every `n`", text)
        self.assertIn("finite conjugation rack", text)

    def test_proof_uses_exponent_and_pairwise_linking(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("e=exp(A)", text)
        self.assertIn("ordinary pairwise-linking matrix", text)
        self.assertIn("lk_{ij}(beta) == 0 mod e", text)
        self.assertIn("B_n / (P_n' P_n^e)", text)
        self.assertIn("displacement under `sigma^{2k}` is `-2k`", text)
        self.assertIn("zero in `C_{2e}` iff `e` divides `k`", text)

    def test_proof_scopes_remaining_nonabelian_problem(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("central/abelian framed longitude layer is not an obstruction", text)
        self.assertIn("What remains", text)
        self.assertIn("genuinely nonabelian", text)
        self.assertIn("full\nnonabelian Artin longitude values", text)


if __name__ == "__main__":
    unittest.main()
