"""
Tugas 4 - Jalur B: Consumer (simulasi modul Kurir/Notifikasi)
Jalankan file ini SEBELUM publisher.py untuk uji normal, atau SESUDAHNYA
untuk membuktikan pesan tetap tersimpan di antrean (asynchronous decoupling).
"""

import pika
import json

QUEUE_NAME = "pembayaran_berhasil"


def callback(ch, method, properties, body):
    pesan = json.loads(body)
    # TODO 1: proses pesan
    print(f"Kurir menerima notifikasi pembayaran untuk {pesan['user_id']} sejumlah Rp {pesan['jumlah']:,.2f}")

    # TODO 2: kirim acknowledgement ke RabbitMQ (ch.basic_ack)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    # TODO 3: buat koneksi & channel, deklarasikan queue (durable=True), daftarkan callback
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)
    
    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=callback
    )

    print("Menunggu event dari antrean 'pembayaran_berhasil'... (Ctrl+C untuk berhenti)")

    # TODO 4: panggil channel.start_consuming()
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()


if __name__ == "__main__":
    main()