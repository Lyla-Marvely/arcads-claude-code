# Rico & Friends — "Telur Pelangi" (revisi 2, pack offline)

**Status: persiapan saja. Belum ada gambar atau video yang dibuat. Tidak ada API yang dipanggil. Menunggu pemeriksaan dan persetujuan Anda.**
Sumber kebenaran: `project.json`. Prompt lengkap: `prompts/prompt-pack.md` (dibaca manusia) dan `prompts/prompts.json`. Bukti gate karakter: `character-gate-report.txt`.

## 0. Revisi 2: keputusan Anda dan penerapannya

| # | Keputusan | Penerapan di pack |
|---|-----------|-------------------|
| 1 | Ukuran Rico mengikuti master sheet referensi scene; ukuran konsisten antar scene dalam satu episode | Setiap scene punya sheet referensi sendiri (S01: sheet Rico solo; S02–S07: sheet grup). **Kunci skala relatif** (bagian 5) dimasukkan ke setiap prompt dan berlaku sama di semua scene. Angka absolut cm tidak dipakai karena kedua sheet berbeda. |
| 2 | Pecah klip bila lima karakter berisiko mengubah wajah/desain; konsistensi di atas jumlah klip | Adegan lima karakter dipecah menjadi **6 klip dengan maksimal 3 karakter per klip** (divalidasi builder). Penilaian risiko ada di bagian 4. Klip grup lima karakter hanya **opsional (S07)**. |
| 3 | Telur boleh jadi pusat cerita, tetap objek, tidak menetas, tidak jadi karakter | Telur hanya objek: tanpa wajah, mata, mulut, atau anggota tubuh; tidak bergerak sendiri; tidak menetas, retak, atau berubah (dikunci di prompt, negative, dan QA). |
| 4 | Tidak ada lencana atau tulisan LYLA MARVELY | Prompt melarang lencana, logo, watermark, dan teks apa pun, serta memerintahkan sheet dipakai **hanya untuk tampilan karakter**. Nama lencana sengaja **tidak** ditulis di prompt (agar tidak memancing model). Ada butir QA khusus untuk menolak hasil yang memuatnya. |
| 5 | Pertahankan lima karakter resmi | Rico, Lila, Bimo, Tika, Piko; semuanya lulus gate. Tidak ada karakter lain, termasuk Pip dan Moss. |
| 6 | Belum ada generasi berbayar | Tidak ada panggilan API. Semua offline. |

Perubahan dari revisi 1: 3 klip (10 detik) menjadi 6 klip (4–8 detik), penataan panggung per scene, kunci skala, catatan referensi anti-lencana, checklist QA.

## 1. Karakter (disetujui pemilik, lulus gate)

| ID | Spesies (menurut sheet) | Ciri khas yang dikunci (menurut sheet) |
|----|-------------------------|-----------------------------------------|
| `Rico-and-Friends:Rico` | bayi dinosaurus fantasi | badan turquoise, perut krem, mata amber, **tiga tonjolan jingga**, 3 jari kaki, ekor pendek melengkung |
| `Rico-and-Friends:Lila` | bayi triceratops | merah muda, tiga tanduk, frill merah muda |
| `Rico-and-Friends:Bimo` | bayi triceratops | kuning, tiga tanduk, frill kuning |
| `Rico-and-Friends:Tika` | bayi brachiosaurus | ungu, leher panjang, motif bintik |
| `Rico-and-Friends:Piko` | bayi pterodactyl | biru, sayap lebar, jambul biru |

Lock hanya memuat yang tertulis atau terlihat di sheet; sisanya "persis seperti sheet". Pip dan Moss tidak ada. Prompt tiap klip **hanya menyebut karakter yang hadir di klip itu**; sudah dipindai: 0 nama karakter yang absen muncul di prompt mana pun.

## 2. Cerita (konsep disetujui)

Rico menemukan Telur Pelangi di hutan. Sahabatnya datang satu per satu (Piko, lalu Lila dan Bimo, lalu Tika). Mereka sepakat menjaga telur bersama-sama. Telur tetap sebuah objek yang bersinar; ia tidak menetas.

## 3. Script dan VO (30 detik, Bahasa Indonesia)

| Klip | Waktu | Aksi | VO |
|------|-------|------|----|
| **S01 hook** | 0–8 s | Rico mengintip dari balik batu berlumut, melihat telur berkilau di antara bunga, matanya melebar, lalu melangkah mendekat. Sinar matahari menyorot tiga tonjolan jingganya. | "Pagi itu di hutan, Rico menemukan sebuah telur pelangi yang berkilau." (11 kata) |
| **S02 datang 1** | 8–12 s | Piko meluncur dari atas dan melayang dekat telur; Rico menatapnya gembira. | "Piko terbang menghampiri." (3) |
| **S03 datang 2** | 12–16 s | Lila dan Bimo masuk dari kanan dan berhenti di samping telur; Rico tersenyum pada mereka. | "Lila dan Bimo menyusul." (4) |
| **S04 datang 3** | 16–20 s | Leher panjang Tika turun dari atas; ia menatap telur, Rico mendongak sambil tersenyum. | "Tika pun datang." (3) |
| **S05 kilau 1** | 20–25 s | Kilau pelangi telur makin terang menyinari wajah Rico, Lila, Bimo; mereka saling tersenyum. | "Mereka sepakat, telur ini harus dijaga bersama." (7) |
| **S06 kilau 2** | 25–30 s | Kilau menyinari Rico, Piko, Tika yang tersenyum; Rico menoleh gembira; kamera mundur pelan dan menahan 1 detik. | "Karena sahabat sejati selalu menjaga hal berharga, bersama-sama." (8) |
| *S07 opsional* | +4 s | Susunan grup lima karakter seperti "Pose Grup Referensi" di sheet grup, nyaris tanpa gerakan. Hanya bila lolos QA (lihat bawah). | — |

