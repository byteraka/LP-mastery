# Bedah 22 Halaman Referensi

Catatan per halaman, lengkap dengan token desain yang diambil langsung dari halamannya
(bukan dikira-kira). Ini bukti yang mendasari `gaya-desain.md`.

**Kapan buka file ini:** saat user menyebut salah satu halaman ini sebagai acuan
("bikin seperti jastip", "mirip lp-mastery"), atau saat butuh detail lebih dalam dari
satu gaya daripada yang muat di `gaya-desain.md`.

Satu halaman tidak dibuka: `fasttrackmarketer.com` — aksesnya ditolak di tingkat robots.

---

# jastip.id/seminar/bali — seminar Rp97rb (kelas C)

## Yang mengejutkan
Background **GELAP**, bukan putih. Temuan lamaku "15 dari 16 putih" ternyata salah baca —
yang aku hitung waktu itu deskripsi teks, bukan tampilannya.

## Token desain (diambil langsung dari halaman)
- Latar utama: `rgb(21,19,22)` hampir hitam · latar alternatif `rgb(250,249,245)` krem, bukan putih murni
- Aksen tunggal: `rgb(255,214,0)` kuning terang
- H1: font **Anton**, 54px, weight 400, line-height 54px (= 1.0, sangat rapat), HURUF KAPITAL SEMUA, rata kiri, putih
- Body: Plus Jakarta Sans 16.5px
- Tombol: bg kuning, teks hampir hitam, radius **4px** (kecil), padding 16px 26px, 15px/700
- Bayangan tombol: `5.11px 5.11px 0px` — **offset keras tanpa blur**, gaya neo-brutalist. Bukan bayangan lembut.
- Tinggi halaman 12.691px · 14 section · 0 gambar >140px · 0 video

## Pola visual
- Hero: teks kapital besar rata kiri + foto orang di kanan dengan badge angka melayang di atasnya
- Blok statistik: empat angka raksasa berwarna kuning ("6,95 JT", "1,63 JT", "$565 JT", "-10,65%")
  dengan keterangan kecil di bawahnya. Ini pengisi visual yang dibuat dari ANGKA, bukan gambar.
- Testimoni: kartu putih berderet di atas latar gelap, ada nama + peran di bawah kutipan
- Eyebrow kecil berwarna aksen di atas tiap judul section

## Pelajaran untuk skill
1. Kontras tinggi (gelap + satu aksen terang) terasa jauh lebih "jadi" daripada putih polos
2. Font display kondensasi kapital untuk H1 memberi karakter tanpa perlu gambar
3. Line-height 1.0 pada headline besar = padat, bertenaga
4. Bayangan offset keras, bukan blur lembut
5. Radius kecil (4px), bukan 8-16px
6. **Blok angka besar adalah pengganti gambar yang sah** — ini jawaban untuk masalah "belum ada aset"
# produk.karyawan.ai/lp-mastery — kelas offline Rp1jt (kelas C)

## Yang paling penting: NOL GAMBAR, tapi tidak terasa kosong
`imgs: 0`. Tidak ada satu pun foto. Tapi halamannya penuh. Ini bukti langsung bahwa
masalah halaman yang aku bikin bukan "belum ada aset", tapi cara mengisi ruangnya.

## Token desain
- Latar: `rgb(10,10,10)` hampir hitam · kartu/section: `rgb(26,26,26)`
- Teks: `rgb(245,245,243)` putih tulang
- Aksen: `rgb(239,193,77)` emas — dipakai penuh untuk teks, dan sebagai **tint transparan**
  `rgba(239,193,77,0.06)` dan `0.12` untuk latar kartu
- H1: system font, 50px, weight **800**, line-height 60px (1.2), rata kiri
- Tombol: latar `rgb(21,17,2)` gelap, teks emas muda `rgb(245,212,127)`,
  **radius 999px (pil penuh)**, bayangan lembut `0 10px 30px rgba(0,0,0,.3)`, 15.5px/800
- Tinggi 9.123px · 13 section

