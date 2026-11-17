# Audit jalur produksi Rico & Friends (tanpa Arcads Pro)

Tanggal audit: 2026-11-17. Status: **audit dan rekomendasi saja. Tidak ada pembelian, transaksi, atau generasi berbayar. Library dan pack Rico & Friends tidak diubah.**

## 1. Yang terverifikasi di lingkungan ini

| Area | Hasil | Cara memeriksa |
|------|-------|----------------|
| Konektor, plugin, resource MCP terpasang | **Tidak ada** | `ListConnectors`, `ListPlugins`, `ListMcpResourcesTool` semuanya kosong |
| Registry MCP (cakupan sebagian) | Tidak ada MCP generator gambar/video yang cocok. Yang muncul: Hugging Face (resmi; mencari model dan Gradio Spaces), Picsart Media Studio (penyuntingan video), Canva, Orshot (template), ElevenLabs (agen suara), Speko (narasi) | `SearchMcpRegistry` |
| Jaringan sandbox | Diblokir proxy (tanpa kredensial): Arcads, OpenAI, fal, Replicate, Together, Hugging Face, Stability, Black Forest Labs, Runway, Luma, Kling, MiniMax, ElevenLabs, Cloudflare, OpenRouter, WaveSpeed, Segmind, ModelsLab, Novita. **Terjangkau: `generativelanguage.googleapis.com` (API Gemini asli: tanpa kunci mengembalikan 403 PERMISSION_DENIED), `aiplatform.googleapis.com`, PyPI, npm, GitHub.** Situs dokumentasi `ai.google.dev` **tidak** terjangkau | `curl` ke tiap host |
| Perangkat keras | 4 CPU, 15 GB RAM, **tanpa GPU**, bobot model tidak bisa diunduh (Hugging Face diblokir): generasi lokal tidak layak | `nproc`, `free`, `nvidia-smi` |
| SDK resmi `google-genai` 3.4.0 | Terpasang dari PyPI. Dari kodenya terverifikasi: `generate_videos` mendukung `reference_images`, `aspect_ratio`, `duration_seconds`, `generate_audio` (audio dapat dimatikan), `negative_prompt`, `seed`, `last_frame`; gambar lewat `generate_content` dengan `image_config.aspect_ratio` dan banyak gambar masukan; suara lewat `speech_config` dengan nama voice bawaan | introspeksi SDK |
| Perakitan video akhir | **Terbukti** (`scripts/assemble_final.py`, hanya ffmpeg): enam klip, VO ditempatkan 0,25 s setelah klip dimulai, bed musik/ambient satu trek, ducking di bawah VO (−38,5 dB menjadi −50,4 dB), 0 jendela hening, durasi video dan audio sama 30,000 s, mendukung 9:16 dan 16:9, menolak VO yang lebih panjang dari klipnya. Diuji dengan **media sintetis**, bukan konten Rico | uji lokal |
| QA teks/lencana otomatis | **Terbukti** (`scripts/qa_text_check.py`, OCR offline): lencana "MARVELY" pada sheet grup terdeteksi (145 teks), frame bersih lolos, teks "LYLA MARVELY" yang disisipkan ditolak | uji lokal |
| QA identitas karakter | Claude dapat melihat gambar (terbukti di sesi ini) dan membandingkannya berdampingan dengan master sheet memakai checklist QA pack | kemampuan bawaan |

## 2. Yang TIDAK terverifikasi (jangan dianggap fakta)

Dokumentasi resmi Google tidak dapat dibuka dari sandbox, jadi **harga, tingkat gratis, ID model yang aktif, dan jumlah maksimum gambar referensi belum terverifikasi.** Hasil pencarian web hanya blog pihak ketiga yang saling bertentangan. Klaim yang beredar (belum terverifikasi): model gambar Nano Banana 2/Pro tidak punya tingkat gratis di API (±US$0,04–0,15 per gambar); Veo di API tidak punya tingkat gratis (±US$0,12–0,40 per detik); model gambar lama mungkin punya kuota gratis; konten tingkat gratis dapat dipakai Google untuk perbaikan produk.

## 3. Penilaian terhadap enam kriteria

