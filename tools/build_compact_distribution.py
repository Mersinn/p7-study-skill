#!/usr/bin/env python3
"""Build the compact install artifact, preserving source and reference content."""
from __future__ import annotations
import argparse
import importlib.util
import io
import json
import re
import tempfile
import zipfile
from pathlib import Path

DEFAULT_REPO = Path(__file__).resolve().parents[1]
PAIRS = {
    'ACTIVE_STUDY.md': ('ACTIVE_STUDY_QUESTION_FIRST.md', 'ACTIVE_STUDY_REVEAL_AFTER_ATTEMPT.md'),
    'STUDY_AND_CLASS.md': ('STUDY_GUIDE_GENERATOR.md', 'AULA_VIVA.md'),
    'FOCUS_AND_SUPPORT.md': ('IGOR_ME_SALVA.md', 'ADHD_AND_TOKEN_POLICY.md'),
    'CLINICAL_PRACTICE_DRILLS.md': ('EXAME_ESTADO_MENTAL_DRILL.md', 'CASE_OSCE_TUTOR.md'),
    'CLINICAL_SAFETY.md': ('CLINICAL_CLAIM_REVIEW.md', 'MEDICAL_SAFETY_LAYER.md'),
    'LEARNER_AND_REVIEW.md': ('LEARNER_STATE_PROTOCOL.md', 'ERROR_NOTEBOOK_REVIEW_QUEUE.md'),
    'PLANNING_AND_SIMULATION.md': ('TARGET_AWARE_STUDY_PLANNER.md', 'SIMULATION_PROTOCOL.md'),
    'SOURCES_AND_PATTERN.md': ('SOURCE_POLICY.md', 'PATTERN_ANALYZER_CONTRACT.md'),
}
ROUTES = {old: (new, old.removesuffix('.md').lower().replace('_', '-'))
          for new, pair in PAIRS.items() for old in pair}
PATTERN = re.compile(r'(?<![\w.-])(' + '|'.join(map(re.escape, ROUTES)) + r')(?![\w.-])')
ROUTING = ('\n\n## Leitura das referências\n\n'
           'Os caminhos com `#` apontam para uma seção dentro de um arquivo. '
           'Abra o arquivo antes de `#` e localize a âncora indicada; leia somente '
           'essa seção e as dependências que ela pedir. O índice no início de cada '
           'arquivo permite escolher o trecho sem carregar os outros modos.\n')

