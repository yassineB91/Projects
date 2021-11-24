#!/usr/bin/env python3
#Function that reads data from DB and returns data as a dataframe
def readdata(host,port,database,user,password, query, columns):
    import psycopg2
    import pandas as pd
    myconnection=psycopg2.connect(host=host,port=port,database=database,user=user, password=password)
    cur=myconnection.cursor()
    cur.execute(query)
    dataaslist=cur.fetchall()
    table=pd.DataFrame(dataaslist,columns=columns)
    return table