---
name: landing-page-jualan
description: "Bikin landing page / halaman penjualan yang tinggi konversi untuk traffic Meta Ads maupun organik — naskah per blok plus halaman HTML jadi yang tidak terdengar dan tidak terlihat buatan AI, langsung dengan preview yang bisa dicek. Untuk edukasi (ebook, ecourse, webinar, seminar, workshop), produk digital, produk fisik, jasa, tiket rendah sampai tinggi. Pakai saat diminta bikin landing page, sales page, halaman jualan, LP, halaman pendaftaran, atau memperbaiki halaman yang konversinya rendah."
---

# Landing Page Jualan

Tugas halaman ini bukan menjelaskan produk. Tugasnya **menghilangkan alasan untuk tidak beli hari ini.**

Output berupa dua hal: **naskah per blok** dan **satu file HTML self-contained**, lalu
**preview yang bisa langsung dicek user.**

Untuk iklan yang mengarah ke halaman ini, pakai skill `meta-ads-creative` kalau tersedia.

---

## BAHASA

Ikuti bahasa user. Dia menulis Indonesia, jawab dan tulis halamannya dalam Bahasa Indonesia.
Dia menulis bahasa lain, ikuti itu. Istilah teknis tetap Inggris.

---

## KAPAN BUKA FILE REFERENSI

Skill ini punya lima file referensi. Membukanya bukan opsional — aturan detailnya ada di sana,
tidak di file ini.

| Buka | Kapan | Wajib? |
|---|---|---|
| `references/arsitektur.md` | Setelah tahu harga, sebelum menyusun blok | Wajib |
| `references/bahasa.md` | Sebelum menulis satu kalimat naskah | Wajib |
| `references/blok.md` | Saat menulis tiap blok | Wajib |
| `references/desain.md` | Sebelum menulis HTML | Wajib |
| `references/swipe.md` | Saat buntu cari bentuk headline, CTA, atau bukti | Kalau perlu |
| `assets/template.html` | Sebagai kerangka HTML | Kalau perlu |

Jangan mengerjakan dari ingatan. Aturan di file-file itu spesifik dan mudah salah diingat.

---

## LANGKAH 1 — Brief. Maksimal dua pertanyaan.

Default yang kuat mengalahkan interogasi. Jangan mewawancarai user.

Yang dibutuhkan: **produk, harga, siapa pembelinya, masalah yang dia rasakan, apa yang bikin
beda, bukti yang tersedia, dan ke mana orang diarahkan setelah klik.**

Aturannya:

- Kalau brief sudah cukup, **langsung kerjakan.** Jangan tanya apa-apa.
- Kalau ada yang kurang, tebak wajar dan **tulis asumsinya di atas output.**
- Kalau yang kurang adalah **produk, harga, atau audiens — berhenti dan tanya.** Tiga hal itu
  menentukan seluruh bentuk halaman. Menebaknya berarti membangun halaman yang salah.
- Maksimal dua pertanyaan, digabung dalam satu giliran. Pakai `AskUserQuestion` kalau tersedia.

**Jangan tanya soal warna.** Itu hal paling tidak berpengaruh ke konversi di seluruh halaman.
Ambil dari brand user kalau disebut, atau pakai default di `references/desain.md`.

**Cek aset visual.** Lihat apakah user melampirkan foto, screenshot, atau logo di sesi ini.
Kalau ada, pakai yang asli. Kalau tidak ada, sebut sekali di awal bahwa foto asli akan menaikkan
hasilnya jauh, lalu lanjut kerjakan dengan penanda `[PERLU DIISI]`. Jangan pakai gambar stok atau
placeholder acak — halaman yang terlihat "sudah jadi" padahal gambarnya palsu gampang lolos ke
produksi tanpa ada yang sadar.

**Minta kalimat asli pembeli**, sekali saja, di awal: chat CS, komentar iklan, testimoni mentah,
DM, review. Kalau ada, copy-nya jauh lebih tajam. Kalau tidak ada, lanjut.

---

## LANGKAH 2 — Tentukan kelas tiket

**Harga menentukan bentuk halaman, bukan jenis produknya.** Ini aturan paling penting di skill ini
dan yang paling sering dilanggar. Ebook Rp79rb dan workshop Rp15jt butuh halaman yang berbeda
secara mendasar, walaupun dua-duanya produk edukasi.

| Kelas | Rentang | Watak halaman |
|---|---|---|
| **Impuls** | < Rp 300rb | Anchor ekstrem, countdown, 3 bonus berlabel rupiah, langsung checkout |
| **Pertimbangan** | Rp 300rb – Rp 3jt | Anchor sopan (2–3x), kuota nyata, tanggal tutup, garansi |
| **Keputusan** | Rp 3jt – Rp 25jt | Tanpa diskon dramatis, kualifikasi, konsultasi/WA, bukti mendalam |
| **Tinggi** | > Rp 25jt | Tanpa diskon, **diskualifikasi eksplisit**, apply bukan beli, kelangkaan nyata |

