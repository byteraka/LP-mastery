# Desain — supaya tidak terlihat buatan AI

Halaman jualan yang convert di pasar Indonesia **tidak terlihat seperti homepage startup.**
Lebih dekat ke dokumen panjang berisi screenshot asli. Justru kerapian berlebihan yang
bikin halaman terasa dibuat mesin.

Data dari 16 halaman berperforma yang dibedah:

| Elemen | Ditemukan |
|---|---|
| Background putih / netral | 15 dari 16 |
| Satu kolom, mobile-first | 16 dari 16 |
| Sangat panjang (5.000px+) | 12 dari 16 |
| Foto asli (founder, kelas, produk) | 14 dari 16 |
| Screenshot mentah sebagai bukti | 13 dari 16 |
| Gradien / glassmorphism | 1 dari 16 |
| Ilustrasi generik | 0 dari 16 |
| Tiga kartu fitur berikon seragam | 1 dari 16 |

---

## YANG DILARANG — sidik jari desain AI

**Gradien ungu-ke-biru** di hero, tombol, atau teks. Ini penanda paling cepat dikenali.
Satu warna solid selalu lebih baik.

**Glassmorphism** — `backdrop-filter: blur()` pada kartu melayang. Tidak pernah muncul
di halaman jualan yang berperforma.

**Tiga kartu fitur sejajar dengan ikon seragam.** Pola yang paling sering dihasilkan AI dan
paling jarang ada di halaman yang convert. Kalau perlu mendaftar manfaat, pakai daftar
vertikal biasa.

**Ilustrasi vektor generik** (gaya undraw, orang tanpa wajah, bentuk abstrak). Nol dari
16 halaman memakainya. Ganti dengan foto asli atau screenshot.

**Hero rata tengah dengan bentuk abstrak di belakangnya.**

**Teks bergradien.**

**`border-radius` besar di semua elemen plus `box-shadow` tebal di mana-mana.**

**Simetri sempurna.** Semua blok tingginya sama, semua kolom seimbang. Halaman asli punya
ritme yang tidak rata.

**Logo "dipercaya oleh" yang tidak nyata.** Kalau user tidak punya klien itu, jangan pasang.

**Dark mode toggle** yang tidak diminta.

---

## YANG DIPAKAI

### Warna

Satu warna aksen saja. Dipakai untuk tombol, angka harga, dan highlight — tidak untuk
yang lain. Sisanya netral.

```css
:root {
  --bg:        #FFFFFF;   /* atau #FAFAF8 untuk kesan cetak */
  --bg-alt:    #F5F4F1;   /* blok selang-seling */
  --ink:       #1A1A1A;   /* hampir hitam, bukan hitam murni */
  --ink-soft:  #55534F;   /* teks sekunder */
  --line:      #E2E0DC;   /* garis dan border */
  --accent:    #D64200;   /* SATU warna aksen — ganti sesuai brand */
  --accent-dk: #A83400;   /* hover */
  --mark:      #FFE8A3;   /* highlight stabilo */
  --ok:        #1B7F4B;   /* garansi, centang */
}
```

Aksen yang bekerja di pasar Indonesia: oranye-merah, merah, hijau tua, biru tua.
Hindari ungu — terlalu lekat dengan tampilan AI.

### Tipografi

Sans-serif, satu keluarga, dua sampai tiga bobot. Jangan campur dua font display.

```css
font-family: "Inter", -apple-system, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
```

Skala mobile-first. **Ukuran badan teks minimal 17px** — halaman ini dibaca sambil jalan.

| Elemen | Mobile | Desktop |
|---|---|---|
| Headline hero | 30px / 1.15 | 46px / 1.1 |
| Judul blok | 24px / 1.2 | 32px |
| Badan teks | 17px / 1.6 | 18px / 1.65 |
| Teks kecil | 14px | 15px |
| Angka harga | 34px | 44px |

Headline pakai bobot 700–800. Badan teks 400. Jangan menebali seluruh paragraf.

### Lebar dan ruang

Teks maksimal **640px**. Blok bukti dan tabel boleh sampai 860px. Halaman penuh untuk
strip warna.

Jarak antar blok: 56px di mobile, 88px di desktop. Di dalam blok: 20px.
Padding samping mobile: 20px, tidak kurang.

### Gambar

Urutan prioritas: **foto asli > screenshot mentah > mockup > tidak ada gambar sama sekali.**
Ilustrasi generik selalu lebih buruk daripada tidak ada gambar.

Screenshot dipasang dengan border tipis dan radius kecil, bukan melayang di kartu berbayang:

