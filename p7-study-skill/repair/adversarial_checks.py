#!/usr/bin/env python3
"""Independent technical checks; synthetic cases are not clinical/release gates."""
import argparse, collections, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
default_root = Path(__file__).resolve().parent.parent
if not (default_root / 'scripts' / 'p7lib.py').is_file():
    default_root = default_root / 'inspection' / 'p7-study-skill'
p=argparse.ArgumentParser(); p.add_argument('--root',type=Path,default=default_root); p.add_argument('--baseline',type=Path,default=Path(__file__).with_name('BASELINE.json'));p.add_argument('--output',type=Path,default=None);a=p.parse_args()
sys.path.insert(0,str(a.root/'scripts')); import p7lib
checks=[]
def check(name,condition,evidence): checks.append(dict(name=name,passed=bool(condition),evidence=evidence))
def case(name,text,ids,status,expected_ids=None):
 got=p7lib.referenced_source_ids(text,ids);check(name,got['status']==status and (expected_ids is None or got['source_ids']==sorted(expected_ids)),dict(text=text,known_ids=ids,expected_status=status,actual=got))
A='Clinicos__1111111111'; B='Clinicos__2222222222'; C='Cl_nicos__3333333333'
case('exact literal',A,[A],'resolved:exact',[A])
case('exact dominates inferred',A+'; Cl_nicos',[A,C],'resolved:exact',[A])
case('distinct explicit IDs preserved',A+'; '+B,[A,B],'resolved:exact',[A,B])
case('stem same-level collision','Clinicos p.1',[A,B],'ambiguous',[])
case('stem dominates placeholder','Clinicos p.1',[A,C],'resolved:stem',[A])
case('folded diacritics','CLÍNICOS p.1',[A],'resolved:folded',[A])
case('folded dominates placeholder','CLÍNICOS p.1',[A,C],'resolved:folded',[A])
case('folded collision','CLÍNICOS p.1',[A,B],'ambiguous',[])
case('placeholder one character','Clinicos p.1',[C],'resolved:placeholder',[C])
case('placeholder cannot eat zero','Clnicos p.1',[C],'unresolved_source_reference',[])
case('placeholder cannot eat two','Cliinicos p.1',[C],'unresolved_source_reference',[])
case('placeholder cannot cross space','Cl nicos p.1',[C],'unresolved_source_reference',[])
case('placeholder cannot cross slash','Cl/nicos p.1',[C],'unresolved_source_reference',[])
case('placeholder same-level collision','Clinicos p.1',[C,'Cli_icos__4444444444'],'ambiguous',[])
case('no prose prefix matching','resumo de Clinicos p.1',[C],'unresolved_source_reference',[])
case('no left-substring','XClinicos p.1',[A],'unresolved_source_reference',[])
case('no right-substring','ClinicosExtra p.1',[A],'unresolved_source_reference',[])
case('unknown hash not inferred','Clinicos__9999999999',[A],'unresolved_source_reference',[])
case('short stem rejected','Asma p.1',['Asma__5555555555'],'unresolved_source_reference',[])
case('short exact preserved','Asma__5555555555',['Asma__5555555555'],'resolved:exact',['Asma__5555555555'])
case('non-hash stem not inferred','Clinicos',['Clinicos__notahash'],'unresolved_source_reference',[])
case('declared general dominates exact',A+'; conhecimento geral',[A],'declared_no_source',[])
case('declared absent dominates exact',A+'; AUSENTE DA FONTE',[A],'declared_no_source',[])
case('declared general dominates inferred','Clinicos (conhecimento geral)',[A],'declared_no_source',[])
case('semicolon segment anchoring','sem referência; Clinicos p.1',[A],'resolved:stem',[A])
case('backtick source title','`Clinicos` p.1',[A],'resolved:stem',[A])
rows=p7lib.precision_rows(a.root); base=json.loads(a.baseline.read_text(encoding='utf-8')); old=base['precision_rows'];key=lambda x:(x['capsule_path'],str(x['section_row'])); current={key(x):x for x in rows}; old_res=[x for x in old if x['source_reference_status']=='resolved'];multi=[x for x in old_res if ';' in x['source_ids']]
check('precision denominator and row identities',len(rows)==2392 and len(current)==2392 and set(current)=={key(x) for x in old},dict(before=len(old),after=len(rows)))
check('all legacy resolved IDs preserved',all(current[key(x)]['source_reference_status']=='resolved:exact' and current[key(x)]['source_ids']==x['source_ids'] for x in old_res),dict(denominator=len(old_res)))
check('all legacy explicit multiple citations preserved',len(multi)==8 and all(current[key(x)]['source_ids']==x['source_ids'] and current[key(x)]['source_reference_status']=='resolved:exact' for x in multi),dict(denominator=len(multi)))
markers=[x for x in rows if any(m in p7lib.fold(x['claim_text']) for m in ['conhecimento geral','ausente da fonte'])]
check('declared absence never resolved',all(x['source_reference_status']=='declared_no_source' and not x['source_ids'] for x in markers),dict(denominator=len(markers)))
allowed={'resolved:exact','resolved:stem','resolved:folded','resolved:placeholder','declared_no_source','ambiguous','unresolved_source_reference'}
check('no generic status',all(x['source_reference_status'] in allowed for x in rows),dict(denominator=len(rows)))
sources=p7lib.load_source_rows(a.root); ids={x['source_id'] for x in sources};check('resolved IDs exist in manifest',all(set(x['source_ids'].split(';'))<=ids for x in rows if x['source_ids']),dict(resolved_rows=sum(bool(x['source_ids']) for x in rows),manifest_rows=len(sources)))
check('source corpus unchanged',all(current[key(x)]['claim_text']==x['claim_text'] for x in old),dict(denominator=len(old)))
files=['scripts/p7lib.py','p7_source_pack/00_SOURCE_MANIFEST.csv']; hashes={f:hashlib.sha256((a.root/f).read_bytes()).hexdigest() for f in files}
report=dict(label='VERIFICADO',measured_at=datetime.now(timezone.utc).isoformat(),documented_source_commit=base['documented_source_commit'],measured_commit=None,source_zip_sha256=base['zip_sha256'],hashes=hashes,precision_denominator=len(rows),precision_counts=dict(collections.Counter(x['source_reference_status'] for x in rows)),checks_passed=sum(x['passed'] for x in checks),checks_denominator=len(checks),checks=checks,limits=['Synthetic adversarial cases are independent technical tests, not reexecution of historical release gates.','Lexical source identity does not prove that a page supports a clinical claim.','This technical check does not inspect primary PDFs or perform clinical validation/promotion.','No real folded matches: original five-per-level sample requirement cannot be met.'])
if a.output is not None:
    a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['checks','limits']},ensure_ascii=False,indent=2));sys.exit(0 if all(x['passed'] for x in checks) else 1)
