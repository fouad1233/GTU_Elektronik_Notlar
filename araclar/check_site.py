#!/usr/bin/env python3
"""check_site.py <site-dir> — iç bağlantıları, kimlik (#anchor) hedeflerini, etiket dengesini ve
Türkçe/İngilizce sayfa eşleşmelerini (hreflang) denetler."""
import os, re, sys, urllib.parse
from html.parser import HTMLParser
VOID = {'meta', 'link', 'img', 'br', 'hr', 'input', 'source', 'wbr', 'area', 'col', 'base', 'embed', 'track', 'param'}
BASE = 'https://fouad1233.github.io/GTU_Elektronik_Notlar/'
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.refs, self.ids = [], [], [], set()
        self.title = None; self._t = False; self.metas = {}; self.canon = None; self.h1 = 0
        self.alts = {}; self.lang = None; self.props = {}
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'a' and a.get('href'): self.refs.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.refs.append(a['src'])
        if tag == 'link' and a.get('href') and a.get('rel') in ('stylesheet', 'icon', 'apple-touch-icon'): self.refs.append(a['href'])
        if tag == 'meta' and a.get('name'): self.metas[a['name']] = a.get('content', '')
        if tag == 'meta' and a.get('property'): self.props.setdefault(a['property'], []).append(a.get('content', ''))
        if tag == 'link' and a.get('rel') == 'canonical': self.canon = a.get('href')
        if tag == 'link' and a.get('rel') == 'alternate' and a.get('hreflang'): self.alts[a['hreflang']] = a.get('href')
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
def url_to_file(url):
    """https://…/GTU_Elektronik_Notlar/en/x/ -> en/x/index.html (None: site dışı)"""
    if not url or not url.startswith(BASE): return None
    rel = url[len(BASE):]
    return rel + 'index.html' if rel == '' or rel.endswith('/') else rel
def lang_of(rel):
    return 'en' if rel.startswith('en/') else 'tr'
root = os.path.abspath(sys.argv[1])
pages = []
for dp, dn, fn in os.walk(root):
    for f in fn:
        # google<kod>.html Search Console doğrulama dosyalarıdır (sayfa değil); denetime girmez
        if f.endswith('.html') and not re.match(r'google[0-9a-f]+\.html$', f): pages.append(os.path.join(dp, f))
bad = 0; nlinks = 0; ids_cache = {}
titles = {}; descs = {}; info = {}; crossrefs = {}
for pg in sorted(pages):
    rel = os.path.relpath(pg, root)
    p = P(); p.feed(open(pg, encoding="utf-8").read())
    ids_cache[pg] = p.ids
    info[rel] = p
    probs = list(p.errors)
    if p.stack: probs.append('unclosed: %s' % p.stack)
    if not p.title: probs.append('no <title>')
    if rel != '404.html':
        if p.h1 != 1: probs.append('h1 count %d' % p.h1)
        d = p.metas.get('description', '')
        if not (50 <= len(d) <= 175): probs.append('description length %d' % len(d))
        titles.setdefault(p.title, []).append(rel); descs.setdefault(d, []).append(rel)
        if p.lang != lang_of(rel): probs.append('html lang=%r, expected %r' % (p.lang, lang_of(rel)))
        if url_to_file(p.canon) != rel: probs.append('canonical %r does not point to this page' % p.canon)
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
        # öteki dilin sayfasına giden bağlantılar (yalnızca dil düğmeleri olmalı)
        if tgt.endswith('.html') and rel != '404.html':
            trel = os.path.relpath(tgt, root)
            if lang_of(trel) != lang_of(rel): crossrefs.setdefault(rel, set()).add(trel)
    for pr in probs:
        bad += 1; print('%s: %s' % (rel, pr))
# hreflang: her sayfa kendisi + karşılığı + x-default vermeli, karşılığı da geri vermeli
nalt = 0
for rel, p in sorted(info.items()):
    if rel == '404.html' or not p.alts: continue
    nalt += 1
    probs = []
    me = lang_of(rel); other = 'tr' if me == 'en' else 'en'
    if set(p.alts) != {'tr', 'en', 'x-default'}: probs.append('hreflang set %s' % sorted(p.alts))
    else:
        if url_to_file(p.alts[me]) != rel: probs.append('hreflang %s is not this page' % me)
        if p.alts['x-default'] != p.alts['tr']: probs.append('x-default is not the Turkish page')
        peer = url_to_file(p.alts[other])
        if peer not in info: probs.append('hreflang %s target missing: %s' % (other, p.alts[other]))
        else:
            back = info[peer].alts
            if url_to_file(back.get(me)) != rel: probs.append('%s does not link back (hreflang %s)' % (peer, me))
            if lang_of(peer) != other: probs.append('hreflang %s points to a %s page' % (other, lang_of(peer)))
            stray = crossrefs.get(rel, set()) - {peer}
            if stray: probs.append('links to other-language pages besides its counterpart: %s' % sorted(stray)[:3])
    loc = p.props.get('og:locale', [None])[0]
    if loc != {'tr': 'tr_TR', 'en': 'en_US'}[me]: probs.append('og:locale %r' % loc)
    for pr in probs:
        bad += 1; print('%s: %s' % (rel, pr))
# Türkçe ve İngilizce sayfa sayıları eşit olmalı
ntr = sum(1 for r, p in info.items() if p.alts and lang_of(r) == 'tr'); nen = sum(1 for r, p in info.items() if p.alts and lang_of(r) == 'en')
if ntr != nen:
    print('page count mismatch: %d Turkish vs %d English' % (ntr, nen)); bad += 1
dup = {t: v for t, v in titles.items() if len(v) > 1}
for t, v in dup.items(): print('DUP TITLE %r: %s' % (t, v[:4])); bad += 1
dupd = {t: v for t, v in descs.items() if len(v) > 1}
for t, v in dupd.items(): print('DUP DESC %r: %s' % (t[:60], v[:4])); bad += 1
print('checked %d pages (%d with hreflang pairs: %d tr / %d en), %d internal refs, %d problem(s)' % (len(pages), nalt, ntr, nen, nlinks, bad))
sys.exit(1 if bad else 0)
