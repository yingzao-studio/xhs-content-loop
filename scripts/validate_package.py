from pathlib import Path
import re, json
root=Path(__file__).resolve().parents[1]
body=(root/'SKILL.md').read_text(encoding='utf-8')
assert body.startswith('---\n')
front=body.split('---',2)[1]
fields=dict(line.split(':',1) for line in front.strip().splitlines())
assert fields['name'].strip()==root.name
assert fields['description'].strip() and len(fields['description'].strip())<=1024
assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',root.name)
count=0
for file in root.rglob('*'):
    if not file.is_file(): continue
    assert file.suffix in {'.md','.yaml','.py','.txt','.json'},file
    text=file.read_text(encoding='utf-8')
    if file.suffix=='.md':
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if '://' not in link and not link.startswith('#'):
                target=(file.parent/link.split('#')[0]).resolve()
                assert target.is_relative_to(root.resolve()) and target.is_file(),(file,link)
                count+=1
    if file.suffix!='.py':
        assert not re.search(r'(?<![A-Za-z])[A-Za-z]:[\\/]|/Users/|/home/|18142|source-workbook|source-media|workbook-index|ten-cases',text),file
assert not (root/'assets').exists()
assert '$'+root.name in (root/'agents/openai.yaml').read_text(encoding='utf-8')
print(json.dumps({'skill':root.name,'local_links':count,'audit':'passed'},ensure_ascii=False))
