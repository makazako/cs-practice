s = open(str(input()))
lines = []
i = 0
o = 0
for line in s:
    i += 1
    line = line.rstrip('\n').split(',')
    if i != 1 and line[0] == 'ошибка':
        o += int(line[1])
    lines.append(line)