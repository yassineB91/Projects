import requests
import json
import pandas as pd
apikey='j4z8zDZyMy9ax8nuEXXa'
getdata=requests.get('https://data.nasdaq.com/api/v3/datasets/FRED/NROUST?api_key='+apikey)
datajsondict= getdata.json()

data=datajsondict['dataset']
dataitems=data['data']
datacolumns=data['column_names']
df=pd.DataFrame(dataitems,columns=datacolumns)
maxvalue=max(df['Value'])