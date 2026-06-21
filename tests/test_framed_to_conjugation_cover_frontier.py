from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proofs" / "framed_to_conjugation_cover_frontier.md"


class FramedToConjugationCoverFrontierTest(unittest.TestCase):
    def test_note_separates_rack_and_group_routes(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Framed-to-Conjugation Cover Frontier", text)
        self.assertIn("Uniform framed fan envelope", text)
        self.assertIn("finite rack domination", text)
        self.assertIn("fan-only regular-module detector", text)
        self.assertIn("Framed-to-Conjugation Cover Lemma", text)
        self.assertIn("K_n(C(G)^conj) subset K_n(A_G^+)", text)
        self.assertIn("regular_module_framed_to_conjugation_cover_theorem.md", text)
        self.assertIn("C(G) = F_2[G] semidirect G", text)
        self.assertIn("not yet unconditional", text)
        self.assertIn("fan_only_regular_module_conjugation_detector_theorem.md", text)

    def test_note_records_two_strand_sanity_check_and_boundary(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Two-Strand Sanity Check", text)
        self.assertIn("A_C2:      ord(sigma_1)=4", text)
        self.assertIn("S3^conj:   ord(sigma_1)=12", text)
        self.assertIn("K_2(S3^conj) subset K_2(A_C2)", text)
        self.assertIn("Arity-3 Residual Check", text)
        self.assertIn("proofs/framed_c2_s3_arity3_cover_probe.md", text)
        self.assertIn("n=3: joint image 279936, kernel size 1", text)
        self.assertIn("for `n=2,3`", text)
        self.assertIn("All-Arity C2 Cover", text)
        self.assertIn("proofs/framed_c2_s3_all_arity_cover_proof.md", text)
        self.assertIn("M_n = B_n / (P_n' P_n^2)", text)
        self.assertIn("for every arity `n`", text)
        self.assertIn("Abelian Framed Cover", text)
        self.assertIn("proofs/framed_abelian_dihedral_cover_theorem.md", text)
        self.assertIn("D_e = C_{2e} semidirect C_2", text)
        self.assertIn("K_n(D_e^conj) subset K_n(A_A)", text)
        self.assertIn("Remaining Boundary", text)
        self.assertIn("one remaining statement", text)
        self.assertIn("uniform finite fan-envelope", text)
        self.assertIn("C_reg(H_1)^conj", text)
        self.assertIn("finite_group_brunnian_fan_evaluation_basis_criterion.md", text)
        self.assertIn("fan-evaluation basis", text)

    def test_note_states_next_fork(self) -> None:
        text = PROOF.read_text(encoding="utf-8")

        self.assertIn("Positive Route", text)
        self.assertIn("Counterexample Route", text)
        self.assertIn("diagonal Brunnian fan ghost", text)
        self.assertIn("eventually invisible to every fixed finite group", text)
        self.assertIn("Uniform Framed Fan-Envelope", text)
        self.assertIn("finite Brunnian\nfan-evaluation basis", text)


if __name__ == "__main__":
    unittest.main()
