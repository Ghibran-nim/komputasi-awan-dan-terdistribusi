# Jurnal Proses — Tugas 4

## Jalur yang dipilih
- [RPC / MQ / keduanya], alasan:
- Menggunakan RPC karna method RPC sendiri memastikan respon yang real time, jadi client bisa langsung tau status transaksi nya berhasil atau gagal.
- Menggunakan RabbitMQ karna di rabbitmq ada sistem decoupling, yang membuat sistem pembayaran dan modul bisa berjalan secara independen, jadi jika ada transaksi tinggal dimasukin ke dalam queue

## Kendala teknis
- Error saat setup (mis. koneksi RabbitMQ ditolak, port bentrok):
  1. akses port RabbitMQ tidak dapat langsung dibuka melalui URL biasa. Dibuka melalui fitur ports yang tersedia di codespace karena pengerjaan yang digunakan melalui github codespace.

## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati: pesan tersimpan aman di dashboard RabbitMQ, terlihat status pesan ready bertambah/menumpuk di dashboard). Saat consumer dinyalakan seluruh pesan yang menumpuk lamgsung diambil dan diproses secara otomastis hingga status antrean kembali 0.(sesuai bukti screenshoot)

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 11 Oktober 2026 | GeminiAI | cara mengakses dashboard RabbitMQ di codespace | menjelaskan bahwa port 15672 dapat dibuka langsung melalui fitur ports yang tersedia di codespace | membuka tab "ports" pada codespace, lalu mengakses dashboard RabbitMQ melalui localhost:15672 tersebut |
