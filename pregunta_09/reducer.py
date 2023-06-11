#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

top_values = []

for line in sys.stdin:
    line = line.strip()
    value, record = line.split('\t', 1)
    value = float(value)

    if len(top_values) < 6:
        top_values.append((value, record))
        top_values.sort()
    elif value < top_values[-1][0]:
        top_values.pop()
        top_values.append((value, record))
        top_values.sort()

for value, record in top_values:
    print(record)