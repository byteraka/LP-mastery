# Desain — aturan craft

Gaya dan tokennya ada di `gaya-desain.md`. File ini aturan yang berlaku lintas gaya:
ritme, tipografi, mobile, kecepatan, komponen.

---

## KOREKSI TERHADAP RISET LAMA

Versi pertama file ini menyatakan "15 dari 16 halaman berlatar putih". **Itu salah.**
Angka itu dari membaca deskripsi teks halaman, bukan melihat halamannya.

Setelah delapan halaman referensi benar-benar dibuka dan diperiksa tokennya:

| | Temuan sebenarnya |
|---|---|
| Latar gelap | 4 dari 8 (jastip, lp-mastery, fortis, konvert) |
| Latar terang | 4 dari 8 (conversionclub, acquisition, nrhouse, klinikmarketing) |
| Satu kolom, mobile-first | 8 dari 8 |
| Ilustrasi vektor generik | 0 dari 8 |
| Satu warna aksen dominan | 6 dari 8 (dua sisanya pakai dua aksen) |
| Panjang halaman | 6.888px – 20.604px |
| Halaman tanpa gambar sama sekali | 1 (lp-mastery — dan tetap terlihat penuh) |

**Gelap bukan pengecualian. Gelap adalah setengah pasarnya.**

---

## SKALA TIPOGRAFI MENURUT KELAS TIKET

Pola paling konsisten dari seluruh referensi: **makin mahal tiketnya, makin kecil
headline-nya.** Halaman murah berteriak, halaman mahal berbicara pelan.

| Kelas tiket | H1 desktop | Weight | Line-height | Rata |
|---|---|---|---|---|
| Impuls | 35–54px | 700–800 | 1.0–1.4 | tengah atau kiri |
| Pertimbangan | 36–50px | 800–900 | 1.1–1.2 | kiri atau tengah |
| Keputusan | 34–40px | 800 | 1.2 | kiri |
| Tinggi | 32–34px | 800 | 1.2 | tengah |

Di mobile, kurangi sekitar 35%. H1 mobile 30–36px sudah cukup besar.

Badan teks: 14px untuk gaya Direct Response dan Korporat Tenang, 16–16.5px untuk sisanya.
Jangan di bawah 14px.

Line-height headline **selalu lebih rapat dari badan teks** — 1.0 sampai 1.2 untuk
headline, 1.5 sampai 1.65 untuk badan.

---

## LEBAR DAN RUANG

Teks maksimal **640px**. Blok bukti dan tabel boleh 860px. Strip warna boleh penuh.

Jarak antar blok: 56px mobile, 88px desktop. Di dalam blok 20px.
Padding samping mobile 20px, tidak kurang.

**Halaman panjang itu normal.** Referensi terpendek 6.888px, terpanjang 20.604px.
Jangan memangkas blok supaya halaman terlihat ringkas — yang dipangkas biasanya
blok bukti atau blok keberatan, dan itu yang menutup penjualan.

---

## RITME SECTION

Halaman sepanjang 10.000px butuh penanda supaya pembaca tahu di mana dia.

- **Latar selang-seling**: beri `--bg-alt` pada section tertentu. Maksimal tiga
  dalam satu halaman, jangan berselang-seling terus-menerus.
- **Eyebrow kecil berwarna aksen** di atas tiap judul section — dipakai di jastip,
  lp-mastery, nrhouse, konvert.
- **Angka besar sebagai penanda section** — "02 CARA MELATIH TIM". Dipakai acquisition.com.
- Jangan bikin semua section tingginya sama. Ritme yang terlalu rata terbaca seperti template.

---

## YANG DILARANG — sidik jari desain AI

**Gradien ungu-ke-biru** di hero, tombol, atau teks. Penanda paling cepat dikenali.
Catatan: gradien *boleh* di gaya SaaS Gelap, tapi sebagai glow di belakang hero,
bukan sebagai isi tombol.

**Glassmorphism** — `backdrop-filter: blur()` pada kartu melayang. Nol dari delapan referensi.

**Tiga kartu fitur sejajar dengan ikon seragam.** Pola paling sering dihasilkan AI,
paling jarang ada di halaman yang convert. Pakai daftar vertikal atau grid 2×2 bergaya.

**Ilustrasi vektor generik.** Nol dari delapan. Ganti dengan foto asli, screenshot,
atau pengisi visual berbasis teks.

**Hero rata tengah dengan bentuk abstrak di belakangnya.**

**Simetri sempurna** — semua blok tingginya sama, semua kolom seimbang.

**Logo "dipercaya oleh" yang tidak nyata.**

**Kotak placeholder di hero.** Ini kesalahan terparah: ruang paling berharga di halaman
diisi lubang abu-abu. Halaman tanpa gambar di hero selalu lebih baik daripada halaman
dengan lubang di hero.

