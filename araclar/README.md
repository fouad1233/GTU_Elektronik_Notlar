# araclar/ — README ve web sitesi üreteçleri

Bu klasördeki betikler, deponun **README sayfalarını** ve **GitHub Pages web sitesini** (https://fouad1233.github.io/GTU_Elektronik_Notlar/) dosya yapısından otomatik üretir. Dosya ekleyip çıkardıktan sonra yeniden çalıştırmanız yeterlidir.

| Dosya | Ne yapar |
|---|---|
| `make_readmes.py` | Ana README, dönem ve ders README'lerini ve `latex-sablon/README.md` dosyasını üretir; tüm bağlantıları denetler |
| `build_site.py` | Statik web sitesini üretir (ana sayfa, dönem/ders/dijital not sayfaları, arama, `sitemap.xml`, `robots.txt`) |
| `check_site.py` | Üretilen sitede bozuk bağlantı, tekrar eden başlık/açıklama ve HTML etiket hatalarını arar |
| `yayinla.sh` | Siteyi üretir, denetler ve `gh-pages` dalına gönderir |
| `courses.json` | Ders adları (TR/EN), kodları, açıklamaları, GitHub depoları, kaynak kitaplar ve proje başlıkları |
| `site_assets/` | Sitenin stil (`style.css`) ve arama (`search.js`) dosyaları |

**Gereksinimler:** Python 3.9+, `poppler-utils` (`pdfinfo`, `pdftoppm`), `Pillow`, `fonttools` (`pyftsubset`), `git`.

```bash
python3 araclar/make_readmes.py                     # README'leri yeniden üret
python3 araclar/build_site.py --out /tmp/gtu-site   # siteyi yerelde üret
python3 araclar/check_site.py /tmp/gtu-site         # siteyi denetle
(cd /tmp/gtu-site && python3 -m http.server 8000)   # http://localhost:8000 adresinde önizle
araclar/yayinla.sh                                  # üret + denetle + gh-pages dalına gönder
```

**Yeni ders / proje eklerken:** önce klasörü `N-Donem/<Ders-Adi>/` altına koyun, sonra `courses.json` içine dersin adını, kodunu ve açıklamasını yazın. Sitede yalnızca **dijital (LaTeX) notların PDF'leri** barındırılır; diğer dosyalar GitHub bağlantılarıyla listelenir.

**Depo adı değişirse** `build_site.py` başındaki `USER` / `REPO` sabitlerini ve `courses.json` içindeki `repo_slug` alanını güncelleyin.

**Arama motorları:** siteyi Google Search Console ve Bing Webmaster Tools'a ekleyip `https://fouad1233.github.io/GTU_Elektronik_Notlar/sitemap.xml` adresini göndermek taranmayı hızlandırır.

---

## English

These scripts generate the repository's **README pages** and the **GitHub Pages website** (https://fouad1233.github.io/GTU_Elektronik_Notlar/) from the folder tree. Re-run them after adding or removing files.

- `make_readmes.py` — writes the main, semester and course READMEs and checks every link.
- `build_site.py` — builds the static website (home, semester, course and digital-note pages, search index, `sitemap.xml`, `robots.txt`); only the PDFs of the digital (LaTeX) notes are hosted on the site, other files are linked to GitHub.
- `check_site.py` — looks for broken links, duplicate titles/descriptions and unbalanced HTML in the generated site.
- `yayinla.sh` — builds, checks and pushes the site to the `gh-pages` branch (served by GitHub Pages).
- `courses.json` — course names (TR/EN), codes, descriptions, GitHub repos, textbooks and project titles. `site_assets/` — CSS and search script.

Requirements: Python 3.9+, `poppler-utils`, `Pillow`, `fonttools`, `git`. Usage is shown in the commands above. If the repository is renamed, update `USER` / `REPO` at the top of `build_site.py` and `repo_slug` in `courses.json`. Submitting the sitemap to Google Search Console and Bing Webmaster Tools speeds up indexing.
