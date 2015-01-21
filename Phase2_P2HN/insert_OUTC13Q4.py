'''
Created on Nov 3, 2014

@author: Puneeth U Bharadwaj
'''
import csv
from pymongo import MongoClient 

OUTC13Q4Array = []
conn = MongoClient(textCustomer)
# connecting to MongoDB and creating a database

with open('E:/workspace/P2HN/csv_files/OUTC13Q4.txt', 'r') as i:
    for OUTC13Q4Row in csv.reader(i, delimiter='$'):
        OUTC13Q4Array.append(OUTC13Q4Row)

db = conn.p2hn
OUTC13Q4Collection = db.OUTC13Q4

j = 0
m = 0
for OUTC13Q4Row in OUTC13Q4Array[1:]:
        dbInsert = {}
	if(OUTC13Q4Row[0]!=''):
        	dbInsert['PRIMARYID'] = str(OUTC13Q4Row[0])
	if(OUTC13Q4Row[1]!=''):
        	dbInsert['CASEID'] = str(OUTC13Q4Row[1])
	if(OUTC13Q4Row[2]!=''):
        	dbInsert['OUTC_COD'] = str(OUTC13Q4Row[2])        

        OUTC13Q4Collection.insert(dbInsert)
	print dbInsert
#print(db.OUTC13Q4.find({PRIMARY_ID: ""}))
