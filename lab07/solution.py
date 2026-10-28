import numpy as np

def reshape_rows(values, width):
    res = np.asarray(values)
    res = res.reshape(len(values)/ width, width)
    return res

def block(matrix, rows, columns):
    res = np.asarray(matrix)
    res = res[np.ix_(rows, columns)]
    return res

def column_means(matrix):
    res = np.asarray(matrix)
    res = np.mean(res)
    return res

def column_range(matrix, column):
    res = np.asarray(matrix)
    res = res[:, column]
    return max(res) - min(res)
            

# [[12, 14.5, 11], [13, 15.5, 10.5]]

# [3.0, 4.0]