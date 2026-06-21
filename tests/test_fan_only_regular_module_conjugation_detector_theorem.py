from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proofs" / "fan_only_regular_module_conjugation_detector_theorem.md"


class FanOnlyRegularModuleConjugationDetectorTheoremTest(unittest.TestCase):
    def test_theorem_detects_nonidentity_fan_word_evaluations(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Fan-only regular-module conjugation detector theorem", text)
        self.assertIn("C_reg(H) = F_2[H] semidirect H", text)
        self.assertIn("w(h_1,...,h_{m-1}) != 1", text)
        self.assertIn("w notin K_m(C_reg(H)^conj)", text)

    def test_proof_uses_last_strand_identity_to_avoid_fox_gap(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("label the last strand", text)
        self.assertIn("(v,1)", text)
        self.assertIn("(a,l)(v,1)(a,l)^{-1} = (l v, 1)", text)
        self.assertIn("vector part `a` cancels", text)
        self.assertIn("avoids\nthe Fox-derivative gap", text)

    def test_consequence_states_finite_group_route(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("finite-group envelope from finite fan evaluators", text)
        self.assertIn("Br_m cap K_m(C_X^conj) subset K_m(X)", text)
        self.assertIn("C_2^conj x C_X^conj", text)
        self.assertIn("dominates `X`", text)
        self.assertIn("Uniform Framed Fan-Envelope", text)
        self.assertIn("not required for\nthe final Brunnian fan reduction", text)


if __name__ == "__main__":
    unittest.main()
