import csv

## Function read_file() reads .CSV files and returns the contents in a generator with yield
def read_file(fileName):
    clusterPointArray = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                yield(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 
                                                 row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])

clusterPointArray = read_file('5_klasterizuoti_rezultatai.csv') #read_file('tile2.csv')