#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import csv

with open('credit.csv', 'r') as csvfile:
    lector = csv.reader(csvfile)
    next(lector)  
    
    for fila in lector:
        purpose = fila[3]  
        amount = int(fila[4])  
        print(f'{purpose}\t{amount}')
