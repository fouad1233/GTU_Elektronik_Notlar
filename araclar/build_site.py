#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_site.py — GTU_Elektronik_Notlar GitHub Pages sitesini (statik HTML, SEO'lu) üretir.

Kullanım (depo kökünden):
    python3 araclar/build_site.py --out /tmp/site
Çıktı klasörü `gh-pages` dalına konur (bkz. araclar/yayinla.sh). Site, depo ağacını `make_readmes.py`
ile aynı modelden (courses.json + klasör yapısı) okur; yalnızca dijital (LaTeX) notların PDF'leri
siteye kopyalanır, diğer dosyalar GitHub bağlantılarıyla listelenir.
"""
import argparse
import datetime
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import make_readmes as mr  # noqa: E402

USER = 'fouad1233'
REPO = 'GTU_Elektronik_Notlar'
SLUG = '%s/%s' % (USER, REPO)
GH = 'https://github.com/' + SLUG
BASE = 'https://%s.github.io/%s' % (USER, REPO)
AUTHOR = 'Fouad Aladhami'
SITE_TR = 'GTÜ Elektronik Mühendisliği Notları'
SITE_EN = 'GTU Electronics Engineering Notes'
EXTRA_TR = {'isaret': 'işaret', 'isaretler': 'işaretler', 'haberlesme': 'haberleşme', 'sayisal': 'sayısal',
            'olasilik': 'olasılık', 'rastgelelik': 'rastgelelik', 'islemci': 'işlemci', 'islemciler': 'işlemciler',
            'goruntu': 'görüntü', 'isleme': 'işleme', 'ogrenmesi': 'öğrenmesi', 'tasarim': 'tasarım',
            'donusum': 'dönüşüm', 'donusumu': 'dönüşümü', 'sinav': 'sınav', 'cozum': 'çözüm', 'cozumleri': 'çözümleri',
            'soru': 'soru', 'sorulari': 'soruları', 'uygulama': 'uygulama', 'notlari': 'notları', 'donem': 'dönem',
            'turev': 'türev', 'integral': 'integral', 'dalga': 'dalga', 'alan': 'alan', 'teorisi': 'teorisi',
            'olcum': 'ölçüm', 'devreler': 'devreler', 'elemanlar': 'elemanlar', 'kontrol': 'kontrol',
            'sistemleri': 'sistemleri', 'modulasyon': 'modülasyon', 'demodulasyon': 'demodülasyon',
            'frekans': 'frekans', 'filtre': 'filtre', 'oneri': 'öneri', 'rapor': 'rapor', 'raporu': 'raporu',
            'hazirlik': 'hazırlık', 'on': 'ön', 'calisma': 'çalışma', 'calismasi': 'çalışması'}
ORDER = ['genel', 'ders-notlari', 'uygulama-notlari', 'ders-tekrari', 'dijital-notlar', 'slaytlar', 'onceki-yil',
         'cikmis-sorular', 'sinav-calismasi', 'odevler', 'laboratuvar', 'projeler', 'kod', 'arastirma', 'diger']

# --------------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------------
_FOLD = str.maketrans({'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u', 'Ç': 'c', 'Ğ': 'g', 'İ': 'i',
                       'I': 'i', 'Ö': 'o', 'Ş': 's', 'Ü': 'u', 'â': 'a', 'î': 'i', 'û': 'u', 'Â': 'a'})


def fold(s):
    return str(s).translate(_FOLD).lower()


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', fold(s)).strip('-') or 'x'


def esc(s):
    return html.escape(str(s), quote=True)


def qpath(rel):
    return urllib.parse.quote(rel, safe='/')


def blob(rel):
    return '%s/blob/main/%s' % (GH, qpath(rel))


def tree(rel):
    return '%s/tree/main/%s' % (GH, qpath(rel))


def trim(s, n=158):
    s = re.sub(r'\s+', ' ', s).strip()
    if len(s) <= n:
        return s
    return s[:n - 1].rsplit(' ', 1)[0].rstrip(' ,;:.-–—') + '…'


def ld_script(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(',', ':'))
    return '<script type="application/ld+json">%s</script>' % s.replace('</', '<\\/')


def breadcrumb_ld(items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(items)]}


def human(n):
    return mr.human_size(n)


def join_en(items):
    items = list(items)
    if len(items) <= 1:
        return ''.join(items)
    return ', '.join(items[:-1]) + (',' if len(items) > 2 else '') + ' and ' + items[-1]


# --------------------------------------------------------------------------------------------
# LaTeX -> outline / plain text
# --------------------------------------------------------------------------------------------
SEC_RE = re.compile(r'\\(section|subsection|subsubsection)\*?\s*(?:\[[^\]]*\])?\s*\{')
BOX_RE = re.compile(r'\\begin\{(tanim|teorem|dikkat|ozet)\}\s*\[')
MATH_ENVS = (r'(?:align\*?|equation\*?|gather\*?|multline\*?|eqnarray\*?|displaymath|math|tikzpicture|circuitikz|'
             r'axis|tabular\*?|array|cases|pmatrix|bmatrix|vmatrix|matrix|aligned|split|figure|table|picture|'
             r'formulkutu|pgfpicture|scope|minipage)')


def tex_headings(src):
    t = mr.strip_tex_comments(src)
    items = []
    for m in SEC_RE.finditer(t):
        g, _ = mr._read_group(t, m.end() - 1, '{', '}')
        if g:
            items.append((m.start(), g))
    for m in BOX_RE.finditer(t):
        g, _ = mr._read_group(t, m.end() - 1, '[', ']')
        if g:
            items.append((m.start(), g))
    items.sort()
    out, seen = [], set()
    for _, g in items:
        s = mr.latex_to_text(g).strip(' .:;,')
        if len(s) < 3 or not re.search(r'[^\W\d_]{3}', s):
            continue
        k = fold(s)
        if k in seen:
            continue
        seen.add(k)
        out.append(s)
    return out


def tex_prose(src, limit=5000):
    """Düz metin parçası (arama motorları ve erişilebilirlik için); formüller ve çizimler atılır."""
    t = mr.strip_tex_comments(src)
    m = re.search(r'\\begin\{document\}', t)
    if m:
        t = t[m.end():]
    t = t.split('\\end{document}')[0]
    t = re.sub(r'\\notbilgi(?:\[[^\]]*\])?\s*(?:\{(?:[^{}]|\{[^{}]*\})*\}\s*){3}', ' ', t)
    for _ in range(3):
        t = re.sub(r'\\begin\{(%s)\}.*?\\end\{\1\}' % MATH_ENVS, ' ', t, flags=re.S)
    t = re.sub(r'\\\[.*?\\\]', ' ', t, flags=re.S)
    t = re.sub(r'\$\$.*?\$\$', ' ', t, flags=re.S)
    t = re.sub(r'\\elcizimi\s*(?:\[[^\]]*\])?\s*\{[^{}]*\}(?:\s*\[[^\]]*\])?', ' ', t)
    t = re.sub(r'\\(?:sayfa|sekilnotu|okunamadi|iptal[A-Za-z]*|footnotetext|footnotemark|sil)\s*(?:\[[^\]]*\])?\s*'
               r'(?:\{(?:[^{}]|\{[^{}]*\})*\})?', ' ', t)
    t = re.sub(r'\\(?:textcolor|colorbox)\s*\{[^{}]*\}\s*', ' ', t)
    t = re.sub(r'\\fcolorbox\s*\{[^{}]*\}\s*\{[^{}]*\}\s*', ' ', t)
    t = re.sub(r'\\(?:color|hspace\*?|vspace\*?|rule|raisebox|setlength|addtolength|hskip|vskip)\s*'
               r'(?:\[[^\]]*\])?\s*\{[^{}]*\}(?:\s*\{[^{}]*\})?', ' ', t)
    t = re.sub(r'\\(?:qquad|quad|noindent|scriptsize|small|footnotesize|tiny|large|Large|normalsize|hfill|medskip|'
               r'bigskip|smallskip|par|centering|itshape|bfseries|newline|nopagebreak|raggedright|ragged|checkmark)'
               r'(?![A-Za-z])', ' ', t)
    t = re.sub(r'\$([^$]{1,40})\$', lambda mm: ' ' + mr.latex_to_text(mm.group(1)) + ' ', t)
    t = re.sub(r'\$[^$]*\$', ' ', t)
    t = re.sub(r'\\(?:begin|end)\{[^{}]*\}(?:\[[^\]]*\])?', '\n', t)
    t = re.sub(r'\\item\b(?:\[[^\]]*\])?', '\n', t)
    t = t.replace('\\\\', '\n')
    lines, last = [], None
    for ln in t.split('\n'):
        s = mr.latex_to_text(ln)
        if len(s) < 14:
            continue
        letters = sum(ch.isalpha() for ch in s)
        words = [w for w in re.findall(r'[^\W\d_]{2,}', s)]
        if letters / len(s) < 0.62 or len(words) < 3 or s == last:
            continue
        lines.append(s)
        last = s
    out, n = [], 0
    for s in lines:
        n += len(s)
        if n > limit:
            break
        out.append(s)
    return out if (len(out) >= 4 and sum(map(len, out)) >= 300) else []


# --------------------------------------------------------------------------------------------
# static assets
# --------------------------------------------------------------------------------------------
def make_og(path, fonts_dir):
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1200, 630
    im = Image.new('RGB', (W, H), (247, 243, 230))
    d = ImageDraw.Draw(im)
    for x in range(0, W, 30):
        d.line([(x, 0), (x, H)], fill=(222, 227, 238), width=1)
    for y in range(0, H, 30):
        d.line([(0, y), (W, y)], fill=(222, 227, 238), width=1)
    d.line([(96, 0), (96, H)], fill=(236, 160, 160), width=3)
    cav = os.path.join(fonts_dir, 'Caveat-Bold.ttf')
    sh = os.path.join(fonts_dir, 'ShantellSans-Regular.ttf')
    f1 = ImageFont.truetype(cav, 168)
    f2 = ImageFont.truetype(cav, 128)
    f3 = ImageFont.truetype(sh, 34)
    f4 = ImageFont.truetype(sh, 30)
    d.text((140, 70), 'GTÜ Elektronik', font=f1, fill=(29, 39, 66))
    w2 = d.textlength('Mühendisliği', font=f2)
    d.rectangle([140, 318, 140 + w2 + 250, 330], fill=(255, 224, 102))
    d.text((140, 215), 'Mühendisliği', font=f2, fill=(29, 39, 66))
    d.text((140 + w2 + 20, 215), 'Notları', font=f2, fill=(42, 90, 168))
    d.text((140, 385), 'Gebze Teknik Üniversitesi · ders notları · çıkmış sorular', font=f3, fill=(70, 78, 100))
    d.text((140, 432), 'ödevler · lab · projeler · dijital LaTeX notlar · ücretsiz', font=f3, fill=(70, 78, 100))
    d.text((140, 536), '%s.github.io/%s' % (USER, REPO), font=f4, fill=(42, 90, 168))
    im.save(path, optimize=True)


def make_icons(out):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" '
           'fill="#2a5aa8"/><path d="M15 19h34M15 30h34M15 41h18" stroke="#fff" stroke-width="4.5" '
           'stroke-linecap="round"/><circle cx="46" cy="44" r="9" fill="#ffe066"/></svg>')
    open(os.path.join(out, 'favicon.svg'), 'w', encoding='utf-8').write(svg)
    from PIL import Image, ImageDraw
    s = 180
    im = Image.new('RGB', (s, s), (42, 90, 168))
    d = ImageDraw.Draw(im)
    k = s / 64.0
    for y, x2 in ((19, 49), (30, 49), (41, 33)):
        d.line([(15 * k, y * k), (x2 * k, y * k)], fill=(255, 255, 255), width=int(4.5 * k))
        d.ellipse([15 * k - 2.2 * k, y * k - 2.2 * k, 15 * k + 2.2 * k, y * k + 2.2 * k], fill=(255, 255, 255))
        d.ellipse([x2 * k - 2.2 * k, y * k - 2.2 * k, x2 * k + 2.2 * k, y * k + 2.2 * k], fill=(255, 255, 255))
    d.ellipse([37 * k, 35 * k, 55 * k, 53 * k], fill=(255, 224, 102))
    im.save(os.path.join(out, 'apple-touch-icon.png'), optimize=True)


# --------------------------------------------------------------------------------------------
# site
# --------------------------------------------------------------------------------------------
class Note:
    pass


class Site:
    def __init__(self, R, repo, out, cache_dir, today):
        self.R, self.repo, self.out, self.cache_dir, self.today = R, repo, out, cache_dir, today
        self.urls = []          # (url, priority)
        self.search = []
        self.cslug = {c.key: mr.site_slug(c.dirname) for c in R.courses}
        self.notes = {}         # course key -> [Note]
        self.sems = sorted(R.semesters)
        self.ncourses = len(R.courses)
        self.nfiles = sum(len(c.files) for c in R.courses)
        self.npdf = sum(1 for c in R.courses for f in c.files if f.ext == 'pdf')
        self.ndig = sum(1 for c in R.courses for d in c.digital if d.pdf)
        self.nproj = sum(len(c.projects) for c in R.courses)

    # ---- file output -----------------------------------------------------------------------
    def write(self, rel, text, sitemap=None):
        p = os.path.join(self.out, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write(text)
        if sitemap is not None:
            self.urls.append((rel[:-len('index.html')] if rel.endswith('index.html') else rel, sitemap))

    def course_url(self, c):
        return 'ders/%s/' % self.cslug[c.key]

    # ---- layout ----------------------------------------------------------------------------
    def layout(self, url, title, desc, body, ld=None, og_type='website', lang='tr', alt=None, active='',
               root=None, noindex=False):
        depth = len([p for p in url.split('/') if p])
        root = root or ('../' * depth if depth else './')
        canon = BASE + '/' + url
        head = ['<meta charset="utf-8">', '<meta name="viewport" content="width=device-width,initial-scale=1">',
                '<title>%s</title>' % esc(title), '<meta name="description" content="%s">' % esc(desc),
                '<link rel="canonical" href="%s">' % esc(canon),
                '<meta name="robots" content="%s">' % ('noindex' if noindex else 'index,follow,max-image-preview:large'),
                '<meta name="author" content="%s">' % AUTHOR]
        for hl, hu in (alt or []):
            head.append('<link rel="alternate" hreflang="%s" href="%s">' % (hl, esc(hu)))
        head += ['<meta name="theme-color" content="#f6f1e3" media="(prefers-color-scheme: light)">',
                 '<meta name="theme-color" content="#131824" media="(prefers-color-scheme: dark)">',
                 '<link rel="icon" href="%sfavicon.svg" type="image/svg+xml">' % root,
                 '<link rel="apple-touch-icon" href="%sapple-touch-icon.png">' % root,
                 '<meta property="og:site_name" content="%s">' % esc(SITE_TR if lang == 'tr' else SITE_EN),
                 '<meta property="og:type" content="%s">' % og_type,
                 '<meta property="og:title" content="%s">' % esc(title),
                 '<meta property="og:description" content="%s">' % esc(desc),
                 '<meta property="og:url" content="%s">' % esc(canon),
                 '<meta property="og:image" content="%s/og-image.png">' % BASE,
                 '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
                 '<meta property="og:locale" content="%s">' % ('tr_TR' if lang == 'tr' else 'en_US'),
                 '<meta name="twitter:card" content="summary_large_image">',
                 '<link rel="preload" href="%sassets/caveat.woff" as="font" type="font/woff" crossorigin>' % root,
                 '<link rel="stylesheet" href="%sassets/style.css">' % root]
        if ld:
            head.append(ld_script(ld))
        if lang == 'tr':
            nav = [('Dersler', root + '#donemler', ''), ('Dijital notlar', root + 'dijital-notlar/', 'dijital'),
                   ('Projeler', root + 'projeler/', 'projeler'), ('English', root + 'en/', 'en'),
                   ('GitHub', GH, 'gh')]
            skip, brand = 'İçeriğe geç', 'Elektronik Notları'
        else:
            nav = [('Courses', root + 'en/#courses', ''), ('Türkçe', root, 'tr'), ('GitHub', GH, 'gh')]
            skip, brand = 'Skip to content', 'Electronics Notes'
        navh = ''.join('<a href="%s"%s%s>%s</a>' % (
            esc(h), ' aria-current="page"' if k and k == active else '',
            ' rel="noopener"' if k == 'gh' else '', esc(t)) for t, h, k in nav)
        if lang == 'tr':
            foot = (
                '<p><strong>%s</strong> — Gebze Teknik Üniversitesi (GTÜ) Elektronik Mühendisliği ders notları, '
                'çıkmış sorular, ödevler, laboratuvar raporları ve projeler. Hazırlayan: '
                '<a href="https://github.com/%s" rel="noopener">%s</a> (@%s), GTÜ Elektronik Mühendisliği mezunu.</p>'
                '<p>%s</p><p>%s</p>'
                '<p><a href="%s" rel="noopener">GitHub deposu</a> · <a href="%s/issues" rel="noopener">Hata bildir / '
                'katkıda bulun</a> · <a href="%sen/">English</a></p>') % (
                SITE_TR, USER, AUTHOR, USER, esc(mr.DISCLAIMER_TR),
                'Çıkmış sorular, slaytlar ve föyler gibi ders materyallerinin hakları ilgili öğretim üyelerine ve '
                'Gebze Teknik Üniversitesi\'ne aittir; burada yalnızca eğitim amacıyla paylaşılmıştır.',
                GH, GH, root)
        else:
            foot = (
                '<p><strong>%s</strong> — lecture notes, past exams, homework, lab reports and projects for '
                'Electronics Engineering at Gebze Technical University (GTU). Maintained by '
                '<a href="https://github.com/%s" rel="noopener">%s</a> (@%s), GTU Electronics Engineering graduate.</p>'
                '<p>%s</p><p>Course materials (past exams, slides, handouts) belong to their instructors and GTU '
                'and are shared for educational purposes only.</p>'
                '<p><a href="%s" rel="noopener">GitHub repository</a> · <a href="%s/issues" rel="noopener">Report an '
                'issue / contribute</a> · <a href="%s">Türkçe</a></p>') % (
                SITE_EN, USER, AUTHOR, USER, esc(mr.DISCLAIMER_EN), GH, GH, root)
        return ('<!doctype html>\n<html lang="%s"><head>\n%s\n</head>\n<body>\n<a class="skip" href="#icerik">%s</a>\n'
                '<header class="top"><div class="wrap"><a class="brand" href="%s"><span class="brand-mark">GTÜ</span>'
                '<span>%s</span></a><nav aria-label="%s">%s</nav></div></header>\n'
                '<main id="icerik" class="wrap">\n%s\n</main>\n<footer class="foot"><div class="wrap">%s</div></footer>\n'
                '</body></html>\n') % (lang, '\n'.join(head), skip, root, brand,
                                      'Ana menü' if lang == 'tr' else 'Main menu', navh, body, foot)

    # ---- small html pieces -------------------------------------------------------------------
    def crumbs(self, root, items):
        parts = []
        for i, (name, href) in enumerate(items):
            parts.append(esc(name) if i == len(items) - 1 or href is None else
                         '<a href="%s">%s</a>' % (esc(href), esc(name)))
        return '<nav class="crumbs" aria-label="Sayfa yolu">%s</nav>' % ' › '.join(parts)

    def search_box(self, root, lang='tr'):
        ph = ('Ders veya konu ara… (ör. Laplace, kontrol sistemleri, ELM)' if lang == 'tr' else
              'Search courses or topics… (e.g. Laplace, control systems)')
        empty = 'Sonuç bulunamadı' if lang == 'tr' else 'No results'
        return ('<form class="search" role="search" onsubmit="return false"><label class="sr" for="q">%s</label>'
                '<input id="q" type="search" placeholder="%s" autocomplete="off"></form><ul id="results" class="results" '
                'aria-live="polite"></ul><script src="%sassets/search.js" defer data-index="%ssearch-index.json" '
                'data-root="%s" data-empty="%s"></script>') % (
            'Ara' if lang == 'tr' else 'Search', esc(ph), root, root, root, empty)

    def sem_card(self, sem, root, lang='tr'):
        cs = self.R.semesters[sem]
        li = []
        for c in cs:
            name = c.name_tr if lang == 'tr' else c.name_en
            li.append('<li><a href="%s%s">%s</a>%s</li>' % (
                root, self.course_url(c), esc(name), ' <span class="code">%s</span>' % esc(c.code) if c.code else ''))
        head = ('<a href="%sdonem/%d/">%s</a>' % (root, sem, mr.sem_label(sem)) if lang == 'tr'
                else 'Semester %d' % sem)
        return '<article class="sem"><h3>%s <small>%s</small></h3><ul>%s</ul></article>' % (
            head, esc(self.R.term(sem, lang)), ''.join(li))

    # ---- notes (digital) ---------------------------------------------------------------------
    def prepare_notes(self):
        os.makedirs(self.cache_dir, exist_ok=True)
        from PIL import Image
        for c in self.R.courses:
            cs = self.cslug[c.key]
            seen, lst = set(), []
            for d in c.digital:
                if not d.pdf:
                    continue
                n = Note()
                n.c, n.d = c, d
                base = slugify(d.stem)
                slug, i = base, 2
                while slug in seen:
                    slug, i = '%s-%d' % (base, i), i + 1
                seen.add(slug)
                n.slug = slug
                n.url = 'ders/%s/%s/' % (cs, slug)
                n.pdf_url = 'pdf/%s/%s.pdf' % (cs, slug)
                n.img_url = 'img/%s/%s.jpg' % (cs, slug)
                n.topic = d.topic or mr.pretty(d.stem)
                src = ''
                if d.tex:
                    try:
                        src = open(d.tex.abs, encoding='utf-8', errors='replace').read()
                    except OSError:
                        src = ''
                n.heads = tex_headings(src)
                n.prose = tex_prose(src)
                n.pages, n.size = d.pdf.pages, d.pdf.size
                # pdf + thumbnail
                dst = os.path.join(self.out, n.pdf_url)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(d.pdf.abs, dst)
                h = hashlib.sha1()
                with open(d.pdf.abs, 'rb') as fh:
                    for chunk in iter(lambda: fh.read(1 << 20), b''):
                        h.update(chunk)
                cached = os.path.join(self.cache_dir, h.hexdigest()[:20] + '.jpg')
                if not os.path.exists(cached):
                    tmp = cached[:-4]
                    subprocess.run(['pdftoppm', '-r', '44', '-f', '1', '-l', '1', '-png', '-singlefile',
                                    d.pdf.abs, tmp], check=True, timeout=180, capture_output=True)
                    im = Image.open(tmp + '.png').convert('RGB')
                    im.save(cached, 'JPEG', quality=72, optimize=True, progressive=True)
                    os.remove(tmp + '.png')
                idst = os.path.join(self.out, n.img_url)
                os.makedirs(os.path.dirname(idst), exist_ok=True)
                shutil.copyfile(cached, idst)
                n.wh = Image.open(cached).size
                lst.append(n)
            self.notes[c.key] = lst
        seen = {}
        for lst in self.notes.values():
            for n in lst:
                seen.setdefault(fold(self.note_title(n)), []).append(n)
        for group in seen.values():
            if len(group) > 1:
                for n in group:
                    n.topic = '%s (%s)' % (n.topic, mr.pretty(n.d.stem))

    def note_title(self, n):
        c = n.c
        if fold(c.name_tr) in fold(n.topic):
            return n.topic
        return '%s – %s' % (c.name_tr, n.topic)

    # ---- static files ------------------------------------------------------------------------
    def static(self):
        a = os.path.join(self.out, 'assets')
        os.makedirs(a, exist_ok=True)
        for f in ('style.css', 'search.js'):
            shutil.copyfile(os.path.join(HERE, 'site_assets', f), os.path.join(a, f))
        fonts = os.path.join(self.repo, 'latex-sablon', 'fonts')
        subprocess.run(['pyftsubset', os.path.join(fonts, 'Caveat-Bold.ttf'),
                        '--unicodes=U+0020-007E,U+00A0-00FF,U+011E-011F,U+0130-0131,U+015E-015F,U+2013-2014,'
                        'U+2018-2019,U+201C-201D,U+2022,U+2026,U+203A,U+2192', '--flavor=woff',
                        '--output-file=' + os.path.join(a, 'caveat.woff')], check=True)
        make_og(os.path.join(self.out, 'og-image.png'), fonts)
        make_icons(self.out)
        open(os.path.join(self.out, '.nojekyll'), 'w').close()
        open(os.path.join(self.out, 'robots.txt'), 'w').write(
            'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % BASE)

    # ---- pages -------------------------------------------------------------------------------
    def home(self):
        R, root = self.R, './'
        n_note_courses = sum(1 for c in R.courses if c.digital)
        title = 'GTÜ Elektronik Mühendisliği Ders Notları ve Çıkmış Sorular | Gebze Teknik Üniversitesi'
        desc = trim('GTÜ Elektronik Mühendisliği ders notları, çıkmış sorular, ödevler, lab raporları ve projeler. '
                    '%d dönem, %d ders, %d dijital (LaTeX) not. Ücretsiz, PDF olarak indirilebilir.' % (
                        len(self.sems), self.ncourses, self.ndig))
        top = sorted([c for c in R.courses if c.digital], key=lambda c: (-len(c.digital), c.sem))[:8]
        examples = ', '.join(c.name_tr for c in top[:6])
        faq = [
            ('GTÜ Elektronik Mühendisliği ders notlarını nereden bulabilirim?',
             'Bu sitede 1. dönemden %d. döneme kadar tüm derslerin sayfaları var. Bir derse tıklayarak ders notlarına, '
             'slaytlara, çıkmış sorulara, ödevlere, laboratuvar föylerine ve projelere ulaşabilirsiniz. Dosyalar '
             '<a href="%s" rel="noopener">GitHub\'daki açık depoda</a> durur ve ücretsizdir.' % (self.sems[-1], GH)),
            ('Çıkmış sorular var mı?',
             'Evet. Birçok dersin vize, final ve quiz soruları ilgili ders sayfasındaki “Çıkmış Sorular” bölümünde '
             'listelenir. Bu materyallerin hakları öğretim üyelerine ve Gebze Teknik Üniversitesi\'ne aittir; '
             'yalnızca eğitim amacıyla paylaşılmıştır.'),
            ('Dijital notlar nedir, güvenilir mi?',
             'Tablette tutulmuş el yazısı notların LaTeX ile yeniden yazılmış, el yazısı görünümlü ve aranabilir PDF '
             'karşılıklarıdır (şu an %d adet). Claude (Anthropic) yardımıyla oluşturuldukları için hata içerebilirler; '
             'her zaman orijinal notlara ve resmi ders kaynaklarına bakın. Her dijital notun yanında orijinal el '
             'yazısı sayfaların bağlantısı vardır.' % self.ndig),
            ('Hangi derslerin dijital notları var?',
             'Örneğin %s ve diğerleri. Tam liste için <a href="dijital-notlar/">dijital notlar</a> sayfasına bakın.'
             % esc(examples)),
            ('Eksik veya hatalı bir şey gördüm, nasıl katkı yapabilirim?',
             'GitHub\'da <a href="%s/issues" rel="noopener">issue açabilir</a> ya da pull request '
             'gönderebilirsiniz. Kendi notlarınızı paylaşmak isterseniz de aynı yoldan ulaşın.' % GH),
        ]
        faq_html = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (esc(q), a) for q, a in faq)
        stats = [('%d' % len(self.sems), 'dönem'), ('%d' % self.ncourses, 'ders'), ('{:,}'.format(self.nfiles).replace(',', '.'), 'dosya'),
                 ('%d' % self.ndig, 'dijital not'), ('%d' % self.nproj, 'proje')]
        body = (
            '<p class="kicker">Gebze Teknik Üniversitesi · Elektronik Mühendisliği</p>'
            '<h1>GTÜ Elektronik Mühendisliği <span class="hl">Ders Notları</span></h1>'
            '<p class="lead">Gebze Teknik Üniversitesi (GTÜ) Elektronik Mühendisliği lisans programının %d dönemine ait '
            '<strong>ders notları, çıkmış sorular, ödevler, laboratuvar raporları ve projeler</strong>. Hepsi ücretsiz; '
            'çoğu el yazısı notun ayrıca LaTeX ile hazırlanmış, aranabilir <strong>dijital</strong> versiyonu da var.</p>'
            % len(self.sems))
        body += self.search_box(root)
        body += '<ul class="chips stats">%s</ul>' % ''.join(
            '<li><strong>%s</strong>%s</li>' % (a, b) for a, b in stats)
        body += '<h2 id="donemler">Dönemler ve dersler</h2><div class="grid">%s</div>' % ''.join(
            self.sem_card(s, root) for s in self.sems)
        body += (
            '<h2>Dijital (LaTeX) notlar</h2><p>El yazısı notların bir kısmı, okunması ve içinde arama yapılması kolay olsun '
            'diye el yazısı görünümlü LaTeX ile yeniden yazıldı; şekiller ve grafikler orijinal çizimlerden alındı. '
            '<a href="dijital-notlar/">%d dijital notun tamamını</a> inceleyebilirsiniz.</p>'
            '<ul class="chips">%s</ul><div class="warn"><strong>Uyarı:</strong> %s</div>' % (
                self.ndig, ''.join('<li><a href="%s%s">%s</a> · %d</li>' % (
                    root, self.course_url(c) + '#dijital-notlar', esc(c.name_tr), len(c.digital)) for c in top),
                esc(mr.DISCLAIMER_TR)))
        body += '<h2>Sık sorulan sorular</h2><div class="faq">%s</div>' % faq_html
        body += (
            '<h2>Katkıda bulunanlar</h2><ul class="people">'
            '<li class="card"><img src="https://github.com/%s.png?size=112" width="56" height="56" alt="" '
            'loading="lazy"><div><a href="https://github.com/%s" rel="noopener"><strong>%s</strong></a> (@%s)<br>'
            '<span class="muted">Notların sahibi, depo yöneticisi</span></div></li>'
            '<li class="card"><div><a href="https://claude.ai" rel="noopener"><strong>Claude (Anthropic)</strong></a><br>'
            '<span class="muted">Dijital notlar, README\'ler ve site altyapısı (ortak yazar)</span></div></li></ul>'
            '<p class="muted">Tüm katkıcılar: <a href="%s/graphs/contributors" rel="noopener">GitHub katkıcı grafiği</a>.</p>'
            % (USER, USER, AUTHOR, USER, GH))
        ld = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'WebSite', '@id': BASE + '/#site', 'name': SITE_TR, 'alternateName': [SITE_EN, 'GTÜ Elektronik Notları'],
             'url': BASE + '/', 'inLanguage': ['tr', 'en'], 'description': desc,
             'author': {'@type': 'Person', 'name': AUTHOR, 'url': 'https://github.com/' + USER}},
        ]}
        alt = [('tr', BASE + '/'), ('en', BASE + '/en/'), ('x-default', BASE + '/')]
        self.write('index.html', self.layout('', title, desc, body, ld=ld, alt=alt), 1.0)
        self.search.append({'t': SITE_TR, 'u': '', 'y': 'Sayfa', 'k': 'ana sayfa gtu gebze teknik universitesi'})

    def en_home(self):
        R, root = self.R, '../'
        title = 'GTU Electronics Engineering Lecture Notes, Past Exams & Projects | Gebze Technical University'
        desc = trim('Free lecture notes, past exams, homework, lab reports and projects for Electronics Engineering at '
                    'Gebze Technical University (GTU): %d semesters, %d courses, %d digital LaTeX notes.' % (
                        len(self.sems), self.ncourses, self.ndig))
        body = (
            '<p class="kicker">Gebze Technical University · Electronics Engineering</p>'
            '<h1>GTU Electronics Engineering <span class="hl">Lecture Notes</span></h1>'
            '<p class="lead">Lecture notes, past exams, homework, lab reports and projects from all %d semesters of the '
            'Electronics Engineering undergraduate programme at <strong>Gebze Technical University (GTU, Turkey)</strong>, '
            'shared for free. Most course pages are in Turkish with English course names and summaries; many handwritten '
            'notes also have searchable <strong>digital (LaTeX) versions</strong>.</p>' % len(self.sems))
        body += self.search_box(root, 'en')
        body += '<h2 id="courses">Semesters and courses</h2>'
        for s in self.sems:
            body += '<h3>Semester %d · %s</h3><ul class="files">' % (s, esc(R.term(s, 'en')))
            for c in R.semesters[s]:
                body += '<li><a href="%s%s">%s</a>%s<span class="meta">%s</span></li>' % (
                    root, self.course_url(c), esc(c.name_en), ' <span class="code">%s</span>' % esc(c.code) if c.code else '',
                    esc(c.desc_en))
            body += '</ul>'
        body += (
            '<h2>Digital notes</h2><p>Parts of the handwritten notes were transcribed into handwriting-style LaTeX '
            '(%d documents) so that they are easier to read and search; hand-drawn figures were copied from the originals.</p>'
            '<div class="warn"><strong>Notice:</strong> %s</div>' % (self.ndig, esc(mr.DISCLAIMER_EN)))
        faq = [
            ('Where can I find GTU Electronics Engineering lecture notes?',
             'Pick a course above. Every course page lists lecture notes, recitation notes, slides, past exams, homework, '
             'lab sheets and projects with direct links to the files in the <a href="%s" rel="noopener">GitHub repository</a>.' % GH),
            ('Are there past exams?',
             'Yes, many courses include past midterms, finals and quizzes. They belong to the instructors and GTU and are '
             'shared for educational purposes only.'),
            ('Can I contribute?',
             'Yes: open an <a href="%s/issues" rel="noopener">issue</a> or a pull request on GitHub.' % GH),
        ]
        body += '<h2>FAQ</h2><div class="faq">%s</div>' % ''.join(
            '<details><summary>%s</summary><p>%s</p></details>' % (esc(q), a) for q, a in faq)
        body += (
            '<h2>Contributors</h2><ul class="people"><li class="card"><img src="https://github.com/%s.png?size=112" '
            'width="56" height="56" alt="" loading="lazy"><div><a href="https://github.com/%s" rel="noopener">'
            '<strong>%s</strong></a> (@%s)<br><span class="muted">Owner of the notes, repository maintainer</span></div></li>'
            '<li class="card"><div><a href="https://claude.ai" rel="noopener"><strong>Claude (Anthropic)</strong></a><br>'
            '<span class="muted">Digital notes, READMEs and site tooling (co-author)</span></div></li></ul>' % (
                USER, USER, AUTHOR, USER))
        ld = {'@context': 'https://schema.org', '@type': 'WebSite', 'name': SITE_EN, 'url': BASE + '/en/',
              'inLanguage': 'en', 'description': desc, 'author': {'@type': 'Person', 'name': AUTHOR,
                                                                  'url': 'https://github.com/' + USER}}
        alt = [('tr', BASE + '/'), ('en', BASE + '/en/'), ('x-default', BASE + '/')]
        self.write('en/index.html', self.layout('en/', title, desc, body, ld=ld, lang='en', alt=alt, active='en'), 0.8)

    def semester(self, sem):
        R = self.R
        root = '../../'
        cs = R.semesters[sem]
        term = R.term(sem, 'tr')
        title = 'GTÜ Elektronik Mühendisliği %d. Dönem Dersleri ve Notları' % sem
        desc = trim('GTÜ Elektronik Mühendisliği %d. dönem (%s) dersleri: %s. Ders notları, çıkmış sorular, ödevler, '
                    'lab ve projeler.' % (sem, term, ', '.join(c.name_tr for c in cs)))
        i = self.sems.index(sem)
        body = self.crumbs(root, [('Ana sayfa', root), (mr.sem_label(sem), None)])
        body += '<h1>%d. Dönem <span class="hl">Dersleri</span></h1>' % sem
        body += '<p class="sub-en" lang="en">Semester %d · %s — Gebze Technical University, Electronics Engineering</p>' % (
            sem, esc(R.term(sem, 'en')))
        body += ('<p class="lead">GTÜ Elektronik Mühendisliği %d. dönem (%s) dersleri: <strong>%d ders</strong>. '
                 'Bir derse tıklayınca o dersin ders notları, çıkmış soruları, ödevleri ve projeleri listelenir.</p>' % (
                     sem, esc(term), len(cs)))
        body += '<div class="notes">'
        for c in cs:
            ct = mr.counts_text(c)
            body += ('<article class="card" style="padding:14px 18px"><h3 style="margin:0"><a href="%s%s">%s</a>%s</h3>'
                     '<p class="muted" style="margin:.2em 0">%s</p><p class="meta" style="margin:0">%s</p></article>' % (
                         root, self.course_url(c), esc(c.name_tr),
                         ' <span class="code">%s</span>' % esc(c.code) if c.code else '', esc(c.desc_tr),
                         esc(ct if ct != '—' else '')))
        body += '</div><p class="pager">'
        if i > 0:
            body += '<a href="%sdonem/%d/">← %s</a>' % (root, self.sems[i - 1], mr.sem_label(self.sems[i - 1]))
        else:
            body += '<span></span>'
        if i + 1 < len(self.sems):
            body += '<a href="%sdonem/%d/">%s →</a>' % (root, self.sems[i + 1], mr.sem_label(self.sems[i + 1]))
        body += '</p>'
        url = 'donem/%d/' % sem
        ld = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'CollectionPage', 'name': title, 'description': desc, 'url': BASE + '/' + url, 'inLanguage': 'tr'},
            breadcrumb_ld([('Ana sayfa', BASE + '/'), (mr.sem_label(sem), BASE + '/' + url)])]}
        self.write(url + 'index.html', self.layout(url, title, desc, body, ld=ld), 0.7)
        self.search.append({'t': '%s · %s' % (mr.sem_label(sem), term), 'u': url, 'y': 'Dönem',
                            'k': ' '.join(c.name_tr + ' ' + c.name_en for c in cs)})

    # ---- course page -------------------------------------------------------------------------
    def vocab_build(self):
        words = {}
        texts = []
        for c in self.R.courses:
            texts += [c.name_tr, c.desc_tr]
            for n in self.notes.get(c.key, []):
                texts += [n.topic] + n.heads
        for t in texts:
            for w in re.findall(r'[A-Za-zÇĞİıÖŞÜçğöşü]{4,}', t or ''):
                lw = mr.tr_lower(w)
                if lw != fold(lw):
                    words.setdefault(fold(lw), lw)
        words.update(EXTRA_TR)
        self.vocab = words

    def tr_fix(self, text):
        def one(m):
            w = m.group(0)
            if w != fold(w) and not w.isascii():
                return w
            repl = self.vocab.get(fold(w))
            if not repl or len(w) < 4:
                return w
            return (repl[:1].replace('i', 'İ').upper() + repl[1:]) if w[:1].isupper() else repl
        return re.sub(r'[A-Za-zÇĞİıÖŞÜçğöşü]+', one, text)

    def label(self, f, base=''):
        sub = f.rel[len(base) + 1:] if base and f.rel.startswith(base + '/') else f.rel
        if f.kind == 'doc':
            parts = sub.split('/')
            return self.tr_fix(' / '.join([mr.folder_label(p) for p in parts[:-1]] + [mr.pretty(f.stem)]))
        return sub

    def file_li(self, f, base, dmap, root):
        info = ', '.join(x for x in (mr.type_label(f.ext), mr.file_info(f)) if x)
        s = '<a href="%s" rel="noopener">%s</a><span class="meta">%s</span>' % (
            esc(blob(f.repo_rel)), esc(self.label(f, base)), esc(info))
        if dmap and f.rel in dmap:
            for i, d in enumerate(dmap[f.rel]):
                n = self.note_of.get(id(d))
                if n:
                    s += '<a class="pill" href="%s%s">%s</a>' % (
                        root, n.url, 'Dijital sürüm' if len(dmap[f.rel]) == 1 else 'Dijital %d' % (i + 1))
        return '<li>%s</li>' % s

    def gallery(self, imgs):
        return '%d görsel: %s' % (len(imgs), ' · '.join(
            '<a href="%s" rel="noopener">%d</a>' % (esc(blob(f.repo_rel)), i + 1) for i, f in enumerate(imgs)))

    def files_html(self, c, files, dmap, root, base=''):
        loose, groups = c.split_section(files)
        out = []
        if loose:
            tops = {f.top for f in loose}
            if not base and len(tops) == 1 and '' not in tops:
                base = next(iter(tops))
            normal, gal = mr.split_gallery(loose)
            normal.sort(key=lambda f: (f.kind != 'doc', mr.natkey(f.name), f.rel))
            items = [self.file_li(f, base, dmap, root) for f in normal]
            items += ['<li>%s</li>' % self.gallery(gal[g]) for g in sorted(gal, key=mr.natkey)]
            out.append('<ul class="files">%s</ul>' % ''.join(items))
        if groups:
            items = []
            for g in sorted(groups, key=lambda g: (mr.natkey(g.rsplit('/', 1)[-1]), g)):
                fl = groups[g]
                normal, gal = mr.split_gallery(fl)
                docs = sorted([f for f in normal if f.kind == 'doc'], key=lambda f: mr.natkey(f.rel))
                inner = [self.file_li(f, g, None, root) for f in docs[:14]]
                for d in sorted(gal, key=mr.natkey):
                    inner.append('<li>%s</li>' % self.gallery(gal[d]))
                other = len(fl) - len([f for f in docs[:14]]) - sum(len(v) for v in gal.values())
                if other > 0:
                    inner.append('<li class="meta"><a href="%s" rel="noopener">+ %d dosya daha (GitHub)</a></li>' % (
                        esc(tree(c.key + '/' + g)), other))
                items.append('<li><a href="%s" rel="noopener"><strong>%s</strong></a><span class="meta">%d dosya</span>'
                             '<ul>%s</ul></li>' % (esc(tree(c.key + '/' + g)),
                                                  esc(mr.folder_label(g.rsplit('/', 1)[-1])), len(fl), ''.join(inner)))
            out.append('<ul class="files">%s</ul>' % ''.join(items))
        return ''.join(out)

    def digital_html(self, c, root):
        notes = self.notes.get(c.key, [])
        h = ['<p>El yazısı notların LaTeX ile yazılmış, aranabilir dijital versiyonları. Şablon ve derleme: '
             '<a href="%s/tree/main/latex-sablon" rel="noopener">latex-sablon</a>.</p>' % GH,
             '<div class="warn"><strong>Uyarı:</strong> %s</div><div class="notes">' % esc(mr.DISCLAIMER_TR)]
        for n in notes:
            d = n.d
            heads = ' · '.join(n.heads[:6])
            links = ['<a href="%s%s">PDF</a>' % (root, n.pdf_url)]
            if d.tex:
                links.append('<a href="%s" rel="noopener">LaTeX kaynağı</a>' % esc(blob(d.tex.repo_rel)))
            if d.source:
                links.append('<a href="%s" rel="noopener">Orijinal el yazısı</a>' % esc(blob(d.source.repo_rel)))
            h.append(
                '<article class="note"><a class="thumb" href="%s%s"><img src="%s%s" width="%d" height="%d" loading="lazy" '
                'alt="%s – dijital ders notunun ilk sayfası"></a><div><h3><a href="%s%s">%s</a></h3>'
                '<p class="meta" style="margin-left:0">%s%s</p>%s<p>%s</p></div></article>' % (
                    root, n.url, root, n.img_url, n.wh[0], n.wh[1], esc(n.topic), root, n.url, esc(n.topic),
                    ('%d sayfa · ' % n.pages) if n.pages else '', human(n.size),
                    '<p class="outline">%s</p>' % esc(heads) if heads else '', ' · '.join(links)))
        h.append('</div>')
        return ''.join(h)

    def projects_html(self, c, root):
        h = []
        for u in c.projects:
            meta = []
            if u.title_en and u.title_en != u.title_tr:
                meta.append('<em>%s</em>' % esc(u.title_en))
            if u.path:
                meta.append('Klasör: <a href="%s" rel="noopener">%s/</a>' % (esc(tree(c.key + '/' + u.path)), esc(u.path)))
            for r in u.repos:
                meta.append('GitHub: <a href="%s" rel="noopener">%s</a>' % (esc(mr.repo_url(r)), esc(r['name'])))
            h.append('<article class="proj"><h3>%s</h3><p class="meta" style="margin-left:0">%s</p>' % (
                esc(u.title_tr), ' · '.join(meta)))
            if u.files:
                base = u.path or ''
                loose, groups = [], {}
                for f in u.files:
                    sub = f.rel[len(base) + 1:] if base and f.rel.startswith(base + '/') else f.rel
                    if '/' in sub:
                        groups.setdefault((base + '/' if base else '') + sub.split('/', 1)[0], []).append(f)
                    else:
                        loose.append(f)
                docs = sorted([f for f in loose if f.kind == 'doc'], key=lambda f: mr.natkey(f.name))
                li = [self.file_li(f, base, None, root) for f in docs]
                for g in sorted(groups, key=mr.natkey):
                    li.append('<li><a href="%s" rel="noopener"><strong>%s</strong></a><span class="meta">%d dosya</span></li>' % (
                        esc(tree(c.key + '/' + g)), esc(mr.folder_label(g.rsplit('/', 1)[-1])), len(groups[g])))
                rest = len(loose) - len(docs)
                if rest > 0:
                    li.append('<li class="meta"><a href="%s" rel="noopener">+ %d dosya daha (GitHub)</a></li>' % (
                        esc(tree(c.key + '/' + base) if base else tree(c.key)), rest))
                h.append('<ul class="files">%s</ul>' % ''.join(li))
            elif u.repos and u.repos[0].get('description_tr'):
                h.append('<p>%s</p>' % esc(u.repos[0]['description_tr']))
            h.append('</article>')
        return ''.join(h)

    def course(self, c):
        R, root = self.R, '../../'
        url = self.course_url(c)
        has_notes = bool(c.digital) or any(c.sections.get(k) for k in mr.NOTE_CATS)
        word = 'Ders Notları' if has_notes else 'Ders Materyalleri'
        extra = ('Çıkmış Sorular' if c.sections.get('cikmis-sorular') else
                 'Ödevler' if c.sections.get('odevler') else 'Lab' if c.sections.get('laboratuvar') else
                 'Proje' if c.projects else '')
        code_s = ' (%s)' % c.code if c.code else ''
        title = '%s%s %s%s | GTÜ Elektronik' % (c.name_tr, code_s, word, ', ' + extra if extra else '')
        tr_cats = [t for t, ok in (('ders notları', has_notes), ('çıkmış sorular', c.sections.get('cikmis-sorular')),
                                    ('ödevler', c.sections.get('odevler')), ('lab', c.sections.get('laboratuvar')),
                                    ('projeler', c.projects), ('slaytlar', c.sections.get('slaytlar'))) if ok]
        en_cats = [t for t, ok in (('lecture notes', has_notes), ('past exams', c.sections.get('cikmis-sorular')),
                                    ('homework', c.sections.get('odevler')), ('lab reports', c.sections.get('laboratuvar')),
                                    ('projects', c.projects), ('slides', c.sections.get('slaytlar'))) if ok]
        desc = trim('GTÜ Elektronik Mühendisliği %d. dönem %s%s dersi: %s. %s' % (
            c.sem, c.name_tr, code_s, ', '.join(tr_cats[:5]) or 'ders materyalleri', c.desc_tr))
        present = []
        for k in ORDER:
            if k == 'dijital-notlar':
                ok = bool(self.notes.get(c.key))
            elif k == 'projeler':
                ok = bool(c.projects)
            else:
                ok = bool(c.sections.get(k))
            if ok:
                present.append(k)
        extra_h = []
        if c.meta.get('repos'):
            extra_h.append(('github', 'GitHub Depoları'))
        if c.meta.get('textbooks'):
            extra_h.append(('kitaplar', 'Kaynak Kitaplar'))
        body = self.crumbs(root, [('Ana sayfa', root), (mr.sem_label(c.sem), root + 'donem/%d/' % c.sem), (c.name_tr, None)])
        body += '<h1>%s%s <span class="hl">%s</span></h1>' % (
            esc(c.name_tr), (' <small class="code" style="font-size:1.1rem">%s</small>' % esc(c.code)) if c.code else '', word)
        body += '<p class="sub-en" lang="en">%s — %s at Gebze Technical University (GTU) Electronics Engineering</p>' % (
            esc(c.name_en), esc(join_en(en_cats) or 'course materials'))
        if c.desc_tr:
            body += '<p class="lead">%s</p>' % esc(c.desc_tr)
        if c.desc_en:
            body += '<p class="lead-en" lang="en">%s</p>' % esc(c.desc_en)
        ct = mr.counts_text(c)
        chips = ['<li>%s · %s</li>' % (mr.sem_label(c.sem), esc(R.term(c.sem, 'tr')))]
        if ct != '—':
            chips += ['<li>%s</li>' % esc(x) for x in ct.split(' · ')]
        body += '<ul class="chips">%s</ul>' % ''.join(chips)
        toc = [(k, mr.CAT[k]['tr']) for k in present] + extra_h
        if len(toc) > 1:
            body += '<p class="toc"><strong>Bu sayfada:</strong> %s</p>' % ' '.join(
                '<a href="#%s">%s</a>' % (k, esc(h)) for k, h in toc)
        dmap = c.digital_by_source()
        for k in present:
            if k == 'dijital-notlar':
                inner = self.digital_html(c, root)
            elif k == 'projeler':
                inner = self.projects_html(c, root)
            else:
                inner = self.files_html(c, c.sections[k], dmap if k in mr.NOTE_CATS else None, root)
            body += '<section id="%s"><h2>%s</h2>%s</section>' % (k, esc(mr.CAT[k]['tr']), inner)
        repos = c.meta.get('repos') or []
        if repos:
            body += '<section id="github"><h2>GitHub Depoları</h2><ul class="files">%s</ul></section>' % ''.join(
                '<li><a href="%s" rel="noopener">%s</a><span class="meta">%s</span></li>' % (
                    esc(mr.repo_url(r)), esc(r['name']), esc(r.get('description_tr') or '')) for r in repos)
        books = c.meta.get('textbooks') or []
        if books:
            li = []
            for b in books:
                s = (esc(b['authors']) + ' — ') if b.get('authors') else ''
                s += '<em>%s</em>' % esc(b['title'])
                if b.get('details'):
                    s += ', ' + esc(b['details'])
                li.append('<li>%s</li>' % s)
            body += ('<section id="kitaplar"><h2>Kaynak Kitaplar</h2><p class="muted">Derste kullanılan kaynaklar '
                     '(kitapların kendisi telif hakları nedeniyle yayımlanmaz):</p><ul class="files">%s</ul></section>' %
                     ''.join(li))
        others = [x for x in R.semesters[c.sem] if x is not c]
        if others:
            body += '<h2>Aynı dönemin diğer dersleri</h2><p>%s</p>' % ' · '.join(
                '<a href="%s%s">%s</a>' % (root, self.course_url(x), esc(x.name_tr)) for x in others)
        body += ('<p><a class="btn alt" href="%s" rel="noopener">GitHub\'da klasörü aç</a>'
                 '<a class="btn alt" href="%sdonem/%d/">← %s</a></p>' % (
                     esc(tree(c.key)), root, c.sem, mr.sem_label(c.sem)))
        body += '<p class="muted"><small>Ders materyallerinin hakları ilgili öğretim üyelerine ve GTÜ\'ye aittir; eğitim amacıyla paylaşılmıştır.</small></p>'
        ld = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'CollectionPage', 'name': title, 'description': desc, 'url': BASE + '/' + url, 'inLanguage': 'tr',
             'author': {'@type': 'Person', 'name': AUTHOR, 'url': 'https://github.com/' + USER},
             'about': {'@type': 'Course', 'name': c.name_tr, 'alternateName': c.name_en,
                       **({'courseCode': c.code} if c.code else {}),
                       'provider': {'@type': 'CollegeOrUniversity', 'name': 'Gebze Teknik Üniversitesi',
                                    'alternateName': 'Gebze Technical University', 'url': 'https://www.gtu.edu.tr/'}}},
            breadcrumb_ld([('Ana sayfa', BASE + '/'), (mr.sem_label(c.sem), BASE + '/donem/%d/' % c.sem),
                           (c.name_tr, BASE + '/' + url)])]}
        self.write(url + 'index.html', self.layout(url, title, desc, body, ld=ld), 0.9)
        kw = ' '.join([c.name_en, c.code or '', ' '.join(c.meta.get('aka') or []), c.desc_tr, c.desc_en,
                       ' '.join(h for n in self.notes.get(c.key, []) for h in n.heads[:4])])
        self.search.append({'t': c.name_tr + code_s, 'u': url, 'y': 'Ders', 'k': trim(kw, 600)})

    def note_page(self, c, i):
        R, root = self.R, '../../../'
        notes = self.notes[c.key]
        n = notes[i]
        d = n.d
        nt = self.note_title(n)
        title = '%s | Ders Notu · GTÜ Elektronik' % nt
        hs = ', '.join(n.heads[:7])
        desc = trim('%s: %s%s dersi dijital ders notu (LaTeX, %s). GTÜ Elektronik Mühendisliği %d. dönem.' % (
            n.topic, c.name_tr, ' (%s)' % c.code if c.code else '', ('%d sayfa PDF' % n.pages) if n.pages else 'PDF', c.sem)
            + (' İçerik: %s.' % hs if hs else ''))
        crumbs = self.crumbs(root, [('Ana sayfa', root), (mr.sem_label(c.sem), root + 'donem/%d/' % c.sem),
                                    (c.name_tr, root + self.course_url(c)), (n.topic, None)])
        facts = ['<dt>Ders</dt><dd><a href="%s%s">%s</a>%s</dd>' % (
            root, self.course_url(c), esc(c.name_tr), ' (%s)' % esc(c.code) if c.code else ''),
            '<dt>Dönem</dt><dd>%s · %s</dd>' % (mr.sem_label(c.sem), esc(R.term(c.sem, 'tr'))),
            '<dt>Biçim</dt><dd>PDF%s · %s · el yazısı görünümlü LaTeX</dd>' % (
                (' · %d sayfa' % n.pages) if n.pages else '', human(n.size))]
        if d.source:
            facts.append('<dt>Orijinal not</dt><dd><a href="%s" rel="noopener">%s</a></dd>' % (
                esc(blob(d.source.repo_rel)), esc(d.source.name)))
        btn = '<a class="btn" href="%s%s">PDF\'i aç (%s)</a>' % (root, n.pdf_url, human(n.size))
        if d.tex:
            btn += '<a class="btn alt" href="%s" rel="noopener">LaTeX kaynağı (.tex)</a>' % esc(blob(d.tex.repo_rel))
        if d.source:
            btn += '<a class="btn alt" href="%s" rel="noopener">Orijinal el yazısı not</a>' % esc(blob(d.source.repo_rel))
        body = crumbs + '<p class="kicker" style="margin-top:22px">%s · Dijital ders notu</p>' % esc(c.name_tr)
        body += '<h1>%s</h1>' % esc(n.topic)
        body += ('<div class="hero-note"><div><dl class="facts">%s</dl><p>%s</p></div>'
                 '<a href="%s%s"><img src="%s%s" width="%d" height="%d" alt="%s – dijital ders notunun ilk sayfası"></a></div>' % (
                     ''.join(facts), btn, root, n.pdf_url, root, n.img_url, n.wh[0], n.wh[1], esc(n.topic)))
        body += '<div class="warn"><strong>Uyarı:</strong> %s<br><span lang="en">%s</span></div>' % (
            esc(mr.DISCLAIMER_TR), esc(mr.DISCLAIMER_EN))
        if n.heads:
            body += '<h2>Bu notta neler var?</h2><ul class="outline-list">%s</ul>' % ''.join(
                '<li>%s</li>' % esc(h) for h in n.heads[:60])
        if n.prose:
            body += ('<h2>Notun metni</h2><details><summary>Düz metin olarak göster (formüller ve çizimler yoktur)</summary>'
                     '<div class="prose">%s</div></details>' % ''.join('<p>%s</p>' % esc(p) for p in n.prose))
        body += '<div class="pager">'
        body += ('<a href="%s%s">← %s</a>' % (root, notes[i - 1].url, esc(notes[i - 1].topic))) if i > 0 else '<span></span>'
        if i + 1 < len(notes):
            body += '<a href="%s%s">%s →</a>' % (root, notes[i + 1].url, esc(notes[i + 1].topic))
        body += '</div>'
        body += '<p><a class="btn alt" href="%s%s#dijital-notlar">← Tüm %s dijital notları</a></p>' % (
            root, self.course_url(c), esc(c.name_tr))
        ld = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'LearningResource', 'name': nt, 'description': desc, 'url': BASE + '/' + n.url,
             'inLanguage': 'tr', 'learningResourceType': 'Lecture notes', 'educationalLevel': 'University',
             'isPartOf': {'@type': 'CollectionPage', 'url': BASE + '/' + self.course_url(c), 'name': c.name_tr},
             'about': {'@type': 'Course', 'name': c.name_tr, **({'courseCode': c.code} if c.code else {})},
             'author': [{'@type': 'Person', 'name': AUTHOR, 'url': 'https://github.com/' + USER}],
             'encoding': {'@type': 'MediaObject', 'encodingFormat': 'application/pdf',
                          'contentUrl': BASE + '/' + n.pdf_url},
             'thumbnailUrl': BASE + '/' + n.img_url},
            breadcrumb_ld([('Ana sayfa', BASE + '/'), (mr.sem_label(c.sem), BASE + '/donem/%d/' % c.sem),
                           (c.name_tr, BASE + '/' + self.course_url(c)), (n.topic, BASE + '/' + n.url)])]}
        self.write(n.url + 'index.html', self.layout(n.url, title, desc, body, ld=ld, og_type='article'), 0.6)
        self.urls.append((n.pdf_url, 0.5))
        self.search.append({'t': nt, 'u': n.url, 'y': 'Dijital not', 'c': c.name_tr,
                            'k': trim(' '.join(n.heads), 500)})

    def digital_hub(self):
        root = '../'
        title = 'Dijital Ders Notları (LaTeX, PDF) | GTÜ Elektronik Mühendisliği'
        desc = trim('GTÜ Elektronik Mühendisliği için el yazısı görünümlü %d dijital ders notu (LaTeX/PDF): %s ve diğer '
                    'dersler.' % (self.ndig, ', '.join(c.name_tr for c in self.R.courses if c.digital)[:80]))
        body = self.crumbs(root, [('Ana sayfa', root), ('Dijital notlar', None)])
        body += '<h1>Dijital Ders <span class="hl">Notları</span></h1>'
        body += ('<p class="lead">Tablette tutulmuş el yazısı ders notlarının LaTeX ile yazılmış, el yazısı görünümlü ve '
                 'aranabilir PDF versiyonları. Toplam <strong>%d not</strong>, %d derste. Şekil ve grafikler orijinal '
                 'çizimlerden alınmıştır.</p><div class="warn"><strong>Uyarı:</strong> %s</div>' % (
                     self.ndig, sum(1 for c in self.R.courses if c.digital), esc(mr.DISCLAIMER_TR)))
        body += self.search_box(root)
        for s in self.sems:
            cs = [c for c in self.R.semesters[s] if self.notes.get(c.key)]
            if not cs:
                continue
            body += '<h2>%s · %s</h2>' % (mr.sem_label(s), esc(self.R.term(s, 'tr')))
            for c in cs:
                body += '<h3><a href="%s%s">%s</a> <span class="meta">%d not</span></h3><ul class="files">%s</ul>' % (
                    root, self.course_url(c), esc(c.name_tr), len(self.notes[c.key]), ''.join(
                        '<li><a href="%s%s">%s</a><span class="meta">%s</span></li>' % (
                            root, n.url, esc(n.topic), ('%d s.' % n.pages) if n.pages else '')
                        for n in self.notes[c.key]))
        url = 'dijital-notlar/'
        ld = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'CollectionPage', 'name': title, 'description': desc, 'url': BASE + '/' + url, 'inLanguage': 'tr'},
            breadcrumb_ld([('Ana sayfa', BASE + '/'), ('Dijital notlar', BASE + '/' + url)])]}
        self.write(url + 'index.html', self.layout(url, title, desc, body, ld=ld, active='dijital'), 0.8)
        self.search.append({'t': 'Dijital ders notları', 'u': url, 'y': 'Sayfa', 'k': 'latex pdf dijital el yazisi'})

    def projects_hub(self):
        root = '../'
        rows = mr.all_projects(self.R)
        title = 'Projeler ve Kodlar | GTÜ Elektronik Mühendisliği'
        desc = trim('GTÜ Elektronik Mühendisliği ders projeleri ve kod depoları: %s.' % ', '.join(
            u.title_tr for _, u in rows[:6]))
        body = self.crumbs(root, [('Ana sayfa', root), ('Projeler', None)])
        body += '<h1><span class="hl">Projeler</span> ve kodlar</h1>'
        body += '<p class="lead">GTÜ Elektronik Mühendisliği derslerinde hazırlanan dönem projeleri, raporlar, simülasyonlar ve kod depoları.</p>'
        last = None
        for c, u in rows:
            if c is not last:
                body += '<h2><a href="%s%s#projeler">%s</a></h2>' % (root, self.course_url(c), esc(c.name_tr))
                last = c
            meta = []
            if u.title_en and u.title_en != u.title_tr:
                meta.append('<em>%s</em>' % esc(u.title_en))
            if u.path:
                meta.append('<a href="%s" rel="noopener">Klasör: %s/</a>' % (esc(tree(c.key + '/' + u.path)), esc(u.path)))
            for r in u.repos:
                meta.append('<a href="%s" rel="noopener">GitHub: %s</a>' % (esc(mr.repo_url(r)), esc(r['name'])))
            body += '<article class="proj"><h3>%s</h3><p class="meta" style="margin-left:0">%s</p></article>' % (
                esc(u.title_tr), ' · '.join(meta))
        codes = mr.code_repos(self.R)
        if codes:
            body += '<h2>Diğer kod depoları</h2><ul class="files">'
            for r, cs in codes:
                body += '<li><a href="%s" rel="noopener">%s</a><span class="meta">%s — %s</span></li>' % (
                    esc(mr.repo_url(r)), esc(r['name']), esc(r.get('description_tr') or ''),
                    ', '.join(esc(c.name_tr) for c in cs))
            body += '</ul>'
        url = 'projeler/'
        ld = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'CollectionPage', 'name': title, 'description': desc, 'url': BASE + '/' + url, 'inLanguage': 'tr'},
            breadcrumb_ld([('Ana sayfa', BASE + '/'), ('Projeler', BASE + '/' + url)])]}
        self.write(url + 'index.html', self.layout(url, title, desc, body, ld=ld, active='projeler'), 0.7)
        self.search.append({'t': 'Projeler ve kodlar', 'u': url, 'y': 'Sayfa',
                            'k': ' '.join(u.title_tr for _, u in rows)})

    def not_found(self):
        body = ('<h1>Sayfa bulunamadı</h1><p class="lead">Aradığınız sayfa taşınmış ya da silinmiş olabilir. '
                '<a href="%s/">Ana sayfaya</a> dönüp dersleri arayabilirsiniz.</p>' % BASE)
        self.write('404.html', self.layout('404.html', 'Sayfa bulunamadı | ' + SITE_TR, 'Sayfa bulunamadı.', body,
                                           root=BASE + '/', noindex=True))

    def finish(self):
        self.write('search-index.json', json.dumps(self.search, ensure_ascii=False, separators=(',', ':')))
        lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for u, p in self.urls:
            lines.append('<url><loc>%s</loc><lastmod>%s</lastmod><priority>%.1f</priority></url>' % (
                esc(BASE + '/' + u), self.today, p))
        lines.append('</urlset>')
        self.write('sitemap.xml', '\n'.join(lines) + '\n')

    def build(self):
        self.static()
        self.prepare_notes()
        self.vocab_build()
        self.note_of = {id(n.d): n for ns in self.notes.values() for n in ns}
        self.home()
        self.en_home()
        for s in self.sems:
            self.semester(s)
        for c in self.R.courses:
            self.course(c)
            for i in range(len(self.notes.get(c.key, []))):
                self.note_page(c, i)
        self.digital_hub()
        self.projects_hub()
        self.not_found()
        self.finish()


def main(argv=None):
    ap = argparse.ArgumentParser(description='GitHub Pages sitesini üretir.')
    here_parent = os.path.normpath(os.path.join(HERE, '..'))
    in_repo = os.path.basename(HERE) == 'araclar'
    ap.add_argument('--repo', default=here_parent if in_repo else '/home/claude/repo')
    ap.add_argument('--courses', default=os.path.join(HERE, 'courses.json') if os.path.exists(
        os.path.join(HERE, 'courses.json')) else os.path.join(here_parent, 'courses.json'))
    ap.add_argument('--out', default='/tmp/gtu-site')
    ap.add_argument('--cache', default=os.path.join(HERE, '.make_readmes_cache.json'))
    ap.add_argument('--thumb-cache', default=os.path.join(HERE, '.thumb_cache'))
    ap.add_argument('--date', default=datetime.date.today().isoformat())
    a = ap.parse_args(argv)
    repo = os.path.abspath(a.repo)
    meta = json.load(open(a.courses, encoding='utf-8'))
    pages = mr.PageCounter(a.cache, enabled=True)
    R = mr.Repo(repo, meta, pages)
    R.scan()
    pages.save()
    out = os.path.abspath(a.out)
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    site = Site(R, repo, out, os.path.abspath(a.thumb_cache), a.date)
    site.build()
    for w in mr.WARNINGS:
        print('WARNING: ' + w)
    print('site: %d pages, %d digital notes, %d search entries -> %s' % (
        len([u for u, _ in site.urls if not u.endswith('.pdf')]), site.ndig, len(site.search), out))
    return 0


if __name__ == '__main__':
    sys.exit(main())
