from PIL import Image
import sys
sys.path.insert(0, '../')
from Aiste_Kiseliovaite import PythonCSVRead


def changeRGBA(clusterPointArray):
    for i in clusterPointArray:
        for j in range(int(i[2]), int(i[4])):
            for k in range(int(i[3]), int(i[5])):
                if(j >= image.height or k >= image.width):
                    continue
                if int(i[15]) == 1:
                    pixelMap[j, k] = COLOR_1
                else:
                    pixelMap[j, k] = COLOR_2


def changeAlpha(newAlpha):
    alpha = newAlpha
    return alpha


def overlay():
    imageRGBA = image.convert("RGBA")
    clustersRGBA = clusters.convert("RGBA")

    return Image.blend(imageRGBA, clustersRGBA, alpha)


def displayImage():
    imageBlended = overlay()
    imageBlended.show()


def saveImage():
    imageBlended = overlay()
    imageBlended.save("tile2_overlayed.png")


clusterPointArray = PythonCSVRead.read_file("Aiste_Kiseliovaite/tile2.csv")

image = Image.open("Max/tile2.png")
clusters = Image.open("Max/tile2_clusters.png")
alpha = .8

COLOR_1 = (120, 120, 255, 255)
COLOR_2 = (255, 255, 0, 255)

pixelMap = clusters.load()

# testing the functions
displayImage()
changeRGBA(clusterPointArray)
displayImage()
alpha = changeAlpha(.5)
displayImage()
saveImage()