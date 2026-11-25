import numpy as np

v = np.array([0, 3, 6, 9, 12, 15, 18, 21])

def make_hours():
    res =np.arange(8)
    res = res * 3
    return res.tolist()

print(make_hours())

def vector_report(values):
    b = {
        "third": int(values[2]),
        "last": int(values[-1]),
        "middle": [int(x) for x in values[2:6]],
        "every_second": [int(x) for x in values[::2]],
        "reversed": [int(x) for x in values[::-1]] 
    }
    return b

print(vector_report(v))

def change_vector(values):
    v = values.copy()
    v[2:5] = [99,99,99]
    v[::2] = [-1] * len(values[::2])   
    return v

print(change_vector(v))

def cap_above(values, limit):
    values = np.array(values)
    values[values > limit] = limit
    return values.tolist()

print(cap_above(v, 10))

def celsius_to_fahrenheit(values):
    values = np.array(values)
    values = (values * 9/5) + 32
    return [float(x) for x in values]

print(celsius_to_fahrenheit(v))

# [ 0  3  6  9 12 15 18 21]
# {'third': 6, 'last': 21, 'middle': [6, 9, 12, 15], 'every_second': [0, 6, 12, 18], 'reversed': [21, 18, 15, 12, 9, 6, 3, 0]}
# [-1  3 -1 99 -1 15 -1 21]
# [ 0  3  6  9 10 10 10 10]
# [32, 37, 42, 48, 50, 50, 50, 50]

arr = np.array([1,2,3,4,5])
print(arr[4:1:-2])