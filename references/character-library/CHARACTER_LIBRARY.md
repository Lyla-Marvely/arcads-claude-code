# Character Library — panduan penggunaan master karakter

Panduan ini berlaku untuk **setiap skill dan sesi** yang membuat gambar, video, storyboard, atau prompt yang memuat karakter proyek LYLA. Ini mencakup `pixar-animation-video`, `pixar-style-ad`, `claymation-ad`, `gemini-omni-flash`, `caption-video`, `generate-youtube-thumbnail`, dan skill image-ad.

Status: folder sudah ada; **gambar belum diunggah**. Sebelum sebuah karakter dipakai, cek `library.json`.

## 0. Keputusan pemilik dan routing proyek

| Jika kontennya… | Gunakan folder |
|-----------------|----------------|
| LYLA Marvely, konten brand LYLA umum | `LYLA/` |
| pendidikan, maskot edukasi (Lyla "Maskot LYLA Education", Lilo), worksheet, serial edukasi, serial perilaku anak dan parenting (Aisyah, Mama Aisyah) | `LYLA-Education/` |
| Rico & Friends | `Rico-and-Friends/` |
| Zeno Family / Arsein Research / The Last Letter / LYLA Anime Universe | folder dengan nama yang sama |

Aturan khusus:
- **LYLA ≠ LYLA-Education.** Jangan mencampur keduanya. Lyla dengan label "Maskot LYLA Education" memakai sheet di `LYLA-Education/`.
- **Rico & Friends:** karakter resmi hanya Rico, Lila, Bimo, Tika, Piko (deklarasi pemilik; desain diverifikasi dari sheet setelah diunggah). **Pip dan Moss bukan karakter resmi** dan tidak boleh dipakai. **Jangan membuat karakter pengganti**, jangan mengubah desain yang ada. Ejaan tertulis **Rico**; gambar sheet tidak diedit.
- Daftar `official_characters` di `library.json` adalah deklarasi pemilik. Detail visualnya tetap hanya dari sheet `approved`; sebelum itu, jangan menuliskan atribut visual apa pun.
- `planned_sheets` di `library.json` adalah rencana, bukan bukti ketersediaan.

## 1. Istilah status

| Status | Arti | Boleh dipakai untuk |
|--------|------|---------------------|
| *(tidak terdaftar)* | gambar belum ada di repo | tidak ada — jangan klaim tersedia |
| `uploaded` | file ada di folder, belum diidentifikasi | tidak ada |
| `identified` | proyek/karakter sudah diidentifikasi, **belum disetujui pemilik** | hanya diskusi dan draf prompt offline berlabel "UNAPPROVED" |
| `approved` | disetujui pemilik, **ini karakter resmi** | semua pekerjaan, termasuk generasi berbayar |
| `deprecated` | digantikan versi baru | tidak boleh dipakai |

Hanya pemilik proyek yang boleh mengubah status menjadi `approved`. Claude/agent **tidak pernah** menyetujui sendiri.

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

## 5. Alur setelah Anda mengunggah gambar

1. Anda mengunggah ke GitHub (atau melampirkan di chat) dan bilang "identifikasi dan tempatkan".
2. Saya membaca setiap gambar dan mengusulkan **proyek, karakter, dan folder tujuan**. Untuk yang ambigu, saya menanyakan Anda dan tidak menebak.
3. Setelah Anda setuju, saya memindahkan/menamai file, mengisi `library.json` (status `identified`), dan memperbarui tabel di `README.md`.
4. Anda menyatakan mana yang `approved`; baru setelah itu saya mengubah status.
5. Duplikat dilaporkan dan tidak disalin dua kali.

## 6. Cara skill memakai library

```bash
./scripts/check-character-library.sh                 # ringkasan semua proyek
./scripts/check-character-library.sh Rico-and-Friends # gate: exit 0 hanya jika ada aset approved yang filenya ada
```

Untuk `pixar-animation-video`: isi `characters[].master_sheet` di `project.json` dengan path file dari library (bukan deskripsi), dan jangan mulai Phase 4+ (berbayar) sebelum gate lulus.

## 7. Catatan teknis

- `references/` di-ignore git (aturan repo untuk media referensi lokal). Unggah lewat web GitHub, atau `git add -f` untuk commit lokal.
- `references/.gitignore` juga mengabaikan `*.png`; pakai JPEG/WEBP atau `git add -f`.
- Ukuran: usahakan di bawah beberapa MB per file; sheet resolusi tinggi lebih baik untuk detail wajah.
