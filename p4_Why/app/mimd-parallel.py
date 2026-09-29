import os
import time
import numpy as np
from multiprocessing import Process, Queue

N = 50000000000000000000000000000000000000000_000_000_000_000_000_000_000_000_000_000_000_000_000
SEPARUH = N // 2

# Instruksi 1: Dipanggil oleh Proses 1
def tugas_partisi_1(queue):
    data = np.arange(1, SEPARUH + 1, dtype=np.float64)
    hasil = np.sum(data * data)
    queue.put(('Partisi 1 (x * x)', hasil))

# Instruksi 2: Dipanggil oleh Proses 2
def tugas_partisi_2(queue):
    data = np.arange(SEPARUH + 1, N + 1, dtype=np.float64)
    hasil = np.sum(np.power(data, 2))
    queue.put(('Partisi 2 (np.power)', hasil))

if __name__ == "__main__":
    cores_used = os.environ.get("CORES_USED", "1")
    print(f"=== Pengujian MIMD ({cores_used} Core Limit) ===")

    start_time = time.time()
    queue = Queue()

    # Inisialisasi 2 proses dengan instruksi dan data yang berbeda
    p1 = Process(target=tugas_partisi_1, args=(queue,))
    p2 = Process(target=tugas_partisi_2, args=(queue,))

    # Jalankan kedua proses
    p1.start()
    p2.start()

    # Tunggu kedua proses selesai
    p1.join()
    p2.join()

    # Ambil hasil dari Queue
    total = 0
    while not queue.empty():
        label, hasil = queue.get()
        print(f"{label} -> Hasil: {hasil:.0f}")
        total += hasil

    durasi = time.time() - start_time
    print(f"Total Sum    : {total:.0f}")
    print(f"Waktu Proses : {durasi:.4f} detik\n")
