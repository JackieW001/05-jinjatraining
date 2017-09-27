from flask import Flask, render_template
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

#print len(dictionary.keys())

for i in dictionary:
    num = 0
    while num < (float(dictionary[i])*10):
        lit.append(i)
        num += 1

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('root.html')

@my_app.route('/occupations')
def occupations():
    return render_template('occupations.html', l = len(dictionary.keys()), keys = dictionary.keys(), values = dictionary.values(), randomOcc = random.choice(lit))

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
