#!/usr/bin/env bash
# Web sitesini üretir, denetler ve `gh-pages` dalına gönderir (GitHub Pages siteyi bu daldan yayınlar).
# Builds + checks the website and pushes it to the `gh-pages` branch (GitHub Pages serves that branch).
#
# Kullanım / usage:   araclar/yayinla.sh ["commit mesajı"]
# Ana dalın çalışma klasörüne dokunmaz; PDF'ler `main` ile aynı git nesneleri olduğu için depo büyümez.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo="$(cd "$here/.." && pwd)"
out="$(mktemp -d)"
idx="$(mktemp -u)"
trap 'rm -rf "$out" "$idx"' EXIT

python3 "$here/build_site.py" --repo "$repo" --out "$out"
python3 "$here/check_site.py" "$out"

msg="${1:-Site güncellemesi $(date +%F)}"
export GIT_DIR="$repo/.git"
git fetch -q origin gh-pages 2>/dev/null || true
parent="$(git rev-parse -q --verify refs/remotes/origin/gh-pages || true)"

cd "$out"
GIT_INDEX_FILE="$idx" GIT_WORK_TREE="$out" git add -A -f .
tree="$(GIT_INDEX_FILE="$idx" git write-tree)"
if [ -n "$parent" ] && [ "$(git rev-parse "$parent^{tree}")" = "$tree" ]; then
  echo "Site zaten güncel (gh-pages ile aynı)."; exit 0
fi
args=()
[ -n "$parent" ] && args=(-p "$parent")
commit="$(printf '%s\n' "$msg" | git commit-tree "$tree" "${args[@]}")"
git push origin "$commit:refs/heads/gh-pages"
echo "gh-pages güncellendi: $commit"
