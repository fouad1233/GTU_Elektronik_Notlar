#!/usr/bin/env bash
# derle.sh -- gtu-el-yazisi şablonunu kullanan .tex dosyalarını XeLaTeX ile derler.
#
# Kullanım / usage:
#   latex-sablon/derle.sh yol/dosya.tex [yol/baska.tex ...]
#
# - .tex dosyası depo içinde herhangi bir yerde olabilir; \usepackage{gtu-el-yazisi}
#   yeterlidir (TEXINPUTS ve font yolu bu betik tarafından ayarlanır).
# - XeLaTeX dosyanın kendi klasöründe çalıştırılır (gerekirse 3 kez),
#   PDF .tex dosyasının yanında kalır, yardımcı dosyalar (.aux, .log, ...) silinir.
# - Hata olursa: hata satırları ekrana yazılır, .log dosyası incelemek için bırakılır
#   ve betik sıfır olmayan bir kodla çıkar.

set -u

SABLON="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "$#" -eq 0 ]; then
  echo "Kullanım: $0 dosya.tex [dosya2.tex ...]" >&2
  exit 2
fi

if ! command -v xelatex >/dev/null 2>&1; then
  echo "HATA: xelatex bulunamadı (TeX Live kurulu mu?)" >&2
  exit 2
fi

# Sondaki ':' kpathsea'nın varsayılan arama yollarını da eklemesini sağlar.
export TEXINPUTS="$SABLON:${TEXINPUTS:-}"
export TTFONTS="$SABLON/fonts//:${TTFONTS:-}"
export OPENTYPEFONTS="$SABLON/fonts//:${OPENTYPEFONTS:-}"

GENEL_KOD=0

derle_bir() {
  local girdi="$1"
  if [ ! -f "$girdi" ]; then
    echo "HATA: dosya yok: $girdi" >&2
    return 1
  fi
  case "$girdi" in
    *.tex) ;;
    *) echo "HATA: .tex dosyası değil: $girdi" >&2; return 1 ;;
  esac

  local klasor ad
  klasor="$(cd "$(dirname "$girdi")" && pwd)"
  ad="$(basename "$girdi" .tex)"

  (
    cd "$klasor" || exit 1
    local tur=1 durum=0
    while [ "$tur" -le 3 ]; do
      xelatex -interaction=nonstopmode -halt-on-error -file-line-error \
              "$ad.tex" > /dev/null 2>&1
      durum=$?
      if [ "$durum" -ne 0 ] || grep -q '^!' "$ad.log" 2>/dev/null; then
        echo "HATA: $girdi derlenemedi (tur $tur). İlgili satırlar:" >&2
        grep -n -A3 -E '^!|^[^ ]*:[0-9]+: ' "$ad.log" | head -n 40 >&2
        echo "Ayrıntılar: $klasor/$ad.log" >&2
        rm -f "$ad.aux" "$ad.out" "$ad.toc" "$ad.lof" "$ad.lot" "$ad.xdv"
        exit 1
      fi
      # Tekrar derleme gerekiyor mu? (LastPage, remember picture, etiketler)
      if [ "$tur" -ge 2 ] && ! grep -qE 'Rerun|may have changed|Label\(s\) may' "$ad.log"; then
        break
      fi
      tur=$((tur + 1))
    done

    # Fontta olmayan karakterler (ör. ✓, ∑ metin içinde) için uyarı
    if grep -q 'Missing character' "$ad.log"; then
      echo "UYARI: $girdi -- fontta bulunmayan karakter(ler):" >&2
      grep -A1 'Missing character' "$ad.log" | grep -oE 'There is no .{1,3} \(U\+[0-9A-F]+\)' \
        | sort -u | head -n 10 >&2
    fi
    if grep -q 'Package gtu-el-yazisi Warning' "$ad.log"; then
      grep -A2 'Package gtu-el-yazisi Warning' "$ad.log" >&2
    fi

    rm -f "$ad.aux" "$ad.log" "$ad.out" "$ad.toc" "$ad.lof" "$ad.lot" \
          "$ad.fls" "$ad.xdv" "$ad.synctex.gz" "$ad.bbl" "$ad.blg"
    echo "TAMAM: $klasor/$ad.pdf"
  )
}

for dosya in "$@"; do
  derle_bir "$dosya" || GENEL_KOD=1
done

exit "$GENEL_KOD"
