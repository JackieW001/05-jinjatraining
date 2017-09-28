import csv

def create_dict():
    occ_dict = {} #dictionary with job class as keys and percentages as values
    #adds keys with corresponding values to dictionary
    with open("data/occupations.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            occ_dict[row[0]] = row[1]

    #deletes first row (column titles)
    del occ_dict["Job Class"]
    del occ_dict["Total"]

    #print len(dictionary.keys())
    return occ_dict

def random_occ():
    rand_occ = [] #list to randomly select occupation
    occ_dict = create_dict()
    #appends percentage*10 number of job into a list
    for i in occ_dict:
        num = 0
        while num < (float(occ_dict[i])*10):
            rand_occ.append(i)
            num += 1
    return rand_occ

if __name__ == '__main__':
    print create_dict()
    print random_occ()
