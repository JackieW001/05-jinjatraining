from flask import Flask, render_template
import csv
import random
occ_dict = {} #dictionary with job class as keys and percentages as values
rand_occ = [] #list to randomly select occupation

def create_dict():
    #adds keys with corresponding values to dictionary
    with open("occupations.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            occ_dict[row[0]] = row[1]

    #deletes first row (column titles)
    del occ_dict["Job Class"]
    del occ_dict["Total"]

    #print len(dictionary.keys())

    #appends percentage*10 number of job into a list
    for i in occ_dict:
        num = 0
        while num < (float(occ_dict[i])*10):
            rand_occ.append(i)
            num += 1
create_dict()

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
    return render_template('occupations.html', l = len(occ_dict.keys()), keys = occ_dict.keys(), values = occ_dict.values(), randomOcc = random.choice(rand_occ))

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
