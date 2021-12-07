#!/usr/bin/env python3

def indeed_scraper(keyword,location,start,end):
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    import time
    pagestart=(10*start)-10
    pageend= (10*end)
    result=pd.DataFrame(columns=['title','wage','companyname','location','date', 'companynote'])
    for page in range(pagestart,pageend,10):
        time.sleep(3)
        url=f'https://fr.indeed.com/jobs?q={keyword}&l={location}&start={page}'
        print(url)
        headers= {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        request= requests.get(url, headers)
        soup= BeautifulSoup(request.content, 'html.parser')
        #soupprety=soup.prettify()
        #print(request.status_code)        
        html= list(soup.children)
        body=html[2]
        content=list(body.children)
        tags=content[3]
        
        jobhtml=tags.find_all('div',class_='job_seen_beacon')
        joblist=[]
        
        for item in jobhtml:
            
            if item.find_all('span')[0].text=='nouveau':
                title=item.find_all('span')[1].text
                
            else:
                title=item.find_all('span')[0].text
            
            span=list(item.find_all('span'))
            wage=''
            companynote=''           
    
            for i in span:
                if '€' in i.text:
                    wage=i.text
                    print(wage)
    
    
            for j in span:
                if ',' in j.text and len(j.text)==3:
                    companynote=j.text
                    print(companynote)
                
            
            companyname=item.find('span', class_='companyName').text
            location=item.find('div',class_='companyLocation').text
            date=item.find('span', class_='date').text
            
            job={'title': title,'wage': wage,'companyname': companyname,'location': location, 'date': date, 'companynote': companynote}
            joblist.append(job)
            
        scraped=pd.DataFrame(joblist,columns=['title','wage','companyname','location','date','companynote'])
        result=result.append(scraped)
        
        result.to_csv(f'jobs_ile_de_france_{keyword}_{start}_{end}.csv', sep=';')
    
