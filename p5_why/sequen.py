# ============================================================
# PROGRAM SEQUENTIAL
# PENJUMLAHAN KUADRAT MENGGUNAKAN LIST
#
# Skenario:
# - CPU hanya menggunakan 1 core
# - Terdapat 2 tugas: Tugas A dan Tugas B
# - Data disimpan dalam list
# - Setiap angka dihitung kuadratnya
# - Hasil kuadrat dijumlahkan terus
# - Jika data pada list ditambah, program otomatis
#   memproses data tambahan tersebut
# - Proses berjalan secara SEQUENTIAL
# ============================================================


# ============================================================
# FUNGSI TUGAS A
# ============================================================

def tugas_a(angka):

    print(f"   [TUGAS A] Menerima angka {angka}")

    # Menghitung kuadrat
    hasil = angka ** 2

    print(f"   [TUGAS A] {angka}² = {hasil}")
    print(f"   [TUGAS A] Mengembalikan hasil {hasil} ke CPU")

    return hasil


# ============================================================
# FUNGSI TUGAS B
# ============================================================

def tugas_b(angka):

    print(f"   [TUGAS B] Menerima angka {angka}")

    # Menghitung kuadrat
    hasil = angka ** 2

    print(f"   [TUGAS B] {angka}² = {hasil}")
    print(f"   [TUGAS B] Mengembalikan hasil {hasil} ke CPU")

    return hasil


# ============================================================
# PROGRAM UTAMA
# ============================================================

print("=" * 65)
print("          PROGRAM SEQUENTIAL - 1 CPU CORE")
print("          PENJUMLAHAN KUADRAT DATA")
print("=" * 65)


# ============================================================
# DATA
# ============================================================
#
# Cukup tambahkan angka di dalam list.
#
# Contoh:
# [1, 2, 3, 4, 5]
#
# Bisa ditambah:
# [1, 2, 3, 4, 5, 6, 7, 8]
#
# Program akan otomatis memproses semuanya.
# ============================================================

angka_list = [1, 2, 3, 4, 5, 6, 1000]


print()
print(f"Data yang akan diproses : {angka_list}")
print(f"Jumlah data             : {len(angka_list)}")


# ============================================================
# MEMBAGI DATA MENJADI 2 TUGAS
# ============================================================
#
# Contoh 5 data:
#
# [1, 2, 3] -> Tugas A
# [4, 5]    -> Tugas B
#
# Pembagian dilakukan otomatis berdasarkan posisi data.
# ============================================================

titik_tengah = (len(angka_list) + 1) // 2

data_tugas_a = angka_list[:titik_tengah]
data_tugas_b = angka_list[titik_tengah:]


print()
print("Pembagian tugas:")
print(f"Tugas A : {data_tugas_a}")
print(f"Tugas B : {data_tugas_b}")


# ============================================================
# VARIABEL HASIL
# ============================================================

hasil_tugas_a = []
hasil_tugas_b = []

total_tugas_a = 0
total_tugas_b = 0

total_kuadrat = 0


# ============================================================
# PROSES TUGAS A
# ============================================================

print()
print("=" * 65)
print("                     TUGAS A")
print("=" * 65)

for angka in data_tugas_a:

    print()
    print(f"[CPU] Mengirim angka {angka} ke Tugas A")

    hasil = tugas_a(angka)

    # Simpan hasil
    hasil_tugas_a.append(hasil)

    # Tambahkan ke total Tugas A
    total_tugas_a += hasil

    # Tambahkan ke total keseluruhan
    total_kuadrat += hasil

    print(f"[CPU] Menerima hasil = {hasil}")
    print(f"[CPU] Total Tugas A sementara = {total_tugas_a}")
    print(f"[CPU] Total keseluruhan sementara = {total_kuadrat}")


# ============================================================
# HASIL TUGAS A
# ============================================================

print()
print("-" * 65)
print("HASIL TUGAS A")

for i in range(len(data_tugas_a)):

    angka = data_tugas_a[i]
    hasil = hasil_tugas_a[i]

    print(f"{angka}² = {hasil}")

print(f"Total Tugas A = {total_tugas_a}")


# ============================================================
# PROSES TUGAS B
# ============================================================

print()
print("=" * 65)
print("                     TUGAS B")
print("=" * 65)

for angka in data_tugas_b:

    print()
    print(f"[CPU] Mengirim angka {angka} ke Tugas B")

    hasil = tugas_b(angka)

    # Simpan hasil
    hasil_tugas_b.append(hasil)

    # Tambahkan ke total Tugas B
    total_tugas_b += hasil

    # Tambahkan ke total keseluruhan
    total_kuadrat += hasil

    print(f"[CPU] Menerima hasil = {hasil}")
    print(f"[CPU] Total Tugas B sementara = {total_tugas_b}")
    print(f"[CPU] Total keseluruhan sementara = {total_kuadrat}")


# ============================================================
# HASIL TUGAS B
# ============================================================

print()
print("-" * 65)
print("HASIL TUGAS B")

for i in range(len(data_tugas_b)):

    angka = data_tugas_b[i]
    hasil = hasil_tugas_b[i]

    print(f"{angka}² = {hasil}")

print(f"Total Tugas B = {total_tugas_b}")


# ============================================================
# HASIL AKHIR
# ============================================================

print()
print("=" * 65)
print("                    HASIL AKHIR")
print("=" * 65)


# Membuat tampilan perhitungan Tugas A
perhitungan_a = " + ".join(
    str(hasil) for hasil in hasil_tugas_a
)

# Membuat tampilan perhitungan Tugas B
perhitungan_b = " + ".join(
    str(hasil) for hasil in hasil_tugas_b
)


print()
print("TUGAS A")
print(f"{perhitungan_a} = {total_tugas_a}")

print()
print("TUGAS B")
print(f"{perhitungan_b} = {total_tugas_b}")

print()
print("-" * 65)

print("TOTAL KESELURUHAN")
print(f"{total_tugas_a} + {total_tugas_b} = {total_kuadrat}")

print("-" * 65)

print(f"Jumlah data       : {len(angka_list)}")
print(f"Total kuadrat     : {total_kuadrat}")
print(f"CPU digunakan     : 1 CORE")
print(f"Mode              : SEQUENTIAL")

print("=" * 65)
print("                 SEMUA PROSES SELESAI")
print("=" * 65)
