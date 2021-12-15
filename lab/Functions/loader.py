#!/usr/bin/env python3

def loader(filepath,database,target_table):
    
    from configDB import config
    from scrap_transformer import scrap_transformer
    from transformer import transformer
    import psycopg2.extras as extras 
    import psycopg2.errorcodes
    from datetime import date
    
    if 'job_freel' in filepath:
        df=transformer(filepath)
    else:
        df=scrap_transformer(filepath)
    number_records= len(df)
    run_date=[date.today()]*number_records
    
    df=df.rename(columns={'date':'date_posted'})
    df['run_date']=run_date
    
    param = config(database, filename='tns.ini')
    conn = psycopg2.connect(**param)
    cur = conn.cursor()
    
    cols=','.join(list(df.columns))
    
    tuples=[tuple(x) for x in df.to_numpy()]
    try:
        query="INSERT INTO %s (%s) VALUES %%s;" % (target_table,cols)
    except:
        pass
    
    
    try:
        extras.execute_values(cur,query,tuples)
        conn.commit()
    except(Exception,psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        conn.rollback()
        cur.close()
        return 1
    print(f'{filepath}  HAS BEEN LOADED SUCCESSFULLY INTO  {target_table}')
    cur.close()