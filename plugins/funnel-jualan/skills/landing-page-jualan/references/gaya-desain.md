# Enam Gaya Desain

Semua token di bawah diambil langsung dari halaman aslinya, bukan dikira-kira.
Tiap gaya punya sikap. **Pilih satu dan jalankan sepenuhnya** — mencampur dua gaya
menghasilkan halaman yang tidak jadi apa-apa.

---

## CARA MEMILIH

Kelas tiket menyaring dulu, baru user memilih dari yang tersisa.

| Kelas tiket | Gaya yang cocok |
|---|---|
| Impuls (< Rp 300rb) | Direct Response · Hangat Editorial · Gelap Brutalist |
| Pertimbangan (Rp 300rb–3jt) | Gelap Premium · Gelap Brutalist · Hangat Editorial |
| Keputusan (Rp 3–25jt) | Gelap Premium · Korporat Tenang |
| Tinggi (> Rp 25jt) | Korporat Tenang |
| Langganan / software | SaaS Gelap |

Kalau user punya link referensi desainnya sendiri, **buka halamannya, tarik tokennya
(warna, font, ukuran heading, radius, bayangan), lalu bangun dari situ** — jangan paksa
masuk ke salah satu dari enam ini.

---

## 1. GELAP BRUTALIST
*Contoh: event.jastip.id/seminar/bali (seminar Rp97rb)*

Berani, padat, berisik dengan cara yang disengaja. Terasa seperti poster.

```css
--bg:        #151316;   /* hampir hitam */
--bg-alt:    #FAF9F5;   /* krem, untuk section selang-seling */
--ink:       #FFFFFF;
--accent:    #FFD600;   /* kuning terang */
--radius:    4px;
--shadow:    5px 5px 0 #151316;   /* offset KERAS, tanpa blur */
```

- **H1: font Anton** (atau Oswald/Bebas Neue), 54px di desktop, weight 400,
  **line-height 1.0**, HURUF KAPITAL SEMUA, rata kiri
- Body: Plus Jakarta Sans 16.5px
- Tombol: latar kuning, teks hampir hitam, 15px/700, padding 16px 26px, radius 4px,
  bayangan offset keras
- **Blok angka raksasa** sebagai pengisi visual: empat angka besar berwarna aksen
  dengan keterangan kecil di bawahnya
- Eyebrow kecil berwarna aksen di atas tiap judul section

Jangan pakai untuk: produk mewah, audiens korporat, produk kesehatan.

---

## 2. GELAP PREMIUM
*Contoh: produk.karyawan.ai/lp-mastery (Rp1jt), fortiscircle.id/saham (Rp1,3jt)*

Mahal, tenang, percaya diri. **Gaya terbaik kalau belum ada foto sama sekali.**

```css
--bg:        #0A0A0A;
--bg-alt:    #1A1A1A;   /* kartu, beda tipis dari latar */
--ink:       #F5F5F3;   /* putih tulang, bukan putih murni */
--accent:    #EFC14D;   /* emas — atau #FFFFFF untuk versi putih */
--tint-1:    rgba(239,193,77,0.06);
--tint-2:    rgba(239,193,77,0.12);
--radius:    999px;     /* tombol pil */
--shadow:    0 10px 30px rgba(0,0,0,.3);
```

- H1: sans 50px, weight **800**, line-height 1.2, rata kiri
  (varian Fortis: font Onest, weight 900, rata tengah, kapital)
- Tombol: dua pilihan yang sama-sama terbukti —
  latar gelap + teks emas, **atau** latar putih + teks hitam (kontras maksimum, terasa lebih mahal)
- Padding tombol tebal: 16px, sampai 26px 32px untuk versi Fortis
- **Kata kunci di dalam headline diberi warna aksen**, sisanya putih
- Kartu bertint aksen 6–12% di atas latar gelap
- Tombol WhatsApp melayang di kanan bawah

---

## 3. DIRECT RESPONSE
*Contoh: conversionclub.id (Rp199rb), learn.klinikmarketing.id (Rp247rb)*

Sengaja tidak dipoles. Terbaca seperti orang yang menunjukkan hasilnya sendiri,
bukan seperti iklan.

```css
--bg:        #F9F6F4;   /* putih hangat */
--ink:       #31373D;   /* abu kebiruan, bukan hitam */
--accent:    #DF0E03;   /* merah CTA */
--mark:      #FFF200;   /* stabilo kuning menyala */
--frame:     #036854;   /* opsional: bingkai warna kiri-kanan */
--radius:    4px;
--shadow:    none;
```

- H1: Helvetica Neue / Arial 35px, weight 700, **rata tengah**, line-height 1.4
- Body **14px** — kecil, gaya dokumen
- **Stabilo pada frasa kunci** di headline dan judul section. Bukan bold — highlight.
- **Screenshot mentah apa adanya**: dashboard iklan, chat WA, invoice, postingan IG.
  Tanpa bingkai, tanpa bayangan, tanpa dirapikan. Angka sensitif disamarkan sebagian.
- Label bergaris bawah miring: "Pengguna 2:", "Hasil member:"
- Tombol merah tipis, padding kecil

Jangan pakai untuk: brand mapan, high-ticket, audiens korporat.

---

## 4. KORPORAT TENANG
*Contoh: acquisition.com/workshop-sales ($5.000)*

Volume visual dikecilkan. Yang mengangkat halaman ini kualitas fotonya dan nada tenangnya.

```css
--bg:        #FFFFFF;
--ink:       #333333;
--ink-head:  #131628;   /* navy hampir hitam untuk heading */
--accent:    #6F00FF;   /* ungu */
--radius:    4px;
--shadow:    none;
```

