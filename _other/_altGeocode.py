import csv
from geopy import Nominatim
import time
import pandas as pd

dataArray = []
geolocator = Nominatim(user_agent="http")

with open("input/testadd"
          ".csv", 'r') as fp:
    for line in fp:
        print(line)
        location = geolocator.geocode(line)
        try:
            print(location.latitude, location.longitude)
            dataArray.append(location)
        except:
            print("No coordinates")
            dataArray.append("-")

        time.sleep(1)
    fp.close()

print(dataArray)

poly_csv = pd.DataFrame(dataArray)
save_path = r'C:\Users\lucas\PycharmProjects\drsgismapper'
fileClearPath = save_path + '\\' + 'geo_data.csv'
fileClear = open(fileClearPath, "w+")
fileClear.close()
poly_csv.to_csv(save_path + '\\' + 'geo_data.csv')