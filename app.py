from flask import Flask, render_template
import csv
import random
dictionary = {}

with open("occupations.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dictionary[row[0]] = row[1]
    
del dictionary["Job Class"]
del dictionary["Total"]

print len(dictionary.keys())

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('root.html')

@my_app.route('/occupations')
def occupations():
    return render_template('occupations.html', l = len(dictionary.keys()), keys = dictionary.keys(), values = dictionary.values())

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
