#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_letter = None
numbers = []

for line in sys.stdin:
    line = line.strip()
    letter, number = line.split('\t', 1)

    if current_letter is None:
        current_letter = letter

    if letter == current_letter:
        numbers.append(int(number))
    else:
        if len(numbers) > 0:
            numbers.sort()
            print(f'{current_letter}\t{",".join(str(num) for num in numbers)}')

        current_letter = letter
        numbers = [int(number)]

if current_letter is not None:
    if len(numbers) > 0:
        numbers.sort()
        print(f'{current_letter}\t{",".join(str(num) for num in numbers)}')