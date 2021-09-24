import numpy as np

amount = np.arange(1, 100)

solution = amount[(amount % 3 == 0) | (amount % 5 == 0)]

print(solution[:1000])

print(solution.sum())