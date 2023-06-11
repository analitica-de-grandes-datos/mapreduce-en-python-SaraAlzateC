#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import csv
with open('credit.csv', 'r') as csvfile:
    lector = csv.reader(csvfile)
    
    for fila in lector:
        credit_history = fila[2]  
        print(f'{credit_history}\t1')
