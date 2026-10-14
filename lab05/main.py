s = open('summary.csv')
lines = []
i = 0
o = 0
for line in s:
    i += 1
    line = line.rstrip('\n').split(',')
    if i != 1 and line[0] == 'ошибка':
        o += 1
    lines.append(line)
lines = lines[1:]
c = 0
for x in lines:
    c += int(x[1])

with open("summary.csv", "a", encoding="utf-8") as out:
    out.write(f"Вывод\n {c}\n {i}\n {o}\n")