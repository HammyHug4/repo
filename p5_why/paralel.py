import multiprocessing as mp
import os
import time
from datetime import datetime
import ctypes


# ============================================================
# WINDOWS API
# ============================================================

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

GetCurrentProcess = kernel32.GetCurrentProcess
GetCurrentProcess.restype = ctypes.c_void_p

SetProcessAffinityMask = kernel32.SetProcessAffinityMask
SetProcessAffinityMask.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t
]
SetProcessAffinityMask.restype = ctypes.c_int


# ============================================================
# DATA ANGKA
# ============================================================

data_angka = [
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    13, 14, 15, 16
]


# ============================================================
# MENGUNCI PROCESS KE CORE
# ============================================================

def set_core(core):

    handle = GetCurrentProcess()

    # Core 1 = 0
    # Core 2 = 1

    mask = 1 << core

    berhasil = SetProcessAffinityMask(
        handle,
        mask
    )

    return berhasil != 0


# ============================================================
# FUNGSI TUGAS
# ============================================================

def hitung_kuadrat(nama_tugas, data, core, queue):

    # --------------------------------------------------------
    # PID PROCESS
    # --------------------------------------------------------

    pid = os.getpid()


    # --------------------------------------------------------
    # KUNCI PROCESS KE CORE
    # --------------------------------------------------------

    affinity = set_core(core)

    waktu_mulai = time.perf_counter()

    print(
        f"\n{nama_tugas} DIMULAI "
        f"| PID {pid} "
        f"| Core {core + 1}",
        flush=True
    )


    hasil_tugas = []


    # ========================================================
    # PERHITUNGAN
    # ========================================================

    for angka in data:

        # Perhitungan sebenarnya
        hasil = angka * angka

        hasil_tugas.append(hasil)


        # ----------------------------------------------------
        # OUTPUT
        # ----------------------------------------------------

        print(
            f"{nama_tugas} | "
            f"{angka}*{angka} = {hasil} | "
            f"Core {core + 1} | "
            f"PID {pid}",
            flush=True
        )


        # ----------------------------------------------------
        # Simulasi proses agar paralel terlihat jelas
        # ----------------------------------------------------

        time.sleep(0.3)


    waktu_selesai = time.perf_counter()


    # ========================================================
    # SELESAI
    # ========================================================

    print(
        f"{nama_tugas} SELESAI "
        f"| PID {pid} "
        f"| Core {core + 1} "
        f"| Durasi "
        f"{waktu_selesai - waktu_mulai:.3f} detik",
        flush=True
    )


    # Kirim hasil ke process utama

    queue.put({
        "tugas": nama_tugas,
        "hasil": hasil_tugas,
        "pid": pid,
        "core": core + 1
    })


# ============================================================
# PROGRAM UTAMA
# ============================================================

