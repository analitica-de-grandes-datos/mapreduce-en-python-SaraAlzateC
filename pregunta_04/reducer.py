#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

letter_counts = {}

for line in sys.stdin:
    line = line.strip()
    letter, count = line.split('\t', 1)

    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

for letter, count in letter_counts.items():
    print(f'{letter},{count}')