# Character Reference Library — LYLA projects

Katalog master character sheet untuk seluruh proyek LYLA. Aturan pemakaian ada di [CHARACTER_LIBRARY.md](CHARACTER_LIBRARY.md). Registri mesin-baca ada di [library.json](library.json).

> **Status saat ini: folder dan dokumentasi sudah disiapkan. Belum ada gambar master character sheet di repository ini.** Pemilik proyek akan mengunggah sekitar 14 gambar secara terpisah lewat GitHub. Tabel di bawah hanya menjadi benar setelah gambar benar-benar ada dan terdaftar di `library.json`.

## Proyek

| Folder | Cakupan (keputusan pemilik) | Gambar di repo | Approved | Rencana sheet (belum diunggah) |
|--------|-----------------------------|:--------------:|:--------:|:------------------------------:|
| [LYLA/](LYLA/) | LYLA Marvely dan konten brand LYLA secara umum | 0 | 0 | 0 |
| [LYLA-Education/](LYLA-Education/) | Semua konten pendidikan: maskot edukasi, worksheet, serial edukasi (termasuk perilaku anak dan parenting) | 0 | 0 | 5 |
| [Rico-and-Friends/](Rico-and-Friends/) | Serial Rico & Friends. Karakter resmi: Rico, Lila, Bimo, Tika, Piko | 0 | 0 | 2 |
| [Zeno-Family/](Zeno-Family/) | The Zeno Family | 0 | 0 | 1 |
| [Arsein-Research/](Arsein-Research/) | Arsein Research | 0 | 0 | 1 |
| [The-Last-Letter/](The-Last-Letter/) | The Last Letter | 0 | 0 | 4 |
| [LYLA-Anime-Universe/](LYLA-Anime-Universe/) | LYLA Anime Universe | 0 | 0 | 1 |

"Rencana sheet" adalah niat yang dicatat di `library.json` (`planned_sheets`), **bukan file dan bukan aset**. Total 14 sheet direncanakan. Folder `LYLA/` belum punya rencana sheet. Sheet Lyla yang bertuliskan "Maskot LYLA Education" ditempatkan di `LYLA-Education/`.

## Keputusan pemilik (dicatat 2026-11-17)

1. **LYLA** dan **LYLA-Education** adalah dua proyek berbeda. LYLA = LYLA Marvely + konten brand umum. LYLA-Education = semua konten pendidikan, maskot edukasi, worksheet, dan serial edukasi.
2. Master sheet **Lyla (solo)** dan **Lyla & Lilo** yang bertuliskan "Maskot LYLA Education" ditempatkan di **LYLA-Education**.
3. **Aisyah** dan **Mama Aisyah** masuk **LYLA-Education** (serial edukasi perilaku anak dan parenting).
4. **Rico & Friends:** karakter resmi hanya **Rico, Lila, Bimo, Tika, Piko**. **Pip dan Moss bukan karakter resmi.** Dilarang membuat karakter pengganti atau mengubah desain karakter yang ada.
5. **Ejaan:** gunakan **Rico**, sesuai nama proyek Rico & Friends. Gambar sheet mungkin bertuliskan "Riko"; gambar tidak diedit, dan dokumen/prompt memakai "Rico".

> Rencana penempatan **Fasha & Kania** ("Seri Edukasi LYLA | Dunia Sekolah") di LYLA-Education adalah kesimpulan dari judul sheet dan cakupan LYLA-Education, bukan keputusan eksplisit. Mohon konfirmasi saat identifikasi.

Cek status sebenarnya (membaca disk, bukan tabel ini):

```bash
./scripts/check-character-library.sh              # ringkasan semua proyek
./scripts/check-character-library.sh Rico-and-Friends   # exit 0 hanya jika ada master sheet approved
```

## Aturan singkat

1. Setiap proyek hanya memakai master sheet dari **foldernya sendiri**.
2. Hanya aset berstatus **`approved`** yang dianggap karakter resmi.
3. **Jangan membuat atau mengubah desain karakter.** Karakter baru usulan = *proposed*, bukan resmi.
4. Jangan menyatakan sebuah gambar "tersedia" sebelum file-nya ada di folder dan terdaftar di `library.json`.

## Cara mengunggah

- **Lewat web GitHub:** buka folder proyek → *Add file → Upload files* → commit ke branch kerja. Direkomendasikan karena `references/` di-ignore git secara lokal.
- **Lewat git lokal:** `git add -f references/character-library/<Folder>/<file>` (perlu `-f`).
- Format **JPEG/JPG/WEBP**. File `.png` di bawah `references/` diabaikan oleh `references/.gitignore`. Ubah ke JPEG atau gunakan `git add -f`.
- Nama file: `<proyek>__<subjek>__master-sheet__v1.jpg` (contoh format; lihat CHARACTER_LIBRARY.md). Jika nama asli kamera (`IMG_xxxx.jpeg`) diunggah, nama itu tetap diterima dulu dan diubah saat identifikasi, dengan nama asli dicatat di `library.json`.

Setelah unggah, minta: *"Identifikasi dan tempatkan gambar yang baru saya unggah."*
