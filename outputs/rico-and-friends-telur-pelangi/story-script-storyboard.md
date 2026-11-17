# Rico & Friends — "Telur Pelangi" (revisi final)

**Status: pack offline, siap untuk persetujuan akhir Anda. Belum ada gambar atau video yang dibuat. Tidak ada API yang dipanggil dan tidak ada kredit yang dipakai.**
Sumber kebenaran: `project.json`. Prompt lengkap: `prompts/prompt-pack.md` dan `prompts/prompts.json`. Bukti pemeriksaan: `final-verification-report.md` dan `character-gate-report.txt`.

## 0. Keputusan Anda dan penerapannya

| # | Keputusan | Penerapan |
|---|-----------|-----------|
| 1 | Enam klip utama, tanpa S07, ±30 detik, maks 3 karakter per klip, konsistensi di atas jumlah klip, telur hanya objek | S07 **dihapus**. Enam klip, total 30 detik. Maks 3 karakter per klip (builder menolak pelanggarannya). Telur: tidak menetas, retak, berwajah, beranggota tubuh, atau bergerak sendiri. |
| 2 | Semua suara dalam video berbahasa Inggris, sederhana, ceria, jelas | VO enam klip dalam bahasa Inggris. Karakter **tidak berbicara** (tanpa dialog), jadi tidak ada ucapan lain. Builder menolak kata Indonesia di VO. |
| 3 | Tanpa angka rasio turunan; proporsi sesuai master sheet; ukuran relatif konsisten | **Semua angka rasio dihapus** (kunci skala numerik tidak lagi ada). Diganti aturan: ukuran relatif mengikuti master sheet dan still terakhir yang disetujui, tidak berubah antar scene. |
| 4 | Referensi sesuai karakter yang hadir; sheet hanya untuk identitas; tanpa latar, layout, tulisan, lencana | Prompt hanya menyebut karakter yang hadir. Catatan referensi di setiap prompt melarang menyalin latar, layout, panel, label, lencana, logo, dan teks. **Rumah jamur dihapus** dari latar, karena berasal dari latar sheet grup. Still bersih dibuat dan diperiksa dulu sebelum dipakai untuk video. |
| 5 | Musik ceria, ambient hutan, SFX sesuai aksi, tanpa jeda audio kosong, musik tidak menutupi VO, satu narator | Bagian 6. |
| 6 | Negative prompt lengkap, disesuaikan per karakter dan adegan | Bagian 5. Negatif fitur hanya untuk karakter yang hadir. |
| 7 | Pemeriksaan kualitas sebelum final | `final-verification-report.md` (dibuat oleh `verify_pack.py`). |
| 8 | Tanpa generasi, API berbayar, kredit, perubahan API key, atau perubahan master sheet | Semua terpenuhi. Hash master sheet diverifikasi tidak berubah. |

## 1. Storyboard final (6 klip, 9:16 dan 16:9)

| Klip | Durasi | Karakter | Shot | Kamera |
|------|--------|----------|------|--------|
| S01 · hook | 8 s | Rico | wide establishing → medium Rico mengintip dari batu berlumut | push-in pelan, tanpa cut |
| S02 · datang 1 | 4 s | Rico, Piko | two-shot di telur: Rico kiri, Piko melayang kanan-atas | statis, dorong sangat halus |
| S03 · datang 2 | 4 s | Rico, Lila, Bimo | three-shot: Rico kiri telur, Lila dan Bimo kanan | statis |
| S04 · datang 3 | 4 s | Rico, Tika | tight two-shot: Tika di atas dan belakang telur | statis, dorong sangat pelan |
| S05 · kilau 1 | 5 s | Rico, Lila, Bimo | three-shot seperti S03 | statis, dorong sangat pelan |
| S06 · kilau 2 | 5 s | Rico, Piko, Tika | medium-wide: Piko kanan-atas, leher Tika di belakang telur | pull-back halus + hold 1 detik |

Total 30 detik per rasio. Tidak ada klip dengan lebih dari 3 karakter. Setiap rasio diframing ulang, tidak di-crop. Rico selalu di kiri telur menghadapnya, dan Rico hadir di semua klip sebagai jangkar konsistensi.

## 2. Voice-over bahasa Inggris dan aksi

