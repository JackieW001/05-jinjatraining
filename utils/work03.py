import csv
import random
dictionary = {}
lit = []

with open("occupations.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dictionary[row[0]] = row[1]
    
del dictionary["Job Class"]
del dictionary["Total"]
for i in dictionary:
    num = 0
    while num < (float(dictionary[i])*10):
        lit.append(i)
        num += 1

#print lit
#print type(float(dictionary["Management"]))
#print len(lit)
print random.choice(lit)
#print dictionary
