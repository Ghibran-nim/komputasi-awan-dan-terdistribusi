"""
Tugas 4 - Jalur B: Publisher (simulasi modul Pembayaran)
Pastikan `docker compose up -d` sudah jalan sebelum menjalankan file ini.
"""

import pika
import json
import time

QUEUE_NAME = "pembayaran_berhasil"


def main():
    # TODO 1: buat koneksi ke RabbitMQ di localhost, lalu buat channel.
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # TODO 2: deklarasikan queue dengan durable=True
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    for i in range(1, 4):
        pesan = {
            "user_id": f"user{i}",
            "jumlah": 20000 * i,
            "timestamp": time.time(),
        }
        # TODO 3: publish `pesan` (di-encode json) ke QUEUE_NAME
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=json.dumps(pesan),
            properties=pika.BasicProperties(
                delivery_mode=2,  # Membuat pesan persisten
            ),
        )
        print(f"Event terkirim: {pesan}")
        time.sleep(1)

    # TODO 4: tutup koneksi
    connection.close()
    print("Publisher selesai mengirim event.")


if __name__ == "__main__":
    main()