---
name: landing-page-jualan
description: "Bikin landing page / halaman penjualan yang tinggi konversi untuk traffic Meta Ads maupun organik — naskah per blok plus halaman HTML jadi, dengan pilihan gaya desain dari referensi halaman yang terbukti convert, langsung dengan preview yang bisa dicek. Untuk edukasi (ebook, ecourse, webinar, seminar, workshop), produk digital, produk fisik, jasa, tiket rendah sampai tinggi. Pakai saat diminta bikin landing page, sales page, halaman jualan, LP, halaman pendaftaran, atau memperbaiki halaman yang konversinya rendah."
---

# Landing Page Jualan

Tugas halaman ini bukan menjelaskan produk. Tugasnya **menghilangkan alasan untuk tidak beli hari ini.**

Output: **naskah per blok** + **satu file HTML self-contained** + **preview yang bisa langsung dicek.**

Ikuti bahasa user. Dia menulis Indonesia, jawab dan tulis halamannya dalam Bahasa Indonesia.
Dia menulis bahasa lain, ikuti itu. Istilah teknis tetap Inggris.

---

## KAPAN BUKA FILE REFERENSI

Aturan detailnya ada di file referensi, tidak di sini. Membukanya bukan opsional.

| Buka | Kapan | Wajib? |
|---|---|---|
| `references/arsitektur.md` | Setelah tahu harga, sebelum menyusun blok | Wajib |
| `references/gaya-desain.md` | Sebelum menawarkan pilihan gaya, dan sebelum menulis CSS | Wajib |
| `references/bahasa.md` | Sebelum menulis satu kalimat naskah | Wajib |
| `references/blok.md` | Saat menulis tiap blok | Wajib |
| `references/desain.md` | Aturan craft: mobile, kecepatan, komponen | Wajib |
| `references/swipe.md` | Saat buntu cari bentuk headline, CTA, atau bukti | Kalau perlu |
| `assets/template.html` | Kerangka HTML | Kalau perlu |

Jangan mengerjakan dari ingatan.

---

## LANGKAH 1 — Brief lengkap, satu kali di depan

Kirim **satu pesan** berisi seluruh yang dibutuhkan. Bukan tanya-jawab beruntun.
User boleh mengisi seadanya dan melewati yang tidak ada — itu dibilang di awal.

Kalau brief awal user sudah menjawab sebagian, **jangan tanya ulang** yang sudah dijawab.

Pakai `AskUserQuestion` untuk yang berupa pilihan (kelas tiket, gaya desain, jalur aksi),
dan daftar tertulis untuk yang berupa isian.

### Yang wajib — berhenti dan tanya kalau tidak ada
- **Produk apa** dan formatnya (ebook, kelas online, workshop offline, produk fisik, jasa)
- **Harga** — menentukan seluruh bentuk halaman
- **Siapa pembelinya** — sespesifik mungkin, bukan "umum"

### Yang sangat menentukan kualitas — minta, tapi jalan terus kalau tidak ada
- **Kalimat asli pembeli** — chat CS, komentar iklan, testimoni mentah, DM, review.
  Bahan paling berharga. Copy emosional dikutip, bukan dikarang.
- **Keunikan produk** — kenapa cara ini beda dari yang lain, mekanismenya apa,
  ada nama metodenya tidak
- **Bukti yang tersedia** — pilih semua yang ada:
  screenshot hasil/dashboard/chat · video testimoni · foto dokumentasi kelas atau acara ·
  angka kampanye atau hasil dengan tanggal · jumlah alumni/pembeli · kredensial pembicara ·
  logo klien atau media
- **Isi produk dalam angka** — berapa bab, berapa modul, berapa resep, berapa jam,
  berapa pertemuan. Angka isi ini dipakai jadi elemen visual.
- **Bonus** — apa saja dan nilainya berapa
- **Garansi** — sanggupnya sampai mana. Jangan tulis garansi yang user tidak sanggup penuhi.
- **Urgensi nyata** — tanggal tutup, kuota, batch, harga naik. Kalau tidak ada, katakan
  dan usulkan bikin satu yang benar.
- **Keberatan yang paling sering muncul** dari calon pembeli
- **Logistik** (untuk event) — tanggal, jam, lokasi, format online/offline
- **Aset visual** — foto founder, foto produk, screenshot, logo. Minta dilampirkan sekarang.
- **Traffic dari mana** — Meta Ads atau organik. Kalau dari iklan, minta hook iklannya
  untuk message match.

### Apa yang TIDAK ditanyakan
**Jangan tanya warna.** Itu hal paling tidak berpengaruh ke konversi. Warna ikut gaya
desain yang dipilih di Langkah 3, atau diambil dari brand user kalau disebut.

Setelah brief masuk: yang kosong ditebak wajar, dan **asumsinya ditulis di atas output.**

---

## LANGKAH 2 — Tentukan kelas tiket

**Harga menentukan bentuk halaman, bukan jenis produknya.** Aturan paling penting di skill
ini dan paling sering dilanggar. Ebook Rp79rb dan workshop Rp15jt butuh halaman yang berbeda
secara mendasar walaupun dua-duanya edukasi.

