def count_items(values):
    res ={}
    for x in values:
        if x not in res:
            res[x] = values.count(x)
    return res

def unique_sorted(values):
    res = count_items(values)
    return sorted(res.keys())

def common(first, second):
    return (sorted(set(first) & set(second)))

def only_in_first(first, second):
    return (sorted(set(first) - set(second)))[:1]

values = ["ошибка", "запуск", "ошибка", "проверка"]
first = ["иванов", "петрова"]
second = ["петрова", "котов"]

print(count_items(values))
print(unique_sorted(values))
print(common(first, second))
print(only_in_first(first, second))

# {'ошибка': 2, 'запуск': 1, 'проверка': 1}
# ['запуск', 'ошибка', 'проверка']
# ['петрова']
# иванов