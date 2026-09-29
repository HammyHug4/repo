import numpy as np
DATA_INPUT = [1, 2, 3, 4]
# Multi Data
data_bagian_1 = [1, 2]
data_bagian_2 = [3, 4]
hasil_1 = [x * x for x in data_bagian_1] # Instruksi 1
hasil_2 = [pow(x, 2) for x in data_bagian_2] # Instruksi 2
total = sum(hasil_1) + sum(hasil_2)

print(f"Data Partisi 1 : {data_bagian_1} -> Instruksi 1 : {hasil_1}")
print(f"Data Partisi 2 : {data_bagian_2} -> Instruksi 2 : {hasil_2}")
print(f"Total Sum MIMD    : {total}\n")