| Kelas | Rentang | Watak halaman |
|---|---|---|
| **Impuls** | < Rp 300rb | Anchor ekstrem, countdown, 3 bonus berlabel rupiah, langsung checkout |
| **Pertimbangan** | Rp 300rb – 3jt | Anchor sopan (2–3x), kuota nyata, tanggal tutup, garansi |
| **Keputusan** | Rp 3–25jt | Tanpa diskon dramatis, kualifikasi, konsultasi/WA, bukti mendalam |
| **Tinggi** | > Rp 25jt | Tanpa diskon, **diskualifikasi eksplisit**, apply bukan beli |

Makin tinggi harga, **makin kecil diskon dan makin banyak diskualifikasi.**

Buka `references/arsitektur.md`, pilih satu dari tujuh arsitektur.

---

## LANGKAH 3 — Tawarkan gaya desain

Buka `references/gaya-desain.md`. Tujuh gaya, semuanya diambil dari 22 halaman nyata
yang sedang jalan, lengkap dengan token aslinya.

**Saring dulu dengan kelas tiket, baru tawarkan sisanya ke user.** Jangan tawarkan semua
tujuh — gaya promo keras di produk Rp15jt merusak kepercayaan, gaya korporat tenang di
ebook Rp79rb membunuh volume.

| Kelas tiket | Tawarkan |
|---|---|
| Impuls | Direct Response · Hangat Editorial · Terang Brutalist |
| Pertimbangan | Gelap Premium · Gelap Brutalist · Terang Brutalist · Hangat Editorial |
| Keputusan | Gelap Premium · Korporat Tenang |
| Tinggi | Korporat Tenang |
| Langganan / software | SaaS Gelap |
| Lead magnet / webinar gratis | Terang Brutalist · Korporat Tenang — halaman pendek |

Selalu sertakan pilihan keempat: **"Aku punya referensi sendiri"**. Kalau user memberi link,
buka halamannya, tarik tokennya — warna, font, ukuran heading, radius, bayangan, cara
mengisi hero — lalu bangun dari situ. Jangan paksa masuk ke salah satu dari tujuh.

Sebutkan singkat kenapa satu gaya cocok untuk produknya, supaya user memilih dengan dasar.
Kalau user tidak menjawab, pakai yang pertama di daftar dan katakan alasannya.

---

## LANGKAH 4 — Pilih register bahasa

**Register A — percakapan.** Edukasi, produk digital, jasa, parenting, audiens 20–40.
**Register B — promo.** Produk fisik consumer, herbal, kesehatan, audiens Facebook 35+.

Pilih dari produk + harga + audiens, bukan kebiasaan.
Buka `references/bahasa.md` sekarang. Wajib, sebelum menulis satu kalimat pun.

---

## LANGKAH 5 — Susun urutan blok

```
1  HERO            janji spesifik + untuk siapa + satu bukti + CTA
2  MASALAH         gejala konkret pakai bahasa pembeli
3  BIAYA MASALAH   apa yang hilang kalau dibiarkan — sumber urgensi sebenarnya
4  MEKANISME       kenapa cara ini bekerja dan kenapa beda
5  ISI             apa yang didapat, konkret dan bisa dibayangkan
6  BUKTI           angka, screenshot, testimoni bernama
7  DISKUALIFIKASI  untuk siapa halaman ini, dan untuk siapa bukan
8  PENAWARAN       inti + bonus + perbandingan nilai
9  GARANSI         pembalikan risiko
10 URGENSI         mekanisme yang sah
11 FAQ             tempat membuang sisa keraguan
12 CTA PENUTUP
```

Yang berubah antar kelas tiket bukan urutannya, tapi bobot tiap blok dan blok mana yang
dibuang. Yang paling sering terlewat tapi dipakai pemenang: **biaya masalah (3)** dan
**diskualifikasi (7)**. `references/blok.md` punya detail dan contoh naskah nyata.

---

## LANGKAH 6 — Tulis naskahnya

Kalimat jadi, bukan ringkasan.

**Kutip, jangan karang.** Copy emosional dikutip dari kalimat asli pembeli.

**Spesifik mengalahkan intens.** Jangan naikkan volume dengan kata sifat, naikkan dengan detail.

> Lemah: "Sudah dipercaya ribuan alumni."
> Kuat: "6,95 juta turis asing datang ke Bali tahun lalu — lalu pulang, dan tetap beli barang Bali. Cuma bukan dari kamu."

**CTA sebagai kalimat orang pertama**, bukan perintah. Pembeda paling tajam antara
halaman praktisi dan halaman buatan AI.

> AI: "Daftar Sekarang" · "Pelajari Lebih Lanjut"
> Pasar: "Saya Mau Belajar Metodenya" · "Oke, Aku Mau Ikut →" · "Ambil Kursimu — Rp 1.000.000 →"

Ulang CTA tiap 1–2 layar. Halaman pendek 2–3 kali, panjang 5–6 kali.

---

## LANGKAH 7 — Tentukan jalur aksinya

Tanya user sekali, setelah arsitektur dipilih:

