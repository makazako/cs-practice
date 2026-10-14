
from tablestats import read_rows, count_types, total_minutes, to_csv


def main():
    with open(str(input()), 'r', encoding='utf-8') as file:
        rows = read_rows(file)

    counts = count_types(rows)

    result = to_csv(counts)

    with open('summary.csv', 'w', encoding='utf-8') as file:
        file.write(result)
    return result


if __name__ == '__main__':
    main()
    