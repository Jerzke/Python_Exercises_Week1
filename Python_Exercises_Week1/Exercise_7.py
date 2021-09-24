import numpy as np

AOne = np.array([[5, 6, 9], [21 ,18, 27]])

ATwo = np.array([[15 ,33, 24], [4 ,7, 1]])

resultA = AOne + ATwo
resultS = AOne + ATwo
print("Sum", resultS)

for num in np.nditer(resultA, op_flags = ['readwrite']):
    num[...] = num*num

print("Sqroots", resultA)