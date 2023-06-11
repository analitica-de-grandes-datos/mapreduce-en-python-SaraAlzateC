#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

with open('data.csv', 'r') as csvfile:
    for line in csvfile:
        line = line.strip()
        columnas = line.split('   ')

        if len(columnas) >= 3:
            letter = columnas[0]
            value = float(columnas[2])
            print(f'{letter}\t{value}\t{line}')