from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proofs" / "framed_c2_s3_all_arity_cover_proof.md"


class FramedC2S3AllArityCoverProofTest(unittest.TestCase):
    def test_proof_states_all_arity_containment(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Framed C2 is dominated by S3 in all arities", text)
        self.assertIn("K_n(S3^conj) <= K_n(A_C2)", text)
        self.assertIn("For every `n >= 1`", text)
        self.assertIn("So `S3^conj` dominates the framed `C2` detector", text)

    def test_proof_records_mod2_factorization_mechanism(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("M_n = B_n / (P_n' P_n^2)", text)
        self.assertIn("The `a`-coordinates follow the ordinary strand permutation", text)
        self.assertIn("Artin longitude values evaluated in `C2`", text)
        self.assertIn("pairwise linking matrix of beta modulo `2`", text)
        self.assertIn("P_n' P_n^2 <= K_n(A_C2)", text)
        self.assertIn("proofs/mod2_pure_braid_s3_detector_bridge.md", text)

    def test_proof_does_not_overclaim_general_cover(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("only for the rank-one framed", text)
        self.assertIn("does not prove the general Framed-to-Conjugation Cover Lemma", text)
        self.assertIn("For nonabelian `G`", text)
        self.assertIn("remains a genuine finite-group route frontier", text)


if __name__ == "__main__":
    unittest.main()