## Cara mengisi ruang tanpa foto
1. **Kata disorot warna aksen di dalam headline** — "Programmer" dan "Sehari" berwarna emas,
   sisanya putih. Satu trik ini saja sudah bikin hero tidak datar.
2. **Kartu mock UI sebagai visual hero** — panel gelap berisi baris ketikan gaya terminal
   dengan teks emas. Dibuat dari teks dan CSS, bukan gambar.
3. **Grid kartu 2x2** untuk blok masalah — tiap kartu: ikon kecil emas, judul, body pendek
4. **Pil eyebrow** di atas headline: "HANYA 20 KURSI · FATMAWATI, JAKARTA SELATAN"
5. Kontras halus antar lapisan: kartu `#1a1a1a` di atas latar `#0a0a0a` — beda tipis
   tapi cukup memisahkan

## Bandingkan dengan yang aku bikin kemarin
Aku: putih, Inter, oranye, radius 8px, bayangan lembut, kotak putus-putus di hero.
Dia: hampir hitam, weight 800, emas, radius pil, kartu mock, nol gambar.
Bukan soal "aturan desainku salah" — aturanku cuma daftar larangan, jadi hasilnya netral
dan hambar. Halaman ini punya sikap.
# conversionclub.id/meta-framework-aa — framework Rp199rb (kelas A)

Gaya yang sama sekali berbeda dari dua sebelumnya: **direct response klasik.**

## Token desain
- Latar: `rgb(249,246,244)` putih hangat, bukan putih murni
- Teks: `rgb(49,55,61)` abu kebiruan gelap, bukan hitam
- Font: Helvetica Neue. Body cuma **14px** — kecil, gaya dokumen lama
- H1: 35px, weight 700, **rata TENGAH**, line-height 49px (1.4 — longgar)
- Aksen: biru `rgb(21,101,192)` untuk link, dan **stabilo kuning pada kata di headline**
- Tinggi 11.106px · **0 section** (layout berbasis div/tabel, bukan semantic) · **19 gambar**
- Tidak ada tombol ber-style terdeteksi — CTA-nya berupa gambar atau link

## Ciri khas gaya ini
1. **Stabilo kuning pada frasa kunci di headline** — bukan bold, tapi highlight
2. **Screenshot mentah apa adanya**: dashboard iklan, chat WhatsApp, postingan Instagram,
   invoice. Tidak dibingkai, tidak dikasih bayangan, tidak dirapikan. Justru itu kekuatannya.
3. **Label bergaris bawah miring**: "Pengguna 2:", "Pengguna 3:" — seperti catatan tulisan tangan
4. Rata tengah untuk headline, rata kiri untuk body
5. Angka disensor sebagian (blur merah muda) — menambah kesan bukti asli

## Kenapa ini bekerja padahal "jelek" secara desain
Tampilannya sengaja tidak dipoles. Halaman yang terlalu rapi terbaca seperti iklan;
halaman ini terbaca seperti orang yang menunjukkan hasilnya sendiri. Untuk produk
tiket rendah dari pengiklan perorangan, itu justru yang dipercaya.

**Jangan dipakai untuk:** brand mapan, produk high-ticket, atau audiens korporat.
# acquisition.com/workshop-sales — workshop $5.000 (kelas E)

## Token desain
- Latar: putih murni · teks `rgb(51,51,51)` · body font **Arial 14px**
- H1: **Poppins**, 34px, weight 800, line-height 40.8px (1.2), **rata tengah**,
  warna `rgb(19,22,40)` biru-navy hampir hitam (bukan hitam)
- Aksen CTA: ungu terang `rgb(111,0,255)`
- Radius tombol: ~4px (kecil) · tanpa bayangan
- Tinggi 11.454px · 13 section · 7 gambar · 1 video

## Ciri khas
1. **Strip pengumuman hitam di paling atas**: "TWO-DAY LIVE SALES WORKSHOP · NOV AND DEC
   SOLD OUT, JAN 28-30 NOW OPEN" — kelangkaan disebut sebelum orang melihat apa pun
