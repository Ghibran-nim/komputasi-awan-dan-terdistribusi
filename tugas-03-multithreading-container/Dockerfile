# TODO 1: Pilih base image Python resmi yang ringan (cari tag "slim" di Docker Hub).
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# TODO 3: Tulis perintah default yang dijalankan saat container start,
# yaitu menjalankan src/order_simulator.py dengan python3.
RUN mkdir -p /app/bukti
CMD ["python", "src/order_simulator.py"]
