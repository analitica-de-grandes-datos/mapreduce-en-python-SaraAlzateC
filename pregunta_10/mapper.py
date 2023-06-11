#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

with open('data.csv', 'r') as csvfile:
    for line in csvfile:
        line = line.strip()
        columnas = line.split('\t')

        if len(columnas) >= 2:
            letters = columnas[1].split(',')  
            number = columnas[0]  

            for letter in letters:
                print(f'{letter}\t{number}')