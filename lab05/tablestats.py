def read_rows(lines):
    rows = []
    for line in lines:
        rows.append(line)
    l1 = rows[0]
    lost = rows[1:]
    a = []
    b =[]
    c = []
    for l in lost:
        if len(l) > 2:
            a.append(l[0])
            b.append(l[1])
            c.append((l[2]))
    answer = {
        str(l1[0]): a,
        str(l1[1]): b,
        'минуты': c
    }
    return answer

def count_types(rows):
    type = rows['тип']
    v = sorted(type)
    vv = set(v)
    answer = {}
    for x in vv:
        answer[str(x)] = v.count(x)
    return answer

def total_minutes(rows, kind):
    answer = []
    c = 0
    i = 0
    for x in rows['тип']:
        i += 1
        if x == kind:
            answer.append(float((rows["минуты"])[i-1]))
            c+=1
    s  = sum(answer)
    if answer == []:
        return 0
        
    else:
        return s/c

def to_csv(counts):
    answer = 'тип,количество\n'

    for key, value in sorted(counts.items()):
        answer += f'{key},{value}\n'

    return answer

s = open('events.csv')
lines = []
for line in s:
    line = line.rstrip('\n')
    lines.append([str(x) for x in line.split(',')])
rows =read_rows(lines)
counts = count_types(rows)

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))