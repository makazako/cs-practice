import numpy as np





hours = np.arange(0,22,3)
# [ 0  3  6  9 12 15 18 21]
# (8,)
# 1
# 8
# int64
print(hours[2])
print(hours[hours.size -1])
print(hours[2:5])
print(hours[::2])
print(hours[::-1])
# 6
# 21
# [ 6  9 12]
# [ 0  6 12 18]
# [21 18 15 12  9  6  3  0]

line = np.linspace(0,1,5)
# [0.   0.25 0.5  0.75 1.  ]
# (5,)
# 1
# 5
# float64

zeros = np.zeros(6, dtype=int)
# [0 0 0 0 0 0]
# (6,)
# 1
# 6
# int64

unknown_table = np.full((2,3),-1, dtype=int)
# [[-1 -1 -1]
#  [-1 -1 -1]]
# (2, 3)
# 2
# 6
# int64

identity = np.eye(3, dtype=int)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]
# (3, 3)
# 2
# 9
# int64

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
# (3, 4)
# 2
# 12
# 18
# [11 13 16 17]
# [15 17 18]
# [[14 13 15]
#  [13 16 17]]
# [[14 13]
#  [13 16]])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print(temperatures[2,3])
print(temperatures[1])
print(temperatures[:,temperatures.shape[1] -1])
print(temperatures[:2,1:])
print(temperatures[0:2,1:3])

matrix = np.arange(1, 26).reshape(5, 5)
# [ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]
# (4, 5)
# [[16 17 18 19 20]
#  [21 22 23 24 25]]
# (1, 5)
# [[ 1  2  3]
#  [ 6  7  8]
#  [11 12 13]
#  [16 17 18]
#  [21 22 23]]
# (5, 3)
# [[ 8  9]
#  [13 14]
#  [18 19]]
# (3, 2)
# [[19 20]
#  [24 25]]
# (2, 2)

print(matrix[:4])
print(matrix[:4].shape)
print(matrix[3:])
print(matrix[4:].shape)
print(matrix[:,:3])
print(matrix[:,:3].shape)
print(matrix[1:4,2:4])
print(matrix[1:4,2:4].shape)
print(matrix[3:,3:])
print(matrix[3:,3:].shape)

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print(hours)
print(changed_hours)

# copy() нужен для того, чтобы создать отдельную копию массива, 
# чтобы изменения в одном массиве не влияли на другой. 
# В данном случае, если бы мы не использовали copy(),
# изменения в changed_hours повлияли бы на массив hours,
# так как они бы ссылались на один и тот же объект в памяти.

# [ 0  3  6  9 12 15 18 21]
# [-1  3 -1 99 -1 15 -1 21]

changed_matrix = matrix.copy()

changed_matrix[1] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4,1:4] = 100

print(matrix)
print(changed_matrix)

numbers = np.arange(12)
table = numbers.reshape(3, 4)

transposed = table.T

print(numbers.shape)      # (12,)
print(table.shape)        # (3, 4)
print(transposed.shape)   # (4, 3)

# reshape(3, 4) работает, потому что 3 * 4 = 12 элементов.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15,
# а в исходном массиве только 12 элементов.