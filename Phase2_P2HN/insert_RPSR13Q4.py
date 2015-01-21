'''
Created on Nov 3, 2014

@author: Puneeth U Bharadwaj
'''
import csv
from pymongo import MongoClient 

RPSR13Q4Array = []
conn = MongoClient(textCustomer)
# connecting to MongoDB and creating a database

with open('E:/workspace/P2HN/csv_files/RPSR13Q4.txt', 'r') as i:
    for RPSR13Q4Row in csv.reader(i, delimiter='$'):
        RPSR13Q4Array.append(RPSR13Q4Row)

db = conn.p2hn
RPSR13Q4Collection = db.RPSR13Q4

j = 0
m = 0
for RPSR13Q4Row in RPSR13Q4Array[1:]:
        dbInsert = {}
	if(RPSR13Q4Row[0]!=''):
        	dbInsert['PRIMARYID'] = str(RPSR13Q4Row[0])
	if(RPSR13Q4Row[1]!=''):
        	dbInsert['CASEID'] = str(RPSR13Q4Row[1])
	if(RPSR13Q4Row[2]!=''):
        	dbInsert['RPSR_COD'] = str(RPSR13Q4Row[2])

        RPSR13Q4Collection.insert(dbInsert)
	print dbInsert
#print(db.RPSR13Q4.find({PRIMARY_ID: ""}))
