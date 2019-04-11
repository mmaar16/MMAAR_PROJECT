import csv, os

class ClusterInfo:
    def __init__(self, column1, objNo, upperLeftX, upperLeftY, lowerRightX, lowerRightY, centroidX, centroidY, 
                 area, convexArea, eccentricity, extent, filledArea, majorAxisLength, perimeter, clusterNo):
        self.column1 = column1
        self.objNo = objNo
        self.upperLeftX = upperLeftX
        self.upperLeftY = upperLeftY
        self.lowerRightX = lowerRightX
        self.lowerRightY = lowerRightY
        self.centroidX = centroidX
        self.centroidY = centroidY
        self.area = area
        self.convexArea = convexArea
        self.eccentricity = eccentricity
        self.extent = extent
        self.filledArea = filledArea
        self.majorAxisLength = majorAxisLength
        self.perimeter = perimeter
        self.clusterNo = clusterNo

tempCluster = ClusterInfo("700",699,560,48,561,50,560.5,49,2,2,1,1,2,2,0,1)

with open('tile2.csv') as csv_file_in, open('tile2_temp.csv', 'w', newline='') as csv_file_out:
    csv_reader = csv.reader(csv_file_in, quotechar = "'")
    csv_writer = csv.writer(csv_file_out, quotechar = "'")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            csv_writer.writerow(row)
            line_count += 1
        elif int(row[1]) == tempCluster.objNo:
            row[15] = tempCluster.clusterNo
            csv_writer.writerow(row)
            break
        else:
            csv_writer.writerow(row)
    csv_writer.writerows(csv_reader)