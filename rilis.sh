#!/usr/bin/env bash
# Naikkan versi plugin dan rilis.
#
# Pakai:  ./rilis.sh 0.2.0 "Tambah arsitektur untuk produk langganan"
#
# Versi HARUS naik tiap rilis. Kalau nomornya tidak berubah, Claude Code
# tidak akan menganggapnya update dan tidak ada yang menerima revisimu.

set -euo pipefail

VERSI="${1:-}"
PESAN="${2:-}"

if [[ -z "$VERSI" ]]; then
  echo "Pakai: ./rilis.sh <versi> \"<catatan perubahan>\""
  echo "Contoh: ./rilis.sh 0.2.0 \"Tambah arsitektur untuk produk langganan\""
  exit 1
fi

if [[ ! "$VERSI" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Versi harus format X.Y.Z, contoh 0.2.0"
  exit 1
fi

AKAR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MP="$AKAR/.claude-plugin/marketplace.json"
PJ="$AKAR/plugins/funnel-jualan/.claude-plugin/plugin.json"

LAMA=$(python3 -c "import json;print(json.load(open('$PJ'))['version'])")

if [[ "$LAMA" == "$VERSI" ]]; then
  echo "Versi $VERSI sama dengan yang sekarang. Naikkan nomornya."
  exit 1
fi

python3 - "$MP" "$PJ" "$VERSI" <<'PY'
import json, sys
mp, pj, v = sys.argv[1], sys.argv[2], sys.argv[3]

d = json.load(open(pj))
d["version"] = v
json.dump(d, open(pj, "w"), indent=2, ensure_ascii=False)
open(pj, "a").write("\n")

d = json.load(open(mp))
for p in d["plugins"]:
    if p["name"] == "funnel-jualan":
        p["version"] = v
json.dump(d, open(mp, "w"), indent=2, ensure_ascii=False)
open(mp, "a").write("\n")
PY

# catat di changelog
CL="$AKAR/CHANGELOG.md"
TGL=$(date +%Y-%m-%d)
if [[ -f "$CL" ]]; then
  python3 - "$CL" "$VERSI" "$TGL" "$PESAN" <<'PY'
import sys
cl, v, tgl, pesan = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
isi = open(cl).read()
baru = f"## {v} — {tgl}\n\n- {pesan or 'Perbaikan kecil.'}\n\n"
tanda = "<!-- rilis-baru-di-sini -->\n"
isi = isi.replace(tanda, tanda + "\n" + baru, 1)
open(cl, "w").write(isi)
PY
fi

echo "Versi: $LAMA → $VERSI"
echo
echo "Langkah berikutnya:"
echo "  git add -A"
echo "  git commit -m \"v$VERSI: ${PESAN:-perbaikan}\""
echo "  git push"
echo
echo "Setelah di-push, orang yang sudah menyalakan auto-update akan menerimanya"
echo "otomatis. Yang belum, tinggal jalankan:  /plugin update funnel-jualan@tukang-lp"
