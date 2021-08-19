import googlemaps
import pandas as pd
import os
import _gmKey
dirname = os.path.dirname(__file__)
dataArray = []
gmaps = googlemaps.Client(key=_gmKey.mapkey)

#Used to fix addresses that fail to geocode (requires additional API call)

with open("input/addressesToFix"
          ".csv", 'r') as fp:
    for line in fp:
        print(line)
        autocomplete_result = gmaps.places_autocomplete(line)
        try:
            print(autocomplete_result[0]["description"])
            dataArray.append(autocomplete_result[0]["description"])
        except:
            print("No coordinates")
            dataArray.append("-")
    fp.close()

print(dataArray)
poly_csv = pd.DataFrame(dataArray)
fileClearPath = os.path.join(dirname, 'output')
fileClearPath = fileClearPath + '\\' + 'fixedAddresses.csv'
fileClear = open(fileClearPath, "w+")
fileClear.close()
poly_csv.to_csv(fileClearPath)
