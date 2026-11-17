# Arsein Research — character references

**Status: 1 master sheet dan 2 logo terdaftar. Karakter disetujui: belum ada. Terdaftar tetapi belum disetujui: Bimo, Lila, Naya, Raka, Tika.** Sumber kebenaran: [../library.json](../library.json).

**Cakupan:** seluruh master karakter dan aset visual brand Arsein Research disimpan di folder ini, dengan pencatatan terpisah.

| Subfolder | Jenis | Dicatat di `library.json` |
|-----------|-------|---------------------------|
| [characters/](characters/) | master character sheet | `assets` |
| [logos/primary/](logos/primary/) | **logo utama** = versi kotak/bertumpuk | `brand_assets`, `logo_primary` |
| [logos/alternate/](logos/alternate/) | **logo alternatif** = versi memanjang/horizontal | `brand_assets`, `logo_alternate` |
| [brand-assets/](brand-assets/) | aset visual pendukung (belum ada) | `brand_assets`, `supporting` |

**Pemakaian logo saat generate:** gunakan **logo utama sebagai default**. Logo alternatif boleh dipilih bila lebih sesuai dengan komposisi (misalnya layout lebar/horizontal). Kedua logo adalah aset terpisah. Logo asli ditempelkan di post-produksi; model AI tidak boleh menulis ulang atau menggambar ulang logo, dan logo tidak di-crop dari sheet karakter.

**Karakter tidak boleh tertukar:** Lila, Bimo, dan Tika di Arsein adalah karakter **berbeda** dari Lila, Bimo, dan Tika di Rico-and-Friends. Selalu gunakan `Arsein-Research:<Nama>`.

**Status logo:** tipe (utama/alternatif) sudah dikonfirmasi pemilik, tetapi **belum disetujui (`approved`)**. Kedua file berlatar (bukan transparan) dan punya garis hitam tipis di tepi atas; tidak dimodifikasi.

## File terdaftar

| File | Karakter (`Proyek:Nama`) | Status | Catatan |
|------|--------------------------|--------|---------|
| `arsein-research__team__master-sheet__v1.jpeg` | Lila, Raka, Naya, Bimo, Tika | `identified` |  |

✔ = disetujui pemilik. Karakter tanpa ✔ baru `identified`.

## Logo dan aset brand (tercatat terpisah dari karakter)

| File | Tipe | Status |
|------|------|--------|
| `arsein-research__logo-primary__v1.jpeg` | `logo_primary` | `identified` (tipe dikonfirmasi pemilik) |
| `arsein-research__logo-alternate-horizontal__v1.jpeg` | `logo_alternate` | `identified` (tipe dikonfirmasi pemilik) |


## Aturan (ringkas; lengkap di [../CHARACTER_LIBRARY.md](../CHARACTER_LIBRARY.md))

- Jangan mengubah gambar asli, jangan menghapus atau mengganti file master. Versi baru = file baru (`v2`).
- Hanya karakter berstatus `approved` yang resmi. Jangan membuat karakter baru atau mengubah desain tanpa persetujuan pemilik.
- Selalu sebut karakter sebagai `Proyek:Nama`; nama yang sama di proyek lain adalah karakter berbeda.
- Gunakan character lock: `./scripts/check-character-library.sh <Proyek> --character <Nama>` mencetak lock dan file referensi.
