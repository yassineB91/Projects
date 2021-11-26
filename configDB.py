#!/usr/bin/env python3
def config(section='POSTGRESQL', filename='tns.ini'):
    import configparser
    parser=configparser.ConfigParser()
    parser.read(filename)
    con={}
    for i in ['host','port','database','user','password']:
        con[i]=parser[section][i]
        
    return con       
    