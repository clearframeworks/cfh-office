#!/usr/bin/env python3
"""Remove CFH Office's donation controls from distributed menu layouts.

CFH modification, 2026-11-07. The upstream donation command definition remains
for compatibility, but the command handler is disabled in this fork.
"""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
MENU = re.compile(r'(?m)^[ \t]*<menu:menuitem\b[^>]*menu:id="\.uno:Donation"[^>]*/>[ \t]*\r?\n')
GTK = re.compile(r'(?s)[ \t]*<child>\s*<object\b(?:(?!<child>).)*?<property name="action[-_]name">\.uno:Donation</property>(?:(?!<child>).)*?</object>\s*</child>[ \t]*\r?\n')
changed = []
for path in ROOT.rglob('*'):
    if not path.is_file() or path.suffix not in ('.xml', '.ui') or 'uiconfig' not in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    if '.uno:Donation' not in text:
        continue
    rewritten, count = (MENU if path.suffix == '.xml' else GTK).subn('', text)
    if not count or '.uno:Donation' in rewritten:
        raise SystemExit(f'Unrecognized donation control in {path.relative_to(ROOT)}')
    ET.fromstring(rewritten)
    path.write_text(rewritten, encoding='utf-8', newline='\n')
    changed.append((str(path.relative_to(ROOT)), count))
print(f'CFH donation controls removed: {sum(n for _, n in changed)} in {len(changed)} files')
for name, count in changed:
    print(f'{name}: {count}')