VO jauh di bawah batas 2,5 kata/detik, jadi akan ada jeda. Opsi: tambah kalimat pendek, atau musik/ambient.

## 4. Storyboard dan penilaian risiko

| Klip | Dur | Karakter (jumlah) | Shot | Kamera |
|------|-----|-------------------|------|--------|
| S01 | 8 s | Rico (1) | wide establishing → medium Rico mengintip dari batu | push-in pelan |
| S02 | 4 s | Rico, Piko (2) | medium two-shot di telur: Rico kiri, Piko melayang kanan-atas | statis, dorong sangat halus |
| S03 | 4 s | Rico, Lila, Bimo (3) | medium three-shot: Rico kiri telur, Lila dan Bimo kanan | statis |
| S04 | 4 s | Rico, Tika (2) | tight medium two-shot: Tika di atas dan belakang telur | statis, dorong sangat pelan |
| S05 | 5 s | Rico, Lila, Bimo (3) | medium three-shot seperti S03 | statis, dorong sangat pelan |
| S06 | 5 s | Rico, Piko, Tika (3) | medium-wide: Piko kanan-atas, leher Tika di belakang telur | pull-back halus + hold 1 detik |
| S07 (opsional) | 4 s | kelimanya (5) | wide statis, susunan pose grup | locked-off |

**Mengapa dipecah:** pada generasi video Arcads/Seedance, referensi dibatasi 3 gambar per klip, sedangkan lima karakter berbeda bergerak bersamaan adalah kondisi yang paling rentan mengubah wajah dan ciri khas. Karena Anda memprioritaskan konsistensi, **tidak ada klip baseline dengan lebih dari 3 karakter** (builder menolak jika dilanggar). Rasa "berkumpul" dibangun lewat montase klip dengan satu karakter inti (Rico) di semua klip sebagai jangkar.

**S07 (lima karakter)** tetap opsional dan tidak dihitung: dirender hanya jika still-nya lolos QA untuk kelima karakter; jika tidak, dilewati. Gerakannya sengaja nyaris nol untuk membatasi drift.

Keluaran: **9:16 dan 16:9**, masing-masing diframing ulang (bukan crop).

## 5. Kunci skala (konsisten antar scene)

Relatif terhadap tinggi Rico = 1,0. Rasio diturunkan dari angka di master sheet: sheet Rico solo (telur ±50 cm vs Rico ±40 cm) dan perbandingan ukuran di sheet grup (Tika ±1,1; Rico ±0,8; Bimo ±0,7; Lila ±0,7; Piko ±0,6).

| Objek/karakter | Rasio (di prompt) | Perhitungan |
|----------------|-------------------|-------------|
| Rico | 1,0 | acuan |
| Telur Pelangi | ± 1,25 (sedikit lebih tinggi dari Rico) | 50 / 40, sheet Rico solo |
| Tika | ± 1,4 (tertinggi) | 1,1 / 0,8, sheet grup |
| Bimo, Lila | ± 0,9 | 0,7 / 0,8, sheet grup |
| Piko | ± 0,75 (tubuh terkecil, sayap lebar) | 0,6 / 0,8, sheet grup (di sheet tertulis "tinggi terbang") |

Sheet Rico solo dan sheet grup **berbeda dalam ukuran absolut Rico** (±40 cm vs ±0,8 m), sehingga pack hanya memakai rasio, dan rasio itu tetap di semua scene. Rasio telur diambil dari sheet Rico solo; rasio teman dari sheet grup. Angka ini adalah turunan saya; mohon dikonfirmasi.

## 6. Penataan panggung (per scene, hanya karakter yang hadir)

Telur di tengah, di petak bunga di samping batu berlumut. Rico selalu di **kiri** telur menghadapnya. Lila dan Bimo di kanan. Tika menunduk dari atas dan belakang telur. Piko melayang di kanan-atas. Cahaya emas dari kiri kamera, tanpa perubahan waktu.

## 7. Continuity lock

1. Semua karakter disalin persis dari master sheet (warna, wajah, mata, ciri khas); Rico dengan tiga tonjolan jingga.
2. Kunci skala tidak berubah antar scene.
3. Telur: tampilan sama (cangkang pelangi iridescent), ukuran dan posisi sama; hanya objek.
4. Hutan dan arah cahaya sama; satu shot kontinu per klip.
5. Antar klip: posisi dan tingkat kilau telur dilanjutkan dari akhir klip sebelumnya.