| Klip | Aksi | VO (English) | Kata |
|------|------|--------------|------|
| S01 | Rico mengintip, melihat telur berkilau, matanya melebar, melangkah mendekat | "One sunny morning, deep in the forest, Rico found something magical. A sparkling rainbow egg!" | 15 |
| S02 | Piko meluncur dari atas dan melayang dekat telur | "Piko swooped down to see the sparkle!" | 7 |
| S03 | Lila dan Bimo masuk dari kanan, berhenti di samping telur | "Lila and Bimo came to see it too!" | 8 |
| S04 | Leher panjang Tika turun dari atas | "Tika stretched up high to take a peek!" | 8 |
| S05 | Kilau telur makin terang menyinari wajah Rico, Lila, Bimo | "Together, they promised to keep the egg safe." | 9 |
| S06 | Kilau lembut pada Rico, Piko, Tika; pull-back; hold 1 detik | "Good friends always take care of special things, together!" | 9 |

Bahasa Inggris sederhana, hangat, mudah dipahami anak-anak secara internasional. Tidak ada kata ganti untuk karakter yang jenis kelaminnya tidak tertulis di sheet. VO tiap klip sekitar 3–7,5 detik pada tempo normal, selebihnya diisi musik, ambient, dan SFX, sehingga tidak ada jeda audio kosong (bagian 6).

## 3. Karakter, character lock, continuity lock

Lima karakter resmi, semuanya lulus gate `check-character-library.sh` (5/5 PASS). Lock hanya memuat yang tertulis atau terlihat di master sheet; sisanya "persis seperti sheet".

| Karakter | Lock (menurut sheet) |
|----------|----------------------|
| Rico | bayi dinosaurus fantasi; badan turquoise, perut krem, mata amber, **tiga tonjolan jingga** di kepala plus spike dan bintik jingga seperti di sheet; 3 jari kaki; ekor pendek melengkung |
| Lila | bayi triceratops; merah muda; tiga tanduk; frill merah muda |
| Bimo | bayi triceratops; kuning; tiga tanduk; frill kuning |
| Tika | bayi brachiosaurus; ungu; leher panjang; motif bintik |
| Piko | bayi pterodactyl; biru; sayap lebar; jambul biru |

**Continuity lock (di semua prompt):**
1. Setiap karakter disalin persis dari master sheet: bentuk wajah dan mata, bentuk kepala, bentuk tubuh, warna, proporsi, ciri khas. Tidak ada yang ditambah dan tidak ada yang dihilangkan.
2. Ukuran relatif tidak berubah antar scene: ukuran karakter terhadap satu sama lain, dan ukuran telur terhadap Rico, tetap seperti di master sheet dan di still terakhir yang disetujui. **Tanpa angka.**
3. Telur Pelangi seperti di sheet Rico (cangkang pelangi iridescent), ukuran dan posisi sama di petak bunga di samping batu berlumut; hanya objek diam.
4. Rico selalu di kiri telur menghadapnya; hutan dan arah cahaya emas dari kiri kamera sama di semua klip.
5. Hanya karakter yang tercantum untuk klip itu; tanpa makhluk lain atau duplikat; satu shot kontinu per klip.
6. Antar klip: posisi dan tingkat kilau telur dilanjutkan dari akhir klip sebelumnya.

**Catatan ukuran:** sheet Rico solo dan sheet grup mencantumkan ukuran absolut Rico yang berbeda (±40 cm vs ±0,8 m). Karena itu pack tidak memakai angka ukuran apa pun. Konsistensi dijaga lewat acuan visual pada sheet dan still yang disetujui.

## 4. Referensi gambar dan alur still bersih

| Klip | Still (gpt-image-2, maks 5) | Video (Seedance 2.0, maks 3) |
|------|-----------------------------|------------------------------|
| S01 | sheet Rico solo | img1 still S01, img2 sheet Rico solo |
| S02–S06 | sheet grup, sheet Rico solo, still klip sebelumnya | img1 still klip, img2 sheet grup, img3 still klip sebelumnya |

Alur: **(1)** buat still bersih per klip per rasio → **(2)** periksa dengan checklist QA, tolak jika ada lencana, teks, atau layout sheet → **(3)** Anda menyetujui still → **(4)** baru video dibuat dari still yang disetujui. Master sheet asli tidak pernah diubah atau ditimpa; path presigned hanya sekali pakai, jadi diunggah ulang per panggilan.

