# Jualan ID — plugin Claude untuk landing page & Meta Ads

Skill untuk bikin halaman penjualan dan materi iklan yang tinggi konversi di pasar Indonesia.
Gratis, boleh dipakai siapa saja.

## Cara install

Di Claude Code, jalankan dua perintah ini:

```
/plugin marketplace add GANTI-USERNAME/claude-plugins-jualan
/plugin install funnel-jualan@jualan-id
```

Di aplikasi Claude desktop, pakai plugin browser-nya.

**Supaya dapat update otomatis**, nyalakan sekali: `/plugin` → tab **Marketplaces** →
pilih `jualan-id` → **Enable auto-update**. Kalau tidak dinyalakan, kamu tetap bisa
update manual kapan saja dengan `/plugin update funnel-jualan@jualan-id`.

## Isinya

**`landing-page-jualan`** — bikin halaman penjualan yang convert. Menghasilkan naskah per blok
plus satu file HTML self-contained yang siap dipublish. Untuk produk edukasi (ebook, ecourse,
webinar, seminar, workshop), produk digital, produk fisik, jasa, dari tiket rendah sampai tinggi.

**`meta-ads-creative`** — bikin iklannya: konstruksi offer, hook, ad copy, dan brief creative
video maupun statis.

Dipakai berpasangan: skill iklan menentukan hook, skill landing page memastikan hook itu
muncul lagi di halaman dengan kata yang mirip.

## Cara pakai

Minta dengan bahasa biasa. Skill-nya aktif sendiri.

```
Bikinin landing page untuk ebook parenting harga 79rb, target ibu muda,
traffic dari Meta Ads
```

```
Halaman pendaftaran webinar gratis tentang meta ads buat pemula
```

```
LP untuk workshop offline 15 juta, buat pemilik bisnis yang omzetnya udah 1M ke atas
```

```
Konversi halaman ini rendah, tolong perbaiki
```

Tiga hal ini wajib disebut karena menentukan seluruh bentuk halaman:
**produk, harga, dan siapa pembelinya.**

Sangat membantu kalau ada: kalimat asli pembeli (chat CS, komentar iklan, testimoni mentah),
angka hasil yang bisa dipakai sebagai bukti, dan aset visual. Kalau bahan bukti belum ada,
halaman tetap dibuat tapi bagian kosong ditandai `[PERLU DIISI]` — tidak dikarang.

## Dasar isinya

Bukan teori umum. Disusun dari pembedahan 16 landing page yang sedang jalan di pasar —
Indonesia dan benchmark high-ticket internasional — plus sekitar 80 ad copy aktif dari
Meta Ad Library.

Tiga prinsip yang lahir dari data itu:

**Harga menentukan bentuk halaman, bukan jenis produknya.** Ebook Rp79rb dan workshop
Rp15jt butuh halaman yang berbeda secara mendasar. Makin tinggi harga, makin kecil diskon
dan makin banyak diskualifikasi.

**Copy emosional dikutip, bukan dikarang.** Ada daftar larangan frasa yang konkret dan
skrip audit yang dijalankan sebelum output dikirim, supaya hasilnya tidak terdengar
seperti brosur atau tulisan AI.

**Halaman yang convert tidak terlihat seperti homepage startup.** Dari 16 halaman yang
dibedah: nol memakai ilustrasi generik, satu memakai gradien, tiga belas memakai
screenshot mentah sebagai bukti.

## Buat yang mau ikut mengembangkan

Struktur repo:

```
.claude-plugin/marketplace.json     katalog marketplace
plugins/funnel-jualan/              plugin-nya
rilis.sh                            naikkan versi + catat changelog
```

Kalau punya data konversi nyata dari landing page sendiri, kirim lewat issue.
Skill ini akan jauh lebih kuat kalau polanya bisa divalidasi dengan angka, bukan cuma
dengan fakta bahwa iklannya jalan lama.

## Lisensi

MIT. Pakai, ubah, jual hasilnya — bebas.
