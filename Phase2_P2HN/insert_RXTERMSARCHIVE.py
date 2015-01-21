'''
Created on Nov 3, 2014

@author: Puneeth U Bharadwaj
'''
import csv
from pymongo import MongoClient 

RxTerms201408Array = []

conn = MongoClient(textCustomer)
# connecting to MongoDB and creating a database

with open('E:/workspace/P2HN/csv_files/RxTermsArchive201408.txt', 'r') as i:
    for RxTerms201408Row in csv.reader(i, delimiter='|'):
        RxTerms201408Array.append(RxTerms201408Row)

db = conn.p2hn
RxTerms201408Collection = db.RxTermsArchive201408
 
j = 0
m = 0
for RxTerms201408Row in RxTerms201408Array[1:]:
    dbInsert = {}
    if(RxTerms201408Row[0]!=''):
        dbInsert['RXCUI'] = str(RxTerms201408Row[0])
    if(RxTerms201408Row[1]!=''):    
        dbInsert['GENERIC_RXCUI'] = str(RxTerms201408Row[1])
    if(RxTerms201408Row[2]!=''):
        dbInsert['TTY'] = str(RxTerms201408Row[2])
    if(RxTerms201408Row[3]!=''):    
        dbInsert['FULL_NAME'] = str(RxTerms201408Row[3])
    if(RxTerms201408Row[4]!=''):    
        dbInsert['RXN_DOSE_FORM'] = str(RxTerms201408Row[4])
    if(RxTerms201408Row[5]!=''):    
        dbInsert['FULL_GENERIC_NAME'] = str(RxTerms201408Row[5])
    if(RxTerms201408Row[6]!=''):    
        dbInsert['BRAND_NAME'] = str(RxTerms201408Row[6])
    if(RxTerms201408Row[7]!=''):    
        dbInsert['DISPLAY_NAME'] = str(RxTerms201408Row[7])
    if(RxTerms201408Row[8]!=''):    
        dbInsert['ROUTE'] = str(RxTerms201408Row[8])
    if(RxTerms201408Row[9]!=''):    
        dbInsert['NEW_DOSE_FORM'] = str(RxTerms201408Row[9])
    if(RxTerms201408Row[10]!=''):   
        dbInsert['STRENGTH'] = str(RxTerms201408Row[10])
    if(RxTerms201408Row[11]!=''):   
        dbInsert['SUPPRESS_FOR'] = str(RxTerms201408Row[11])
    if(RxTerms201408Row[12]!=''):   
        dbInsert['DISPLAY_NAME_SYNONYM'] = str(RxTerms201408Row[12])
    if(RxTerms201408Row[13]!=''):   
        dbInsert['IS_RETIRED'] = str(RxTerms201408Row[13])
    if(RxTerms201408Row[14]!=''):   
        dbInsert['SXDG_RXCUI'] = str(RxTerms201408Row[14])
    if(RxTerms201408Row[15]!=''):   
        dbInsert['SXDG_TTY'] = str(RxTerms201408Row[15])
    if(RxTerms201408Row[16]!=''):   
        dbInsert['SXDG_NAME'] = str(RxTerms201408Row[16])

    RxTerms201408Collection.insert(dbInsert)
    print dbInsert
#print(db.RxTerms201408.find({RXCUI: "1011841"}))
