import time

# ==========================================
# DATA
# Bisa ditambah kapan saja
# ==========================================
data = [1, 2, 3, 4, 8, 9]

hasil_a = []
hasil_b = []

waktu_mulai = time.perf_counter()

# ==========================================
# PROSES SINGLE CORE
# A dan B berjalan bergantian
# ==========================================
for i, angka in enumerate(data):

    if i % 2 == 0:
        # Tugas A
        print(f"Tugas A hitung angka {angka}")

        kuadrat = angka ** 2

        # Simpan hasil, JANGAN ditampilkan dulu
        hasil_a.append((angka, kuadrat))

    else:
        # Tugas B
        print(f"Tugas B hitung angka {angka}")

        kuadrat = angka ** 2

        # Simpan hasil, JANGAN ditampilkan dulu
        hasil_b.append((angka, kuadrat))


waktu_selesai = time.perf_counter()
waktu_total = waktu_selesai - waktu_mulai


# ==========================================
# SETELAH SEMUA SELESAI
# BARU TAMPILKAN HASIL
# ==========================================

print("\n\n================================")
print("       SEMUA TUGAS SELESAI")
print("================================")


# ==========================================
# HASIL TUGAS A
# ==========================================
print("\n=== HASIL TUGAS A ===")

total_a = 0

for angka, hasil in hasil_a:
    print(f"{angka}² = {hasil}")
    total_a += hasil

print(f"Total Tugas A = {total_a}")


# ==========================================
# HASIL TUGAS B
# ==========================================
print("\n=== HASIL TUGAS B ===")

total_b = 0

for angka, hasil in hasil_b:
    print(f"{angka}² = {hasil}")
    total_b += hasil

print(f"Total Tugas B = {total_b}")


# ==========================================
# TOTAL AKHIR
# ==========================================
total_akhir = total_a + total_b

print("\n================================")
print("          TOTAL AKHIR")
print("================================")

print(f"Tugas A = {total_a}")
print(f"Tugas B = {total_b}")
print(f"Total   = {total_a} + {total_b} = {total_akhir}")

print(f"\nWaktu pengerjaan = {waktu_total:.9f} detik")
