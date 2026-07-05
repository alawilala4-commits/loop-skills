from pathlib import Path
import re, sys
skills = sorted(Path('skills').rglob('SKILL.md'))
errors = []
for p in skills:
    text = p.read_text()
    fm = re.search(r'^---(.*?)---', text, re.S)
    if not fm:
        errors.append(f'no-frontmatter: {p}')
        continue
    fm_text = fm.group(1)
    for field in ['name','description']:
        if field not in fm_text:
            errors.append(f'frontmatter-missing:{field}: {p}')
    if re.search(r'^#{1,6}\s*$', text, re.M):
        errors.append(f'empty-heading: {p}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'semantic checks passed for {len(skills)} skills')
