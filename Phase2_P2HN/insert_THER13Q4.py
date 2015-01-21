'''
Created on Nov 3, 2014

@author: Puneeth U Bharadwaj
'''
import csv
from pymongo import MongoClient 

THER13Q4Array = []
conn = MongoClient(textCustomer)
# connecting to MongoDB and creating a database

with open('E:/workspace/P2HN/csv_files/THER13Q4.txt', 'r') as i:
    for THER13Q4Row in csv.reader(i, delimiter='$'):
        THER13Q4Array.append(THER13Q4Row)

db = conn.p2hn
THER13Q4Collection = db.THER13Q4

j = 0
m = 0
for THER13Q4Row in THER13Q4Array[1:]:
    dbInsert = {}
    if(THER13Q4Row[0]!=''):
        dbInsert['PRIMARYID'] = str(THER13Q4Row[0])
    if(THER13Q4Row[1]!=''):
        dbInsert['CASEID'] = str(THER13Q4Row[1])
    if(THER13Q4Row[2]!=''):
        dbInsert['DSG_DRUG_SEQ'] = str(THER13Q4Row[2])
    if(THER13Q4Row[3]!=''):
        dbInsert['START_DT'] = str(THER13Q4Row[3])
    if(THER13Q4Row[4]!=''):
        dbInsert['END_DT'] = str(THER13Q4Row[4])
    if(THER13Q4Row[5]!=''):
        dbInsert['DUR'] = str(THER13Q4Row[5])
    if(THER13Q4Row[6]!=''):
        dbInsert['DUR_COD'] = str(THER13Q4Row[6])
    
    THER13Q4Collection.insert(dbInsert)
    print dbInsert
#print(db.THER13Q4.find({PRIMARY_ID: ""}))
