import csv


# generating html file **maybe need a custom width and height input
def html_generate(picture_name, csv_file_name, html_file_name):
    with open(csv_file_name, 'r') as csvfile:
        with open(html_file_name, 'w') as htmlfile:
            csv_reader = csv.reader(csvfile)

            htmlfile.write("<!DOCTYPE html>\n")
            htmlfile.write("<html>\n")
            htmlfile.write("<body>\n")
            htmlfile.write('<img src=' + picture_name + 'width="1000" height="1000" usemap="#clustermap">\n')
            htmlfile.write('<map name="clustermap">\n')

            lineno = 0

            for line in csv_reader:
                if lineno == 0:
                    lineno += 1
                else:
                    htmlfile.write('    <area shape="rect" coords="' + line[2] + "," + line[3] + "," + line[4] + "," + line[5]
                               + '" href="#">\n')

            htmlfile.write("</map>\n")
            htmlfile.write("</body>\n")
            htmlfile.write("</html>\n")


# function call
picture_name = "tile2.png"
csv_file_name = "tile2.csv"
html_name = "tile2.html"

html_generate(picture_name, csv_file_name, html_name)
