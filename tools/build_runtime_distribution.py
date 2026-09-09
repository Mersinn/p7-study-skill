#!/usr/bin/env python3
"""Build a minimal P7 install ZIP without modifying the engineering checkout."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

DESCRIPTION = ('Tutor de estudo médico P7: plano, temas, arquivos, questões, discursivas, '
               'simulação, OSCE, revisão e Diagnos; EISA II, EISCA, EISM e Casos Clínicos, '
               'com fontes e continuidade honesta.')
ROOT_FILES = {'SKILL.md', 'VERSION', 'LICENSE.md', 'PRIVACY.md'}
EXPLICIT = {
    'scripts/ledger.py', 'scripts/priority.py', 'scripts/p7lib.py',
    'artifacts/METRICS.json', 'artifacts/CLINICAL_CLAIMS.csv',
    'artifacts/OPERATION_COUNTS.json', 'registry/clinical_claims.jsonl',
    'registry/sources.jsonl', 'registry/source_versions.jsonl',
    'registry/aliases.json', 'registry/reviewers.json',
}
DIRECTORIES = {'capsules', 'config', 'p7_source_pack'}
ENGINEERING_REFERENCES = {'TEST_PLAN.md', 'EVALUATION_SUITE.md'}
BANNED = {'.git', '__pycache__', '.p7-state', 'corpus_text', 'vision_png'}
BANNED_SUFFIXES = {'.pyc', '.pyo', '.pdf', '.ppt', '.pptx'}


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def selected(name: str) -> bool:
    p = Path(name)
    return (name in ROOT_FILES | EXPLICIT or p.parts[0] in DIRECTORIES
            or p.parts[0] == 'references' and p.name not in ENGINEERING_REFERENCES)


def source_files(root: Path) -> dict[str, bytes]:
    result = {}
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlink not supported: {path}')
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if (set(relative.parts) & BANNED or path.suffix.lower() in BANNED_SUFFIXES
                or path.name.lower() in {'.ds_store', 'thumbs.db'}):
            continue
        result[relative.as_posix()] = path.read_bytes()
    return result


def zip_bytes(files: dict[str, bytes]) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo('p7-study-skill/' + name, (2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return output.getvalue()


def references(root: Path, runtime: dict[str, bytes]) -> dict:
    """Check markdown links and inline path literals; classify absent original sources."""
    resolved, dropped, absent = [], [], []
    for name, data in runtime.items():
        if not name.endswith('.md'):
            continue
        text = data.decode('utf-8')
        tokens = set(re.findall(r'\[[^\]]*\]\(([^)]+)\)', text))
        tokens.update(token for token in re.findall(r'`([^`\n]+)`', text)
                      if '/' in token and not any(c.isspace() for c in token))
        for token in sorted(tokens):
            target = token.strip('<>').split('#')[0]
            if not target or '://' in target or target.startswith('#'):
                continue
            candidates = [root / target, root / Path(name).parent / target]
            if name.startswith('capsules/'):
                candidates.append(root / 'capsules' / target)
            existing = next((p.resolve() for p in candidates if p.exists()), None)
            record = {'from': name, 'reference': token}
            if existing is None:
                if target.startswith('qualification/'):
                    record['classification'] = 'engineering reference already external to the original skill ZIP; not needed to apply the following runtime safety rule'
                elif target.startswith(('corpus_text/', 'vision_png/')):
                    record['classification'] = 'optional raw source layer, explicitly unavailable in both distributions'
                elif target == '.p7-state/':
                    record['classification'] = 'private user state created at runtime, never distributed'
                elif target == 'references/CLINICAL_CLAIM_REGISTRY.csv':
                    record['classification'] = 'explicitly prohibited nonexistent legacy path, not a load instruction'
                else:
                    record['classification'] = 'inline vocabulary/unit, not an existing package dependency'
                absent.append(record)
                continue
            if not existing.is_relative_to(root):
                dropped.append({**record, 'reason': 'outside package'})
                continue
            rel = existing.relative_to(root).as_posix()
            if existing.is_dir():
                present = any(f.startswith(rel + '/') for f in runtime)
            else:
                present = rel in runtime
            (resolved if present else dropped).append({**record, 'target': rel})
    return {'resolved': resolved, 'references_to_excluded_files': dropped,
            'already_absent_or_non_file_literals': absent,
            'scope': 'Markdown links and inline slash path literals; original unavailable sources and non-path examples are reported, not invented.'}


def exercise_zip(archive: bytes) -> dict:
    with tempfile.TemporaryDirectory(prefix='p7-runtime-') as temp:
        temp_root = Path(temp)
        with zipfile.ZipFile(io.BytesIO(archive)) as z:
            z.extractall(temp_root)
        root = temp_root / 'p7-study-skill'
        ledger = root / 'scripts/ledger.py'
        state = temp_root / 'synthetic-state'
        def run(*args: str, success: bool = True):
            proc = subprocess.run([sys.executable, '-B', *map(str, args)], cwd=temp_root,
                                  capture_output=True, text=True, encoding='utf-8')
            if success and proc.returncode:
                raise RuntimeError(proc.stderr or proc.stdout)
            return proc
        run(ledger, '--state-dir', state, 'init')
        event = {'event_id': 'event:runtime-install', 'learner_id': 'learner:synthetic',
                 'occurred_at': '2026-09-09T12:00:00Z', 'event_type': 'answer_submitted',
                 'interaction_id': 'runtime-smoke', 'capsule_id': 'capsule:eisca:synthetic',
                 'concept_id': 'concept:synthetic',
                 'payload': {'result': 'incorrect', 'independent': True, 'hint_level': 'none'}}
        run(ledger, '--state-dir', state, 'append', '--event-json', json.dumps(event))
        validation = run(ledger, '--state-dir', state, 'validate').stdout.strip()
        assert validation == 'valid ledger: 1 events', validation
        run(ledger, '--state-dir', state, 'project')
        tasks = list(csv.DictReader((state / 'review_tasks.csv').read_text().splitlines()))
        assert len(tasks) == 1 and tasks[0]['due_at'] == '2026-09-11T12:00:00Z', tasks
        exported = temp_root / 'events.csv'
        run(ledger, '--state-dir', state, 'export-csv', exported)
        assert len(list(csv.DictReader(exported.read_text().splitlines()))) == 1
        priority = json.loads(run(root / 'scripts/priority.py', '--exam-recurrence', '2',
                                 '--clinical-risk', '2', '--curriculum-imminence', '2',
                                 '--learner-gap', '2', '--transfer-value', '2').stdout)
        events_path = state / 'events.jsonl'
        events_path.write_text(events_path.read_text().replace('incorrect', 'correct'))
        tamper = run(ledger, '--state-dir', state, 'validate', success=False)
        assert tamper.returncode != 0, 'Tampered ledger was accepted'
        return {'result': 'PASS', 'fresh_process_append_read_project_export': True,
                '48h_due_date': tasks[0]['due_at'], 'tamper_rejected': True,
                'priority_cli': priority, 'synthetic_data_only': True,
                'claude_upload': 'NOT_EXECUTED',
                'scope': 'Extracted ZIP Python runtime smoke; not model behavioral or clinical qualification.'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output_dir.resolve()
    if output.is_relative_to(root):
        raise ValueError('Output must be outside engineering source tree')
    full = source_files(root)
    runtime = {name: data for name, data in full.items() if selected(name)}
    assert len(DESCRIPTION) <= 200
    original = runtime['SKILL.md']
    replacement, count = re.subn(rb'(?m)^description: [^\r\n]*',
                                ('description: "' + DESCRIPTION + '"').encode(), original, count=1)
    assert count == 1
    runtime['SKILL.md'] = replacement
    ref_report = references(root, runtime)
    if ref_report['references_to_excluded_files']:
        raise ValueError(json.dumps(ref_report['references_to_excluded_files'], indent=2))
    capsule_hashes = {n: digest(b) for n, b in full.items() if n.startswith('capsules/')}
    assert capsule_hashes == {n: digest(b) for n, b in runtime.items() if n.startswith('capsules/')}
    changed = [n for n in runtime if runtime[n] != full[n]]
    assert changed == ['SKILL.md']
    zip_data = zip_bytes(runtime)
    assert zip_data == zip_bytes(runtime), 'Non-deterministic runtime build'
    with zipfile.ZipFile(io.BytesIO(zip_data)) as archive:
        assert archive.testzip() is None
        assert {n.removeprefix('p7-study-skill/'): archive.read(n) for n in archive.namelist()} == runtime
    smoke = exercise_zip(zip_data)
    version = full['VERSION'].decode().strip()
    output.mkdir(parents=True, exist_ok=True)
    runtime_path = output / f'P7-Study-Skill-{version}-runtime.zip'
    engineering_path = output / f'P7-Study-Skill-{version}-engineering.zip'
    runtime_path.write_bytes(zip_data)
    engineering = zip_bytes(full)
    engineering_path.write_bytes(engineering)
    report = {'result': 'PASS', 'runtime_entries': len(runtime), 'engineering_entries': len(full),
              'runtime_zip_sha256': digest(zip_data), 'engineering_zip_sha256': digest(engineering),
              'deterministic_runtime': True, 'capsule_hashes': capsule_hashes,
              'all_capsules_byte_identical': True, 'source_checkout_unchanged': full == source_files(root),
              'selected_files': sorted(runtime), 'excluded_from_runtime': sorted(set(full)-set(runtime)),
              'counts': dict(Counter(Path(n).parts[0] for n in runtime)),
              'transformations': [{'file': 'SKILL.md', 'field': 'description',
                  'characters': len(DESCRIPTION), 'body_byte_identical': original.split(b'---', 2)[2] == replacement.split(b'---', 2)[2],
                  'reason': 'Claude Help Center specifies a 200-character description maximum.',
                  'source': 'https://support.claude.com/en/articles/12512198-how-to-create-custom-skills'}],
              'references': ref_report, 'runtime_smoke': smoke,
              'file_count_limit': 'No official 200/250-file limit verified; count is descriptive, not upload certification.'}
    (output / 'RUNTIME_BUILD_REPORT.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'result': report['result'], 'entries': len(runtime), 'zip': str(runtime_path),
                      'report': str(output / 'RUNTIME_BUILD_REPORT.json')}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
