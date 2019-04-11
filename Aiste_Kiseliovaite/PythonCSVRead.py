import csv

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

clusterPointArray = []

with open('tile2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            clusterPointArray.append(ClusterInfo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 
                                                 row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))
            line_count += 1


for clusterPoints in clusterPointArray:
    #print(clusterPoints.objNo + " " + clusterPoints.clusterNo)
    print(clusterPoints.objNo + " " + clusterPoints.upperLeftX + " " + clusterPoints.upperLeftY + " " + clusterPoints.lowerRightX + " " + 
          clusterPoints.lowerRightY + " " + clusterPoints.centroidX + " " + clusterPoints.centroidY + " " + clusterPoints.area + " " + clusterPoints.convexArea + " " + 
          clusterPoints.eccentricity + " " + clusterPoints.extent + " " + clusterPoints.filledArea + " " + clusterPoints.majorAxisLength + " " + clusterPoints.perimeter + " " + 
          clusterPoints.clusterNo)