2. **Angka besar sebagai penanda section**: "02 HOW YOU TRAIN THEM", "03 HOW YOU MANAGE THEM"
3. **Fotografi acara asli** — peserta duduk di meja, pencahayaan ungu, suasana ruangan.
   Bukan foto stok, bukan mockup.
4. **Video testimoni berjajar** dengan tombol play bundar di tengah
5. Headline **34px saja** — jauh lebih kecil dari halaman tiket rendah. Tenang, tidak berteriak.
6. Tanpa emoji, tanpa countdown, tanpa harga coret

## Pelajaran
Halaman tiket tinggi justru **mengecilkan volume visualnya**. Headline lebih kecil,
warna lebih sedikit, tidak ada hiasan. Yang mengangkat halaman ini adalah kualitas
fotografinya dan ketenangan nadanya — dua hal yang tidak bisa ditiru dengan CSS.

**Catatan:** banner cookie menutupi sebagian tampilan. Aku tidak menutupnya karena itu
persetujuan atas nama user.
# fortiscircle.id/saham — webinar saham Rp899rb–1,299jt (kelas C)

## Token desain
- Latar: `lab(1.5609 0 0)` hampir hitam pekat
- Teks: putih, body font **Lato** 16px
- H1: font **Onest**, 36px, weight **900**, line-height 39.6px (1.1), rata tengah, KAPITAL
- Tombol: **latar putih, teks hitam** — kebalikan dari yang lain. Weight 800, 14px,
  padding **26px 32px** (sangat tebal), radius pil penuh, tanpa bayangan
- Tint aksen kehijauan pada opacity 0.05 dan 0.1 untuk latar kartu
- Tombol WhatsApp melayang hijau di kanan bawah
- Tinggi **14.620px** — terpanjang sejauh ini · 13 section · 9 gambar

## Catatan
Screenshot banyak yang hitam karena kontennya dimuat saat scroll dan belum sempat render
di panel. Data token di atas diambil langsung dari halaman jadi tetap akurat.

## Yang dipinjam
- **CTA putih di atas latar gelap** — kontras maksimum, dan terasa lebih mahal daripada
  tombol berwarna terang
- Padding tombol yang sangat tebal (26px atas-bawah) bikin tombol terasa berbobot
- Tombol WhatsApp melayang: konvensi pasar Indonesia untuk tiket menengah ke atas
# nrhouse.id/dpp — ebook playbook Rp149rb (kelas A)

Gaya kelima: **hangat editorial**. Satu-satunya yang pakai serif, dan satu-satunya
yang tidak memakai hitam sama sekali.

## Token desain
- Latar: `rgb(253,246,238)` krem hangat · kartu `rgba(255,250,244,0.62)`
- Teks: `rgb(58,42,34)` **cokelat tua, bukan hitam** — ini yang bikin terasa lembut
- H1: font **Fraunces** (serif display), 32px, weight 600, line-height 35.2px (1.1),
  rata tengah
- Frasa kunci di headline dibuat **serif miring berwarna terakota** ("Produk Digital?")
- Aksen 1: terakota `rgba(217,122,108, .14)` untuk tint kartu
- Aksen 2: sage hijau `rgba(122,140,90, .14)` — dua aksen, bukan satu
- Body: Inter 16px
- Tinggi 7.840px — **terpendek dari semua** · 7 section · 4 gambar

## Cara mengisi ruang tanpa foto besar
1. **Pil eyebrow** di atas headline: "PANDUAN UTAMA + VIDEO EKSKLUSIF + AKSES TOOLS"
2. **Trio kartu angka**: "16 Bab Lengkap · 90+ Sub-Bab Praktis · 30 Hari Action Plan"
   — angkanya besar dan berserif, keterangannya kecil
3. **Daftar manfaat dengan chip ikon bulat bertint** (🎯 ⚡ 💰) di sebelah kiri tiap baris
4. Kontras dibuat dari suhu warna, bukan dari gelap-terang