- H1: **Poppins 34px** weight 800, line-height 1.2, rata tengah
  (perhatikan: jauh lebih kecil dari halaman tiket rendah)
- Body Arial 14px
- **Strip pengumuman hitam di paling atas**, sebelum apa pun:
  "WORKSHOP 2 HARI · NOV & DES HABIS, 28–30 JAN DIBUKA"
- **Angka besar sebagai penanda section**: "02 CARA MELATIH TIM", "03 CARA MENGELOLA"
- Fotografi acara asli — peserta, ruangan, suasana. Bukan stok, bukan mockup.
- Video testimoni berjajar dengan tombol play bundar
- **Tanpa emoji, tanpa countdown, tanpa harga coret**

Butuh foto asli yang bagus. Tanpa itu gaya ini kosong — pakai Gelap Premium.

---

## 5. HANGAT EDITORIAL
*Contoh: nrhouse.id/dpp (Rp149rb)*

Personal, lembut, tidak agresif. Satu-satunya yang pakai serif.

```css
--bg:        #FDF6EE;   /* krem hangat */
--bg-card:   rgba(255,250,244,0.62);
--ink:       #3A2A22;   /* COKELAT TUA, bukan hitam */
--accent:    #D97A6C;   /* terakota */
--accent-2:  #7A8C5A;   /* sage — gaya ini boleh dua aksen */
--tint:      rgba(217,122,108,0.14);
--radius:    16px;
```

- **H1: font Fraunces** (serif display) 32px weight 600, line-height 1.1, rata tengah
- Frasa kunci dibuat **serif miring berwarna terakota**
- Body: Inter 16px
- **Trio kartu angka**: "16 Bab Lengkap · 90+ Sub-Bab · 30 Hari Action Plan",
  angka besar berserif, keterangan kecil
- Daftar manfaat dengan **chip ikon bulat bertint** di sebelah kiri tiap baris
- Kontras dibangun dari suhu warna, bukan gelap-terang
- Halaman terpendek dari semua gaya (~7.800px)

Untuk: parenting, wellness, kreatif, self-improvement, produk untuk perempuan.
Jangan untuk: finansial, B2B, apa pun yang butuh kesan otoritas teknis.

---

## 6. SAAS GELAP
*Contoh: konvert.id (langganan Rp48–258rb/bln)*

```css
--bg:        #000314;   /* navy sangat gelap */
--ink:       #EFEFF7;
--accent:    #F57A00;   /* oranye, CTA utama */
--accent-2:  #3D90F7;   /* biru */
--ghost:     rgba(255,255,255,0.04);
--radius:    12px;
```

- H1: Plus Jakarta Sans 38px weight 800, rata tengah, line-height 1.08
- **Headline multi-warna per baris**: baris 1 putih, baris 2 oranye, baris 3 biru
- Glow gradien di belakang hero
- Dua tombol berdampingan: satu solid, satu ghost berborder
- **Baris chip kepercayaan di bawah CTA**: "✓ Mulai gratis ✓ Tanpa kartu kredit
  ✓ Live dalam 1 menit" — tiga keberatan dihapus dalam satu baris
- Screenshot produk dimiringkan sedikit sebagai visual hero

Butuh screenshot antarmuka yang bagus. Tanpa itu gaya ini kosong.

---

## KALAU BELUM ADA ASET SAMA SEKALI

`lp-mastery` punya **nol gambar** dan tetap terlihat penuh. Ini bukti bahwa halaman kosong
bukan masalah aset, tapi masalah cara mengisi ruang.

**Dilarang keras menaruh kotak placeholder di hero.** Ruang paling berharga di halaman
tidak boleh diisi lubang. Kalau belum ada foto, hero disusun supaya utuh tanpa gambar.

Tujuh pengisi visual yang dibuat dari teks dan CSS saja:

1. **Kata disorot warna aksen di dalam headline** — satu trik ini saja menghilangkan kesan datar
2. **Blok angka raksasa** — 3–4 angka besar berwarna aksen dengan keterangan kecil
   (jastip: "6,95 JT · 1,63 JT · $565 JT · -10,65%")
3. **Kartu mock UI** — panel gelap berisi baris ketikan gaya terminal atau chat
4. **Trio kartu angka isi produk** — "16 Bab · 90+ Sub-Bab · 30 Hari"
5. **Grid kartu 2×2** untuk blok masalah, tiap kartu: ikon kecil, judul, body pendek
6. **Pil eyebrow** di atas headline berisi logistik — kuota, tanggal, lokasi, format
7. **Baris chip kepercayaan** di bawah CTA — garansi, jumlah pemakai, kecepatan akses

Kalau user memang punya foto tapi belum dikirim, tandai `[PERLU DIISI: ...]` **di bagian
tengah atau bawah halaman**, jangan di hero, dan sebutkan persis foto apa yang dibutuhkan.

---

## YANG BERLAKU DI SEMUA GAYA

**Makin mahal tiketnya, makin kecil headline-nya dan makin sedikit hiasannya.**
Tiket Rp97rb pakai 54px kapital dengan bayangan keras. Workshop $5.000 pakai 34px tenang
tanpa satu pun emoji. Ini pola paling konsisten dari seluruh referensi.

Semua halaman referensi: satu kolom, mobile-first, sangat panjang (6.800–20.600px).
Tidak ada satu pun yang memakai ilustrasi vektor generik.

Sembilan dari sembilan memakai **satu warna aksen dominan** (dua hanya di Hangat Editorial
dan SaaS Gelap). Tidak ada yang memakai tiga atau lebih.
