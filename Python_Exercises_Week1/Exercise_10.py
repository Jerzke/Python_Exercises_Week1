import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

sortRow = sampleArray[:,sampleArray[1,:].argsort()]
sortCol = sampleArray[:,sampleArray[:,1].argsort()]

print("Original", sampleArray,"2nd row",sortRow,"2nd col", sortCol)