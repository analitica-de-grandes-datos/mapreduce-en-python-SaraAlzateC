#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

with open('data.csv', 'r') as csvfile:
    for line in csvfile:
        line = line.strip()
        columnas = line.split('   ')

        if len(columnas) >= 1:
            letter = columnas[0]  
            print(f'{letter}\t1')