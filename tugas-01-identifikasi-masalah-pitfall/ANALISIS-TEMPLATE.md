# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| [nama 1] | [nim] | [pitfall/bagian yang dikerjakan] |
| Riyan Chandra Saputra | 103072400129 | Pitfall 2: Latency is Zero |
| [nama 3] | [nim] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: [nama pitfall] — ditulis oleh [nama]

**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** [penjelasan]

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]

---

## Pitfall 2: Latency is Zero — ditulis oleh Riyan Chandra Saputra

**Bukti di skenario:** Pada FoodGo, proses pemesanan melibatkan beberapa service, seperti pesanan, pembayaran, dan notifikasi. Dari beberapa service tersebut saling terhubung sehingga harus membutuhkan waktu untuk berkomunikasi antar service lainnya. Hal ini dapat dilihat ketika jumlah pesanan meningkat, aplikasi menjadi sangat lambat dan beberapa permintaan bahkan dapat mengalami timeout.

**Kenapa ini keliru:** Kesalahan yang terjadi adalah menganggap bahwa komunikasi antar service dapat berlangsung secara cepat tanpa membutuhkan waktu sama sekali. Pada dasarnya setiap suatu service ingin berkomunikasi dengan service lainnya, akan membutuhkan waktu juga. Ketika jumlah requst pada aplikasi semakin banyak, waktu yang dibutuhkan akan semakin lama untuk mendapat respons.

**Dampak ke FoodGo:** Ketika terjadi peningkatan pesanan yang sangat banyak, misalnya pada jam makan siang, keterlambatan dari setiap proses akan membuat request semakin menumpuk. Akibatnya, pengguna harus menunggu lebih lama bahkan beberapa request bisa mengalami timeout.

**Solusi desain awal:** Memberikan timeout untuk komunikasi antar service dan menggunakan proses asynchronus atau message queue untuk proses yang tidak perlu langsung dikerjakan, misalnya notifikasi.

**Trade-off:** Sistem menjadi lebih kompleks karena harus menambahkan komponen message queue. Ada juga beberapa data atau status tertentu mungkin yang tidak langsung diperbarui pada waktu yang sama dikarenakan proses berjalan secara asynchronus.

---

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