```css
.shot { width:100%; border:1px solid var(--line); border-radius:6px; display:block; }
```

Foto orang tidak dipotong bulat kecil. Foto founder yang besar dan biasa saja lebih
dipercaya daripada headshot bulat 64px.

Kalau aset belum ada, pasang placeholder yang **menyebut persis apa yang harus diisi**:

```html
<div class="ph">[PERLU DIISI: screenshot chat WhatsApp dari 3 alumni, tanpa nama]</div>
```

Jangan pakai gambar dummy dari internet.

### Highlight stabilo

Ciri khas halaman jualan Indonesia yang asli. Pakai untuk 3–5 frasa kunci di seluruh
halaman, tidak lebih.

```css
mark { background: var(--mark); padding:0 2px; border-radius:2px; }
```

### Tombol

Satu bentuk tombol untuk seluruh halaman. Besar, kontras tinggi, teks kalimat orang pertama.

```css
.cta {
  display:block; width:100%; max-width:440px; margin:24px auto;
  padding:18px 24px; background:var(--accent); color:#fff;
  font-size:18px; font-weight:700; text-align:center;
  border:0; border-radius:8px; text-decoration:none;
  box-shadow:0 2px 0 var(--accent-dk);
}
```

Tanpa gradien, tanpa bayangan tebal, tanpa animasi berdenyut.

**Sticky CTA di mobile** muncul setelah hero lewat:

```css
.sticky { position:fixed; left:0; right:0; bottom:0; padding:10px 16px;
          background:rgba(255,255,255,.96); border-top:1px solid var(--line); z-index:50; }
@media (min-width:768px){ .sticky{ display:none; } }
```

### Blok harga

Blok paling menonjol di halaman. Harga coret kecil dan abu, harga akhir besar dan berwarna
aksen. Beri border tegas, bukan bayangan.

```css
.harga-box { border:2px solid var(--ink); border-radius:10px; padding:28px 20px; }
.harga-coret { font-size:18px; color:var(--ink-soft); text-decoration:line-through; }
.harga-final { font-size:40px; font-weight:800; color:var(--accent); line-height:1.1; }
```

### Daftar

Daftar vertikal dengan penanda konsisten. Satu simbol untuk seluruh halaman, bukan emoji
berbeda tiap baris.

Register A: tanda centang sederhana.
Register B: ✅ pada setiap baris adalah konvensi pasar dan boleh dipakai penuh.

### Blok selang-seling

Beri latar `--bg-alt` pada blok tertentu supaya halaman panjang tetap terbaca dan pembaca
tahu di mana dia. Jangan lebih dari tiga blok berlatar di seluruh halaman.

---

## MOBILE

Lebih dari 90% traffic Meta Ads di Indonesia dari HP. Desain untuk HP dulu,
desktop cuma pelebaran.

- Satu kolom selalu. Tidak ada grid dua kolom di bawah 768px.
- Target sentuh minimal 44px.
- Tidak ada scroll horizontal. Cek tabel dan kode — bungkus dengan `overflow-x:auto`.
- Form: `inputmode="numeric"` untuk nomor, `type="tel"` untuk WhatsApp.
- Sticky CTA di bawah.
- Tes lebar 360px sebelum kirim.

---

## KECEPATAN

Halaman yang lambat membakar budget iklan sebelum orang sempat membaca. Kalau
landing page view jauh lebih kecil dari link click, itu kebocoran teknis, bukan masalah copy.

- Satu file HTML, CSS inline di `<style>`, JS inline dan seminimal mungkin.
- Tanpa framework, tanpa jQuery, tanpa library animasi.
- Font: pakai font sistem kalau bisa. Kalau memakai webfont, maksimal dua bobot
  dan `font-display:swap`.
- Gambar `loading="lazy"` kecuali gambar hero.
- Tanpa library carousel — pakai `scroll-snap` CSS.
- Countdown ditulis dengan JS polos, maksimal 15 baris.

---

## STRUKTUR FILE

Satu file HTML self-contained:

```
<style> ... </style>          token + komponen, inline
<body>
  <section class="hero"> ... </section>
  <section> ... </section>     satu section per blok, diberi komentar nama bloknya
  <div class="sticky"> ... </div>
</body>
<script> ... </script>        countdown + smooth scroll saja
```

Beri komentar HTML di atas tiap section dengan nama bloknya, supaya user gampang
mengedit sendiri:

```html
<!-- ===== BLOK 3: BIAYA MASALAH ===== -->
```

Sertakan di paling atas file satu blok komentar berisi daftar semua `[PERLU DIISI]`
yang ada di halaman, supaya user tinggal menyisir.
