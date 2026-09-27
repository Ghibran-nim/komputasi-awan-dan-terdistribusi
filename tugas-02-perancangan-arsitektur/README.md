# Tugas 2 (Pekan 2) — Perancangan Arsitektur untuk FoodGo

**Materi terkait:** Architectural style (Layered, SOA, Peer-to-Peer, Publish-Subscribe).

## Studi Kasus

Melanjutkan Tugas 1: FoodGo butuh sistem yang **decoupled** agar tim kurir dan tim resto tidak saling mengganggu ketika salah satu modul diperbarui/deploy ulang. Saat ini semua modul (pesanan, pembayaran, notifikasi kurir, katalog resto) berjalan sebagai satu aplikasi monolitik — sekali deploy, semua modul ikut restart dan berisiko downtime total.

## Tugas Kelompok

1. Pilih **satu** gaya arsitektur utama: **Service-Oriented Architecture (SOA)** atau **Publish-Subscribe**. Boleh dikombinasikan (mis. SOA untuk service inti + Pub-Sub untuk notifikasi), tapi harus dijustifikasi kenapa kombinasi ini yang dipilih.
2. Gambarkan minimal 4 komponen berikut dan interaksinya: modul Pesanan, modul Pembayaran, modul Kurir/Notifikasi, modul Katalog Resto (dan message broker/API gateway jika relevan).
3. Jelaskan alur satu skenario penuh secara end-to-end di diagram (misalnya: pelanggan buat pesanan → bayar → resto terima notifikasi → kurir ditugaskan) — tunjukkan komponen mana berkomunikasi dengan siapa, dan **jenis komunikasinya** (sinkron/asinkron, request-response/event).
4. Analisis tertulis: kenapa gaya ini mengatasi masalah *coupling* dari Tugas 1, dan apa trade-off-nya (mis. Pub-Sub menambah kompleksitas debugging karena alur tidak linear).

## Cara Membuat Diagram (Gratis, Cukup Laptop)

Tidak perlu software berbayar. Dua opsi:

**Opsi A — Mermaid di dalam Markdown (disarankan).** Ditulis sebagai teks biasa di `README.md`, otomatis dirender jadi diagram oleh GitHub — tidak perlu install apa pun.

````markdown
```mermaid
graph LR
  Client[Pelanggan] -->|HTTP request pesan| OrderSvc[Service Pesanan]
  OrderSvc -->|RPC sinkron| PaymentSvc[Service Pembayaran]
  OrderSvc -->|publish event OrderCreated| Broker[(Message Broker)]
  Broker -->|subscribe| NotifSvc[Service Notifikasi Kurir]
  Broker -->|subscribe| RestoSvc[Service Katalog Resto]
```
````

**Opsi B — draw.io / diagrams.net** (gratis, jalan di browser tanpa akun, atau app desktop offline di [app.diagrams.net](https://app.diagrams.net/)). Ekspor sebagai `.png` dan simpan di folder `diagram/`.

## Struktur Submission

```
tugas-02-perancangan-arsitektur/
├── README.md          # Analisis + diagram Mermaid (jika Opsi A) atau referensi ke diagram/
├── JURNAL.md
└── diagram/            # File .png/.drawio jika pakai Opsi B
```

## Rubrik Penilaian (Tugas 2)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan pemilihan gaya arsitektur | 20% | Justifikasi SOA/Pub-Sub sesuai kebutuhan *decoupling* di skenario |
| Kelengkapan & kejelasan diagram | 30% | Semua komponen kunci ada, jenis komunikasi (sinkron/asinkron) jelas ditandai |
| Analisis trade-off | 30% | Bukan hanya kelebihan — kekurangan/kompleksitas baru juga dibahas |
| Proses & kontribusi kelompok | 20% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh memakai AI untuk brainstorming komponen apa saja yang umum ada di gaya arsitektur SOA/Pub-Sub; **tidak boleh** meminta AI menggambar diagram final atau menuliskan analisis trade-off yang tinggal ditempel. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Diagram Mermaid/draw.io yang "terlalu generik" (identik dengan contoh tutorial di internet tanpa penyesuaian ke kasus FoodGo) akan dinilai rendah pada komponen kelengkapan & kejelasan diagram.


## Jawaban diskusi kami:

1. Kami memiih Service-Oriented Architecture(SOA) yang dikombinasikan dengan Publish-Subscribe. SOA berfungsi untuk memisahkan sistem menjadi beberapa service, seperti Pesanan, Pembayaran, Katalog Resto, dan Kurir/Notifikasi. Publish-Subscribe untuk komunikasi asinkron melalui Message Broker untuk event seperti pembayaran berhasil, notifikasi restoran, dan penugasan kurir.

2. Diagram
```mermaid
graph LR
    C[Customer] -->|Sync Request| API[API Gateway]
    API -->|Sync| O[Order Service]
    O -->|Sync Request/Response| K[Catalog Service]
    O -->|Sync Request/Response - Timeout| P[Payment Service]
    P -->|Async Event: PaymentSuccessful| MB[(Message Broker)]
    MB -->|Async Event| O
    O -->|Async Event: OrderConfirmed| MB
    MB -->|Async Event| N[Courier / Notification Service]
    N -->|Async Notification| R[Restaurant]
    N -->|Async Assignment| CR[Courier]
    N -->|Async Event: CourierAssigned| MB'''
```

3. Alur dimulai ketika pelanggan membuat pesanan melalui aplikasi FoodGo. Pesanan dikirim ke API Gateway secara sinkron menggunakan request-response, kemudian diteruskan ke Order Service. Order Service melakukan pengecekan menu, harga, dan ketersediaan ke Catalog Service secara sinkron. Setelah itu, Order Service mengirim permintaan pembayaran ke Payment Service secara sinkron dengan menggunakan timeout agar sistem tidak menunggu tanpa batas waktu.

Jika pembayaran berhasil, Payment Service mengirim event "PaymentSuccessful" ke Message Broker secara asinkron. Event tersebut kemudian diterima oleh Order Service untuk mengonfirmasi pesanan. Setelah pesanan dikonfirmasi, Order Service mengirim event "OrderConfirmed" ke Message Broker.

Message Broker kemudian meneruskan event tersebut ke Courier/Notification Service secara asinkron. Service ini mengirim notifikasi pesanan kepada restoran dan melakukan penugasan kurir. Setelah kurir ditugaskan, informasi penugasan dikirim kepada kurir secara asinkron. Dengan cara ini, proses yang membutuhkan respons langsung menggunakan komunikasi sinkron, sedangkan notifikasi dan pembaruan status menggunakan komunikasi asinkron melalui Message Broker.

4. 