| Kriteria | Jalur A: Gemini API (satu kunci AI Studio) | Hugging Face MCP | fal / Replicate / OpenAI / Runway / Kling | Lokal |
|----------|---------------------------------------------|------------------|--------------------------------------------|-------|
| 1. Terintegrasi dengan Claude Code | Ya (SDK Python; host sudah terjangkau) | Ya, tetapi harus Anda pasang sebagai konektor | Butuh izin host di lingkungan + akun | Tidak layak |
| 2. API/MCP benar-benar tersedia | Terverifikasi (endpoint dan SDK) | Terdaftar di registry | Host diblokir; belum terverifikasi | Tidak ada GPU |
| 3. Referensi master sheet | SDK mendukung; batas jumlah belum terverifikasi | Tergantung Space | Belum terverifikasi | — |
| 4. Gambar dan image-to-video | SDK mendukung keduanya; ketersediaan model belum terverifikasi | Tidak ada jaminan kualitas dan kuota | Belum terverifikasi | — |
| 5. Biaya / opsi gratis | **Belum terverifikasi** (lihat bagian 4) | Gratis, kuota kecil, antrean | Belum terverifikasi | Gratis, tidak berfungsi |
| 6. Tanpa mengulang proyek | Ya (library dan pack tetap) | Ya | Ya | — |

## 4. Rekomendasi satu jalur

**Gemini API (satu kunci Google AI Studio) untuk gambar, image-to-video, dan narasi; Claude sebagai pemeriksa konsistensi; ffmpeg untuk perakitan.**

Alasan: ini satu-satunya penyedia generatif yang endpoint dan SDK-nya terbukti dapat dijangkau dari sini tanpa mengubah jaringan, mencakup ketiga kebutuhan dengan satu kunci, dan seluruh sistem Anda (library, pack, verifikasi) tetap dipakai.

Pembagian kerja:
1. **Gambar:** model gambar Gemini dengan master sheet dan still sebelumnya sebagai referensi; prompt image dari pack dipakai tanpa diubah (netral model).
2. **Konsistensi:** `qa_text_check.py` (teks/lencana) lalu tinjauan visual Claude berdampingan dengan sheet memakai checklist pack, lalu persetujuan Anda.
3. **Video:** `generate_videos` dari still yang disetujui, 9:16, `generate_audio=False`, `negative_prompt`, `seed`.
4. **Suara:** Gemini TTS (kunci yang sama). Suara "Brian" milik ElevenLabs, jadi suara pengganti dipilih dari voice bawaan Gemini; Brian tetap opsi nanti. Musik, ambient, dan SFX: berkas berlisensi/bebas royalti yang Anda sediakan sekali (tidak ada generator terverifikasi untuk ini).
5. **Hasil akhir:** `assemble_final.py`.

Uji tanpa biaya sebelum memutuskan apa pun:
1. Anda membuat **kunci gratis** di Google AI Studio (**tanpa kartu, tanpa mengaktifkan billing**).
2. Kunci disimpan di lingkungan lewat jalur aman (header `x-goog-api-key` untuk host `generativelanguage.googleapis.com`).
3. Claude menjalankan `models.list` (tidak menghasilkan apa pun) untuk melihat model gambar, video, dan TTS yang benar-benar tersedia di kunci itu, lalu satu uji gambar kecil. Tanpa billing, model berbayar menurut dokumentasi billing Google (via ringkasan hasil pencarian, belum dibaca langsung) akan menolak panggilan, bukan menagih.
4. Keputusan diambil dari fakta itu. Jika video ternyata hanya berbayar, pilihannya: (a) bayar per pemakaian khusus Veo dengan batas yang Anda tetapkan di akun Google, atau (b) fallback tanpa biaya: gambar dari Gemini dan gerak sederhana (zoom/parallax) dari still lewat ffmpeg. Itu bukan image-to-video generatif, tetapi bisa menghasilkan Shorts.

Yang akan ditambahkan setelah Anda menyetujui (hanya file baru): adapter `gemini` untuk gambar, video, dan TTS di `skills/pixar-animation-video/providers/gemini/`, varian prompt video tanpa token `@(imgN)` khas Seedance, dan log pemanggilan. Tidak ada file yang dihapus atau diganti.

## 5. Risiko yang perlu dicek
- Kebijakan Google untuk karakter anak (LYLA-Education) pada video: parameter `person_generation` ada di SDK, nilai yang diizinkan belum terverifikasi. Rico & Friends adalah hewan kartun.
- Tingkat gratis dapat memakai konten Anda untuk perbaikan produk; master sheet adalah IP Anda. Periksa Terms sebelum mengunggahnya.
- Watermark tak terlihat pada keluaran: kemungkinan, belum terverifikasi.
- Tidak ada batas biaya keras yang terverifikasi; jangan mengaktifkan billing sebelum angka sebenarnya dibaca.
- Kredensial sandbox Google (gcloud) milik infrastruktur sesi, **bukan** untuk produksi ini, dan tidak dipakai.
