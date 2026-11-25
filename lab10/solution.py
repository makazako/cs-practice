import numpy as np

def make_table(rows, columns):
    return np.arange(rows*columns).reshape((rows, columns)).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    return [
        row[column_start:column_stop]
        for row in matrix[row_start:row_stop]
    ]
m = make_table(3, 4)
print(m)
print(rectangle(m, 1, 3, 1, 3))

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    for i in range(row_start, row_stop):
        for j in range(column_start, column_stop):
            matrix[i][j] = value
    return matrix
print(replace_rectangle(m, 1, 3, 1, 3, 99))

def matrix_vector_product(matrix, vector):
    return np.array(matrix) @ np.array(vector)

print(matrix_vector_product(m, np.array([1, 2, 3, 4])))

def matrix_multiply(left, right):
    return np.array(left) @ np.array(right)

print(matrix_multiply(m, np.array([[1, 2], [3, 4], [5, 6], [7, 8]])))

def transpose_matrix(matrix):
    return np.array(matrix).T

def solve_system(matrix, vector):
    return np.linalg.solve(np.array(matrix), np.array(vector))

def tensor_channel_mean(tensor):
    return np.mean(np.array(tensor), axis=(0, 1))

def point_distance(first, second):
    return np.linalg.norm(np.array(first) - np.array(second))
 
print(tensor_channel_mean(np.random.rand(4, 4, 3)))