import numpy as np

def reshape_rows(values, width):
    res = np.asarray(values)
    res = res.reshape((len(values)// width), width)
    return res

def block(matrix, rows, columns):
    res = np.asarray(matrix)
    res = res[np.ix_(rows, columns)]
    return res

def column_means(matrix):
    res = np.asarray(matrix)
    res = np.mean(res, axis=0)
    return res

def column_range(matrix, column):
    res = np.asarray(matrix)
    res = res[:, column]
    return np.max(res) - np.min(res)
            
print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))
# [[12, 14.5, 11], [13, 15.5, 10.5]]

# [3.0, 4.0]