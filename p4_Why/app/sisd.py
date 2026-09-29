import numpy as np
DATA_INPUT = [1, 2, 3, 4] # Single Data
hasil = []
for x in DATA_INPUT:
    kuadrat = x * x # Single Instruction
    hasil.append(kuadrat)
total = sum(hasil)
print(f"Total Sum SISD  : {total}\n")
