#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    columnas = line.split(',')
    
    if len(columnas) >= 2:
        key = columnas[1]
        value = line
        print(f'{key}\t{value}')
