
from tablestats import read_rows, count_types, total_minutes, to_csv


def main():
    with open('events.csv', 'r', encoding='utf-8') as file:
        rows = read_rows(file)

    counts = count_types(rows)

    result = to_csv(counts)

    with open('summary.csv', 'w', encoding='utf-8') as file:
        file.write(result)

    print('Количество событий:', counts)

    for kind in sorted(counts):
        print(kind, total_minutes(rows, kind))


if __name__ == '__main__':
    main()
