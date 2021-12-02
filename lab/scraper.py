import pandas as pd
from bs4 import BeautifulSoup
import requests
start=2
end=11
pagestart=(10*start)-10
pageend= (10*end)
result=pd.DataFrame(columns=['title','salary','companyname','location','date', 'companynote'])
for page in range(pagestart,pageend,10):
    url=f'https://fr.indeed.com/jobs?q=product+owner&l=Paris+%2875%29&start={page}'
    headers= {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    request= requests.get(url, headers)
    soup= BeautifulSoup(request.content, 'html.parser')
    soupprety=soup.prettify()
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
            salary=item.find_all('span')[6].text
            companynote=item.find_all('span')[4].text
        else:
            title=item.find_all('span')[0].text
            salary=item.find_all('span')[3].text
            companynote=item.find_all('span')[4].text
        
        companyname=item.find('span', class_='companyName').text
        location=item.find('div',class_='companyLocation').text
        date=item.find('span', class_='date').text
        
        job={'title': title,'Salary': salary,'companyname': companyname,'location': location, 'date': date, 'companynote': companynote}
        joblist.append(job)
        
    scraped=pd.DataFrame(joblist,columns=['title','salary','companyname','location','date','companynote'])
    result=result.append(scraped)


#for i in jobhtml[5].find_all('span'):
    #print(i.text)