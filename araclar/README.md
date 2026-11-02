# araclar/ — README ve web sitesi üreteçleri

Bu klasördeki betikler, deponun **README sayfalarını** ve **GitHub Pages web sitesini** (https://fouad1233.github.io/GTU_Elektronik_Notlar/) dosya yapısından otomatik üretir. Dosya ekleyip çıkardıktan sonra yeniden çalıştırmanız yeterlidir.

| Dosya | Ne yapar |
|---|---|
| `make_readmes.py` | Ana README, dönem ve ders README'lerini ve `latex-sablon/README.md` dosyasını üretir; tüm bağlantıları denetler |
| `build_site.py` | Statik, **iki dilli** web sitesini üretir: Türkçe sayfalar kökte, İngilizce karşılıkları `en/` altında (ana sayfa, dönem/ders/dijital not/proje sayfaları, arama, `sitemap.xml`, `robots.txt`) |
| `check_site.py` | Üretilen sitede bozuk bağlantı, tekrar eden başlık/açıklama, HTML etiket hataları ve Türkçe↔İngilizce sayfa eşleşmesini (hreflang) arar |
| `yayinla.sh` | Siteyi üretir, denetler ve `gh-pages` dalına gönderir |
| `courses.json` | Ders adları (TR/EN), kodları, açıklamaları (TR/EN), GitHub depoları, kaynak kitaplar ve proje başlıkları (TR/EN) |
| `note_titles_en.json` | Dijital notların İngilizce başlıkları (`<ders klasörü>/<pdf adı>` → başlık); yeni dijital not ekleyince buraya da ekleyin, yoksa İngilizce sayfada Türkçe başlık görünür |
| `site_assets/` | Sitenin stil (`style.css`) ve arama (`search.js`) dosyaları |
| `site_root/` | Site köküne olduğu gibi kopyalanan dosyalar (ör. Google Search Console doğrulama dosyası — **silmeyin**, silinirse doğrulama bozulur) |

**Gereksinimler:** Python 3.9+, `poppler-utils` (`pdfinfo`, `pdftoppm`), `Pillow`, `fonttools` (`pyftsubset`), `git`.

```bash
python3 araclar/make_readmes.py                     # README'leri yeniden üret
python3 araclar/build_site.py --out /tmp/gtu-site   # siteyi yerelde üret
python3 araclar/check_site.py /tmp/gtu-site         # siteyi denetle
(cd /tmp/gtu-site && python3 -m http.server 8000)   # http://localhost:8000 adresinde önizle
araclar/yayinla.sh                                  # üret + denetle + gh-pages dalına gönder
```

**Yeni ders / proje eklerken:** önce klasörü `N-Donem/<Ders-Adi>/` altına koyun, sonra `courses.json` içine dersin adını, kodunu ve açıklamasını (Türkçe ve İngilizce) yazın; yeni dijital notların İngilizce başlıklarını `note_titles_en.json` dosyasına ekleyin. Sitede yalnızca **dijital (LaTeX) notların PDF'leri** barındırılır; diğer dosyalar GitHub bağlantılarıyla listelenir.

**Depo adı değişirse** `build_site.py` başındaki `USER` / `REPO` sabitlerini ve `courses.json` içindeki `repo_slug` alanını güncelleyin.

**Arama motorları:** siteyi Google Search Console ve Bing Webmaster Tools'a eklemek taranmayı hızlandırır. Search Console'da mülkü **URL ön eki** olarak `https://fouad1233.github.io/GTU_Elektronik_Notlar/` adresiyle ekleyin (sonuna `sitemap.xml` yazmayın); doğrulama için verilen `google….html` dosyasını `site_root/` klasörüne koyup `yayinla.sh` çalıştırın. Ardından "Site haritaları" bölümüne `sitemap.xml` yazarak gönderin.

---

## English

These scripts generate the repository's **README pages** and the **GitHub Pages website** (https://fouad1233.github.io/GTU_Elektronik_Notlar/) from the folder tree. Re-run them after adding or removing files.

- `make_readmes.py` — writes the main, semester and course READMEs and checks every link.
- `build_site.py` — builds the static **bilingual** website: Turkish pages at the root, an English counterpart of every page under `en/` (home, semester, course, digital-note and project pages, one search index per language, `sitemap.xml`, `robots.txt`); only the PDFs of the digital (LaTeX) notes are hosted on the site (shared by both languages), other files are linked to GitHub.
- `check_site.py` — looks for broken links, duplicate titles/descriptions, unbalanced HTML and Turkish↔English pairing problems (hreflang) in the generated site.
- `note_titles_en.json` — English titles of the digital notes (`<course folder>/<pdf name>` → title); add an entry when you add a digital note, otherwise the English page falls back to the Turkish title.
- `yayinla.sh` — builds, checks and pushes the site to the `gh-pages` branch (served by GitHub Pages).
- `courses.json` — course names (TR/EN), codes, descriptions, GitHub repos, textbooks and project titles. `site_assets/` — CSS and search script.
- `site_root/` — files copied as-is to the site root, e.g. the Google Search Console verification file (do not delete it, or verification breaks).

Requirements: Python 3.9+, `poppler-utils`, `Pillow`, `fonttools`, `git`. Usage is shown in the commands above. If the repository is renamed, update `USER` / `REPO` at the top of `build_site.py` and `repo_slug` in `courses.json`. To speed up indexing, add the site to Google Search Console and Bing Webmaster Tools: use a **URL-prefix** property `https://fouad1233.github.io/GTU_Elektronik_Notlar/` (not the sitemap address), put the verification `google….html` file into `site_root/`, run `yayinla.sh`, then submit `sitemap.xml` under Sitemaps.
