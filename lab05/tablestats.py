
def read_rows(lines):
    rows = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        parts = line.split(',')

        if len(parts) != 3:
            continue

        date, kind, minutes = parts

        if date.strip() == 'дата':
            continue

        date = date.strip()
        kind = kind.strip()
        minutes = minutes.strip()

        if not date or not kind:
            continue

        try:
            minutes = str(minutes)
        except ValueError:
            continue

        rows.append({
            'дата': date,
            'тип': kind,
            'минуты': minutes
        })

    return rows


def count_types(rows):
    counts = {}

    for row in rows:
        kind = row['тип']

        if kind not in counts:
            counts[kind] = 0

        counts[kind] += 1

    return counts


def total_minutes(rows, kind):
    total = 0

    for row in rows:
        if row['тип'] == kind:
            total += float(row['минуты'])

    return round(total, 1)


def to_csv(counts):
    lines = ['тип,количество']

    for kind in sorted(counts):
        lines.append(f'{kind},{counts[kind]}')

    return '\n'.join(lines) + '\n'
