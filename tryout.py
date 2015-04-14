import csv

f = open('start.csv')
a = csv.reader(f)
new = []
for read in a:
	new.append(read[0])
print new