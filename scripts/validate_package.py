#!/usr/bin/env python3
"""Standard-library static validation for a personal Claude Code brand repository.

Covers structure, metadata, path references, placeholders and obvious privacy hazards;
NOT a substitute for visual/clinical/legal review or a live Claude Code install.
"""
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
SK=ROOT/'skills'/'izzul-brand'
REQUIRED=[
 'README.md','.claude-plugin/plugin.json','.claude-plugin/marketplace.json',
 'skills/izzul-brand/SKILL.md',
 *[f'skills/izzul-brand/references/{x}' for x in ['brand-strategy.md','visual-identity.md','voice-and-messaging.md','design-tokens.css','quality-checklist.md','source-provenance.md','brand-decisions.md','content-claims.md','orynlab-repo-reference.md','component-patterns.md']],
 *[f'skills/izzul-brand/templates/{x}' for x in ['quotation.html','proposal.html','proposal.md','technical-report.html','technical-report.md','presentation.html','presentation.md','website-starter.html','website.md']],
 'skills/izzul-brand/assets/palette-reference.svg'
]
errors=[]
for rel in REQUIRED:
 if not (ROOT/rel).is_file():errors.append('Missing '+rel)
for m in ['.claude-plugin/plugin.json','.claude-plugin/marketplace.json']:
 try: meta=json.loads((ROOT/m).read_text())
 except Exception as e:errors.append('Invalid JSON '+m+': '+str(e));continue
 if not isinstance(meta,dict):errors.append('Expected object '+m)
 if m.endswith('plugin.json') and meta.get('name')!='izzul-brand':errors.append('Wrong plugin name')
 if m.endswith('marketplace.json') and not any(p.get('name')=='izzul-brand' for p in meta.get('plugins',[])):errors.append('Marketplace omits plugin')
text=(SK/'SKILL.md').read_text()
if not text.startswith('---\nname: izzul-brand\n'):errors.append('SKILL.md frontmatter missing/incorrect')
for html in (SK/'templates').glob('*.html'):
 body=html.read_text()
 if '<html lang=' not in body or '<title>' not in body:errors.append('No semantic HTML/language/title: '+html.name)
 for href in re.findall(r'<link[^>]+href="([^"]+)"',body):
  if href.startswith(('https:','http:')):continue
  if not (html.parent/href).exists():errors.append('Broken stylesheet '+str(html)+' -> '+href)
 if '[CLIENT' not in body and html.name in ('quotation.html','proposal.html'):errors.append('No client placeholder: '+html.name)
for private in ['portfolio-reference.pdf','Portfolio_Izzul.pdf','portrait.jpg','email.txt']:
 if list(ROOT.rglob(private)):errors.append('Private file included: '+private)
if 'accepted working ethos' in (SK/'references/brand-strategy.md').read_text().lower():errors.append('Previously mistaken approved ethos still present')
if errors:
 print('FAIL: '+str(len(errors))+' issues')
 for err in errors:print(' - '+err)
 sys.exit(1)
print('PASS: required files, plugin metadata, skill frontmatter, HTML stylesheets and basic privacy/approval guards')
print('Note: this does not test Claude Code installation or validate print/visual quality.')