## 8. Negative prompt

**Gambar:** tidak fotorealistik, bukan live-action, bukan anime, bukan 2D/cel-shaded/ilustrasi datar; tanpa jari berlebih, fitur menyatu, properti cacat, karakter tambahan, teks, caption, watermark, logo. **Plus:** jangan mendesain ulang karakter; tidak ada fitur lebih, kurang, atau berubah; tanpa karakter atau bayi dinosaurus baru; tanpa aksesori; **tanpa lencana, logo, watermark, atau teks apa pun**; telur hanya objek (tanpa wajah, mata, mulut, anggota tubuh; tidak bergerak sendiri; tidak menetas, retak, atau menjadi karakter).

**Video:** tidak live-action/fotorealistik, tidak anime/2D, tanpa karakter tambahan, anggota tubuh tambahan, morphing, perubahan warna, scene cut, lompatan cahaya, teks/caption/watermark. **Plus:** tanpa karakter baru; tanpa lencana, logo, atau teks; telur tanpa wajah atau anggota tubuh.

Arcads tidak punya field `negativePrompt`; negatif ditulis di dalam teks prompt.

## 9. Rencana referensi (belum dijalankan)

| Klip | Still (gpt-image-2, maks 5) | Video (Seedance 2.0, maks 3) |
|------|-----------------------------|------------------------------|
| S01 | sheet Rico solo | img1 still S01, img2 sheet Rico solo |
| S02–S06, S07 | sheet grup, sheet Rico solo, still klip sebelumnya | img1 still klip, img2 sheet grup, img3 still klip sebelumnya |

Still dibuat per rasio, dan klip memakai still dengan rasio yang sama. Path presigned hanya sekali pakai, jadi file diunggah ulang untuk setiap panggilan.

**Risiko lencana:** sheet grup memuat lencana dan teks. Aturan library mewajibkan sheet dilampirkan di setiap panggilan, jadi mitigasinya ada di prompt (sheet hanya untuk tampilan karakter) dan di QA. **Alternatif yang lebih aman, tetapi menyimpang dari aturan library:** untuk video, hanya pakai still yang sudah disetujui (bersih dari lencana) sebagai referensi, dan sheet hanya untuk still. Tidak saya terapkan tanpa persetujuan Anda.

## 10. Checklist QA (setiap still dan klip)

- [ ] Wajah, mata, warna, dan penanda cocok dengan sheet (bandingkan berdampingan).
- [ ] Rico: tepat tiga tonjolan jingga di kepala, badan turquoise, perut krem, mata amber.
- [ ] Lila dan Bimo: tiga tanduk dan frill berwarna benar; Tika: leher panjang dan bintik; Piko: sayap lebar dan jambul biru.
- [ ] Skala sesuai kunci di semua scene (Rico 1,0; telur ±1,25; Tika tertinggi; Piko terkecil).
- [ ] Telur: tampilan, ukuran, dan posisi sama; tanpa wajah atau anggota tubuh; tidak bergerak sendiri, menetas, atau retak.
- [ ] **Tidak ada lencana, logo, watermark, atau teks; khususnya tidak ada lencana atau tulisan "LYLA MARVELY"** (tolak dan ulangi).
- [ ] Hanya karakter yang tercantum untuk klip itu (maks 3).
- [ ] Penataan panggung dan arah layar sesuai.
- [ ] Rasio benar (9:16 atau 16:9), disusun terpisah.
- [ ] Maks 2 retry per aset, lalu tanya Anda. Jika klip ramai bermasalah, **pecah shot, jangan retry terus**.

## 11. Jumlah request jika disetujui (hitungan, bukan biaya)

- Sheet karakter baru: **0**.
- Baseline: **12 still** (6 klip × 2 rasio) + **12 klip** = **24 request**, dua kali lipat revisi 1 (12 request) karena pemecahan klip. Total 30 detik per rasio.
- Opsional S07: +2 still +2 klip.
- Biaya credit **tidak** dihitung di sini. Konfirmasikan harga di platform Arcads sebelum generasi.
- Prompt Seedance 282–316 kata (S07 344), sedikit di atas target 260 dari panduan (bukan batas API yang terdokumentasi).

## 12. Menunggu keputusan Anda

1. **Setujui kunci skala** (bagian 5), atau berikan rasio lain.
2. **S07 (grup lima karakter, opsional):** masukkan ke rencana atau lewati?
3. **VO jarang dan klip pendek:** tambah kalimat atau musik/ambient?
4. **Video bebas-sheet** (alternatif bagian 9) untuk mengurangi risiko lencana: dipakai atau tetap sesuai aturan library?
5. Persetujuan cerita, script, dan storyboard revisi ini.

## 13. Sebelum generasi berbayar

`.env` Arcads dan `PRODUCT_ID` belum ada di sesi ini (`check-requirements.sh` = **BLOCKED**), jadi autentikasi, akses model, dan saldo belum terverifikasi. Konfirmasi estimasi credit, dan setiap still disetujui sebelum menjadi referensi klip.
