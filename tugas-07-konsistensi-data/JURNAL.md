# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi
- Argumen yang dipertimbangkan:
Membandingkan antara *Sequential Consistency* (yang menuntut semua replika melihat urutan operasi secara identik namun memiliki latensi tinggi dan mahal) dan *Eventual Consistency* (yang cepat dan efisien, tetapi membiarkan replika berbeda sementara waktu tanpa kepastian waktu sinkron). Untuk data non-kritis seperti jumlah *like* media sosial, *Eventual Consistency* sudah sangat cukup. Namun, untuk saldo *e-wallet*, keterlambatan replikasi berdampak langsung pada kerugian bisnis nyata (misalnya pesanan ditolak padahal saldo cukup, risiko *double-spend*, dan memicu *churn* pelanggan).
  
- Kesimpulan akhir & alasan:
*Eventual Consistency* saja tidak cukup untuk saldo *e-wallet*. Pendekatan yang dipilih adalah mengombinasikannya dengan **Client-Centric Consistency (*Read-Your-Writes*)**. Hal ini karena sistem tidak membutuhkan keketatan global di semua replika secara serentak (yang mahal secara performa), melainkan konsistensi urutan operasi yang dijamin per akun pelanggan—sehingga pengguna yang baru melakukan *top-up* akan selalu langsung melihat pembaruan saldo mereka sendiri di server mana pun.

## Simulasi (jika dikerjakan)
- Hasil skenario naif vs Read-Your-Writes:
  - Pada pendekatan naif, pembacaan dari replika Bandung 0,5 detik setelah *top-up* pertama menghasilkan data basi (`0.0`), dan setelah *top-up* kedua menghasilkan nilai tertinggal (`50000.0` seharusnya `70000.0`) karena replikasi asinkron yang tertunda.
  - Pada pendekatan *Read-Your-Writes*, sistem berhasil mendeteksi versi lokal yang tertinggal lalu melakukan *redirect* pembacaan langsung ke server Jakarta, sehingga menghasilkan nilai saldo yang akurat (`70000.0`).

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
|17/11/2026|Gemini| "Jelaskan perbedaan Eventual vs Sequential Consistency dan mengapa data finansial butuh konsistensi lebih ketat." | Eventual hanya menjamin sinkron "pada akhirnya" (*stale read*), berisiko *double-spend* pada transaksi uang dibanding jumlah *like*. | Dikembangkan menjadi poin dampak bisnis FoodGo (order ditolak, *churn*, *double-spend*, audit) dan konsistensi per akun pada **Soal 1**. |
|17/11/2026|Gemini| "Apa solusi Client-Centric Consistency untuk mencegah user membaca data lama setelah melakukan update?" | Menyarankan *Read-Your-Writes* (RYW) dengan pelacakan nomor versi/timestamp di sisi klien. | Dirumuskan menjadi mekanisme 4 langkah pakai `versi_minimal` dan *redirect* baca dari Bandung ke Jakarta pada **Soal 2**. |
|17/11/2026|Gemini| "Bagaimana sintaks dasar membuat sequence diagram di Mermaid untuk alur sinkron dan asinkron?" | Memberikan contoh sintaks `sequenceDiagram`, `actor`/`participant`, panah `->>`/`-->>`, dan `autonumber`. | Dipakai untuk menggambar mandiri dua diagram alir urutan (skenario gagal *stale* & skenario *redirect* RYW) pada **Soal 3**. |
