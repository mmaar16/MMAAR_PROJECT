from PIL import Image
import sys
sys.path.insert(0, '../')
from Aiste_Kiseliovaite import PythonCSVRead


def changeRGBA(clusterPointArray, clusterNo, RGBA):
    for i in clusterPointArray:
        if clusterNo == int(i[1]):
            for j in range(int(i[2]), int(i[4])):
                for k in range(int(i[3]), int(i[5])):
                    pixelMap[j, k] = RGBA


def changeAlpha(newAlpha):
    alpha = newAlpha
    return alpha


def displayImage():
    imageRGBA = image.convert("RGBA")
    clustersRGBA = clusters.convert("RGBA")

    imageBlended = Image.blend(imageRGBA, clustersRGBA, alpha)

    imageBlended.show()

clusterPointArray = PythonCSVRead.read_file("Aiste_Kiseliovaite/tile2.csv")

image = Image.open("Max/tile2.png")
clusters = Image.open("Max/tile2_clusters.png")
alpha = .8

pixelMap = clusters.load()

#testing the functions
displayImage()
changeRGBA(clusterPointArray, 761, (180, 180, 255, 255))
displayImage()
alpha = changeAlpha(.5)
displayImage()
