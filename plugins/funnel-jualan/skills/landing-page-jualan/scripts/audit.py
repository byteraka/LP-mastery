#!/usr/bin/env python3
"""
Audit naskah landing page terhadap aturan bahasa anti-AI.

Pakai:  python3 audit.py halaman.html
        python3 audit.py naskah.md
        cat naskah.txt | python3 audit.py

Keluaran: daftar pelanggaran + skor. Skrip ini tidak menggantikan pembacaan manual;
tugasnya menangkap yang gampang terlewat.
"""
import sys, re, html

TERLARANG = {
    "pembuka hampa": [
        "di era digital", "di zaman serba cepat", "di zaman yang serba cepat",
        "seiring berkembangnya", "tidak dapat dipungkiri", "seperti yang kita ketahui",
        "sudah bukan rahasia", "mari kita", "selamat datang di",
        "pernahkah kamu merasa", "pernahkah anda merasa",
    ],
    "klaim tanpa bukti": [
        "solusi tepat", "solusi terbaik", "one stop solution", "dirancang khusus",
        "kualitas terbaik", "profesional dan terpercaya", "standar industri",
        "sesuai kebutuhan anda", "revolusioner", "inovatif", "terdepan",
        "telah terbukti dan teruji", "tim ahli kami", "berpengalaman bertahun-tahun",
    ],
    "metafora perjalanan": [
        "mulai perjalanan", "langkah pertama menuju", "wujudkan impian",
        "raih kesuksesan", "ubah hidupmu", "buka potensi", "unlock potensi",
        "versi terbaik dirimu", "naik level hidup", "level up hidup",
    ],
    "penutup hampa": [
        "tunggu apa lagi", "jangan sampai ketinggalan", "segera daftarkan dirimu",
        "siap untuk memulai", "kesempatan emas", "ayo bergabung sekarang juga",
    ],
    "pengisi kosong": [
        "tentunya", "pastinya", "tentu saja", "pada dasarnya", "dalam hal ini",
        "hal ini dikarenakan",
    ],
    "diksi kaku": [
        "merupakan", "memperoleh", "melakukan pembelian", "terdapat",
        "mengalami kesulitan", "memberikan kemudahan", "dalam waktu singkat",
    ],
    "pola kalimat": [
        "bukan hanya", "tidak hanya", "baik itu",
    ],
    "cta lemah": [
        ">daftar sekarang<", ">pelajari lebih lanjut<", ">selengkapnya<",
        ">klik di sini<", ">beli sekarang<",
    ],
}

def bersihkan(t):
    t = re.sub(r"<script.*?</script>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S | re.I)
    return t

def teks_saja(t):
    return html.unescape(re.sub(r"<[^>]+>", " ", t))

def dash_prosa(teks):
    """Hitung tanda hubung panjang di dalam kalimat saja.

    Tidak dihitung: atribusi testimoni ("— Dwi, Bekasi"), item daftar,
    dan pasangan label—nilai yang pendek. Yang dihitung cuma yang muncul
    di tengah prosa, karena itu yang jadi sidik jari AI.
    """
    n = 0
    for baris in teks.splitlines():
        b = baris.strip()
        if not b or b.lstrip("-–—•*").strip() != b:   # atribusi / bullet
            continue
        if len(b) < 60:                                # label — nilai
            continue
        n += b.count("—")
    return n

def main():
    src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    src = bersihkan(src)
    low_markup = src.lower()
    teks = teks_saja(src)
    low = teks.lower()

    temuan = []
    for kategori, frasa in TERLARANG.items():
        target = low_markup if kategori == "cta lemah" else low
        for f in frasa:
            for m in re.finditer(re.escape(f), target):
                potong = target[max(0, m.start() - 45): m.end() + 45].replace("\n", " ")
                temuan.append((kategori, f, " ".join(potong.split())))

    kata = re.findall(r"\w+", teks)
    n = len(kata)
    dash = dash_prosa(teks)
    seru = teks.count("!")
    angka = len(re.findall(r"\d", teks))
    perlu_diisi = len(re.findall(r"\[PERLU DIISI", src, re.I))
    placeholder = len(re.findall(r"\[[A-Z][^\]]{3,}\]", src))

    print(f"\n{'='*64}\n  AUDIT NASKAH LANDING PAGE\n{'='*64}")
    print(f"  Jumlah kata            : {n}")
    print(f"  Tanda hubung panjang — : {dash}   (maks ~1 per blok)")
    print(f"  Tanda seru !           : {seru}")
    print(f"  Digit angka            : {angka}   (0 = naskah masih abstrak)")
    print(f"  Penanda [PERLU DIISI]  : {perlu_diisi}")
    print(f"  Placeholder tersisa    : {placeholder}")

    if not temuan:
        print("\n  Tidak ada frasa terlarang yang terdeteksi.")
    else:
        print(f"\n  {len(temuan)} PELANGGARAN:\n")
        urut = {}
        for k, f, c in temuan:
            urut.setdefault(k, []).append((f, c))
        for k, items in urut.items():
            print(f"  [{k.upper()}]")
            for f, c in items:
                print(f"    • \"{f}\"")
                print(f"      …{c}…")
            print()

    print(f"{'='*64}")
    if n and angka == 0:
        print("  PERINGATAN: tidak ada satu pun angka. Naskah masih abstrak.")
    if n > 300 and angka / max(n, 1) < 0.005:
        print("  PERINGATAN: sangat sedikit angka/nama konkret untuk panjang segini.")
    if dash > n / 250:
        print("  PERINGATAN: tanda hubung panjang terlalu sering. Sidik jari AI.")
    if perlu_diisi:
        print(f"  CATATAN: {perlu_diisi} bagian masih menunggu aset dari user.")
    print(f"{'='*64}\n")
    return 1 if temuan else 0

if __name__ == "__main__":
    sys.exit(main())
