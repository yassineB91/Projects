#!/usr/bin/env python3
def transformer(filepath):
    import pandas as pd
    import numpy as np

    newdata = pd.read_csv(filepath, usecols=['title', 'companyname', 'location', 'duration','salary','date','joblink','jobskills'], sep=';')
    newdata['salary']=newdata['salary'].str.replace(' Tarif non renseigné', '0-0 €')
    
    mask=newdata['salary'].str.contains('-')
    for i in range(len(newdata)):
        if  mask[i]:
             newdata['salary'][i]=newdata['salary'][i]
        else:
            newdata['salary'][i]=newdata['salary'].str.rstrip('€')[i] + '-' + newdata['salary'][i]

    newdata[['lower_tjm', 'upper_tjm']] = newdata['salary'].str.split('-', expand=True)
    
    
    newdata['upper_tjm']= newdata['upper_tjm'].str.lstrip(' ')
    newdata['currency'] = newdata['upper_tjm'].str.rsplit(' ', expand=True)[1]
    newdata['upper_tjm'] = newdata['upper_tjm'].str.rsplit(' ', expand=True)[0]
    newdata['duration'] = newdata['duration'].str.rstrip(' ')
    newdata['duration'] = newdata['duration'].str.lstrip(' ')
    newdata = newdata.drop('salary', axis=1)
    newdata['duration_number'] = newdata.duration.str.split(' ', expand = True)[0]
    newdata['duration_unit'] = newdata.duration.str.split(' ', expand = True)[1]
    newdata = newdata.drop('duration', axis=1)
    newdata['duration_number']=newdata['duration_number'].str.replace('Durée','0',regex=True)
    mask = newdata['duration_number'].str.len() > 4
    
    for i in range(len(newdata)):
        if mask[i]:
            newdata['duration_number'][i]='0'
           
    newdata['duration_number']=pd.to_numeric(newdata['duration_number'])
    newdata['currency']= newdata['currency'].fillna('€')
    newdata['upper_tjm']= pd.to_numeric(newdata['upper_tjm'].fillna('0'))
    newdata['lower_tjm']= newdata['lower_tjm'].str.replace(" Tarif non renseigné","0")
    newdata['lower_tjm']= pd.to_numeric(newdata['lower_tjm'].str.rstrip('€'))
    
    return newdata

  