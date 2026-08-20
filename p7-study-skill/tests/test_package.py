from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from p7lib import build_capsule_catalog, build_manifest, build_metrics, index_capsule_paths  # noqa: E402


class PackageTests(unittest.TestCase):
    def test_manifest_is_stable_and_excludes_artifacts(self):
        first = build_manifest(ROOT)
        second = build_manifest(ROOT)
        self.assertEqual(first, second)
        self.assertTrue(all(not item["path"].startswith("artifacts/") for item in first["files"]))

    def test_capsule_index_reconciles_by_path(self):
        discovered = {item["path"] for item in build_capsule_catalog(ROOT)}
        self.assertGreaterEqual(len(discovered), 156)
        self.assertEqual(discovered, index_capsule_paths(ROOT))

    def test_legacy_enums_have_one_canonical_join_value(self):
        catalog = build_capsule_catalog(ROOT)
        self.assertTrue(all(item["unit"] in {"UNIT_1", "UNIT_2", "UNIT_3", "UNIT_4", "UNASSIGNED"} for item in catalog))
        self.assertTrue(all(item["legacy_priority_normalized"] in {"high", "medium", "low"} for item in catalog))
        self.assertTrue(all(item["priority"] == "unscored" for item in catalog))

    def test_missing_runtime_sources_degrade_honestly(self):
        metrics = build_metrics(ROOT)
        for name in ("corpus_text", "vision_png"):
            if metrics["runtime_source_availability"][name]["availability"] == "absent":
                self.assertEqual(metrics["runtime_source_availability"][name]["behavior"], "metadata_only_do_not_claim_inspection")


if __name__ == "__main__":
    unittest.main()
