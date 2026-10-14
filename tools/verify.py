#!/usr/bin/env python3
"""Validate published aggregates and file integrity; does not rerun models."""
import csv,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'results/aggregate.json').read_text())
for version,row in d['fragment']['versions'].items():
 assert sum(row.values())==116
 assert row['tp']+row['fn']==52 and row['fp']+row['tn']==64
 tp,fp,fn=row['tp'],row['fp'],row['fn']
 print(version,'P/R/F1:',*(f'{v:.1%}' for v in [tp/(tp+fp),tp/(tp+fn),2*tp/(2*tp+fp+fn)]))
with (ROOT/'results/fragment_metrics.csv').open() as f:
 for r in csv.DictReader(f):
  v=d['fragment']['versions'][r['version']]
  assert all(int(r[k])==v[k] for k in ['tp','fp','fn','tn'])
  for key,value in [('precision',v['tp']/(v['tp']+v['fp'])),('recall',v['tp']/(v['tp']+v['fn'])),('f1',2*v['tp']/(2*v['tp']+v['fp']+v['fn']))]:assert abs(float(r[key])-value)<0.000001
for row in d['endpoint']['versions'].values():assert sum(row['label_sources'].values())==row['cards'] and row['media_cards']<=row['cards']
assert sum(d['ghost']['categories'])==d['ghost']['selected_problem_cases']
g=d['generation_gate'];assert g['produce_groups']+g['skip_groups']==g['decision_groups']
for p in ROOT.rglob('*.md'):
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' not in link and not link.startswith('#'):assert (p.parent/link.split('#')[0]).exists(),link
zh_docs=sorted(p.name for p in (ROOT/'docs').glob('[0-9][0-9]-*.md'))
en_docs=sorted(p.name for p in (ROOT/'docs/en').glob('[0-9][0-9]-*.md'))
assert zh_docs==en_docs and len(zh_docs)==16,(zh_docs,en_docs)
assert (ROOT/'README.en.md').is_file() and (ROOT/'PUBLICATION.en.md').is_file()
manifest=json.loads((ROOT/'MANIFEST.json').read_text())
for name,entry in manifest.items():
 p=ROOT/name;assert p.is_file() and p.stat().st_size==entry['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],name
print('Aggregate arithmetic, bilingual coverage, local links and',len(manifest),'file sizes/SHA256 verified.')
