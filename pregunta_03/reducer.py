#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    print(value)