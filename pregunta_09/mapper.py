#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

with open('data.csv', 'r') as csvfile:
    for line in csvfile:
        line = line.strip()
        columnas = line.split('   ')

        if len(columnas) >= 3:
            value = float(columnas[2])  
            print(f'{value}\t{line}')