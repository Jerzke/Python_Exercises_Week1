import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

print("original", sampleArray)


min = np.amin(sampleArray, 1)
max = np.amax(sampleArray, 0)

print(min, max)