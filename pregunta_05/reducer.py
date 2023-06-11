#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

month_counts = {}

for line in sys.stdin:
    line = line.strip()
    month, count = line.split('\t')

    if month in month_counts:
        month_counts[month] += int(count)
    else:
        month_counts[month] = int(count)

for month, count in month_counts.items():
    print(f'{month}\t{count}')