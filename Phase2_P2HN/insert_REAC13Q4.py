'''
Created on Nov 3, 2014

@author: Puneeth U Bharadwaj
'''
import csv
from pymongo import MongoClient 

REAC13Q4Array = []
conn = MongoClient(textCustomer)
# connecting to MongoDB and creating a database

with open('E:/workspace/P2HN/csv_files/REAC13Q4.txt', 'r') as i:
    for REAC13Q4Row in csv.reader(i, delimiter='$'):
        REAC13Q4Array.append(REAC13Q4Row)

db = conn.p2hn
REAC13Q4Collection = db.REAC13Q4

j = 0
m = 0
for REAC13Q4Row in REAC13Q4Array[1:]:
    dbInsert = {}
    if(REAC13Q4Row[0]!=''):
        dbInsert['PRIMARYID'] = str(REAC13Q4Row[0])
    if(REAC13Q4Row[1]!=''):
        dbInsert['CASEID'] = str(REAC13Q4Row[1])
    if(REAC13Q4Row[2]!=''):
        dbInsert['PT'] = str(REAC13Q4Row[2])     

    REAC13Q4Collection.insert(dbInsert)
    print dbInsert
#print(db.REAC13Q4.find({PRIMARY_ID: ""}))
