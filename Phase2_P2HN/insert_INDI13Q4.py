'''
Created on Nov 3, 2014

@author: Puneeth U Bharadwaj
'''
import csv
from pymongo import MongoClient 

INDI13Q4Array = []
conn = MongoClient(textCustomer)
# connecting to MongoDB and creating a database

with open('E:/workspace/P2HN/csv_files/INDI13Q4.txt', 'r') as i:
    for INDI13Q4Row in csv.reader(i, delimiter='$'):
        INDI13Q4Array.append(INDI13Q4Row)

db = conn.p2hn
INDI13Q4Collection = db.INDI13Q4

j = 0
m = 0
for INDI13Q4Row in INDI13Q4Array[1:]:
        dbInsert = {}
	if(INDI13Q4Row[0]!=''):
	        dbInsert['PRIMARYID'] = str(INDI13Q4Row[0])
	if(INDI13Q4Row[1]!=''):
        	dbInsert['CASEID'] = str(INDI13Q4Row[1])
	if(INDI13Q4Row[2]!=''):
        	dbInsert['INDI_DRUG_SEQ'] = str(INDI13Q4Row[2])
	if(INDI13Q4Row[3]!=''):
        	dbInsert['INDI_PT'] = str(INDI13Q4Row[3])        

        INDI13Q4Collection.insert(dbInsert)
	print dbInsert
#print(db.INDI13Q4.find({PRIMARY_ID: ""}))
