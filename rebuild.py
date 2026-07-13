#!/usr/bin/env python3
"""Rebuild index.html + sw.js from the current reference-source.json.
Run this after regenerating the reference from the build kit, then commit.
Requires the base java-reference.html (PWA tags get injected here)."""
import json, hashlib, pathlib, sys

here = pathlib.Path(__file__).parent
src = here / 'reference-source.json'
base = here / 'java-reference.html'   # the plain reference (no PWA tags)
if not base.exists():
    sys.exit("Place the freshly built java-reference.html next to this script first.")

ver = hashlib.sha1(src.read_bytes()).hexdigest()[:8]

PWA_HEAD = '''<link rel="manifest" href="./manifest.webmanifest">
<meta name="theme-color" content="#0F7B8A">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Java Ref">
<link rel="apple-touch-icon" href="./icon-192.png">
<link rel="icon" type="image/png" sizes="512x512" href="./icon-512.png">'''

SW_REG = '''<script>
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('./sw.js').catch(function(){});
  });
}
</script>'''

html = base.read_text(encoding='utf-8')
anchor = '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
if 'manifest.webmanifest' not in html:
    html = html.replace(anchor, anchor + '\n' + PWA_HEAD, 1)
    html = html.replace('</body>', SW_REG + '\n</body>', 1)
(here / 'index.html').write_text(html, encoding='utf-8')

sw = (here / 'sw.js').read_text(encoding='utf-8')
import re
sw = re.sub(r"const CACHE = 'javaref-[^']*';", f"const CACHE = 'javaref-{ver}';", sw)
(here / 'sw.js').write_text(sw, encoding='utf-8')
print(f"Rebuilt. Cache version → javaref-{ver}. Commit and push to publish.")
