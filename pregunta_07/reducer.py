#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_letter = None
current_values = []

for line in sys.stdin:
    line = line.strip()
    letter, value, record = line.split('\t', 2)

    if current_letter is None:
        current_letter = letter

    if letter == current_letter:
        current_values.append((value, record))
    else:
        
        sorted_values = sorted(current_values, key=lambda x: float(x[0]))

        for sorted_value in sorted_values:
            print(sorted_value[1])

        current_letter = letter
        current_values = [(value, record)]

if current_letter is not None:
    sorted_values = sorted(current_values, key=lambda x: float(x[0]))
    for sorted_value in sorted_values:
        print(sorted_value[1])