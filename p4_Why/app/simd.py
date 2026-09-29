import numpy as np
DATA_INPUT = [1, 2, 3, 4] # Single Data
data_vector = np.array(DATA_INPUT) # Multi Data
hasil_vector = data_vector * data_vector # Single Instruction
total = np.sum(hasil_vector)
print(f"Total Sum SIMD   : {total}\n")
