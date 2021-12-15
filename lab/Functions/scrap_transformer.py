#!/usr/bin/env python3
def scrap_transformer(filepath):
    import pandas as pd
    import numpy as np
    
    newdata = pd.read_csv(filepath, usecols=['title', 'wage', 'companyname', 'location', 'date', 'companynote'], sep=';')
    newdata['wage'] = newdata['wage'].replace(np.nan, '0 € - 0 € par nan')
    newdata[['salary', 'frequency']] = newdata['wage'].str.split('par', expand=True)
    newdata = newdata.drop('wage', axis=1)
    newdata[['lower_salary', 'upper_salary']] = newdata['salary'].str.split('-', expand=True)
    newdata = newdata.drop('salary', axis=1)
    
    newdata['currency'] = newdata['lower_salary'].str.rsplit(' ', n=2, expand=True)[1]
    newdata['lower_salary'] = newdata['lower_salary'].str.rsplit(' ', n=2, expand=True)[0]
    newdata['upper_salary'] = newdata['upper_salary'].str.rsplit(' ', n=2, expand=True)[0]
    newdata['upper_salary'] = newdata['upper_salary'].fillna(newdata['lower_salary'])
    newdata['date']=newdata.date.str.extract('(\d+)')
    newdata['date']= pd.to_numeric(newdata['date'].fillna('0'))
    newdata['companynote']= pd.to_numeric(newdata['companynote'].str.replace(",","."))
    
    for i in range(len(newdata)):
        try:
            newdata['upper_salary'][i]=[a for a in newdata['upper_salary'][i].split() if a.isdigit()]
            newdata['upper_salary'][i]=int(''.join(newdata['upper_salary'][i]))
            newdata['lower_salary'][i]=[a for a in newdata['lower_salary'][i].split() if a.isdigit()]
            newdata['lower_salary'][i]=int(''.join(newdata['lower_salary'][i]))
        except:
            newdata['upper_salary'][i]=0
            newdata['lower_salary'][i]=0

            
    return newdata


