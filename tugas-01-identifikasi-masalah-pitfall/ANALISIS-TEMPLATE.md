# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| [Anandhaka Ghibran MAS] | [103072400135] | [Pitfall 1:The Network Is Reliable] |
| Riyan Chandra Saputra | 103072400129 | Pitfall 2: Latency is Zero |
| Achbarul Filmi | 103072400166 | Pitfall 3:  |

## Pitfall 1: [network is always reliable, no need for retry] — ditulis oleh [Anandhaka Ghibran MAS]

**Bukti di skenario:** Pada point ke 3 yaitu "Tim menemukan bahwa kode mereka menulis asumsi seperti # network is always reliable, no need for retry dan tidak ada timeout sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu)."

**Kenapa ini keliru:** Dalam sebuah sistem apalagi sistem terdistribusi, komunikasi yang dilakukan melalui jaringann tidak mungkin tidak mengalami sebuah error setidaknya sekali. Request dapat mengalami keterlambatan, packet loss, koneksi terputus, atau service tujuan tidak merespons. Asumsi yang menganggap jaringan selalu reliable membuat tidak adanya sistem yang memiliki mekanisme penanganan saat terjadi gagal komunikasi atau sistem pencegahnya.

**Dampak ke FoodGo:** Jika salah satu service mengalami gangguan, service lain yang sedang menunggu respons dapat ikut mengalami masalah. Request bisa menumpuk dan waktu respons menjadi semakin lama. Jika kondisi tersebut terjadi ketika jumlah pesanan sedang tinggi, beberapa request dapat mengalami timeout dan membuat aplikasi menjadi tidak responsif.

**Solusi desain awal:** FoodGo dapat menerapkan timeout agar sistem tidak menunggu respons terlalu lama. Selain itu, dapat digunakan mekanisme retry ketika terjadi kegagalan sementara, misalnya dengan memberikan jeda sebelum mencoba kembali. Untuk mencegah service yang bermasalah terus menerima request, FoodGo juga dapat menggunakan circuit breaker.

**Trade-off:** Penggunaan retry memang dapat membantu ketika terjadi gangguan sementara, tetapi jika dilakukan terlalu sering justru dapat menambah beban pada service yang sedang bermasalah. Karena itu, jumlah percobaan perlu dibatasi dan dapat menggunakan exponential backoff. Selain itu, penggunaan message queue dan circuit breaker membuat sistem menjadi lebih kompleks karena membutuhkan komponen dan pengelolaan tambahan.

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
