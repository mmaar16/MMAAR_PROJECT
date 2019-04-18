import csv

lineno = 0

with open('tile2.csv', 'r') as csvfile:
    with open('tile2.html', 'w') as htmlfile:
        csv_reader = csv.reader(csvfile)

        htmlfile.write("<!DOCTYPE html>\n")
        htmlfile.write("<html>\n")
        htmlfile.write("<body>\n")
        htmlfile.write('<img src="tile2_clusters.png" width="1000" height="1000" usemap="#planetmap">\n')
        htmlfile.write('<map name="planetmap">\n')

        for line in csv_reader:
            if lineno == 0:
                lineno += 1
            else:
                htmlfile.write('    <area shape="rect" coords="' + line[2] + "," + line[3] + "," + line[4] + "," + line[5]
                           + '" href="#">\n')

        htmlfile.write("</map>\n")
        htmlfile.write("</body>\n")
        htmlfile.write("</html>\n")