Makin tinggi harga, **makin kecil diskon dan makin banyak diskualifikasi.**
Countdown "hemat 95%" di produk Rp15 juta membunuh kepercayaan. Bahasa kualifikasi
di ebook Rp79rb membunuh volume.

Sekarang buka `references/arsitektur.md` dan pilih satu dari tujuh arsitektur.

---

## LANGKAH 3 — Pilih register bahasa

**Register A — percakapan.** Edukasi, produk digital, jasa, parenting, audiens 20–40.
**Register B — promo.** Produk fisik consumer, herbal, kesehatan, audiens Facebook 35+.

Register B terasa murah untuk produk mahal. Register A terasa kurang meyakinkan untuk
produk kesehatan COD. Pilih dari **produk + harga + audiens**, bukan kebiasaan.

Buka `references/bahasa.md` sekarang. Wajib, sebelum menulis satu kalimat pun.

---

## LANGKAH 4 — Susun urutan blok

Urutan dasar yang konvergen di hampir semua halaman berperforma:

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

Yang berubah antar kelas tiket bukan urutannya, tapi **bobot tiap blok** dan blok mana yang
dibuang. Blok yang paling sering terlewat tapi terbukti dipakai pemenang: **biaya masalah (3)**
dan **diskualifikasi (7)**.

`references/blok.md` berisi fungsi tiap blok, kapan dibuang, dan contoh naskah nyata.

---

## LANGKAH 5 — Tulis naskahnya

Kalimat jadi, bukan ringkasan. Empat hal yang menentukan kualitas:

**Kutip, jangan karang.** Copy emosional tidak ditulis, tapi dikutip dari kalimat asli pembeli.

**Spesifik mengalahkan intens.** Jangan naikkan volume dengan kata sifat. Naikkan dengan detail.

> Lemah: "Sudah dipercaya ribuan alumni."
> Kuat: "6,95 juta turis asing datang ke Bali tahun lalu — lalu pulang, dan tetap beli barang Bali. Cuma bukan dari kamu."

**CTA ditulis sebagai kalimat orang pertama**, bukan perintah. Pembeda paling tajam antara
halaman praktisi dan halaman buatan AI.

> AI: "Daftar Sekarang" · "Pelajari Lebih Lanjut"
> Pasar: "Saya Mau Belajar Metodenya" · "Oke, Aku Mau Ikut →" · "Ambil Kursimu — Rp 1.000.000 →"

**Ulang CTA tiap 1–2 layar.** Halaman pendek 2–3 kali, halaman panjang 5–6 kali.

---

## LANGKAH 6 — Tanya jalur aksinya

Setelah arsitektur dipilih, arsitekturnya yang menentukan apakah halaman butuh form.
Tanya user satu kali, dengan `AskUserQuestion` kalau tersedia:

| Pilihan | Cocok untuk |
|---|---|
| **Tombol WhatsApp** dengan pesan terisi | Konsultasi, high-ticket, jasa, produk yang perlu tanya dulu |
| **Form yang POST ke endpoint user** | Produk fisik COD, pendaftaran webinar, order langsung |
| **Tombol ke halaman checkout eksternal** | Produk digital dengan payment gateway yang sudah ada |

Kalau pilihannya form POST, minta URL endpoint-nya. Kalau belum ada, pasang
`action="[PERLU DIISI: URL endpoint]"` dan sebutkan di penutup.

Jangan bikin form yang tidak mengarah ke mana-mana. Form yang submit-nya hilang lebih buruk
daripada tombol WhatsApp yang sederhana.

---

## LANGKAH 7 — Bangun halamannya

Satu file HTML self-contained. CSS dan JS inline, tanpa framework, tanpa CDN.

**Jangan pakai Tailwind CDN.** Tailwind sendiri menyatakan Play CDN bukan untuk produksi —
dia memindai HTML dan membuat CSS-nya di browser saat halaman dibuka. Untuk halaman yang
menerima traffic berbayar dari HP, itu ongkos yang tidak perlu dibayar. Dan default Tailwind
(gradien, `rounded-2xl`, `shadow-lg`, grid tiga kolom berikon) justru persis tampang yang
bikin halaman terasa dibuat mesin.

**Halaman jualan yang convert tidak terlihat seperti homepage startup.** Dari 16 halaman
berperforma yang dibedah: 15 background putih/netral, 16 satu kolom, 0 ilustrasi generik,
1 gradien, 13 pakai screenshot mentah sebagai bukti.

Buka `references/desain.md` sebelum menulis HTML. `assets/template.html` bisa dipakai
sebagai kerangka.

