import csv

# function to update the CSV file (find by objectNo and update clusterNo)
def updateCSVFile(CSVFileName, objectNo, clusterNo):
    with open(CSVFileName) as csv_file_in, open('tile2_temp.csv', 'w', newline='') as csv_file_out:
        csv_reader = csv.reader(csv_file_in, quotechar = "'")
        csv_writer = csv.writer(csv_file_out, quotechar = "'")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                csv_writer.writerow(row)
                line_count += 1
            elif int(row[1]) == objectNo:
                #print("Old Cluster number:",row[15], " -> New Cluster Number:",clusterNo)
                row[15] = clusterNo
                csv_writer.writerow(row)
                break
            else:
                csv_writer.writerow(row)
        csv_writer.writerows(csv_reader)

# temporary variables for testing updateCSVFile function
tempObjectNo = 699
tempClusterNo = 1
tempCSVFileName = "tile2.csv"

updateCSVFile(tempCSVFileName, tempObjectNo, tempClusterNo)