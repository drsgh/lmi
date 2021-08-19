import pandas as pd
from sodapy import Socrata
import os

#Pulls polygon data directly from Socrata (not integrated into program)

dirname = os.path.dirname(__file__)
client = Socrata("data.ny.gov", None)
results = client.get("t6wd-tdrv", limit=5000)
results_df = pd.DataFrame.from_records(results)
print(results_df["the_geom"].values)
fileClearPath = dirname + '\\' + 'polygonApiData.csv'
fileClear = open(fileClearPath, "w+")
fileClear.close()
results_df.to_csv(dirname + '\\' + 'polygonApiData.csv')


