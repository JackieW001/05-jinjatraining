from flask import Flask, render_template
from utils import work03
import random

occ_dict = work03.create_dict()
rand_occ = work03.random_occ()
    
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
