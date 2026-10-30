# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): Pada awal implementasi, pencarian successor hanya memeriksa kondisi nilai node `>= key_hash`. Akibatnya, ketika nilai `key_hash` lebih besar daripada seluruh ID node yang ada di dalam *ring*, fungsi mengembalikan nilai kosong atau gagal karena tidak memperhitungkan sifat wrap-around dari topologi Chord.
- Cara memperbaikinya: Mengurutkan daftar ID node terlebih dahulu menggunakan `sorted()`, lalu melakukan iterasi pengecekan node `>= key_hash`. Jika perulangan selesai tanpa hasil, fungsi ditambahkan logika wrap-around untuk mengembalikan node pertama dengan ID terkecil di dalam ring (`sorted_nodes[0]`).

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: 
  - Sebelum: Sistem hanya mengandalkan 4 node awal untuk memetakan data kurir, dan pengujian *lookup* awal berhasil menemukan IP kurir terkait.
  - Sesudah: Setelah `node-medan-1` (id=123) bergabung, node baru ini masuk ke dalam urutan *ring* dan mengambil alih tanggung jawab data di rentangnya dari *successor* lama. Hasil *lookup* tetap akurat mengembalikan IP aslinya.
- Hasil sebelum & sesudah node keluar: 
  - Sebelum: node dikeluarkan, pencarian *lookup* berjalan normal melalui node tersebut.
  - Sesudah: `node-jakarta-1` dikeluarkan (`leave`), sistem secara otomatis memindahkan tanggung jawab data ke *successor* barunya yaitu `node-bandung-1` (id=40) melalui aturan wrap-around. Pengujian lookup untuk `kurir-001` dan `kurir-002` tetap berhasil mengembalikan alamat IP yang benar tanpa error.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 30/10/2026 | Gemini AI | Meminta brainstorming konsep logika *wrap-around* pada `find_successor` dan mekanisme perpindahan data saat node `join`/`leave` Chord DHT. | Memberikan kerangka logika *sorting keys*, pengecekan batas `>= key_hash`, serta penanganan *wrap-around* ke indeks pertama. | Konsep logika dipelajari untuk memahami aturan *successor*, lalu kode diketik/disesuaikan sendiri ke dalam struktur skrip `chord_simulation.py` dan diuji langsung di terminal. |
