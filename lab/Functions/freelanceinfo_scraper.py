#!/usr/bin/env python3
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import date
import math
rooturl='https://www.freelance-info.fr/missions-entreprise?'
headers= {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
request= requests.get(rooturl, headers)
soup= BeautifulSoup(request.content, 'html.parser')
soupprety=soup.prettify()


    
html= list(soup.children)
try:
    body=html[2]
except:
    print('Captcha blocking the scraping')

content=list(body.children)
tags=content[3]

    
job_href_all=tags.find_all('a',href=True)

prefix='https://www.freelance-info.fr'
joblist=[]

for item in job_href_all:
    if item['href'].startswith('/missions-') and item.find('p') is not None:
        job_href=prefix+item['href'][:-8]+'?page=%s'
        companyname=item.find('p').text.split('[')[0]
        numberjobs=item.find('p').text.split('[')[1].replace(']','')
        numberjobs=int(numberjobs)
        if numberjobs%10==0:
            num_job=numberjobs/10
        else:
            num_job=math.ceil(numberjobs/10)
        print(job_href)
        print(companyname)
        print(num_job)
        job={'companyname':companyname, 'job_href':job_href,'num_job':num_job}
        joblist.append(job)


scraped=pd.DataFrame(joblist)
run_date=date.today()
i=0



for ref in scraped['job_href']:
    joblist=[]
    titlelist=[]
    locationlist=[]
    durationlist=[]
    salarylist=[]
    datelist=[]
    companyname=[]
    df=pd.DataFrame(columns=['title','companyname','location','duration','salary','date'])
    for pagenumber in range(1,int(scraped['num_job'][i])):
        url=ref
        url=url %str(pagenumber)
        request2= requests.get(url, headers)
        soup2= BeautifulSoup(request2.content, 'html.parser')
        html2= list(soup2.children)
        body2=html2[2]
        content2=list(body2.children)
        tags2=content2[3]
        titlehtml=tags2.find_all('a',class_='rtitre filter-link')
        locationhtml= tags2.find_all('span',class_='textvert9')
        dur_tarhtm= tags2.find_all('span')
        datehtml=tags2.find_all('span',class_='textgrisfonce9')
        
        #titlehref=jobhtml.find('a',class_='rtitr filter-link')
        for item in titlehtml:
            title=item['href'].split('/')[2]
            titlelist.append(title)
        
        for item in locationhtml:
            location=item.text
            locationlist.append(location)
            
        for item in dur_tarhtm:
            if '€' in item.text or 'Tarif' in item.text:
                dur_tar=item.text
                duration=dur_tar.split('|')[1]
                duration=duration.lstrip(' ')
                duration=duration.rstrip(' ')            
                durationlist.append(duration)
                salary=dur_tar.split('|')[2]
                salarylist.append(salary)
        for item in datehtml:
            date_posted=item.text
            datelist.append(date_posted)
            print(date_posted)
            companyname.append(scraped['companyname'][i])
    
        
        
        
    df['title']=pd.Series(titlelist)
    df['location']=pd.Series(locationlist)
    df['duration']=pd.Series(durationlist)
    df['salary']=pd.Series(salarylist)
    df['date']=pd.Series(datelist)
    df['companyname']=pd.Series(companyname)
    com=str(df['companyname'][0]).strip().split('http')[0]
    try:
        df.to_csv(f'job_freel_{pagenumber}_{run_date}_{com}.csv', sep=';')
    except:
        pass
    i=i+1


            
            
            
            
            
            
            
            
            
            
            
            
        
    
