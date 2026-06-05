import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_size5_6_everywhere_singular_search_plan import build_report


class SizeFiveSixEverywhereSingularSearchPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_coordinate_model_uses_u_v_arrays_and_exact_bijectivity(self):
        model = self.report["coordinate_model"]

        self.assertIn("U[x,y]=L_x(y)", model["arrays"])
        self.assertIn("V[x,y]=R_y(x)", model["arrays"])
        self.assertIn("output pairs", model["bijectivity"])
        self.assertIn("exactly d times", model["balanced_counts"])
        self.assertIn("U^{-1}(u)", model["pair_orthogonality"])

    def test_ybe_identities_and_stage_a_feasibility_are_explicit(self):
        identities = {row["name"]: row for row in self.report["ybe_identities"]}
        stage_a = self.report["stage_a_u_enumeration"]

        self.assertIn("Y1", identities)
        self.assertIn("singular row transformations", stage_a["preferred_implementation"])
        self.assertIn("L_{U[x,y]} L_v = L_x L_y", identities["Y1"]["use"])
        self.assertIn("A_xy={v in X", stage_a["feasibility_set"])
        self.assertIn("multiset{L_x L_y", stage_a["multiset_factorization"])
        self.assertIn("C(u,P)", stage_a["bucket_checkpoint"])
        self.assertIn("nonempty", " ".join(stage_a["constraints"]))
        self.assertIn("multiset-factorization", " ".join(stage_a["constraints"]))
        self.assertIn("d!", stage_a["canonicalization"])
        self.assertTrue(
            self.report["next_prompt"].endswith(
                "2026-06-04-stage-a-u-array-enumeration_ask_now.md"
            )
        )

    def test_stage_b_is_exact_cover_with_y2_y3_and_noninvolutive(self):
        stage_b = self.report["stage_b_v_exact_cover"]
        constraints = " ".join(stage_b["constraints"])

        self.assertIn("bucket domain", stage_b["variables"])
        self.assertIn("bucket permutations", stage_b["bucket_variables"])
        self.assertIn("(U[x,y],V[x,y])", constraints)
        self.assertIn("Y2 and Y3", constraints)
        self.assertIn("r^2", constraints)
        self.assertIn("remaining allowed unused values", stage_b["branching"])

    def test_everywhere_singular_filters_include_stronger_pro_filters(self):
        filters = {
            row["name"]: row["rule"]
            for row in self.report["everywhere_singular_filters"]
        }

        self.assertIn("minimal-image filter", filters)
        self.assertIn("semigroup-minimal image filter", filters)
        self.assertIn("fibre-pair congruence filter", filters)
        self.assertIn("kernel-hypergraph connectedness", filters)
        self.assertIn("<L_x>", filters["semigroup-minimal image filter"])
        self.assertIn("kernel pairs", filters["fibre-pair congruence filter"])

    def test_pressure_stage_uses_disjoint_union_not_product_set(self):
        pressure = self.report["rack_prefix_pressure"]
        priority = " ".join(pressure["priority"])

        self.assertIn("do not build the product rack", pressure["warning"])
        self.assertIn("disjoint union", pressure["compression"])
        self.assertIn("coprod_R R^n", pressure["compression"])
        self.assertIn("P_{<=3}, n<=8", priority)
        self.assertIn("P_{<=4}, n<=5", priority)
        self.assertIn("n=6,7", priority)

    def test_pipeline_and_status_are_non_exhaustive(self):
        pipeline = " ".join(self.report["pipeline"])

        self.assertIn("enumerate canonical U arrays", pipeline)
        self.assertIn("solve V as exact cover", pipeline)
        self.assertIn("compressed rack-prefix pressure", pipeline)
        self.assertIn("no exhaustive", self.report["status"])


if __name__ == "__main__":
    unittest.main()
