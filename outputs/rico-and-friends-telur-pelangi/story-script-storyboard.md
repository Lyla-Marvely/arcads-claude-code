# Rico & Friends — "Telur Pelangi" (pack offline)

**Status: persiapan saja. Belum ada gambar atau video yang dibuat. Tidak ada API yang dipanggil.**
Sumber kebenaran: `project.json`. Prompt lengkap: `prompts/prompt-pack.md` dan `prompts/prompts.json`. Bukti gate karakter: `character-gate-report.txt`.

## 1. Karakter (lima karakter resmi, disetujui pemilik)

Semua dari `references/character-library/Rico-and-Friends/` dan lulus `check-character-library.sh` (PASS untuk kelimanya; Pip ditolak karena tidak terdaftar). Pack ini **tidak mengarang atribut visual**: lock hanya memuat yang tertulis atau terlihat di master sheet, sisanya "persis seperti sheet".

| ID | Spesies (menurut sheet) | Ciri khas yang dikunci (menurut sheet) | Sheet referensi |
|----|-------------------------|------------------------------------------|-----------------|
| `Rico-and-Friends:Rico` | bayi dinosaurus fantasi | badan turquoise, perut krem, mata amber, **tiga tonjolan jingga**, 3 jari kaki, ekor pendek melengkung | sheet Rico solo + sheet grup |
| `Rico-and-Friends:Lila` | bayi triceratops | merah muda, tiga tanduk, frill merah muda | sheet grup |
| `Rico-and-Friends:Bimo` | bayi triceratops | kuning, tiga tanduk, frill kuning | sheet grup |
| `Rico-and-Friends:Tika` | bayi brachiosaurus | ungu, leher panjang, motif bintik | sheet grup |
| `Rico-and-Friends:Piko` | bayi pterodactyl | biru, sayap lebar, jambul biru | sheet grup |

Pip dan Moss tidak ada di pack ini. Tidak ada karakter pengganti dan tidak ada karakter baru. Lila, Bimo, dan Tika di sini berbeda dari karakter bernama sama di Arsein-Research.

**Objek cerita:** Telur Pelangi adalah "Objek Utama" pada sheet Rico solo (cangkang pelangi iridescent). Tampilannya tidak diubah dan telur **tidak menetas** (agar tidak lahir karakter baru).

## 2. Ide cerita (dipilih: A)

| | Ide | Inti |
|--|-----|------|
| **A** | **Telur Pelangi** — Rico menemukan Telur Pelangi; sahabatnya datang satu per satu, dan mereka sepakat menjaganya bersama. | persahabatan, menjaga hal berharga |
| B | **Hutan Penuh Bunga** — Piko memandu semua sahabat menemukan bunga paling warna-warni. | kebersamaan, rasa ingin tahu |
| C | **Berlomba ke Batu Berlumut** — para sahabat berlomba lalu memutuskan sampai bersama. | sportivitas |

Dipilih A: satu lokasi, memakai objek resmi dari sheet, memperlihatkan kelima karakter, tanpa perlu menciptakan karakter baru.

## 3. Script (30 detik, VO Bahasa Indonesia)

| Scene | Durasi | Aksi | VO |
|-------|--------|------|----|
| **S01 · Hook** | 10 s | Hutan cerah. Rico mengintip dari balik batu berlumut, melihat Telur Pelangi berkilau di antara bunga, matanya melebar, lalu ia melangkah mendekat dengan penasaran. Sinar matahari menyorot tiga tonjolan jingganya. | "Pagi itu di hutan, Rico menemukan sebuah telur pelangi yang berkilau." (11 kata) |
| **S02 · Berkumpul** | 10 s | Piko meluncur dari atas dan melayang dekat telur. Lila dan Bimo datang dari kiri dan kanan. Leher panjang Tika turun ke dalam frame. Kelimanya berkumpul mengelilingi telur dengan takjub. | "Satu per satu, para sahabat datang. Mereka sepakat, telur ini harus dijaga bersama." (13 kata) |
| **S03 · Resolusi** | 10 s | Kilau pelangi telur makin terang dan menyinari wajah para sahabat. Mereka saling tersenyum; Rico menoleh ke teman-temannya dengan bahagia. Shot menahan di grup (susunan seperti "Pose Grup Referensi" di sheet grup). | "Karena sahabat sejati selalu menjaga hal berharga, bersama-sama." (8 kata) |

VO 8–13 kata per 10 detik, jauh di bawah batas 2,5 kata/detik. Akan ada jeda panjang; opsi: tambah satu kalimat pendek per scene, atau pakai musik/ambient.

## 4. Storyboard

| # | Dur | Karakter | Shot | Kamera | Kilau telur |
|---|-----|----------|------|--------|-------------|
| S01 | 10 s | Rico | wide establishing → medium Rico mengintip dari batu | push-in pelan, tanpa cut | lembut |
| S02 | 10 s | Rico, Piko, Lila, Bimo, Tika | medium-wide di sekitar telur | hampir statis, drift pelan ke kanan | lembut |
| S03 | 10 s | kelimanya | wide, susunan seperti pose grup di sheet | pull-back halus + hold 1 detik | makin terang |

Keluaran: **9:16 dan 16:9**, masing-masing diframing ulang (bukan crop).

