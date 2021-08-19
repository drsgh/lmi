import pandas as pd
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt
import shapely.wkt
import json
import os
dirname = os.path.dirname(__file__)
outputPath = os.path.join(dirname, 'output')

# Checks if a polygon contains a point (point = lat/lon representing an address)

obj1 = json.loads('["a", ["b", "c", "d"], "e"]')
path = dirname + '\\' + "formattedPolygons.csv"
path2 = outputPath + '\\' + "geocodedAddresses.csv"

gisfile = pd.read_csv(path, index_col=0,header=0)
custfile = pd.read_csv(path2, index_col=0,header=0)

polyCount = len(gisfile.iloc[:, 0].array)
custCount = len(custfile.iloc[:, 0].array)

polyArray = [0] * polyCount
dataArray = [0] * polyCount

#This builds the polygons from the csv file of formatted polygon data. It was necessary to re-format the Socrata provided csv file for a number of the polygons, as the coordinates for
#   some polygons contained too many characters. the _gmGetPolygons file uses the Socrata API to directly pull in the polygons, but it hasn't been integrated with the rest of the program.

#BUILD POLYGONS
for x in range(0, polyCount):
    polySeries = gisfile.loc[[x]].to_numpy()
    polySeriesCount = len(polySeries[0])
    polyStringArray = []

    for i in range(0, polySeriesCount):
        if len(str(polySeries[0][i])) > 0:
            if str(polySeries[0][i]) != 'nan':
                polyString = polySeries[0][i].split(",")
                polyString[0] = polyString[0].replace("[","").replace('"','')
                polyString[1] = polyString[1].replace("]","").replace('"','')
                if [float(polyString[0]), float(polyString[1])] != 0:
                    polyStringArray.append((float(polyString[0]), float(polyString[1])))

    print(x)
    polyArray[x] = Polygon(polyStringArray)
    dataArray[x] = polyStringArray

#DROP POINTS INTO POLYGONS
custArray = []
for x in range(0, custCount):
    custPointArray = []
    custSeries = custfile.iloc[[x]].to_numpy()
    lat = float(custSeries[0][0])
    lon = float(custSeries[0][1])
    point = Point(lon,lat)

    for i in range(0, polyCount):
        if polyArray[i].contains(point):
            custPointArray.append(i)

    if len(custPointArray) > 0:
        custArray.append([custSeries[0][0],custSeries[0][1],custSeries[0][2],custPointArray])

for x in range(0, polyCount):
    plt.plot(*polyArray[x].exterior.xy, color='green')

for x in range(0, len(custArray)):
    plt.plot(custArray[x][1], custArray[x][0], marker=".", markersize=1, color='red')

plt.show()

print(custArray)

cust_csv = pd.DataFrame(custArray)
fileClearPath = dirname + '\\' + 'foundAddresses.csv'
fileClear = open(fileClearPath, "w+")
fileClear.close()
cust_csv.to_csv(dirname + '\\' + 'foundAddresses.csv')
