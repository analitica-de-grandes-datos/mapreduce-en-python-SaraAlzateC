#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

max_values = {}
min_values = {}

for line in sys.stdin:
    line = line.strip()
    letter, value = line.split('\t', 1)
    value = float(value)

    if letter in max_values:
        max_values[letter] = max(max_values[letter], value)
    else:
        max_values[letter] = value

    if letter in min_values:
        min_values[letter] = min(min_values[letter], value)
    else:
        min_values[letter] = value

for letter in max_values:
    max_value = max_values[letter]
    min_value = min_values[letter]
    print(f'{letter}\t{max_value}\t{min_value}')