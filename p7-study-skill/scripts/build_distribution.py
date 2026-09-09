#!/usr/bin/env python3
"""Build and audit a deterministic standalone P7 Study Skill ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


FIXED_TIME = (2020, 1, 1, 0, 0, 0)
BANNED_PARTS = {".git", ".p7-state", "__pycache__", "corpus_text", "vision_png"}
BANNED_SUFFIXES = {".pyc", ".pyo", ".pdf", ".ppt", ".pptx"}
BANNED_NAMES = {".ds_store", "thumbs.db"}


def excluded(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    lowered_parts = {part.casefold() for part in rel.parts}
    return bool(lowered_parts & {part.casefold() for part in BANNED_PARTS}) or path.suffix.casefold() in BANNED_SUFFIXES or path.name.casefold() in BANNED_NAMES


def distribution_files(root: Path) -> list[Path]:
    files = []
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"symlink is not allowed: {path}")
        if path.is_file() and not excluded(path, root):
            files.append(path)
    files.sort(key=lambda path: path.relative_to(root).as_posix())
    names = [f"p7-study-skill/{path.relative_to(root).as_posix()}" for path in files]
    folded = [name.casefold() for name in names]
    if len(folded) != len(set(folded)):
        raise ValueError("case-insensitive duplicate path")
    return files


def build(root: Path, output: Path) -> dict:
    files = distribution_files(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            name = f"p7-study-skill/{path.relative_to(root).as_posix()}"
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return audit(output, root)


def audit(zip_path: Path, root: Path | None = None) -> dict:
    with zipfile.ZipFile(zip_path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        folded = [name.casefold() for name in names]
        unsafe = []
        for name in names:
            posix = PurePosixPath(name)
            if posix.is_absolute() or ".." in posix.parts or not posix.parts or posix.parts[0] != "p7-study-skill":
                unsafe.append(name)
        banned = [name for name in names if any(part.casefold() in {p.casefold() for p in BANNED_PARTS} for part in PurePosixPath(name).parts) or PurePosixPath(name).suffix.casefold() in BANNED_SUFFIXES]
        comparison = None
        if root is not None:
            expected = {f"p7-study-skill/{path.relative_to(root).as_posix()}": hashlib.sha256(path.read_bytes()).hexdigest() for path in distribution_files(root)}
            actual = {info.filename: hashlib.sha256(archive.read(info)).hexdigest() for info in infos}
            comparison = {
                "missing": sorted(set(expected) - set(actual)),
                "unexpected": sorted(set(actual) - set(expected)),
                "hash_mismatch": sorted(name for name in set(expected) & set(actual) if expected[name] != actual[name]),
            }
        findings = {
            "zip_sha256": hashlib.sha256(zip_path.read_bytes()).hexdigest(),
            "entries": len(names),
            "single_root": all(name.startswith("p7-study-skill/") for name in names),
            "unsafe_paths": unsafe,
            "case_insensitive_duplicates": len(folded) - len(set(folded)),
            "banned_entries": banned,
            "tree_comparison": comparison,
        }
        findings["result"] = "PASS" if findings["single_root"] and not unsafe and not banned and findings["case_insensitive_duplicates"] == 0 and (comparison is None or not any(comparison.values())) else "FAIL"
        return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify-reproducible", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    output = (args.output or root.parent / "dist" / f"P7-Study-Skill-{version}.zip").resolve()
    result = build(root, output)
    if args.verify_reproducible:
        with tempfile.TemporaryDirectory(prefix="p7-dist-") as temp:
            second = Path(temp) / output.name
            second_result = build(root, second)
            result["second_zip_sha256"] = second_result["zip_sha256"]
            result["byte_identical_rebuild"] = output.read_bytes() == second.read_bytes()
            if not result["byte_identical_rebuild"]:
                result["result"] = "FAIL"
    result["output"] = str(output)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
