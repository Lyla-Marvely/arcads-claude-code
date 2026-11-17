# Character Reference Library — LYLA projects

Katalog master character sheet dan aset brand untuk seluruh proyek LYLA. Aturan pemakaian: [CHARACTER_LIBRARY.md](CHARACTER_LIBRARY.md). Registri mesin-baca (sumber kebenaran): [library.json](library.json).

> **Status saat ini:** 14 master character sheet dan 2 logo Arsein Research sudah diunggah, diverifikasi (hash tercatat), dan terdaftar. **Disetujui pemilik:** Rico, Lila, Bimo, Tika, Piko (Rico-and-Friends), Fasha dan Kania (LYLA-Education), dan Maya tanpa pita rambut sebagai desain kanonik (The-Last-Letter). **Semua yang lain masih `identified` (menunggu persetujuan)**, termasuk kedua logo Arsein. Folder `LYLA/` masih kosong.

## Proyek

| Folder | Cakupan | Sheet | Logo/aset brand | Karakter disetujui (`Proyek:Nama`) |
|--------|---------|:-----:|:---------------:|------------------------------------|
| [LYLA/](LYLA/) | LYLA Marvely dan konten brand LYLA umum | 0 | — | — |
| [LYLA-Education/](LYLA-Education/) | semua konten pendidikan, maskot edukasi, worksheet, serial edukasi | 5 | — | Fasha, Kania |
| [Rico-and-Friends/](Rico-and-Friends/) | serial Rico & Friends | 2 | — | Bimo, Lila, Piko, Rico, Tika |
| [Zeno-Family/](Zeno-Family/) | The Zeno Family | 1 | — | — |
| [Arsein-Research/](Arsein-Research/) | master karakter **dan** seluruh aset brand Arsein Research | 1 | 2 | — |
| [The-Last-Letter/](The-Last-Letter/) | The Last Letter (satu universe dengan LYLA-Anime-Universe) | 4 | — | Maya |
| [LYLA-Anime-Universe/](LYLA-Anime-Universe/) | LYLA Anime Universe (satu universe dengan The-Last-Letter) | 1 | — | — |

Jumlah di atas hanyalah ringkasan. Kebenarannya dibaca dari disk dan registri: `./scripts/check-character-library.sh`.

## Keputusan pemilik (2026-11-17)

1. **LYLA ≠ LYLA-Education.** LYLA = LYLA Marvely + konten brand umum. LYLA-Education = konten pendidikan, maskot edukasi, worksheet, serial edukasi. Sheet "Maskot LYLA Education" (Lyla, Lyla & Lilo) dan Aisyah, Mama Aisyah ada di LYLA-Education.
2. **Rico & Friends:** karakter resmi hanya Rico, Lila, Bimo, Tika, Piko. Pip dan Moss bukan karakter resmi. Tidak boleh ada karakter pengganti. Ejaan "Rico".
3. **Arsein Research:** semua master karakter dan aset visual brand ada di `Arsein-Research/`. **Logo utama = versi kotak/bertumpuk** (default saat generate). **Logo alternatif = versi memanjang/horizontal** (boleh dipilih bila lebih sesuai dengan komposisi). Dua aset terpisah. Master karakter Arsein tidak boleh tertukar dengan karakter bernama sama di proyek lain.
4. **The Last Letter — Maya:** desain kanonik adalah **Maya tanpa ikat rambut atau pita**. Bila sheet berbeda, desain tanpa pita menjadi acuan utama. Sheet Maya solo (dengan pita) disimpan sebagai varian non-kanonik, tidak dihapus.
5. **The Last Letter dan LYLA Anime Universe = satu universe.** Karakter boleh dipakai bersama dan punya hubungan cerita; identitas, desain, dan kesinambungan cerita dipertahankan; tidak ada karakter baru atau perubahan desain tanpa persetujuan pemilik.
6. **LYLA-Education:** Fasha dan Kania adalah karakter resmi; sheet-nya di LYLA-Education/; tidak boleh masuk LYLA umum.
7. **Aturan persetujuan aset:** jangan mengubah gambar asli; jangan menghapus atau mengganti file master; jangan menjadikan sesuatu `approved` selain yang jelas disetujui pemilik; pertahankan hash dan catatan asal file; semua proyek memakai character lock.

## Pemeriksaan

```bash
./scripts/check-character-library.sh                                    # integritas semua proyek (exit 1 bila ada masalah)
./scripts/check-character-library.sh Rico-and-Friends                   # gate proyek: ada karakter approved?
./scripts/check-character-library.sh The-Last-Letter --character Maya   # gate per karakter + cetak character lock dan file referensi
./scripts/check-character-library.sh LYLA-Anime-Universe --character Maya   # lintas proyek dalam satu universe
./scripts/check-character-library.sh Arsein-Research --brand            # logo utama approved? (--logo alternate untuk alternatif)
```

## Aturan singkat

1. Setiap proyek memakai master sheet dari foldernya (atau dari proyek lain **dalam universe yang sama**).
2. Hanya karakter/aset berstatus **`approved`** yang resmi.
3. **Jangan membuat atau mengubah desain.** Karakter baru = *proposed*, bukan resmi.
4. Nama karakter tidak unik antar proyek; selalu `Proyek:Nama`.
5. Jangan menyatakan sebuah gambar "tersedia" sebelum file-nya ada dan terdaftar.

## Cara mengunggah

- **Lewat web GitHub:** buka folder proyek, *Add file, Upload files*, commit ke branch kerja. Direkomendasikan karena `references/` di-ignore git secara lokal.
- **Lewat git lokal:** `git add -f references/character-library/<Folder>/<file>`.
- Format JPEG/WEBP/PNG/SVG. Upload web tidak terpengaruh ignore; `git add` lokal butuh `-f`.
- Nama file: `<proyek>__<subjek>__master-sheet__v1.<ext>`. Nama asli dicatat di `library.json`.

Setelah unggah, minta: *"Identifikasi dan tempatkan gambar yang baru saya unggah."*
