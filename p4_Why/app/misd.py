import numpy as np
DATA_INPUT = [1, 2, 3, 4] # Single Data
n = 4
hasil_instruksi_1 = sum(i * i for i in range(1, n + 1)) # Instruction 1 Loop)
hasil_instruksi_2 = (n * (n + 1) * (2 * n + 1)) // 6 # Instruction 2 Formula Matimatika

print(f"Single Data (N)        : {n}")
print(f"Hasil Instruksi 1 (Loop): {hasil_instruksi_1}")
print(f"Hasil Instruksi 2 (Form): {hasil_instruksi_2}")
print(f"Validasi (Match?)       : {hasil_instruksi_1 == hasil_instruksi_2}\n")
