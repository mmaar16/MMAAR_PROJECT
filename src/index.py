#!/usr/bin/env python
import csv
from PIL import Image
import sys
import cgi, cgitb
cgitb.enable()
print "Content-Type: text/plain\r\n\r\n"
print
# Global variables.
form = cgi.FieldStorage()
COLOR_1 = (120, 120, 255, 255)
COLOR_2 = (255, 255, 0, 255)
CSV_FILE = "tile2.csv"
MAIN_IMAGE = "tile2.png"
CLUSTER_IMAGE = "tile2_clusters.png"
IMAGE_NAME = "tile2_overlayed.png"
HTML_FILE_NAME = "index.html"
NEW_CSV_FILE = "new_file.csv"

## Function read_file() reads .CSV files and returns the contents in a generator with yield.
#  @param fileName The file we read data from.
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

## Function html_generate() generates an .HTML file containing a list of interactable rectangle objects.
#  @param picture_name The picture we are applying interactable objects on.
#  @param csv_file_name The newly generated .CSV file.
def html_generate(picture_name, csv_file_name):
    with open(csv_file_name, 'r') as csvfile:
        with open(HTML_FILE_NAME, 'w') as htmlfile:
            csv_reader = csv.reader(csvfile)

            htmlfile.write("<!DOCTYPE html>\n")
            htmlfile.write("<html>\n")
            htmlfile.write("<body>\n")
            htmlfile.write('<img src=' + picture_name + ' width="1000" height="1000" usemap="#clustermap">\n')
            htmlfile.write('<map name="clustermap">\n')

            lineno = 0

            for line in csv_reader:
                if lineno == 0:
                    lineno += 1
                else:
                    htmlfile.write('    <area shape="rect" class="points" cluster_no = "' + line[15] + '" coords="' + line[2] + "," + line[3] + "," + line[4] + "," + line[5]
                               + '" href="#" id = "' + line[1] + '">\n')
            htmlfile.write(open("popup.html", "r").read())
            htmlfile.write("</map>\n")
            htmlfile.write("</body>\n")
            htmlfile.write("</html>\n")
            htmlfile.write(open("js.html", "r").read())

## Function updateCSVFile() updates the .CSV file.
#  @param CSVFileName The file we read data from.
#  @param objectNo The number of the selected object we change the data of.
#  @param clusterNo The new cluster number of the selected object.
def updateCSVFile(CSVFileName, objectNo, clusterNo):
    with open(CSVFileName) as csv_file_in, open(NEW_CSV_FILE, 'w') as csv_file_out:
        csv_reader = csv.reader(csv_file_in, quotechar = "'")
        csv_writer = csv.writer(csv_file_out, quotechar = "'")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                csv_writer.writerow(row)
                line_count += 1
            elif int(row[1]) == objectNo:
                print("Old Cluster number:",row[15], " -> New Cluster Number:",clusterNo)
                row[15] = clusterNo
                csv_writer.writerow(row)
                break
            else:
                csv_writer.writerow(row)
        csv_writer.writerows(csv_reader)

    with open(NEW_CSV_FILE) as csv_file_in, open(CSVFileName, 'w') as csv_file_out:
        csv_reader = csv.reader(csv_file_in, quotechar = "'")
        csv_writer = csv.writer(csv_file_out, quotechar = "'")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                csv_writer.writerow(row)
                line_count += 1
            else:
                csv_writer.writerow(row)
        csv_writer.writerows(csv_reader)

## Function changeRGBA() colors the cluster in the image with one of the two colors, dependant on the clusterNo.
#  @param clusterPointArray Generator of the data that was read from the .CSV file.
#  @param image The image we draw the clusters on.
#  @param pixelMap The image where the clusters are marked.
def changeRGBA(clusterPointArray, image, pixelMap):
    for i in clusterPointArray:
        for j in range(int(i[2]), int(i[4])):
            for k in range(int(i[3]), int(i[5])):
                if(j >= image.height or k >= image.width):
                    continue
                if int(i[15]) == 1:
                    pixelMap[j, k] = COLOR_1
                else:
                    pixelMap[j, k] = COLOR_2

## Function changeAlpha() updates the value of the variable alpha.
#  @param newAlpha The new alpha value.
def changeAlpha(newAlpha):
    alpha = newAlpha
    return alpha

## Function overlay() converts the images into RGBA and blends them together.
#  @param image The image we draw clusters on.
#  @param clusters The image which contains the clusters.
#  @param alpha The alpha channel value.
def overlay(image, clusters, alpha):
    imageRGBA = image.convert("RGBA")
    clustersRGBA = clusters.convert("RGBA")
    return Image.blend(imageRGBA, clustersRGBA, alpha)

## Function saveImage() saves the overlayed images as a new image.
#  @param image The image we draw clusters on.
#  @param clusters The image which contains the clusters.
#  @param alpha The alpha channel value.
def saveImage(image, clusters, alpha):
    imageBlended = overlay(image, clusters, alpha)
    imageBlended.save(IMAGE_NAME)

## Function overlayImage() opens .CSV and image files, calls functions to overlay them together and save the new image.
def overlayImage():
    clusterPointArray = read_file(NEW_CSV_FILE)
    image = Image.open(MAIN_IMAGE)
    clusters = Image.open(CLUSTER_IMAGE)
    alpha = .8
    pixelMap = clusters.load()
    changeRGBA(clusterPointArray, image, pixelMap)
    alpha = changeAlpha(.5)
    saveImage(image, clusters, alpha)
    
## Function generateNewImage() calls functions updateCSVFile(), overlayImage(), html_generate().
#  @param objectNo The number of the object that will be updated.
#  @param clusterNo The new cluster number of the object that is being updated.
def generateNewImage(objectNo, clusterNo):
    updateCSVFile(CSV_FILE,objectNo,clusterNo)
    overlayImage()
    html_generate(IMAGE_NAME, NEW_CSV_FILE)


generateNewImage(int(form["obj_id"].value), int(form["cluster_no"].value))

