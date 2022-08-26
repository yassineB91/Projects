#!/usr/bin/env python3



def skillextract(df):
    
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    import re
    #i=2
    for i in df.index:
        description=''
        techvalues=[]
        rooturl=''
        rooturl=df['joblink'][i]
        headers= {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        request= requests.get(rooturl, headers)
        soup= BeautifulSoup(request.content, 'html.parser')
        
        
        html= list(soup.children)
        try:
            body=html[2]
        except:
            print('Captcha blocking the scraping')
        
        content=list(body.children)
        tags=content[3]
        
        
        textall=tags.find_all(['p','br','li'])
        for element in textall:
            description= description + str(element.text) + ' '
        
        
        techno=['datastage','qlik','talend','java',' git ','github','gitlab','jenkins','terdata',\
                'tableau','powerbi','power bi', 'aws','azure','kafka', 'elk', 'puppet',' odi ',\
                'docker','ansible','kubernates',' r ','python','spark','data lake','hive',\
                'maven','hortonworks',' excel ','sql','databricks','microstrategy','gcp','airflow','ci/cd',\
                'hadoop','pyspark','api rest','bigquery','redshift','snowflake','datawarehouse',\
                 'glue','jira',' bo ','db2','oracle','qliksense','agile','confluence','xray','terraform',\
                'cloudera','sonar','modélisation','anglais', 'tableaux de bord','apache','tomcat',\
                'TDD', 'springboot','grafana','logstash','telegraf','postgresql','powerpoint','itil',\
                'prince2', 'pmp','zscaler','firewalls','vpn','cartographie','ldap','mysql','kanban',\
                'scrum','jboss','splunk','mariadb','mongodb','blueprism','sonarqube','scala','vba',' sas ',\
                'salesforce','powershell','tsql','ssrs',' ssis','ssas','linux','microservice', ' c ', ' c# ',\
                ' c # ','flask','django',' php ', 'prédiction','pytest','bash','elasticsearch', 'sap bo','looker',\
                'machine learning', 'tensorflow','pytorch','business object','knime','cobol','intégration continue',\
                'postgré sql','datalake','data lake', 'alteryx','adobe campaign','athena',' emr ','data factory',\
                'reactjs','mongo','google analytics','dataiku','big query','gdpr','data visualisation','yarn','hdfs',\
                'nifi','c++','uml','redhat','vertica','numpy',' spacy','julia','sqlalchemy','web scraping','spss',\
                ' acl ','matlab','keras','tests d''acceptance','stress testing','stress test',' ann', 'supervision des flux',\
                'back testing','gestion des flux','compagnes sea','bonne communication orale et écrite','problem solving',\
                'pandas','kdb','cloud tech','full stack web','jupyter','plotly',' sql','google analytics']
            
            
        for tech in techno:
            if tech in description.lower():
                techvalues.append(tech)
        v = list(techvalues)
        df['jobskills'][i]= v
        
    return df