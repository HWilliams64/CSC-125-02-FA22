import csv

with open('./Heroes.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file, dialect='excel')

    while True:
        hero_info = input('Please enter your information: ')

        if not hero_info:
            break
        
        segments = hero_info.split()

        if len(segments) == 5:
            writer.writerow(segments)

    