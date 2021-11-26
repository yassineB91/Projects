#!/usr/bin/env python3
#Function that reads data from DB and returns data as a dataframe
def readdata(query, columns):
    import psycopg2
    import pandas as pd
    from configDB import config
    con=config()
    myconnection=psycopg2.connect(**con)
    cur=myconnection.cursor()
    cur.execute(query)
    dataaslist=cur.fetchall()
    table=pd.DataFrame(dataaslist,columns=columns)
    return table