**Keterbatasan yang jujur:** sheet grup adalah satu gambar yang memuat kelima karakter, jadi karakter yang tidak hadir tetap terlihat pada gambar referensinya. Mitigasinya: prompt hanya menyebut karakter yang hadir dan memerintahkan "gunakan HANYA karakter yang disebut", serta QA menolak karakter yang muncul padahal tidak terdaftar. Alternatif yang lebih aman, tetapi menyimpang dari aturan library bahwa sheet dilampirkan di setiap panggilan: video hanya memakai still yang sudah disetujui. Belum diterapkan tanpa persetujuan Anda.

## 5. Negative prompt

Prompt gambar dan video memuat semua butir yang Anda minta: tidak ada redesain; wajah/bentuk mata, bentuk kepala, proporsi, dan warna berbeda; fitur asli hilang; anggota tubuh tambahan; karakter duplikat atau tidak sah; lencana, logo, watermark, teks, atau layout/latar lembar referensi; telur menetas, retak, berwajah, beranggota tubuh, atau hidup; cut kamera, kedipan, morphing, dan latar tidak konsisten. Video juga: karakter tidak berbicara (tanpa lip-sync).

**Disesuaikan per klip (tanpa memancing fitur):** negatif fitur hanya untuk karakter yang hadir:
- Rico: tanpa spike jingga lebih, kurang, atau berubah warna; mata amber tidak berubah.
- Lila dan Bimo: tanpa tanduk lebih atau kurang; frill tidak berubah.
- Tika: leher panjang dan bintik tidak berubah.
- Piko: tanpa sayap lebih atau kurang; jambul biru tidak berubah.

Contoh: klip S04 (Rico, Tika) tidak memuat kata "sayap", "tanduk", atau "frill".

**Sengaja tidak ditulis sebagai negatif:** "pakaian atau aksesori berubah". Kelima karakter tidak memakai pakaian atau aksesori di sheet, dan menyebutnya bisa memancing generator menambahkannya. Pencegahannya lewat aturan positif "tidak ada yang ditambah dan tidak ada yang dihilangkan". Frasa "karakter muncul di scene yang tidak terdaftar" ditulis sebagai "tanpa karakter tidak sah atau duplikat" tanpa menyebut nama karakter yang tidak hadir.

Arcads tidak punya field `negativePrompt`, jadi negatif ditulis di dalam teks prompt.

## 6. Arahan audio dan musik (seluruhnya bahasa Inggris)

- **Bahasa:** semua ucapan yang terdengar bahasa Inggris. Tidak ada bahasa Indonesia. Karakter tidak berbicara.
- **Narator:** satu narator untuk keenam klip: hangat, ramah, ceria, gaya pendongeng anak; bahasa Inggris internasional yang jelas dan natural; tempo sedang; suara dan pengaturan yang sama untuk semua baris.
- **Musik:** instrumental ceria, hangat, dan playful untuk anak (misalnya marimba, ukulele, glockenspiel, pizzicato lembut), tempo ringan, **satu bed 30 detik** di bawah semua klip, tanpa vokal atau lirik, penutup hangat saat hold terakhir. Prompt teknis: "Cheerful, warm, playful instrumental children's music, light marimba, ukulele and glockenspiel with soft pizzicato strings, gentle upbeat tempo, friendly and magical, no vocals, no lyrics, 30 seconds, soft warm resolving ending."
- **Ambient:** bed hutan lembut sepanjang 30 detik: angin pelan, daun, beberapa burung jauh.
- **SFX per klip (disinkronkan dengan aksi):**

| Klip | Cue |
|------|-----|
| S01 | 0–2 s gemerisik daun dan bunga saat mengintip; ±2,5 s dentingan ajaib lembut saat telur terlihat; 5–8 s langkah ringan di rumput |
| S02 | 0–1,5 s kepakan sayap lembut saat meluncur; 1,5–4 s kepakan ringan saat melayang |
| S03 | 0–3 s langkah ringan Lila dan Bimo; gemerisik daun kecil |
| S04 | 0–2 s gemerisik daun di atas saat leher turun; kicau burung kecil |
| S05 | kilau ajaib naik sebagai chime swell sepanjang klip; kicau burung lembut |
| S06 | kilau lembut bertahan; kicau burung; chime hangat di hold 1 detik terakhir lalu memudar |