## Kapan dipakai
Produk untuk perempuan, parenting, wellness, kreatif, self-improvement, ebook lifestyle.
Terasa personal dan tidak agresif. **Jangan** untuk produk finansial, B2B, atau apa pun
yang butuh kesan otoritas teknis — di situ serif hangat terbaca lemah.
# konvert.id — SaaS langganan Rp48rb–258rb/bln

Gaya keenam: **SaaS gelap bergradien**. Satu-satunya produk langganan di daftar referensi.

## Token desain
- Latar: `rgb(0,3,20)` navy sangat gelap, dengan glow gradien biru-oranye di belakang hero
- H1: Plus Jakarta Sans 38px weight 800, rata tengah, line-height 41px (1.08)
- **Headline tiga warna per baris**: baris 1 putih, baris 2 oranye, baris 3 biru.
  Bukan cuma satu kata disorot — tiap baris punya warnanya sendiri.
- Aksen 1 (CTA utama): oranye `rgb(245,122,0)` · Aksen 2: biru `rgb(61,144,247)`
- Tombol sekunder: ghost `rgba(255,255,255,0.04)` dengan border tipis
- Radius **12px** (menengah, bukan 4px bukan pil)
- Tinggi **20.604px** — terpanjang dari semua · 15 section · 13 gambar

## Ciri khas
1. **Pil eyebrow berdot** di atas headline: "● AI-Powered Landing Page Builder"
2. **Baris chip kepercayaan** tepat di bawah CTA: "✓ Mulai gratis ✓ Tanpa kartu kredit
   ✓ Live dalam 1 menit" — menghapus tiga keberatan dalam satu baris
3. Dua tombol berdampingan: satu solid (aksi utama), satu ghost (Lihat Demo)
4. **Screenshot dashboard produk** sebagai visual hero, dimiringkan sedikit
5. Glow gradien di belakang hero untuk kedalaman

## Kapan dipakai
Produk software, tools, langganan, apa pun yang punya tampilan antarmuka untuk dipamerkan.
Butuh screenshot produk yang bagus — tanpa itu gaya ini kosong.
# learn.klinikmarketing.id/was-ig — shortcut Rp247rb (kelas A)

Varian dari gaya direct response, dengan tiga ciri tambahan yang khas pasar Indonesia.

## Token desain
- **Bingkai hijau tua** `rgb(3,104,84)` di kiri-kanan, konten putih di tengah —
  efek "halaman di dalam bingkai", bukan full-width
- Teks `rgb(51,51,51)` · ui-sans-serif 16px
- CTA: **merah `rgb(223,14,3)`**, teks putih, 18px weight 500, radius 4px,
  padding cuma 8px (tombol tipis, tidak tebal)
- **Stabilo hijau-neon menyala** pada judul section ("Tutorial Eksklusif - Winning Ads Shortcut -")
- Screenshot dashboard iklan mentah sebagai bukti, tanpa dibingkai
- Tinggi 6.888px · 0 section · 4 gambar · **tidak ada elemen h1 sama sekali**

## Catatan
HTML-nya tidak rapi (tanpa h1, tanpa section). Ini dibuat dengan page builder.
Bukan masalah untuk konversi, tapi jangan ditiru strukturnya — cuma gayanya.

## Yang dipinjam
- Bingkai warna di kiri-kanan sebagai pembatas kolom konten
- Stabilo neon untuk judul section, bukan cuma di headline utama
- CTA merah: agresif, cocok untuk tiket rendah, terlalu keras untuk tiket tinggi
# learn.klinikmarketing.id/ecourse-s1jt-ig — ecourse (kelas A)

Varian penting: **halaman berbasis banner gambar**, bukan teks HTML.

## Token
- Body: Source Sans Pro 16px, teks `rgb(51,51,51)` — tapi tampilan sebenarnya GELAP
  karena tiap section punya latar sendiri dan hero-nya berupa gambar banner
- CTA: merah `rgb(223,14,3)`, 18px/500, radius 4px, padding 8px — sama persis dengan
  halaman klinikmarketing yang lain (konsisten antar halaman mereka)
