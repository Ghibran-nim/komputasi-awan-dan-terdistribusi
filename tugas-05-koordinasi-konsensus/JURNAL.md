# Jurnal Proses — Tugas 5

## Implementasi Bully
- Kendala saat mengisi TODO 1-4: ...

## Skenario 1: Start normal
- Leader yang terpilih: node 5
- Log/observasi:
  1. Ketika semua node di jalankan bersama, masing-masing langsung mengirim sebuah pesan ELECTION ke node dengan ID yg lebih besar
  2. Node 1, 2, 3, dan 4 menerima balasan OK dari node yang ID-nya lebih tinggi, jadi node-node tersebut cancel dan nunggu intruksi
  3. Node 5 tidak memiliki peer dengan ID yang lebih tinggi, sehingga langsung mendeklarasikan dirinya sebagai leader dan mem-broadcast pesan COORDINATOR ke seluruh node
  4. Seluruh node selain 5 mencatat Node 5 sebagai leader.

## Skenario 2: Leader dimatikan
- Leader baru yang terpilih: node 4
- Berapa lama waktu sampai leader baru terdeteksi: sepersekian detik / instan / 2-3detik
node 5 di force matiin, dan node 4 menjadi leader.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.


| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
| :--- | :--- | :--- | :--- | :--- |
| 20 Oktober 2026 | Gemini | Bagaimana alur logika Bully Algorithm dan cara menangani timeout socket di Python? | Menjelaskan alur komunikasi pesan (ELECTION, OK, COORDINATOR) serta menyarankan penggunaan threading.Event untuk timeout. | Memahami flow lalu mencoba mengimplementasikan ke code |
| ... | ... | ... | ... | ... |

