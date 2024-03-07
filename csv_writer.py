import csv

with open('example.csv', mode= 'w') as file:
    writer = csv.writer(file, delimiter='\\', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer

