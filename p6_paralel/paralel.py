import multiprocessing
import os
import time
import psutil
from datetime import datetime
from zoneinfo import ZoneInfo

WIB = ZoneInfo("Asia/Jakarta")


def waktu_sekarang():
    sekarang = datetime.now(WIB)
    return sekarang.strftime("%H:%M:%S.%f")[:-3]


def hitung_kuadrat(nama, data, core, barrier, hasil):
    proses = psutil.Process(os.getpid())
    proses.cpu_affinity([core])

    print(
        f"{nama} PID={os.getpid()} "
        f"menggunakan CPU Core {core}",
        flush=True
    )

    barrier.wait()

    mulai = time.perf_counter()
    waktu_mulai = waktu_sekarang()

    total = 0

    for x in data:
        kuadrat = x ** 2
        total += kuadrat

        print(
            f"{nama} Core {core} -> "
            f"{x}² = {kuadrat} "
            f"{waktu_sekarang()}",
            flush=True
        )

    nilai = 0

    for i in range(2_000_000):
        nilai += i * i

    selesai = time.perf_counter()
    waktu_selesai = waktu_sekarang()

    hasil[nama] = {
        "total": total,
        "mulai": mulai,
        "selesai": selesai,
        "waktu_mulai": waktu_mulai,
        "waktu_selesai": waktu_selesai,
        "core": core,
        "pid": os.getpid()
    }


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:

        hasil = manager.dict()

        barrier = multiprocessing.Barrier(2)

        task_A = multiprocessing.Process(
            target=hitung_kuadrat,
            args=(
                "Tugas A",
                [1, 2],
                0,
                barrier,
                hasil
            )
        )

        task_B = multiprocessing.Process(
            target=hitung_kuadrat,
            args=(
                "Tugas B",
                [3, 4],
                1,
                barrier,
                hasil
            )
        )

        task_A.start()
        task_B.start()

        task_A.join()
        task_B.join()

        data_A = hasil["Tugas A"]
        data_B = hasil["Tugas B"]

        total = data_A["total"] + data_B["total"]

        print(f"Total : {total}")
