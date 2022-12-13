import csv

d = {
    "a": 1,
    "b": 2,
    "c": 3
}

two_d_list = [(1, 2, 3), (1, 3, 4), (1, 4, 5)]

with open('./Heroes.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, dialect='excel')

    for row in reader:
        print(row)

    # for index, value in enumerate(reader):

        '''if index == 4:
            continue'''

        #print(index, value[2]+" "+value[1])