---

## GAMBAR

Urutan prioritas: **foto asli > screenshot mentah > mockup > pengisi berbasis teks >
tidak ada gambar.** Ilustrasi generik ada di bawah "tidak ada gambar".

Screenshot dipasang berbeda tergantung gaya:
- Direct Response: **mentah, tanpa bingkai, tanpa bayangan.** Itu kekuatannya.
- Gaya lain: border tipis, radius kecil.

```css
.shot { width:100%; border:1px solid var(--line); border-radius:6px; display:block; }
```

Foto orang jangan dipotong bulat kecil. Foto founder besar dan biasa saja lebih dipercaya
daripada headshot bulat 64px.

Placeholder ditulis spesifik dan **tidak pernah di hero**:

```html
<div class="ph">[PERLU DIISI: screenshot chat WhatsApp dari 3 alumni, nama disamarkan]</div>
```

---

## TOMBOL

Satu bentuk untuk seluruh halaman. Besar, kontras tinggi, teks kalimat orang pertama.

Radius mengikuti gaya: 4px (Brutalist, Direct Response, Korporat), 12px (SaaS),
999px pil (Gelap Premium).

Padding minimal 16px atas-bawah. Gaya Gelap Premium bahkan sampai 26px.

```css
.cta{
  display:block; width:100%; max-width:440px; margin:24px auto;
  padding:18px 24px; background:var(--accent); color:var(--on-accent);
  font-size:18px; font-weight:700; text-align:center;
  border:0; border-radius:var(--radius); text-decoration:none;
}
```

Tanpa animasi berdenyut. Bayangan hanya kalau gayanya memang memakainya —
offset keras untuk Brutalist, lembut untuk Gelap Premium, nihil untuk sisanya.

**Sticky CTA di mobile**, muncul setelah hero lewat:

```css
.sticky{ position:fixed; left:0; right:0; bottom:0; padding:10px 16px;
         background:var(--bg); border-top:1px solid var(--line); z-index:50;
         transform:translateY(120%); transition:transform .2s; }
.sticky.on{ transform:none; }
@media(min-width:768px){ .sticky{ display:none; } }
```

Tombol WhatsApp melayang di kanan bawah adalah konvensi pasar Indonesia —
dipakai fortis dan banyak halaman lain. Pakai kalau jalur aksinya WhatsApp.

---

## BLOK HARGA

Blok paling menonjol di halaman. Harga coret kecil dan redup, harga akhir besar
dan berwarna aksen. Border tegas, bukan bayangan.

```css
.harga-box{ border:2px solid var(--ink); border-radius:10px; padding:28px 20px; }
.harga-coret{ font-size:18px; opacity:.6; text-decoration:line-through; }
.harga-final{ font-size:40px; font-weight:800; color:var(--accent); line-height:1.1; }
```

---

## MOBILE

Lebih dari 90% traffic Meta Ads di Indonesia dari HP. Desain untuk HP dulu.

- Satu kolom selalu. Tidak ada grid dua kolom di bawah 768px.
- Target sentuh minimal 44px.
- Tidak ada scroll horizontal. Bungkus tabel dengan `overflow-x:auto`.
- Form: `type="tel"` dan `inputmode="numeric"` untuk nomor.
- Tes di 390px **dan** 1440px sebelum kirim. Halaman yang benar di 390px bisa
  terbaca kosong di 1440px — itu yang bikin halaman terasa belum jadi.

---

## KECEPATAN

Halaman lambat membakar budget iklan sebelum orang sempat membaca. Kalau landing page
view jauh lebih kecil dari link click, itu kebocoran teknis, bukan masalah copy.

- Satu file HTML, CSS inline di `<style>`, JS inline seminimal mungkin.
- Tanpa framework, tanpa jQuery, tanpa library animasi, **tanpa Tailwind CDN.**
- Webfont maksimal dua bobot, `font-display:swap`. Font sistem kalau bisa.
  Font display untuk H1 (Anton, Fraunces, Onest) cukup satu bobot.
- Gambar `loading="lazy"` kecuali hero.
- Carousel pakai `scroll-snap` CSS, bukan library.
- Countdown JS polos, maksimal 15 baris.

---

## STRUKTUR FILE

```
<style> ... </style>          token + komponen, inline
<body>
  <section class="hero"> ... </section>
  <!-- ===== BLOK 3: BIAYA MASALAH ===== -->
  <section> ... </section>
  <div class="sticky"> ... </div>
</body>
<script> ... </script>        countdown + smooth scroll saja
```

Beri komentar HTML di atas tiap section dengan nama bloknya supaya user gampang mengedit.
Di paling atas file, satu blok komentar berisi daftar semua `[PERLU DIISI]` di halaman.
