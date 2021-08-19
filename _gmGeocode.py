import googlemaps
import pandas as pd
import os
import _gmKey
dirname = os.path.dirname(__file__)
gmaps = googlemaps.Client(key=_gmKey.mapkey)


#Geocodes addresses using Google Maps. An alternative geocoder tool Nominatim is in the _other directory, but is slower.

dataArray = []
dataArrayNew = []
x = 0

with open("input/addressesToGeocode.csv", 'r') as fp:
    for line in fp:
        x = x + 1
        geocode_result = gmaps.geocode(line)
        try:
            #NEW METHOD
            dataArrayAdd = [0]*3
            dataArrayAdd[0] = geocode_result[0]["geometry"]["location"]["lat"]
            dataArrayAdd[1] = geocode_result[0]["geometry"]["location"]["lng"]
            dataArrayAdd[2] = str(line)
            dataArrayNew.append(dataArrayAdd)

            #OLD METHOD - NEW METHOD splits string so that results feed directly to mapping process
            dataArray.append(str(geocode_result[0]["geometry"]["location"]["lat"]) + "," + str(geocode_result[0]["geometry"]["location"]["lng"]))
        except:
            print("No coordinates")
            print(line)
            dataArray.append("-")
    fp.close()
with open("output/fixedAddresses.csv", 'r') as fp:
    for line in fp:
        x = x + 1
        geocode_result = gmaps.geocode(line)
        try:
            #NEW METHOD
            dataArrayAdd = [0]*3
            dataArrayAdd[0] = geocode_result[0]["geometry"]["location"]["lat"]
            dataArrayAdd[1] = geocode_result[0]["geometry"]["location"]["lng"]
            dataArrayAdd[2] = str(line)
            dataArrayNew.append(dataArrayAdd)

            #OLD METHOD - NEW METHOD splits string so that results feed directly to mapping process
            dataArray.append(str(geocode_result[0]["geometry"]["location"]["lat"]) + "," + str(geocode_result[0]["geometry"]["location"]["lng"]))
        except:
            print("No coordinates")
            print(line)
            dataArray.append("-")
    fp.close()

poly_csv = pd.DataFrame(dataArray)
poly_csv_new = pd.DataFrame(dataArrayNew)
print(poly_csv_new)

fileClearPath = os.path.join(dirname, 'output')
fileClearPath = fileClearPath + '\\' + 'geocodedAddresses.csv'
fileClear = open(fileClearPath, "w+")
fileClear.close()

#OLD poly_csv.to_csv(fileClearPath)
poly_csv_new.to_csv(fileClearPath)