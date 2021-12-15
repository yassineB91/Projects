#!/usr/bin/env python3
def looper(filepath):
    
    import os
    from loader import loader
    for filename in os.listdir(filepath):
        f=os.path.join(filepath,filename)
        if os.path.isfile(f) and ('jobs_ile' in filename):
            loader(f,database='POSTGRESQL_jobmarket',target_table='d_os.jobs')
        elif 'job_freel' in filename:
            loader(f,database='POSTGRESQL_jobmarket',target_table='d_os.jobs_freelance')
            


