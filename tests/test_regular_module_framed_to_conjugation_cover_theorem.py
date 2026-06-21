from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proofs" / "regular_module_framed_to_conjugation_cover_theorem.md"


class RegularModuleFramedToConjugationCoverTheoremTest(unittest.TestCase):
    def test_note_states_candidate_cover_and_status(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Regular-module framed-to-conjugation cover frontier", text)
        self.assertIn("C_reg(G) = V_G semidirect G", text)
        self.assertIn("K_n(C_reg(G)^conj) <= K_n(A_G^+)", text)
        self.assertIn("desired cover statement", text)
        self.assertIn("not yet proved", text)

    def test_note_records_fox_derivative_gap(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("The gap", text)
        self.assertIn("not generally independent", text)
        self.assertIn("Fox-derivative expression", text)
        self.assertIn("(l_i - 1)v_i + (1 - x_i) a", text)
        self.assertIn("can, in principle, cancel", text)

    def test_note_states_exact_missing_lemma_and_consequence(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Regular-Module Artin Longitude Separation Lemma", text)
        self.assertIn("some Artin longitude", text)
        self.assertIn("acts nontrivially on C_reg(G)^n", text)
        self.assertIn("cannot cancel every nontrivial", text)
        self.assertIn("If the Regular-Module Artin Longitude Separation Lemma holds", text)
        self.assertIn("Uniform Framed Fan-Envelope", text)


if __name__ == "__main__":
    unittest.main()
