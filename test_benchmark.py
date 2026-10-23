import json
import unittest
from benchmark import evaluate, report, CANDIDATES

class BenchmarkTests(unittest.TestCase):
    def test_reference_passes_every_case(self):
        result = evaluate("reference")
        self.assertEqual(result["earned"], result["possible"])
        self.assertGreaterEqual(len(result["cases"]), 12)
    def test_faulty_candidate_is_detected(self):
        result = evaluate("plausible_but_wrong")
        self.assertLess(result["earned"], result["possible"])
        self.assertTrue(any(not c["passed"] for c in result["cases"]))
    def test_report_is_deterministic_and_json_serializable(self):
        self.assertEqual(report(), report())
        self.assertIn("reference", json.dumps(report()))
    def test_unknown_candidate_rejected(self):
        with self.assertRaises(ValueError):
            evaluate("../../anything")
    def test_results_cover_all_tasks(self):
        result = evaluate("reference")
        self.assertEqual({"intervals", "events", "tenant_total"}, {c["task"] for c in result["cases"]})

if __name__ == "__main__":
    unittest.main()

