import multiprocessing as mp
import os
import time
import ctypes
from datetime import datetime


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
]


# ============================================================
# MENGUNCI PROCESS KE CORE TERTENTU
# ============================================================

def set_core(core):

    """
    Core 1 -> core = 0
    Core 2 -> core = 1
    """

    handle = GetCurrentProcess()

    # CPU affinity mask
    mask = 1 << core

    berhasil = SetProcessAffinityMask(
        handle,
        mask
    )

    return berhasil != 0


# ============================================================
# MENDAPATKAN CORE AFFINITY PROCESS
# ============================================================

def get_core_from_affinity(core):

    """
    Karena process sudah dikunci ke satu core,
    kita tahu process tersebut hanya boleh berjalan
    pada core tersebut.
    """

    return core + 1


# ============================================================
# FUNGSI PERHITUNGAN
# ============================================================

def hitung_kuadrat(nama_tugas, data, core):

    pid = os.getpid()

    # --------------------------------------------------------
    # KUNCI PROCESS KE CORE
    # --------------------------------------------------------

    affinity_berhasil = set_core(core)

    core_terkunci = get_core_from_affinity(core)

    waktu_mulai = time.perf_counter()

    print()
    print("=" * 70)
    print(f"{nama_tugas} DIMULAI")
    print("=" * 70)

    print(f"PID          : {pid}")
    print(f"Core         : Core {core_terkunci}")

    if affinity_berhasil:
        print("CPU affinity  : BERHASIL")
    else:
        print("CPU affinity  : GAGAL")

    print(
        "Waktu mulai  : "
        f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}"
    )

    print()


    hasil = []


    # ========================================================
    # PERHITUNGAN SEBENARNYA
    # ========================================================

    for angka in data:

        # Perhitungan benar-benar dilakukan di sini
        hasil_kuadrat = angka * angka

        hasil.append(hasil_kuadrat)


        # Informasi Core berasal dari konfigurasi
        # CPU affinity process, bukan angka acak
        print(
            f"{angka}*{angka} = {hasil_kuadrat} "
            f"| {nama_tugas} "
            f"| Core {core_terkunci} "
            f"| PID {pid}",
            flush=True
        )

        time.sleep(0.2)


    waktu_selesai = time.perf_counter()

    print()
    print("-" * 70)
    print(f"{nama_tugas} SELESAI")
    print(
        f"Core         : Core {core_terkunci}"
    )
    print(
        f"PID          : {pid}"
    )
    print(
        f"Durasi       : "
        f"{waktu_selesai - waktu_mulai:.3f} detik"
    )
    print("-" * 70)


# ============================================================
# PROGRAM UTAMA
# ============================================================

if __name__ == "__main__":

    mp.freeze_support()


    print("=" * 70)
    print("PROGRAM PERHITUNGAN KUADRAT")
    print("=" * 70)

    print(
        f"CPU logical processor tersedia : "
        f"{os.cpu_count()}"
    )

    print(
        f"Jumlah data : {len(data_angka)}"
    )

    print(
        f"Data        : {data_angka}"
    )


    # ========================================================
    # BAGI DATA MENJADI TUGAS A DAN B
    # ========================================================

    tengah = (len(data_angka) + 1) // 2

    data_a = data_angka[:tengah]
    data_b = data_angka[tengah:]


    print()
    print("=" * 70)
    print("PEMBAGIAN DATA")
    print("=" * 70)

    print(f"Tugas A -> Core 1 : {data_a}")
    print(f"Tugas B -> Core 2 : {data_b}")


    # ========================================================
    # WAKTU PROGRAM
    # ========================================================

    waktu_mulai = time.perf_counter()

    waktu_mulai_real = datetime.now()


    # ========================================================
    # TUGAS A
    # ========================================================

    print()
    print("=" * 70)
    print(">>> MEMBUAT PROCESS TUGAS A")
    print("=" * 70)


    proses_a = mp.Process(
        target=hitung_kuadrat,
        args=(
            "TUGAS A",
            data_a,
            0       # Core 1
        )
    )


    proses_a.start()

    print(
        f">>> Tugas A berjalan dengan PID "
        f"{proses_a.pid}"
    )


    # --------------------------------------------------------
    # TUNGGU TUGAS A SAMPAI SELESAI
    # --------------------------------------------------------

    proses_a.join()


    print()
    print("=" * 70)
    print(">>> TUGAS A SELESAI")
    print(">>> CORE 1 SELESAI")
    print(">>> SEKARANG TUGAS B DIMULAI")
    print("=" * 70)


    # ========================================================
    # TUGAS B
    # ========================================================

    proses_b = mp.Process(
        target=hitung_kuadrat,
        args=(
            "TUGAS B",
            data_b,
            1       # Core 2
        )
    )


    proses_b.start()

    print(
        f">>> Tugas B berjalan dengan PID "
        f"{proses_b.pid}"
    )


    # Tunggu Tugas B selesai

    proses_b.join()


    print()
    print("=" * 70)
    print(">>> TUGAS B SELESAI")
    print(">>> CORE 2 SELESAI")
    print("=" * 70)


    # ========================================================
    # HASIL AKHIR
    # ========================================================

    print()
    print()
    print("=" * 70)
    print("HASIL AKHIR")
    print("=" * 70)


    total_a = 0
    total_b = 0


    print()
    print("TUGAS A - CORE 1")
    print("-" * 70)


    for angka in data_a:

        hasil = angka * angka

        total_a += hasil

        print(
            f"{angka}*{angka} = {hasil}"
        )


    print()
    print(f"TOTAL TUGAS A = {total_a}")


    print()
    print("TUGAS B - CORE 2")
    print("-" * 70)


    for angka in data_b:

        hasil = angka * angka

        total_b += hasil

        print(
            f"{angka}*{angka} = {hasil}"
        )


    print()
    print(f"TOTAL TUGAS B = {total_b}")


    # ========================================================
    # TOTAL AKHIR
    # ========================================================

    total_akhir = total_a + total_b


    print()
    print("=" * 70)
    print("TOTAL AKHIR")
    print("=" * 70)

    print(
        f"Total Tugas A : {total_a}"
    )

    print(
        f"Total Tugas B : {total_b}"
    )

    print(
        f"TOTAL         : {total_akhir}"
    )


    # ========================================================
    # WAKTU SELESAI
    # ========================================================

    waktu_selesai = time.perf_counter()

    waktu_selesai_real = datetime.now()


    print()
    print("=" * 70)
    print("INFORMASI WAKTU")
    print("=" * 70)

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
    print("=" * 70)
    print("PROGRAM SELESAI")
    print("=" * 70)
