import hashlib
import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_distribution", ROOT / "scripts" / "build_distribution.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class DistributionTests(unittest.TestCase):
    def test_zip_is_safe_single_root_and_matches_tree(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "one.zip"
            result = MOD.build(ROOT, target)
            self.assertEqual(result["result"], "PASS")
            self.assertEqual(result["unsafe_paths"], [])
            self.assertEqual(result["banned_entries"], [])
            with zipfile.ZipFile(target) as archive:
                self.assertTrue(all(name.startswith("p7-study-skill/") for name in archive.namelist()))

    def test_two_builds_are_byte_identical(self):
        with tempfile.TemporaryDirectory() as temp:
            first = Path(temp) / "first.zip"
            second = Path(temp) / "second.zip"
            MOD.build(ROOT, first)
            MOD.build(ROOT, second)
            self.assertEqual(hashlib.sha256(first.read_bytes()).hexdigest(), hashlib.sha256(second.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