- Latar section: `rgb(246,249,252)` biru sangat muda, dan hijau tua `rgb(25,84,71)`
- Tinggi **4.739px** — terpendek dari semua referensi · 3 gambar

## Yang baru dan belum tertangkap gaya lain
1. **Hero berupa banner gambar desain** (gaya Canva/Photoshop), bukan teks HTML.
   Headline "SPENDING GEDE BUKAN SOAL NYALI, TAPI SOAL NGERTI." ada di dalam gambar.
   Konsekuensinya: tidak bisa di-A/B test cepat, tidak bisa diseleksi, buruk untuk SEO —
   tapi kontrol visualnya penuh dan cepat dibuat.
2. **Kartu keberatan dengan ikon tanda tanya**: latar hijau tua, pertanyaan berwarna merah
   muda, jawaban putih, ikon "?" besar di pojok kanan. Bentuk FAQ yang tidak terlihat
   seperti FAQ.
3. **Kartu kredensial pembicara** dengan foto bulat + nama + jabatan + daftar centang
   sertifikasi di bawahnya
4. Highlight kuning-hijau menyala pada teks di atas latar gelap

## Catatan
Pola "hero berupa banner gambar" ini umum di pasar Indonesia karena dibuat dengan page
builder. Skill tidak meniru ini — kita menulis HTML supaya bisa direvisi dan dites —
tapi komposisi banner-nya layak ditiru: kapital tebal, tiga baris, satu baris berwarna aksen.
# lp.consulting.com/pr — Side Hustle Challenge $145–245 (kelas A/B internasional)

Varian dari Gelap Premium dengan aksen **neon** dan bar countdown menempel di atas.

## Token
- Latar: `rgb(0,10,0)` hitam bersemburat hijau · kartu `rgb(27,29,35)`
- H1: font **Sora** 36px weight 700, rata tengah, putih —
  dengan "$2,000 Online" berwarna **kuning-hijau neon**
- Subhead **miring** dalam kurung: "(Without Investing Thousands To Get Started)"
- CTA: pil neon `radius 800px`, teks hitam
- 38 gambar · tinggi 12.673px

## Yang baru
1. **Bar sticky di paling atas** berisi countdown + tombol CTA:
   "PRICE GOES UP IN: 00D 23H 18M 04S" — kelangkaan selalu terlihat, tidak perlu scroll
2. **Aksen neon** (kuning-hijau menyala) di atas latar hitam — lebih agresif dari emas,
   cocok untuk audiens muda dan tawaran bertenggat
3. Video dengan caption tertanam di atas frame-nya
4. Tombol WhatsApp melayang — bahkan di halaman berbahasa Inggris

## Dipakai untuk
Tawaran bertenggat dengan harga naik bertahap. Bar countdown atas + aksen neon
bekerja sama: dua-duanya bilang "ini akan habis".
# Sisa 14 halaman — temuan tambahan

## akademimarketer.com (dark, kelas C/D)
- Latar `rgb(18,18,18)` · Inter · CTA **biru `rgb(36,99,235)`** radius 12px, 18px/600
- Headline multi-warna per frasa: biru / putih / kuning dalam satu kalimat
- **Kolase foto member mengelilingi video hero, dengan angka omzet melayang**
  di samping tiap wajah (Rp50.000.000+ · Rp500.000.000+ · Rp70.000.000+)
- 5 video · 9 gambar · 17.205px

## page.karyawan.ai/all-in-one (TERANG brutalist)
- Latar **krem `rgb(255,254,242)`** · teks `rgb(15,15,15)`
- H1 **Bebas Neue** 42px weight 400, KAPITAL, rata kiri, line-height 44px
- Aksen kuning `rgb(255,214,0)` — sama persis dengan jastip
- **Kotak highlight berborder tegas** mengelilingi satu kata ("MARKETING"),
  latar kuning, border hitam
