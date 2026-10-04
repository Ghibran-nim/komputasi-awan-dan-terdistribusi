# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: 78
- Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): Terjadi lost update ketika multiple thread read dan merubah varibel global 'processed.count' secara bersamaan. Dua atau lebih thread membaca thread membaca nilai yang sama lalu update hasil increment, jadinya hasil increment lain hilang dan jadi hasil finalnya tidak mencapai 100.

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: 100

## Kendala Docker
- Error yang ditemui saat `docker build`/`docker run` dan cara memperbaikinya: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| --- | --- | --- | --- | --- |
|04 Oktober 2026|gemini|membantu menganalisis race condition pada foodGO|Inilisiasi dan penyiapan hal-hal yang dibutuhkan|menyusun struktur folder proyek serta menyiapkan konfigurasi awal file|
| ... | ... | ... | ... | ... |