Telur hanya berbunyi kilau, tidak pernah suara, detak, ketukan, atau retakan.

- **Mix:** VO selalu paling jelas; musik dan ambient diturunkan (ducking) di bawah setiap baris VO sehingga **musik tidak menutupi VO**; bed musik dan ambient berjalan **tanpa putus** (satu trek 30 detik, bukan per klip) sehingga tidak ada jeda audio kosong; sambungan klip di-crossfade 0,1–0,2 s; VO dimulai ±0,25 s setelah klip dimulai.
- **Jalur produksi (belum dijalankan):** klip video dibuat **senyap** (`audioEnabled: false` pada Seedance, sesuai pipeline repo) agar tidak ada suara liar atau ucapan non-Inggris. VO lewat ElevenLabs dengan satu suara (skrip repo `generate-vo-elevenlabs.sh`, bawaan suara pria Amerika hangat "Brian", dapat diganti; **pilihan suara menunggu persetujuan Anda**). Musik: skrip repo `generate-music-elevenlabs.sh` atau lagu berlisensi. Kedua skrip butuh kunci ElevenLabs milik Anda; **pack ini tidak meminta atau mengubah kunci apa pun**. **SFX:** repo ini tidak mendokumentasikan generator SFX, jadi dibutuhkan pustaka SFX berlisensi atau editor; tidak dibuat atau diverifikasi di sini.

## 7. Prompt image dan video

Semua prompt (6 klip × 2 rasio × image dan video, plus versi Omni opsional) ada di `prompts/prompt-pack.md`, siap disalin ke generator. Setiap prompt memuat character lock, setting lock, continuity lock, catatan referensi anti-layout, dan negatif yang disesuaikan. Prompt Seedance 292–338 kata, sedikit di atas target 260 dari panduan, karena daftar negatif Anda cukup panjang; `reference.md` tidak mencatat batas panjang prompt.

## 8. Checklist sebelum produksi

Hasil pemeriksaan otomatis: **lihat `final-verification-report.md`** (13 pemeriksaan: enam klip sesuai storyboard, maks 3 karakter, hanya karakter yang hadir, VO berbahasa Inggris, tanpa Pip/Moss, tanpa lencana, telur objek, lock lengkap, dua rasio, prompt siap generator, gate karakter, integritas master sheet, tidak ada media atau kredit).

Checklist manual sebelum dan selama produksi:
- [ ] Anda menyetujui storyboard, VO, dan arahan audio ini.
- [ ] Anda memilih suara narator dan sumber SFX.
- [ ] `.env` Arcads dan `PRODUCT_ID` siap, `check-requirements.sh` lulus (sekarang **BLOCKED**).
- [ ] Estimasi kredit dikonfirmasi di platform Arcads.
- [ ] Setiap still bersih diperiksa dan disetujui sebelum menjadi dasar video.
- [ ] QA setiap still dan klip (lihat `prompt-pack.md`), maksimal 2 retry per aset; bila klip bermasalah, pecah shot dan jangan retry terus.
- [ ] Setelah video: periksa audio (hanya narator Inggris, tanpa suara liar, musik tidak menutupi VO).

## 9. Jumlah kebutuhan

- Sheet karakter baru: **0** (memakai master sheet resmi).
- **Still image: 12** (6 klip × 2 rasio). **Klip video: 12** (6 klip × 2 rasio). Total **24 request**. Total video 30 detik × 2 rasio = 60 detik.
- **Estimasi** (bukan angka pasti): `reference.md` mencatat Seedance image-to-video ±48 credit/detik di 720p (divalidasi ulang 2026-05-19), jadi 60 detik ≈ **2.880 credit** untuk video, belum termasuk retry (maks 2 per aset). Biaya gambar gpt-image-2 tidak tercatat di log repo, jadi tidak saya perkirakan. Konfirmasikan harga di platform Arcads.

## 10. Yang menunggu keputusan Anda

1. Persetujuan akhir pack ini.
2. Suara narator (bawaan repo: "Brian") dan sumber musik serta SFX.
3. Referensi video: tetap sesuai aturan library (sheet dilampirkan), atau hanya still yang disetujui (lebih aman dari lencana, tetapi menyimpang dari aturan library).
4. `.env` Arcads dan `PRODUCT_ID` (saya tidak meminta atau mengubah kunci apa pun).
