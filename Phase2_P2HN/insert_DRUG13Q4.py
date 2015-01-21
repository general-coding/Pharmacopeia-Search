'''
Created on Nov 3, 2014

@author: Puneeth U Bharadwaj
'''
import csv
from pymongo import MongoClient 

DRUG13Q4Array = []
conn = MongoClient(textCustomer)
# connecting to MongoDB and creating a database

with open('E:/workspace/P2HN/csv_files/DRUG13Q4.txt', 'r') as i:
    for DRUG13Q4Row in csv.reader(i, delimiter='$'):
        DRUG13Q4Array.append(DRUG13Q4Row)

db = conn.p2hn
DRUG13Q4Collection = db.DRUG13Q4

j = 0
m = 0
for DRUG13Q4Row in DRUG13Q4Array[1:]:
        dbInsert = {}
	if(DRUG13Q4Row[0]!=''):
        	dbInsert['PRIMARYID'] = str(DRUG13Q4Row[0])
	if(DRUG13Q4Row[1]!=''):
        	dbInsert['CASEID'] = str(DRUG13Q4Row[1])
	if(DRUG13Q4Row[2]!=''):
        	dbInsert['DRUG_SEQ'] = str(DRUG13Q4Row[2])
	if(DRUG13Q4Row[3]!=''):
        	dbInsert['ROLE_COD'] = str(DRUG13Q4Row[3])
	if(DRUG13Q4Row[4]!=''):
        	dbInsert['DRUGNAME'] = str(DRUG13Q4Row[4])
	if(DRUG13Q4Row[5]!=''):
        	dbInsert['VAL_VBM'] = str(DRUG13Q4Row[5])
	if(DRUG13Q4Row[6]!=''):
        	dbInsert['ROUTE'] = str(DRUG13Q4Row[6])
	if(DRUG13Q4Row[7]!=''):
        	dbInsert['DOSE_VBM'] = str(DRUG13Q4Row[7])
	if(DRUG13Q4Row[8]!=''):
        	dbInsert['CUM_DOSE_CHR'] = str(DRUG13Q4Row[8])
	if(DRUG13Q4Row[9]!=''):
        	dbInsert['CUM_DOSE_UNIT'] = str(DRUG13Q4Row[9])
	if(DRUG13Q4Row[10]!=''):
        	dbInsert['DECHAL'] = str(DRUG13Q4Row[10])
	if(DRUG13Q4Row[11]!=''):
        	dbInsert['RECHAL'] = str(DRUG13Q4Row[11])
	if(DRUG13Q4Row[12]!=''):
        	dbInsert['LOT_NUM'] = str(DRUG13Q4Row[12])
	if(DRUG13Q4Row[13]!=''):
        	dbInsert['EXP_DT'] = str(DRUG13Q4Row[13])
	if(DRUG13Q4Row[14]!=''):
        	dbInsert['NDA_NUM'] = str(DRUG13Q4Row[14])
	if(DRUG13Q4Row[15]!=''):
        	dbInsert['DOSE_AMT'] = str(DRUG13Q4Row[15])
	if(DRUG13Q4Row[16]!=''):
        	dbInsert['DOSE_UNIT'] = str(DRUG13Q4Row[16])
	if(DRUG13Q4Row[17]!=''):
        	dbInsert['DOSE_FORM'] = str(DRUG13Q4Row[17])
	if(DRUG13Q4Row[18]!=''):
        	dbInsert['DOSE_FREQ'] = str(DRUG13Q4Row[18])

        DRUG13Q4Collection.insert(dbInsert)
	print dbInsert
print(db.DRUG13Q4.count())
