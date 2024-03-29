#!/usr/bin/env python3
def indeed_scraper(keyword,location,start,end):
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    from datetime import date
    from skillextract import skillextract
    import re
    #import random
    #from time import sleep
    pagestart=(10*start)-10
    pageend= (10*end)
    run_date=date.today()
    result=pd.DataFrame(columns=['title','wage','companyname','location','date', 'companynote','joblink','jobskills'])
    for page in range(pagestart,pageend,10):
        #sleep(random.randint(10,100))
        url=f'https://fr.indeed.com/jobs?q={keyword}&l={location}&fromage=60&start={page}'
        prefix='https://fr.indeed.com'
                
        print(f'Scraping in progress for the page number: {page}')
        print(url)
        headers= {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        request= requests.get(url, headers)
        soup= BeautifulSoup(request.content, 'html.parser')
          
        html= list(soup.children)
        try:
            body=html[2]
        except:
            print('Captcha blocking the scraping')
            
        content=list(body.children)
        tags=content[3]
        
        jobhtml=tags.find_all('a', class_=re.compile("tapItem"))
      
        
        joblist=[]
        joblinklist=[]
        
        for item in jobhtml:
            
            if item.find_all('span')[0].text=='nouveau':
                title=item.find_all('span')[1].text
                
            else:
                title=item.find_all('span')[0].text
            
            
            joblink=prefix + item['href']
            
            
            span=list(item.find_all('span'))
            wage=''
            companynote=''           
    
            for i in span:
                if '€' in i.text:
                    wage=i.get_text(strip=True)
                    #print(wage)
    
    
            for j in span:
                if ',' in j.text and len(j.text)==3:
                    companynote=j.text
                    #print(companynote)
                
            
            companyname=item.find('span', class_='companyName').text
            location=item.find('div',class_='companyLocation').text
            date=item.find('span', class_='date').text
            jobskill=[]
            
            job={'title': title,'wage': wage,'companyname': companyname,'location': location, 'date': date, 'companynote': companynote,'joblink':joblink}
            joblist.append(job)
            
        scraped=pd.DataFrame(joblist,columns=['title','wage','companyname','location','date','companynote','joblink','jobskills'])
        #result=result.append(scraped)
        
        page=int(page/10)
        df=skillextract(scraped)
        try:
            df.to_csv(f'jobs_ile_de_france_{keyword}_{page}_{run_date}.csv', sep=';')
        except:
            print('issue happened during file generation')
            return 1
        
