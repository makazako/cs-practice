from tablestats import read_rows, count_types, total_minutes, to_csv


s = input()

with open(s, encoding="utf-8") as table:
    rows = read_rows(table)

c = len(rows)
ct = count_types(rows)
cm = total_minutes(rows, 'ошибка')

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(ct))

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(f'{c}\n{len(ct)}\n{cm}\n')

#14
#4 
#2.5 