- Baris chip: "⚙ Tanpa coding · ⛔ Tanpa skill teknis · 📈 Step-by-step dari nol"
- Tombol kuning radius 10–12px weight 800 · 63 gambar · 12.443px

## page.karyawan.ai/join (terang brutalist, varian)
- Latar `rgb(250,250,247)` · H1 **Sora** 30px weight 800 KAPITAL
- Tombol kuning `rgb(255,214,10)` radius 9999px (pil)
- **Mockup HP** sebagai visual hero, dengan **badge harga melekat di pojoknya**:
  "Rp 100.000 EARLY BIRD"
- **Bar sticky bawah berisi harga**: "Daftar Webinar — Rp 100.000 →"
- Pil eyebrow: "⚡ WEBINAR PRAKTEK AI PEMULA" · 31 gambar · 11.691px

## produk.karyawan.ai/kai-bali-page (terang)
- Putih · Inter 17px · H1 **Poppins** 32px weight 700 rata kiri
- Tombol kuning radius 999px
- **Foto acara asli** (kerumunan peserta berkaos kuning) dengan
  **badge harga menempel di pojok foto**: "Rp197.000 EARLY BIRD"
- Bar sticky bawah dengan harga · 10 gambar · 1 video · 16.972px

## masterclass-playmakers.com/masterclass04 (terang editorial)
- **Lingkaran gambar tangan berwarna hijau melingkari satu kata di headline** ("Bongkar")
- Kata-kata berwarna di dalam headline (kuning, hijau)
- Kata bergaris bawah di body: "mandek", "boncos"
- Baris logo klien (Brighty, Ciara, Jiera, Herbi Kids)
- Kartu pemateri dengan foto potongan + jabatan
- Tombol CTA gelap

## masterclass-playmakers.com/masterclass02-order
- H1 font **heebo-medium** 50px weight 400
- Blok latar **biru pekat** dengan foto pemateri dipotong (cut-out) di atasnya
- Baris logo klien · 6 gambar · 7.214px

## acquisition.com/roadmap + /fivescalingframeworks (lead magnet)
- **Sangat pendek: 2.490px dan 2.423px** — bandingkan halaman jualannya 11.000px+.
  Ini konfirmasi kuat: halaman lead magnet memang pendek.
- H1 Poppins **53px** weight 700 rata tengah, hitam di atas putih
- Bar pengumuman ungu di paling atas: "NEW · 2026 Scaling Workshop Dates Announced"
- Blok hero ungu dengan badge "Best for" + teks "BUSINESS OWNERS ONLY" kapital besar
  dan foto orang dipotong
- **CTA kuning gemuk**: `rgb(246,210,52)`, radius 50px, 20px/900, padding 25px 10px
  — aksen berbeda dari halaman jualannya yang ungu
- Form berupa **checkbox kuis**, bukan isian

## acquisition.com/workshop-marketing + /workshop-4b
- Poppins 30–32px weight 700–800 rata tengah, KAPITAL
- 5 video di workshop-4b · 8.557px dan 11.043px
- Design system identik dengan workshop-sales — konfirmasi bahwa keempatnya satu sistem

## learn.klinikmarketing.id/crh25-ig
- Sistem sama dengan dua halaman klinikmarketing lain: CTA merah `rgb(223,14,3)` radius 4px
- **Headline berupa kutipan dalam tanda kutip**: "Percuma aja retargeting dan remarketing
  Meta CPAS kalau hasilnya masih stuck gini..."
- Kalimat pembuka berwarna merah: "Eits.. jangan salahin iklannya"
- Label "From this ⬇" di atas screenshot dashboard mentah
- 5.967px

## edutify.lynk.id
Halaman marketplace lynk.id, isinya dimuat lewat iframe dan tidak ter-render.
CTA merah `rgb(178,31,31)`. Tidak ada identitas desain sendiri — dilewati.

## fasttrackmarketer.com
**Tidak dibuka.** Aksesnya ditolak di tingkat robots waktu percobaan pertama,
jadi aku tidak menembusnya lewat jalan lain.