| Pilihan | Cocok untuk |
|---|---|
| **Tombol WhatsApp** dengan pesan terisi | Konsultasi, high-ticket, jasa |
| **Form POST ke endpoint user** | Produk fisik COD, pendaftaran webinar, order langsung |
| **Tombol ke checkout eksternal** | Produk digital dengan payment gateway |

Kalau form POST, minta URL endpoint-nya. Belum ada → `action="[PERLU DIISI: URL endpoint]"`.
Jangan bikin form yang submit-nya tidak mengarah ke mana-mana.

---

## LANGKAH 8 — Bangun halamannya

Satu file HTML self-contained. CSS dan JS inline, tanpa framework, tanpa CDN.

**Jangan pakai Tailwind CDN.** Tailwind sendiri menyatakan Play CDN bukan untuk produksi —
dia memindai HTML dan membuat CSS di browser saat halaman dibuka. Untuk halaman yang
menerima traffic berbayar dari HP, itu ongkos yang tidak perlu. Dan default-nya
(gradien, `rounded-2xl`, `shadow-lg`, grid tiga kolom berikon) justru persis tampang
yang bikin halaman terasa dibuat mesin.

Pakai token gaya yang dipilih di Langkah 3, **persis seperti tertulis** di `gaya-desain.md`.
Aturan craft — mobile, kecepatan, komponen — ada di `references/desain.md`.

**Dilarang menaruh kotak placeholder di hero.** Kalau belum ada foto, hero disusun supaya
utuh tanpa gambar. `gaya-desain.md` punya tujuh pengisi visual yang dibuat dari teks dan
CSS saja. Penanda `[PERLU DIISI]` ditaruh di tengah atau bawah halaman, tidak pernah di hero.

---

## LANGKAH 9 — Audit. Wajib.

**Pass 1 — bahasa.** Jalankan skripnya:

```
python3 scripts/audit.py <file naskah atau html>
```

Perbaiki semua temuannya, jalankan lagi sampai bersih. Exit code 1 = masih ada pelanggaran.
Skrip cuma menangkap yang gampang dipola. Setelah bersih, baca hero dan semua CTA seolah
diucapkan keras. Kalimat yang tidak akan pernah diucapkan orang, tulis ulang.

**Pass 2 — bukti.** Tiap angka, testimoni, nama, tanggal, klaim garansi harus berasal dari
bahan user. Yang tidak ada sumbernya: `[PERLU DIISI]`, jangan dikarang. Termasuk kelangkaan.

**Pass 3 — message match.** Hook iklan harus muncul lagi di layar pertama dengan kata mirip.

**Pass 4 — desain.** Buka halamannya di lebar 390px dan 1440px. Di 1440px halaman tidak
boleh terbaca kosong. Cek: hero utuh tanpa lubang · satu warna aksen dominan ·
nol ilustrasi generik · kontras teks cukup · target sentuh ≥44px · tidak ada scroll horizontal.

---

## LANGKAH 10 — Tampilkan previewnya

Tampilkan halamannya, jangan cuma kirim kodenya. Ambil cara pertama yang tersedia:

1. **Kalau sesi bisa mempublikasikan HTML jadi URL** — pakai ini. Terbaik, karena user bisa
   membukanya di HP. Penting: 90%+ traffic Meta dari HP.
2. **Kalau sesi bisa menampilkan file di percakapan** — tulis file lalu tampilkan.
3. **Kalau tidak dua-duanya** — simpan filenya, sebutkan lokasinya.

**Jangan pernah menempelkan HTML utuh sebagai blok kode di chat.**

User tetap butuh file HTML-nya untuk dipasang di domain sendiri. Kasih dua-duanya.
Kalau previewnya URL, ingatkan sekali: buka di HP dulu sebelum dipakai iklan.

---

## LANGKAH 11 — Revisi

- **Tulis ulang HTML UTUH.** Jangan potongan atau diff. Halaman rusak pelan-pelan
  kalau direvisi dengan fragmen.
- **Perbarui preview yang SAMA.** Jangan bikin link baru tiap revisi.
- Jalankan ulang audit.

Jangan bilang halaman sudah live sampai itu benar-benar terjadi. Preview bukan halaman live.

---

## ATURAN MAIN

Jangan mengarang fitur, testimoni, hasil, harga, tenggat, atau kelangkaan yang tidak ada
di bahan yang diberikan. Kalau butuh bukti dan buktinya tidak ada, minta.

Kalau penawarannya lemah, katakan sekali di awal, lalu tetap kerjakan yang diminta.

Cek angka, lima detik: `CPA maksimum = harga × margin ÷ 1,3`.

---

## FORMAT OUTPUT

**Naskah per blok** — di atasnya sebutkan: kelas tiket, arsitektur, gaya desain, register
bahasa, dan asumsi yang diambil.

**File HTML** — satu file self-contained.

**Preview** — sesuai Langkah 10.

Tutup dengan tiga baris: bagian yang perlu diisi user, satu elemen yang paling layak
di-A/B test duluan, dan kelemahan penawaran yang terlihat selama mengerjakan.
