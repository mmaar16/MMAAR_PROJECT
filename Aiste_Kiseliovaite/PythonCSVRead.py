import csv

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
                line_count += 1

clusterPointArray = read_file('tile2.csv')
print(clusterPointArray)
print(next(clusterPointArray))
print(next(clusterPointArray))
