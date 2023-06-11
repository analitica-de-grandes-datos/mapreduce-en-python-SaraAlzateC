#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

with open('data.csv', 'r') as csvfile:
    for line in csvfile: 
      line = line.strip()

      columns = line.split('   ')

      if len(columns) != 3:
          continue

      month = columns[1].split('-')[1]

      print(f"{month}\t1")