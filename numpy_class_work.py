import numpy as np
#
# array = np.zeros((8, 8), dtype=np.int32)
# array[1::2, ::2] = 1
# array[::2, 1::2] = 1
# print(array)

import numpy as np

# text = input()
# numbers = np.array(list(map(int, text.split())))
# result = np.where(numbers > 0, numbers, 0)
# print(result)


import numpy as np

matrix = np.loadtxt('matrix.txt', dtype=float)
print(np.sum(matrix, axis=0))
print(np.max(matrix, axis=1))
