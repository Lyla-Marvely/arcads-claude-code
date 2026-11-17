# Character Reference Library — LYLA projects

Katalog master character sheet untuk seluruh proyek LYLA. Aturan pemakaian ada di [CHARACTER_LIBRARY.md](CHARACTER_LIBRARY.md). Registri mesin-baca ada di [library.json](library.json).

> **Status saat ini: folder dan dokumentasi sudah disiapkan. Belum ada gambar master character sheet di repository ini.** Pemilik proyek akan mengunggah sekitar 14 gambar secara terpisah lewat GitHub. Tabel di bawah hanya menjadi benar setelah gambar benar-benar ada dan terdaftar di `library.json`.

## Proyek

| Folder | Proyek | Gambar di repo | Approved | Catatan |
|--------|--------|:--------------:|:--------:|---------|
| [LYLA/](LYLA/) | LYLA | 0 | 0 | menunggu unggahan |
| [LYLA-Education/](LYLA-Education/) | LYLA Education | 0 | 0 | menunggu unggahan |
| [Rico-and-Friends/](Rico-and-Friends/) | Rico & Friends | 0 | 0 | menunggu unggahan |
| [Zeno-Family/](Zeno-Family/) | Zeno Family | 0 | 0 | menunggu unggahan |
| [Arsein-Research/](Arsein-Research/) | Arsein Research | 0 | 0 | menunggu unggahan |
| [The-Last-Letter/](The-Last-Letter/) | The Last Letter | 0 | 0 | menunggu unggahan |
| [LYLA-Anime-Universe/](LYLA-Anime-Universe/) | LYLA Anime Universe | 0 | 0 | menunggu unggahan |

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
