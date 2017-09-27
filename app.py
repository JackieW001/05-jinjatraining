from flask import Flask, render_template
import csv
import random
dictionary = {} #dictionary with job class as keys and percentages as values
lit = [] #list to randomly select occupation

#adds keys with corresponding values to dictionary
with open("occupations.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dictionary[row[0]] = row[1]

#deletes first row (column titles)
del dictionary["Job Class"]
del dictionary["Total"]

#print len(dictionary.keys())

#appends percentage*10 number of job into a list
for i in dictionary:
    num = 0
    while num < (float(dictionary[i])*10):
        lit.append(i)
        num += 1

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('root.html')

'''
length is used to figure out how many table rows we need
keys is used as a list of keys for first column of table
values is used as a list of values for second column of table
randomOcc chooses a random occupation
'''
@my_app.route('/occupations')
def occupations():
    return render_template('occupations.html', l = len(dictionary.keys()), keys = dictionary.keys(), values = dictionary.values(), randomOcc = random.choice(lit))

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