## 5. Continuity lock (berlaku semua scene)

1. Semua karakter disalin **persis** dari master sheet: warna, wajah, mata, spike/tanduk/frill/leher/sayap.
2. Rico: badan turquoise, perut krem, mata amber, tiga tonjolan jingga di kepala, tanpa spike lebih atau kurang.
3. Skala relatif seperti perbandingan ukuran di sheet grup: Tika tertinggi, Rico lebih tinggi dari Bimo dan Lila, Bimo ≈ Lila, Piko bertubuh paling kecil dengan sayap lebar.
4. Telur Pelangi: tampilan sama seperti di sheet Rico, ukuran dan posisi sama (di petak bunga di samping batu berlumut), **tidak menetas, retak, atau berubah bentuk**.
5. Hutan yang sama di setiap scene, cahaya emas dari kiri kamera, tanpa perubahan waktu.
6. Hanya lima karakter ini; tidak ada makhluk lain.
7. Satu shot kontinu per klip, tanpa cut.
8. Antar scene: S02 mulai dari posisi telur akhir S01; S03 mulai dari posisi akhir S02.

## 6. Negative prompt

**Gambar:** tidak fotorealistik, bukan live-action, bukan anime, bukan 2D/cel-shaded/ilustrasi datar; tanpa jari berlebih, fitur menyatu/meleleh, properti cacat, karakter tambahan, teks, caption, subtitle, watermark, logo. **Plus:** jangan mendesain ulang karakter mana pun (warna, wajah, mata, spike/tanduk/frill/leher/sayap persis sheet); tidak ada spike atau tanduk lebih/kurang; tidak ada karakter atau bayi dinosaurus baru; telur tidak menetas/retak/berubah; tanpa aksesori tambahan; tanpa logo, lencana, atau teks dari master sheet.

**Video:** tidak live-action/fotorealistik, tidak anime/2D, tanpa karakter tambahan, anggota tubuh tambahan, morphing/meleleh, perubahan kostum/warna, scene cut, lompatan cahaya, teks/caption/watermark. **Plus:** tanpa spike/tanduk lebih atau kurang, tanpa karakter baru, telur tidak menetas.

Arcads tidak punya field `negativePrompt` terpisah; negatif ditulis di dalam teks prompt.

## 7. Rencana referensi (belum dijalankan)

| Scene | Still (gpt-image-2, maks 5) | Klip (Seedance 2.0, maks 3) |
|-------|-----------------------------|-----------------------------|
| S01 | sheet Rico solo | img1 = still S01, img2 = sheet Rico solo |
| S02 | sheet grup, sheet Rico solo, still S01 | img1 = still S02, img2 = sheet grup, img3 = still S01 |
| S03 | sheet grup, sheet Rico solo, still S02 | img1 = still S03, img2 = sheet grup, img3 = still S02 |

Still dibuat per rasio (9:16 dan 16:9) dan klip memakai still dengan rasio yang sama. Path presigned hanya sekali pakai, jadi file diunggah ulang untuk setiap panggilan. Sheet asli tidak pernah dibuat ulang atau diubah.

## 8. Jumlah request jika nanti disetujui (hitungan, bukan biaya)

- Sheet karakter baru: **0** (semua memakai master sheet resmi).
- Still: **6** (3 scene × 2 rasio). Klip: **6**. Total durasi 30 detik per rasio.
- Biaya credit **tidak** dihitung di sini. Konfirmasikan harga di platform Arcads sebelum generasi.
- Prompt Seedance: S01 243 kata, S02/S03 299 kata (lima karakter), sedikit di atas target 260 dari panduan. `reference.md` tidak mencatat batas panjang prompt.

## 9. Hal yang perlu keputusan Anda

1. **Ukuran Rico tidak konsisten antar sheet:** sheet Rico solo menyatakan ±40 cm (telur ±50 cm), sedangkan sheet grup menyatakan Rico ±0,8 m (Tika ±1,1 m, Bimo dan Lila ±0,7 m, Piko ±0,6 m). Pack memakai **urutan relatif** dari sheet grup dan tidak memasukkan angka. Ukuran telur relatif terhadap Rico sengaja tidak dikunci karena kedua sheet bertentangan. Mana yang berlaku?
2. **Lima karakter dalam satu klip 10 detik (S02, S03) berisiko drift.** Jika hasil bermasalah, saya sarankan memecah S02 menjadi dua klip (Piko dan Tika datang, lalu Lila dan Bimo datang). Itu menambah request, jadi tidak saya lakukan tanpa persetujuan.
3. **Telur Pelangi** dipakai sebagai properti dari sheet Rico. Apakah boleh dipakai sebagai pusat cerita?
4. **Lencana "LYLA MARVELY"** ada di sheet grup. Pack melarangnya muncul di hasil.

## 10. Sebelum generasi berbayar

1. `.env` Arcads dan `PRODUCT_ID` (sekarang **BLOCKED**: `.env` tidak ada di sesi ini; `check-requirements.sh` belum bisa memverifikasi autentikasi, akses model, atau saldo).
2. Persetujuan cerita, script, dan storyboard ini.
3. Konfirmasi estimasi credit dan jawaban pertanyaan di atas.
4. Setiap still disetujui sebelum menjadi referensi klip.