if __name__ == "__main__":

    mp.freeze_support()


    print("=" * 75)
    print("PROGRAM PERHITUNGAN KUADRAT - MODE PARALEL")
    print("=" * 75)


    print(
        f"CPU tersedia : {os.cpu_count()}"
    )

    print(
        f"Jumlah data  : {len(data_angka)}"
    )

    print(
        f"Data         : {data_angka}"
    )


    # ========================================================
    # BAGI DATA
    # ========================================================

    tengah = (len(data_angka) + 1) // 2

    data_a = data_angka[:tengah]
    data_b = data_angka[tengah:]


    print()
    print("=" * 75)
    print("PEMBAGIAN DATA")
    print("=" * 75)

    print(
        f"Tugas A -> Core 1 : {data_a}"
    )

    print(
        f"Tugas B -> Core 2 : {data_b}"
    )


    # ========================================================
    # QUEUE
    # ========================================================

    queue = mp.Queue()


    # ========================================================
    # WAKTU PROGRAM
    # ========================================================

    waktu_mulai = time.perf_counter()

    waktu_mulai_real = datetime.now()


    # ========================================================
    # BUAT PROCESS A
    # ========================================================

    print()
    print(">>> MEMBUAT PROCESS TUGAS A")

    proses_a = mp.Process(
        target=hitung_kuadrat,
        args=(
            "TUGAS A",
            data_a,
            0,
            queue
        )
    )


    # ========================================================
    # BUAT PROCESS B
    # ========================================================

    print(">>> MEMBUAT PROCESS TUGAS B")

    proses_b = mp.Process(
        target=hitung_kuadrat,
        args=(
            "TUGAS B",
            data_b,
            1,
            queue
        )
    )


    # ========================================================
    # MULAI PROCESS A
    # ========================================================

    print()
    print("=" * 75)
    print(">>> MEMULAI TUGAS A DAN TUGAS B SECARA PARALEL")
    print("=" * 75)


    proses_a.start()

    print(
        f"Tugas A berjalan "
        f"| PID {proses_a.pid} "
        f"| Core 1"
    )


    # ========================================================
    # LANGSUNG MULAI PROCESS B
    # TIDAK MENUNGGU A SELESAI
    # ========================================================

    proses_b.start()

    print(
        f"Tugas B berjalan "
        f"| PID {proses_b.pid} "
        f"| Core 2"
    )


    # ========================================================
    # TUNGGU KEDUANYA SELESAI
    # ========================================================

    proses_a.join()

    proses_b.join()


    # ========================================================
    # AMBIL HASIL
    # ========================================================

    hasil_a = queue.get()

    hasil_b = queue.get()


    # ========================================================
    # WAKTU SELESAI
    # ========================================================

    waktu_selesai = time.perf_counter()

    waktu_selesai_real = datetime.now()


    # ========================================================
    # HASIL AKHIR
    # ========================================================

    print()
    print()
    print("=" * 75)
    print("HASIL AKHIR")
    print("=" * 75)


    total_a = sum(hasil_a["hasil"])

    total_b = sum(hasil_b["hasil"])


    # --------------------------------------------------------
    # HASIL A
    # --------------------------------------------------------

    print()
    print("TUGAS A")
    print("-" * 75)

    for angka, hasil in zip(
        data_a,
        hasil_a["hasil"]
    ):

        print(
            f"{angka}*{angka} = {hasil} "
            f"| Tugas A "
            f"| Core {hasil_a['core']} "
            f"| PID {hasil_a['pid']}"
        )


    print(
        f"TOTAL TUGAS A = {total_a}"
    )


    # --------------------------------------------------------
    # HASIL B
    # --------------------------------------------------------

    print()
    print("TUGAS B")
    print("-" * 75)

    for angka, hasil in zip(
        data_b,
        hasil_b["hasil"]
    ):

        print(
            f"{angka}*{angka} = {hasil} "
            f"| Tugas B "
            f"| Core {hasil_b['core']} "
            f"| PID {hasil_b['pid']}"
        )


    print(
        f"TOTAL TUGAS B = {total_b}"
    )


    # ========================================================
    # TOTAL
    # ========================================================

    total_akhir = total_a + total_b


    print()
    print("=" * 75)
    print("TOTAL KESELURUHAN")
    print("=" * 75)

    print(
        f"Total Tugas A : {total_a}"
    )

    print(
        f"Total Tugas B : {total_b}"
    )

    print(
        f"TOTAL AKHIR   : {total_akhir}"
    )


    # ========================================================
    # WAKTU
    # ========================================================

    print()
    print("=" * 75)
    print("INFORMASI WAKTU")
    print("=" * 75)

    print(
        "Waktu mulai   : "
        f"{waktu_mulai_real.strftime('%H:%M:%S.%f')[:-3]}"
    )

    print(
        "Waktu selesai : "
        f"{waktu_selesai_real.strftime('%H:%M:%S.%f')[:-3]}"
    )

    print(
        "Total waktu   : "
        f"{waktu_selesai - waktu_mulai:.3f} detik"
    )


    print()
    print("=" * 75)
    print("PROGRAM SELESAI")
    print("=" * 75)
