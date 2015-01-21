'''
Created on Nov 3, 2014

@author: Puneeth U Bharadwaj
'''
import csv
from pymongo import MongoClient 

DEMO13Q4Array = []

conn = MongoClient(textCustomer)
# connecting to MongoDB and creating a database

with open('E:/workspace/P2HN/csv_files/DEMO13Q4.txt', 'r') as i:
    for DEMO13Q4Row in csv.reader(i, delimiter='$'):
        DEMO13Q4Array.append(DEMO13Q4Row)

db = conn.p2hn
DEMO13Q4Collection = db.DEMO13Q4

j = 0
m = 0
import pdb
pdb.set_trace()
for DEMO13Q4Row in DEMO13Q4Array[1:]:
    dbInsert = {}
    if(DEMO13Q4Row[0]!=''):
    	dbInsert['PRIMARYID'] = str(DEMO13Q4Row[0])
    if(DEMO13Q4Row[1]!=''):
    	dbInsert['CASEID'] = str(DEMO13Q4Row[1])
    if(DEMO13Q4Row[2]!=''):
    	dbInsert['CASEVERSION'] = str(DEMO13Q4Row[2])
    if(DEMO13Q4Row[3]!=''):
    	dbInsert['I_F_CODE'] = str(DEMO13Q4Row[3])
    if(DEMO13Q4Row[4]!=''):
    	dbInsert['EVENT_DT'] = str(DEMO13Q4Row[4])
    if(DEMO13Q4Row[5]!=''):
    	dbInsert['MFR_DT'] = str(DEMO13Q4Row[5])
    if(DEMO13Q4Row[6]!=''):
    	dbInsert['INIT_FDA_DT'] = str(DEMO13Q4Row[6])
    if(DEMO13Q4Row[7]!=''):
    	dbInsert['FDA_DT'] = str(DEMO13Q4Row[7])
    if(DEMO13Q4Row[8]!=''):
    	dbInsert['REPT_COD'] = str(DEMO13Q4Row[8])
    if(DEMO13Q4Row[9]!=''):
    	dbInsert['MFR_NUM'] = str(DEMO13Q4Row[9])
    if(DEMO13Q4Row[10]!=''):
    	dbInsert['MFR_SNDR'] = str(DEMO13Q4Row[10])
    if(DEMO13Q4Row[11]!=''):
    	dbInsert['AGE'] = str(DEMO13Q4Row[11])
    if(DEMO13Q4Row[12]!=''):
    	dbInsert['AGE_COD'] = str(DEMO13Q4Row[12])
    if(DEMO13Q4Row[13]!=''):
    	dbInsert['GNDR_COD'] = str(DEMO13Q4Row[13])
    if(DEMO13Q4Row[14]!=''):
    	dbInsert['E_SUB'] = str(DEMO13Q4Row[14])
    if(DEMO13Q4Row[15]!=''):
    	dbInsert['WT'] = str(DEMO13Q4Row[15])
    if(DEMO13Q4Row[16]!=''):
    	dbInsert['WT_COD'] = str(DEMO13Q4Row[16])
    if(DEMO13Q4Row[17]!=''):
    	dbInsert['REPT_DT'] = str(DEMO13Q4Row[17])
    if(DEMO13Q4Row[18]!=''):
    	dbInsert['TO_MFR'] = str(DEMO13Q4Row[18])
    if(DEMO13Q4Row[19]!=''):
    	dbInsert['OCCP_COD'] = str(DEMO13Q4Row[19])
    if(DEMO13Q4Row[20]!=''):
    	dbInsert['REPORTER_COUNTRY'] = str(DEMO13Q4Row[20])
    if(DEMO13Q4Row[21]!=''):
    	dbInsert['OCCR_COUNTRY'] = str(DEMO13Q4Row[21])
 
    
    DEMO13Q4Collection.insert(dbInsert)
    print dbInsert

print(db.DEMO13Q4.count())
