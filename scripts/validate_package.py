"""Maintenance checks; requires PyYAML, not needed for using the skill."""
from pathlib import Path
import re,json,sys
import yaml
root=Path(__file__).resolve().parents[1]
body=(root/'SKILL.md').read_text(encoding='utf-8')
front,content=body.split('---',2)[1:]
meta=yaml.safe_load(front)
assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',meta['name']) and len(meta['name'])<=64
assert meta['name']==root.name and 0<len(meta['description'])<=1024
assert meta['license']=='MIT' and meta['metadata']['version']=='2.1.0'
assert len(body.splitlines())<500
assert 'MIT License' in (root/'LICENSE').read_text(encoding='utf-8')
assert all(isinstance(k,str) and isinstance(v,str) for k,v in meta['metadata'].items())
links=0
for f in root.rglob('*'):
 if not f.is_file() or '.git' in f.relative_to(root).parts:continue
 assert f.suffix in {'.md','.txt','.json','.yaml','.yml','.py','.csv'} or f.name in {'LICENSE','.gitignore'},f
 text=f.read_text(encoding='utf-8-sig')
 if f.suffix!='.py': assert not re.search(r'(?<![A-Za-z])[A-Za-z]:[\\/]|/Users/|/home/|18142',text),f
 if f.suffix=='.md':
  for link in re.findall(r'\]\(([^)]+)\)',text):
   if '://' in link or link.startswith('#'):continue
   target=(f.parent/link.split('#')[0]).resolve()
   assert target.is_relative_to(root.resolve()) and target.is_file(),(f,link)
   links+=1
 if f.suffix=='.json':json.loads(text)
cases=json.loads((root/'evals/cases.json').read_text(encoding='utf-8'))
assert len(cases)>=5 and len({c['id'] for c in cases})==len(cases)
assert all(c['execution_status']=='not_run' for c in cases)
ui=yaml.safe_load((root/'agents/openai.yaml').read_text(encoding='utf-8'))
assert '$'+root.name in ui['interface']['default_prompt']
print(json.dumps({'skill':root.name,'local_links':links,'structure':'passed','behavioral_eval':'not_run'},ensure_ascii=False))