def transform(text):
    def replace(match):
        old = match[1]
        if text[match.end():].startswith('#'):
            raise ValueError('Existing fragment needs explicit migration: '+old)
        new, anchor = ROUTES[old]
        return new+'#'+anchor
    return PATTERN.sub(replace, text)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=DEFAULT_REPO)
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent/'final-delivery')
    args=parser.parse_args()
    repo=args.repo.resolve()
    root=repo/'p7-study-skill'
    output=args.output_dir.resolve()
    assert not output.is_relative_to(root)
    spec=importlib.util.spec_from_file_location('runtime_builder',repo/'tools/build_runtime_distribution.py')
    base=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    source=base.source_files(root)
    original={name:data for name,data in source.items() if base.selected(name)}
    before_links=base.references(root,original)
    assert not before_links['references_to_excluded_files'],before_links['references_to_excluded_files']
    runtime={name:transform(data.decode('utf-8')).encode('utf-8') if name.endswith('.md') else data
             for name,data in original.items()}
    roundtrip=[]
    for bundle,pair in PAIRS.items():
        # Marker delimiters allow exact extraction and verification of every preserved source.
        parts=[f'# {bundle.removesuffix(".md").replace("_", " ")}\n\n',
               'Leia somente a seção solicitada; cada entrada abaixo leva ao seu início.\n\n']
        for old in pair:
            anchor=ROUTES[old][1]
            title=original['references/'+old].decode('utf-8').splitlines()[0].lstrip('# ')
            parts.append(f'- [{title}](#{anchor})\n')
        for old in pair:
            anchor=ROUTES[old][1]
            content=runtime.pop('references/'+old).decode('utf-8')
            parts.extend([f'\n<a id="{anchor}"></a>\n\n<!-- BEGIN {anchor} -->\n',content,
                          f'\n<!-- END {anchor} -->\n'])
        runtime['references/'+bundle]=''.join(parts).encode('utf-8')
        for old in pair:
            anchor=ROUTES[old][1]
            generated=runtime['references/'+bundle].decode('utf-8')
            recovered=generated.split(f'<!-- BEGIN {anchor} -->\n',1)[1].split(f'\n<!-- END {anchor} -->',1)[0]
            expected=transform(original['references/'+old].decode('utf-8'))
            assert recovered==expected,old
            roundtrip.append({'source':'references/'+old,'destination':'references/'+bundle+'#'+anchor,
                              'source_sha256':base.digest(original['references/'+old]),
                              'transformed_content_sha256':base.digest(recovered.encode('utf-8')),
                              'content_preserved_except_reference_paths':True})
    # The two independent references stay separate and are also round-tripped.
    for name,data in original.items():
        if name.startswith('references/') and Path(name).name not in ROUTES:
            assert runtime[name]==transform(data.decode('utf-8')).encode('utf-8')
            roundtrip.append({'source':name,'destination':name,'source_sha256':base.digest(data),
                              'transformed_content_sha256':base.digest(runtime[name]),
                              'content_preserved_except_reference_paths':True})
    skill=runtime['SKILL.md']
    skill,n=re.subn(rb'(?m)^description: [^\r\n]*',('description: "'+base.DESCRIPTION+'"').encode('utf-8'),skill,count=1)
    assert n==1 and len(base.DESCRIPTION)<=200
    runtime['SKILL.md']=skill+ROUTING.encode('utf-8')
    runtime['VERSION']=b'1.5.1\n'
    assert len(runtime)<=199,len(runtime)
    # Full filename token scan includes bare filenames, backticks and Markdown links.
    for name,data in runtime.items():
        assert not PATTERN.search(data.decode('utf-8')),name
    preserved={}
    for prefix in ('capsules/','registry/','scripts/','config/','p7_source_pack/','artifacts/'):
        expected={n:base.digest(d) for n,d in original.items() if n.startswith(prefix)}
        actual={n:base.digest(d) for n,d in runtime.items() if n.startswith(prefix)}
        assert expected==actual,prefix
        preserved[prefix]={'files':len(expected),'byte_identical':True}
    with tempfile.TemporaryDirectory(prefix='p7-compact-links-') as temp:
        virtual=Path(temp)
        for name,data in runtime.items():
            p=virtual/name
            p.parent.mkdir(parents=True,exist_ok=True)
            p.write_bytes(data)
        links=base.references(virtual,runtime)
        assert not links['references_to_excluded_files'],links['references_to_excluded_files']
        # Check all moved-path references, including bare filenames omitted by the base checker.
        moved=[]
        token_pattern=re.compile(r'(?<![\w.-])('+ '|'.join(map(re.escape,PAIRS)) +r')#([a-z0-9-]+)')
        for name,data in runtime.items():
            for m in token_pattern.finditer(data.decode('utf-8')):
                target='references/'+m[1]
                assert target in runtime
                assert f'<a id="{m[2]}"></a>'.encode() in runtime[target],(name,m[0])
                moved.append({'from':name,'target':target+'#'+m[2]})
        assert moved
        # Any originally resolved package dependency must still resolve after migration.
        for record in before_links['resolved']:
            target=record['target']
            old=Path(target).name
            if target.startswith('references/') and old in ROUTES:
                target='references/'+ROUTES[old][0]
            assert target in runtime or any(n.startswith(target+'/') for n in runtime),record
    archive=base.zip_bytes(runtime)
    assert archive==base.zip_bytes(runtime)
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        assert z.testzip() is None
        assert {n.removeprefix('p7-study-skill/'):z.read(n) for n in z.namelist()}==runtime
    smoke=base.exercise_zip(archive)
    assert source==base.source_files(root),'Source changed during build'
    output.mkdir(parents=True,exist_ok=True)
    version=runtime['VERSION'].decode().strip()
    filename=output/f'P7-Study-Skill-{version}.zip'
    filename.write_bytes(archive)
    report={'result':'PASS','zip':str(filename),'sha256':base.digest(archive),'entries':len(runtime),
            'bytes':len(archive),'reference_files_before':18,'reference_files_after':10,
            'all_18_references_roundtrip':roundtrip,'moved_path_references_verified':moved,
            'original_resolved_dependencies_preserved':len(before_links['resolved']),
            'remaining_preexisting_nonpackage_references':links['already_absent_or_non_file_literals'],
            'description_characters':len(base.DESCRIPTION),'version':version,
            'preserved':preserved,'source_checkout_unchanged':True,'deterministic_zip':True,
            'runtime_smoke':smoke,'selected_files':sorted(runtime),
            'scope':'Packaging and extracted Python runtime checks; no behavioral gate or Claude upload certification.'}
    report_path=output/'COMPACT_BUILD_REPORT.json'
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('result','zip','sha256','entries','bytes')},ensure_ascii=False))
    print('report: '+str(report_path))

if __name__=='__main__':
    main()
