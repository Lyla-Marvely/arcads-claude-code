# Character Library — panduan penggunaan master karakter

Panduan ini berlaku untuk **setiap skill dan sesi** yang membuat gambar, video, storyboard, atau prompt yang memuat karakter proyek LYLA. Ini mencakup `pixar-animation-video`, `pixar-style-ad`, `claymation-ad`, `gemini-omni-flash`, `caption-video`, `generate-youtube-thumbnail`, dan skill image-ad.

Status: 14 master sheet dan 2 logo Arsein sudah terdaftar. **Disetujui pemilik:** Rico, Lila, Bimo, Tika, Piko; Fasha, Kania; dan Maya tanpa pita (kanonik). **Lainnya `identified`, termasuk kedua logo.** Sebelum sebuah karakter dipakai, cek `library.json` atau jalankan skrip pemeriksa.

## 0. Keputusan pemilik dan routing proyek

Ringkasan keputusan final ada di [README.md](README.md#keputusan-pemilik-2026-11-17) dan `owner_decisions` di `library.json`.

| Jika kontennya… | Gunakan folder |
|-----------------|----------------|
| LYLA Marvely, konten brand LYLA umum | `LYLA/` |
| pendidikan, maskot edukasi (Lyla "Maskot LYLA Education", Lilo), worksheet, serial edukasi, perilaku anak/parenting (Aisyah, Mama Aisyah, Fasha, Kania) | `LYLA-Education/` |
| Rico & Friends | `Rico-and-Friends/` |
| The Last Letter dan LYLA Anime Universe | `The-Last-Letter/` dan `LYLA-Anime-Universe/` (satu universe, lihat 2c) |
| Zeno Family / Arsein Research | folder dengan nama yang sama |

Aturan khusus:
- **LYLA ≠ LYLA-Education.** Fasha dan Kania hanya di LYLA-Education; dilarang di LYLA umum (`forbidden_characters`, dicek skrip).
- **Rico & Friends:** resmi hanya Rico, Lila, Bimo, Tika, Piko. Pip dan Moss bukan karakter resmi, tidak boleh dipakai, tanpa karakter pengganti. Ejaan **Rico**.
- `official_characters` di `library.json` adalah deklarasi pemilik; atribut visual hanya dari sheet yang disetujui.
- `planned_sheets` adalah rencana awal, bukan bukti ketersediaan.

## 1. Status dan persetujuan

| Status aset | Arti | Boleh dipakai untuk |
|-------------|------|---------------------|
| *(tidak terdaftar)* | file belum ada di repo | tidak ada, jangan klaim tersedia |
| `uploaded` / `identified` | ada dan diidentifikasi, **belum disetujui pemilik** | diskusi dan draf offline berlabel "UNAPPROVED" |
| `partially_approved` | hanya karakter bertanda `approved` di `characters_status` yang resmi | hanya karakter yang disetujui |
| `approved` | seluruh karakter di sheet disetujui pemilik | semua pekerjaan, termasuk generasi berbayar |
| `deprecated` | digantikan versi baru | tidak boleh dipakai |

**Persetujuan bersifat per karakter** (`characters_status`), karena satu sheet bisa memuat banyak karakter. Contoh: sheet "Maya & Ren" `partially_approved`: Maya disetujui, Ren belum.

**Hanya pemilik yang menyetujui.** Agent tidak pernah menyetujui sendiri, dan tidak menganggap penetapan tipe (misalnya "logo utama") atau penempatan folder sebagai persetujuan. Setiap persetujuan mencatat `approved_by`, `approved_at`, dan `approval_basis` (kutipan keputusan pemilik).

Persetujuan yang tercatat saat ini:

| Aset | Disetujui | Dasar |
|------|-----------|-------|
| Rico & Friends: sheet grup dan Rico solo | Rico, Lila, Bimo, Tika, Piko | pemilik menetapkan kelimanya sebagai karakter resmi |
| LYLA-Education: sheet Fasha & Kania | Fasha, Kania | keputusan final 4 |
| The-Last-Letter: sheet Maya & Ren, Full Cast | Maya (tanpa pita) | keputusan final 2; diverifikasi visual |

Menunggu persetujuan: Lyla, Lilo, Aisyah, Mama Aisyah, seluruh Zeno Family, Arsein (Lila, Raka, Naya, Bimo, Tika), Ren dan karakter lain The Last Letter, Lady Aradena, serta **kedua logo Arsein**.

## 2. Aturan wajib untuk semua skill

1. **Cocokkan proyek.** Tentukan proyek dari permintaan (mis. "Rico & Friends" → `Rico-and-Friends/`). Jika ambigu, tanyakan; jangan menebak.
2. **Cek registri sebelum generasi.** Jalankan `./scripts/check-character-library.sh <Folder>`. Exit ≠ 0 berarti tidak ada master sheet `approved` → **berhenti sebelum langkah berbayar**. Prompt dan script offline boleh dibuat, dengan label "karakter belum terverifikasi terhadap master sheet".
3. **Lampirkan master sheet sebagai gambar referensi** di setiap panggilan gambar/video yang memuat karakter itu. Pada Arcads: `referenceImages` (gpt-image-2 maks 5, nano-banana-2 maks 14, Seedance 2.0 maks 3). Path presigned hanya sekali pakai, jadi unggah ulang untuk setiap panggilan.
4. **Jangan pernah membuat atau mengubah desain.** Dilarang: mengarang warna, spesies, pakaian, aksesori, proporsi, atau ciri yang tidak tertulis/terlihat di sheet; menyederhanakan atau "memperbaiki" desain. Lock teks ditulis sebagai *"salin persis dari master sheet"* ditambah fakta yang terbaca dari sheet. Yang tidak diketahui ditulis "per master sheet", bukan ditebak.
5. **Jangan campur proyek.** Karakter dari proyek lain tidak boleh muncul kecuali pemilik meminta crossover secara eksplisit dan kedua sheet berstatus `approved`.
6. **Karakter baru = *proposed*.** Teman, figuran, atau hewan yang dibuat untuk sebuah cerita bukan karakter resmi. Tandai "PROPOSED — needs approval" di semua dokumen. Jangan membuatnya jika sheet resmi untuk peran itu sudah ada di folder proyek; pakai yang resmi.
7. **Pakai hanya yang ada di sheet.** Satu sheet bisa memuat ekspresi, pose, outfit, dan turnaround. Itu referensi yang boleh dipakai. Outfit atau pose di luar sheet = perubahan desain, perlu persetujuan.
8. **Jangan menimpa file.** Versi baru disimpan sebagai `v2`, `v3`; yang lama diberi status `deprecated`.
9. **Laporkan sumbernya.** Setiap hasil menyebut sheet (file + versi) yang dipakai. Jangan menyatakan hasil "sesuai master sheet" tanpa membandingkan.
10. **QA terhadap sheet.** Tolak output yang menggeser warna, bentuk wajah, mata, atau ciri khas, dan coba ulang maksimal 2 kali sebelum bertanya.
11. **Hak cipta dan privasi.** Sheet milik pemilik proyek. Jangan dipakai di luar proyeknya atau dibagikan ke layanan pihak ketiga selain generator yang dipakai untuk pekerjaan itu.
12. **Nama karakter tidak unik antar proyek.** Selalu pakai `Proyek:Nama`. `Arsein-Research:Lila` bukan `Rico-and-Friends:Lila`, dan juga Bimo dan Tika. Dilarang mencari karakter dengan nama polos lintas proyek.
13. **Character lock wajib.** Setiap prompt untuk karakter menyertakan lock dari `./scripts/check-character-library.sh <Proyek> --character <Nama>` (wajah, rambut, pakaian, warna, proporsi, ciri khas persis seperti sheet) dan melampirkan file referensi yang dicetaknya. Jangan menulis atribut visual yang tidak ada di sheet.
14. **Acuan kanonik.** Jika sheet berbeda, ikuti `character_locks` di `library.json`. Maya: tanpa ikat rambut/pita; sheet Maya solo (berpita) adalah varian non-kanonik, tidak dijadikan acuan utama tetapi tidak dihapus.
15. **Universe.** The-Last-Letter dan LYLA-Anime-Universe satu universe: karakter boleh dipakai bersama dan punya hubungan cerita. Sheet tetap di folder proyek asal; proyek lain merujuk file yang sama (tidak menyalin, tidak mendesain ulang). Pertahankan identitas, desain, kesinambungan cerita. Tanpa karakter baru atau perubahan desain tanpa persetujuan pemilik.
16. **Aturan file.** Jangan mengubah gambar asli; jangan menghapus atau mengganti file master; pertahankan `sha256`, `original_name`, dan `origin`. Skrip memeriksa hash, file hilang, duplikat, file salah folder, dan file tak terdaftar.
17. **Logo Arsein.** Gunakan **logo utama (kotak/bertumpuk) sebagai default**; **logo alternatif (horizontal)** boleh dipilih bila lebih sesuai dengan komposisi. Overlay file asli di post-produksi; jangan digambar ulang oleh model.


## 3. Struktur dan penamaan

```
references/character-library/
  README.md               katalog dan status
  CHARACTER_LIBRARY.md    panduan ini
  library.json            registri (sumber kebenaran status)
  <Project-Folder>/
    README.md             cakupan dan slot folder
    <project>__<subject>__master-sheet__v1.jpg
    proposed/             (opsional) karakter usulan yang belum resmi
```

Contoh nama: `rico-and-friends__group__master-sheet__v1.jpg` (hanya contoh format; bukan file yang sudah ada).

## 4. Skema entri `library.json`

```json
{
  "file": "Rico-and-Friends/rico-and-friends__group__master-sheet__v1.jpg",
  "original_name": "IMG_xxxx.jpeg",
  "characters": ["<nama persis seperti di sheet>"],
  "version": 1,
  "status": "identified",
  "uploaded_at": "YYYY-MM-DD",
  "approved_by": null,
  "approved_at": null,
  "sha256": "<hash file>",
  "notes": ""
}
```

Entri ditambahkan hanya setelah file benar-benar ada di folder.

Field tambahan pada entri karakter:
- `character_ids`: `["Proyek:Nama", ...]` (nama tidak unik antar proyek).
- `characters_status`: `{"Nama": "approved|identified"}` untuk persetujuan per karakter.
- `approval_basis`: dasar persetujuan (keputusan pemilik).
- `origin`: `{"channel", "original_name", "upload_commit"}`, catatan asal file.
- `canonical` / `canonical_for` / `canonical_note`: menandai sheet acuan kanonik atau varian non-kanonik.

Field tingkat proyek: `official_characters`, `forbidden_characters`, `character_locks`, `universe`, `name_collisions`, `brand_usage`. Tingkat atas: `universes`, `character_lock_template`, `name_collision_rule`.

## 4b. Aset brand: logo dan visual pendukung (dicatat terpisah dari karakter)

Master karakter dicatat di `assets`. **Logo dan aset brand dicatat di `brand_assets`**, daftar terpisah pada proyek yang sama. Yang satu tidak pernah dihitung sebagai yang lain, dan gate karakter tidak terpengaruh oleh aset brand.

Saat ini diaktifkan untuk **Arsein-Research**, yang menyimpan semua master karakter dan seluruh identitas visual brand ARSEIN RESEARCH:

| `type` | Isi | Subfolder |
|--------|-----|-----------|
| `logo_primary` | logo utama | `Arsein-Research/logos/primary/` |
| `logo_alternate` | logo alternatif (varian sebagaimana diunggah pemilik) | `Arsein-Research/logos/alternate/` |
| `supporting` | aset visual pendukung (isi `kind`: palet, pola, ikon, banner, template, foto, dan sebagainya) | `Arsein-Research/brand-assets/` |
| *(karakter)* | master character sheet | `Arsein-Research/characters/` |

Entri `brand_assets`:

```json
{
  "file": "Arsein-Research/logos/primary/arsein-research__logo-primary__v1.png",
  "original_name": "<nama file asli>",
  "type": "logo_primary",
  "kind": "",
  "version": 1,
  "status": "identified",
  "uploaded_at": "YYYY-MM-DD",
  "approved_by": null,
  "approved_at": null,
  "sha256": "<hash file>",
  "notes": ""
}
```

Status dan persetujuan memakai aturan yang sama dengan karakter (hanya pemilik yang mengubah ke `approved`).

Aturan aset brand:
1. **Tidak membuat aset baru dan tidak mengubah desain asli.** Dilarang menggambar ulang, mewarnai ulang, mengubah proporsi/teks, menghapus latar, mengubah ukuran dengan distorsi, atau "membersihkan" logo. Varian baru dari pemilik = file baru.
2. **Logo tidak ditulis ulang oleh model AI.** Teks dan bentuk logo hampir selalu rusak saat digenerate. Pada gambar/video, buat ruang kosong dan tempelkan file logo asli di post-produksi. Model hanya boleh diberi logo sebagai referensi gaya/warna bila pemilik mengizinkan, dan hasilnya tidak boleh disebut logo resmi.
3. **Logo di dalam master character sheet** adalah bagian dari sheet itu, bukan file logo. Jangan di-crop menjadi aset logo.
4. **Pilih varian sesuai fungsi**, dan jangan menebak: tanyakan pemilik jika tidak jelas logo mana yang cocok untuk sebuah penggunaan.
5. **Format:** PNG/SVG dengan latar transparan disarankan untuk logo. Upload lewat web GitHub tidak terpengaruh aturan ignore. Untuk `git add` lokal gunakan `-f`.
6. **Pemakaian saat generate (keputusan pemilik):** logo utama = versi kotak/bertumpuk, **default**. Logo alternatif = versi memanjang/horizontal, boleh dipilih bila lebih sesuai dengan komposisi. Keduanya aset terpisah. Tipe sudah dikonfirmasi pemilik, tetapi **keduanya belum `approved`**.
7. Gate: `./scripts/check-character-library.sh Arsein-Research --brand` (logo utama) atau `--brand --logo alternate`; exit 0 hanya jika logo berstatus `approved` dan filenya ada.

## 5. Alur setelah Anda mengunggah gambar

1. Anda mengunggah ke GitHub (atau melampirkan di chat) dan bilang "identifikasi dan tempatkan".
2. Saya membaca setiap gambar dan mengusulkan **proyek, karakter, dan folder tujuan**. Untuk yang ambigu, saya menanyakan Anda dan tidak menebak.
3. Setelah Anda setuju, saya memindahkan/menamai file, mengisi `library.json` (status `identified`), dan memperbarui tabel di `README.md`.
4. Anda menyatakan mana yang `approved`; baru setelah itu saya mengubah status.
5. Duplikat dilaporkan dan tidak disalin dua kali.

## 6. Cara skill memakai library

```bash
./scripts/check-character-library.sh                                          # integritas (exit 1 bila ada masalah)
./scripts/check-character-library.sh Rico-and-Friends                         # gate proyek
./scripts/check-character-library.sh Rico-and-Friends --character Rico --character Lila   # gate per karakter + LOCK + referensi
./scripts/check-character-library.sh LYLA-Anime-Universe --character Maya     # Maya diselesaikan dari The-Last-Letter (universe)
./scripts/check-character-library.sh Arsein-Research --brand                  # logo utama approved
./scripts/check-character-library.sh Arsein-Research --brand --logo alternate # logo alternatif approved
```

Gate **gagal (exit 1)** jika karakter tidak ditemukan, belum disetujui, ada di beberapa proyek dalam universe yang sama (ambigu), file hilang, atau hash berubah. Jika gagal: jangan jalankan langkah berbayar; hanya prompt offline berlabel "character unverified".

Untuk `pixar-animation-video`: isi `characters[].master_sheet` dengan path dari library (bukan deskripsi), pakai lock yang dicetak skrip, dan jangan mulai Phase 4+ (berbayar) sebelum gate lulus untuk **setiap** karakter yang dipakai.

## 7. Catatan teknis

- `references/` di-ignore git (aturan repo untuk media referensi lokal). Unggah lewat web GitHub, atau `git add -f` untuk commit lokal.
- `references/.gitignore` juga mengabaikan `*.png`; pakai JPEG/WEBP atau `git add -f`.
- Ukuran: usahakan di bawah beberapa MB per file; sheet resolusi tinggi lebih baik untuk detail wajah.
