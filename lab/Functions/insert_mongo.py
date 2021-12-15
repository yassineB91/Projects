#!/usr/bin/env python3
def insertMG(filepath,database):
    import sys
    import pymongo
    import pandas as pd
    import os
    from configDB import config
    
    param=config(database,'tns.ini')  
    con=pymongo.MongoClient(param['host'],int(param['port']))
    for filename in os.listdir(filepath):
        f=os.path.join(filepath,filename)
        if os.path.isfile(f):
            if 'job_freel' in filename:
                df=pd.read_csv(f,sep=';')
                data=df.to_dict(orient='record')
                db=con.jobmarket
                collection=db.freelance_info
                collection.insert_many(data)
            else:
                df=pd.read_csv(f,sep=';')
                data=df.to_dict(orient='record')
                db=con.jobmarket
                collection=db.indeed
                collection.insert_many(data)
            
