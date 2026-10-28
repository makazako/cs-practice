def reshape_rows(values, width):
    i = 0
    res = []
    res1 = []
    for x  in values:
        
        if i == 0 and len(values[values.index(x):] ) <= width:
            width = len(values[values.index(x):] )
        i += 1
        if i < width:
            res1.append(x)
        elif i == width:
            i = 0
            res1.append(x)
            res.append(res1)
            res1 = []
        
    return res

def block(matrix, rows, columns):
    res = []
    i = 0
    for x in matrix:
       
        if i in rows:
            r = [el for el in x if x.index(el) in columns]
            res.append(r)
        i += 1
    return res

def column_means(matrix):
    c = len(matrix[0])
    i = 0
    res = []
    for x1 in range(c):
        r = 0
        i1 = 0
        for x in matrix:
            r += x[i]
            i1 += 1
        r = r / i1
        res.append(r)
        i += 1
    return res

def column_range(matrix, column):
    res = []
    i = 0
    for x in matrix:
            i += 1
            res.append(x[column])
    return max(res) - min(res)
            
values = [1, 2, 3]
width = 2
column = 1
rows = [0,2]
print(reshape_rows(values, width))

# [[12, 14.5, 11], [13, 15.5, 10.5]]

# [3.0, 4.0]