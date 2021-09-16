import pandas as pd
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt

path = "C:/Users/lucas/PycharmProjects/drsgismapper/polygons-gis-lmi.csv"
gisfile = pd.read_csv(path, index_col=0,header=0)
polyCount = len(gisfile.iloc[:, 0].array)
polyArray = [0] * polyCount
dataArray = [0] * polyCount

for x in range(0, polyCount):
    polySeries = gisfile.iloc[:, 0].array[x]
    if len(str(gisfile.iloc[:, 1].array[x])) > 0:
        if str(gisfile.iloc[:, 1].array[x]) != 'nan':
            polySeries = polySeries + "," + str(gisfile.iloc[:, 1].array[x])
    splitPolySeries = polySeries.split(",")
    multiPolyStringArray = [0] * len(splitPolySeries)
    multiPolyCount = len(multiPolyStringArray)

    for i in range(0, multiPolyCount):
        multiPolyStringArray[i] = splitPolySeries[i].strip().split(" ")

    multiPolyFloatArray = [0] * len(splitPolySeries)

    for i in range(0, multiPolyCount):
        multiPolyFloatArray[i] = [float(multiPolyStringArray[i][0]), float(multiPolyStringArray[i][1])]

    polyArray[x] = Polygon(multiPolyFloatArray)
    dataArray[x] = multiPolyFloatArray

    print(multiPolyFloatArray)
    print(x)

for x in range(0, polyCount):
    plt.plot(*polyArray[x].exterior.xy)

print(polyArray)
plt.show()

poly_csv = pd.DataFrame(dataArray)
save_path = r'C:\Users\lucas\PycharmProjects\drsgismapper'
fileClearPath = save_path + '\\' + 'formattedPolygons.csv'
fileClear = open(fileClearPath, "w+")
fileClear.close()
poly_csv.to_csv(save_path + '\\' + 'formattedPolygons.csv')


