#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

estado = None
contador = 0

for line in sys.stdin:
    line = line.strip()
    state, value = line.split('\t', 1)
    
    if estado == state:
        contador += int(value)
    else:
        if estado:
            # Emite el resultado del estado anterior
            print(f'{estado}\t{contador}')
        estado = state
        contador = int(value)

# Emite el resultado del último estado
if estado:
    print(f'{estado}\t{contador}')