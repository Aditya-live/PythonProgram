"""
Monitor module
"""
import pymysql as db

def login():

    conn=db.connect("monitor")

    qry="create table if not exists prospect(prospId int primary )"

    
    