---

## LANGKAH 8 — Audit. Wajib, bukan opsional.

**Pass 1 — bahasa.** Jalankan skrip auditnya dulu:

```
python3 scripts/audit.py <file naskah atau html>
```

Skrip ini menangkap frasa terlarang, tanda hubung berlebih, dan naskah yang masih nol angka.
**Perbaiki semua temuannya, lalu jalankan lagi sampai bersih.** Exit code 1 berarti masih ada
pelanggaran.

Skrip cuma menangkap yang gampang dipola. Setelah bersih, baca sendiri: cocokkan dengan
daftar larangan di `references/bahasa.md`, lalu baca hero dan semua CTA seolah diucapkan keras.
Kalau ada kalimat yang tidak akan pernah diucapkan orang ke temannya, tulis ulang.

**Pass 2 — bukti.** Tiap angka, testimoni, nama, tanggal, dan klaim garansi harus berasal dari
bahan yang diberikan user. Yang tidak ada sumbernya: tandai `[PERLU DIISI]`, jangan dikarang.
Termasuk kelangkaan — kuota dan deadline yang tidak nyata adalah cara tercepat kehilangan
pembeli berulang.

**Pass 3 — message match.** Kalau ada iklan yang mengarah ke halaman ini, hook iklannya harus
muncul lagi di layar pertama dengan kata yang mirip.

Lalu cek: layar pertama terbaca dalam 5 detik · audiensnya jelas · masalahnya spesifik ·
ada mekanisme bukan cuma klaim · bukti di tempat yang tepat · urgensinya nyata ·
CTA satu tujuan · form seminimal mungkin · terbaca cepat di HP · tidak ada jaminan yang
tidak didukung · tidak ada klaim medis, penghasilan pasti, atau atribut personal yang
melanggar policy Meta.

---

## LANGKAH 9 — Tampilkan previewnya

**Tampilkan halamannya, jangan cuma kirim kodenya.** Ambil cara pertama yang tersedia di sesi ini:

1. **Kalau sesi bisa mempublikasikan HTML jadi URL** (misalnya lewat tool artifact) — pakai ini.
   Terbaik, karena user bisa membukanya di HP. Itu penting: 90%+ traffic Meta Ads datang dari HP,
   dan halaman yang bagus di layar laptop bisa berantakan di layar 360px.
2. **Kalau sesi bisa menampilkan file di dalam percakapan** — tulis file HTML-nya lalu tampilkan.
3. **Kalau dua-duanya tidak ada** — simpan filenya, sebutkan lokasinya, minta user membukanya
   di browser.

**Jangan pernah menempelkan HTML utuh sebagai blok kode di chat.**

Selain preview, user tetap butuh **file HTML-nya** untuk dipasang di domain sendiri. Kasih dua-duanya.

Kalau previewnya berupa URL, ingatkan sekali: buka di HP dulu sebelum dipakai iklan.

---

## LANGKAH 10 — Revisi

Saat user memberi masukan:

- **Tulis ulang HTML UTUH.** Jangan kirim potongan, diff, atau "ganti bagian ini saja".
  Halaman rusak pelan-pelan kalau direvisi dengan fragmen.
- **Perbarui preview yang SAMA.** Republish ke URL yang sama, atau timpa file yang sama.
  Jangan bikin halaman atau link baru tiap revisi — user jadi bingung mana yang terbaru.
- Jalankan ulang audit di Langkah 8.

Jangan bilang halaman sudah live atau sudah terpasang sampai itu benar-benar terjadi dan
kamu punya buktinya. Preview bukan halaman live.

---

## ATURAN MAIN

Jangan mengarang fitur, testimoni, hasil, harga, tenggat, atau kelangkaan yang tidak ada
di bahan yang diberikan. Kalau butuh bukti dan bukti itu tidak ada, minta.

Kalau penawarannya sendiri lemah, katakan sekali di awal, lalu tetap kerjakan yang diminta.
Halaman bagus untuk penawaran lemah cuma memperbesar kerugian.

Satu cek angka, lima detik: `CPA maksimum = harga × margin ÷ 1,3`. Kalau biaya akuisisi
realistis di atas itu, halaman sebagus apa pun tidak menyelamatkan.

---

## FORMAT OUTPUT

**Naskah per blok** — kalimat jadi, ditandai nama bloknya. Di atasnya sebutkan: kelas tiket,
arsitektur yang dipilih, register bahasa, dan asumsi yang diambil.

**File HTML** — satu file self-contained.

**Preview** — sesuai Langkah 9.

Tutup dengan tiga baris: bagian mana yang perlu diisi user (`[PERLU DIISI]`), satu elemen yang
paling layak di-A/B test duluan, dan — kalau ada — kelemahan penawaran yang terlihat selama
mengerjakan.
