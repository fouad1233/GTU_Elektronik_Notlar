#!/usr/bin/env python3
"""check_site.py <site-dir> — iç bağlantıları, kimlik (#anchor) hedeflerini ve etiket dengesini denetler."""
import os, re, sys, urllib.parse
from html.parser import HTMLParser
VOID = {'meta', 'link', 'img', 'br', 'hr', 'input', 'source', 'wbr', 'area', 'col', 'base', 'embed', 'track', 'param'}
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.refs, self.ids = [], [], [], set()
        self.title = None; self._t = False; self.metas = {}; self.canon = None; self.h1 = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'a' and a.get('href'): self.refs.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.refs.append(a['src'])
        if tag == 'link' and a.get('href') and a.get('rel') in ('stylesheet', 'icon', 'apple-touch-icon'): self.refs.append(a['href'])
        if tag == 'meta' and a.get('name'): self.metas[a['name']] = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical': self.canon = a.get('href')
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self._t = True
        if tag not in VOID: self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag == 'title': self._t = False
        if tag in VOID: return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append('closing </%s> but open stack ends with %s' % (tag, self.stack[-3:]))
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag: pass
        else:
            self.stack.pop()
    def handle_data(self, d):
        if self._t: self.title = (self.title or '') + d
root = os.path.abspath(sys.argv[1])
pages = []
for dp, dn, fn in os.walk(root):
    for f in fn:
        # google<kod>.html Search Console doğrulama dosyalarıdır (sayfa değil); denetime girmez
        if f.endswith('.html') and not re.match(r'google[0-9a-f]+\.html$', f): pages.append(os.path.join(dp, f))
bad = 0; nlinks = 0; ids_cache = {}
titles = {}; descs = {}
for pg in sorted(pages):
    rel = os.path.relpath(pg, root)
    p = P(); p.feed(open(pg, encoding="utf-8").read())
    ids_cache[pg] = p.ids
    probs = list(p.errors)
    if p.stack: probs.append('unclosed: %s' % p.stack)
    if not p.title: probs.append('no <title>')
    if rel != '404.html':
        if p.h1 != 1: probs.append('h1 count %d' % p.h1)
        d = p.metas.get('description', '')
        if not (50 <= len(d) <= 175): probs.append('description length %d' % len(d))
        titles.setdefault(p.title, []).append(rel); descs.setdefault(d, []).append(rel)
    for r in p.refs:
        if re.match(r'(https?:|mailto:|data:|javascript:)', r): continue
        nlinks += 1
        path, _, frag = r.partition('#'); path = path.split('?')[0]
        base = os.path.dirname(pg)
        tgt = os.path.normpath(os.path.join(base, urllib.parse.unquote(path))) if path else pg
        if os.path.isdir(tgt): tgt = os.path.join(tgt, 'index.html')
        if not os.path.exists(tgt):
            probs.append('missing target %s' % r); continue
        if frag and tgt.endswith('.html'):
            if tgt not in ids_cache:
                q = P(); q.feed(open(tgt, encoding='utf-8').read()); ids_cache[tgt] = q.ids
            if frag not in ids_cache[tgt]: probs.append('missing anchor %s' % r)
    for pr in probs:
        bad += 1; print('%s: %s' % (rel, pr))
dup = {t: v for t, v in titles.items() if len(v) > 1}
for t, v in dup.items(): print('DUP TITLE %r: %s' % (t, v[:4])); bad += 1
dupd = {t: v for t, v in descs.items() if len(v) > 1}
for t, v in dupd.items(): print('DUP DESC %r: %s' % (t[:60], v[:4])); bad += 1
print('checked %d pages, %d internal refs, %d problem(s)' % (len(pages), nlinks, bad))
sys.exit(1 if bad else 0)
