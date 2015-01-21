'''
Created on Nov 10, 2014

@author: Puneeth U Bharadwaj
'''
import csv
from pymongo import MongoClient 

RxTermsIngredients201408Array = []

conn = MongoClient(textCustomer)
# connecting to MongoDB and creating a database

with open('E:/workspace/P2HN/csv_files/RxTermsIngredients201408.txt', 'r') as i:
    for RxTermsIngredients201408Row in csv.reader(i, delimiter='|'):
        RxTermsIngredients201408Array.append(RxTermsIngredients201408Row)

db = conn.p2hn
RxTerms201408IngredientsCollection = db.RxTermsIngredients201408

j = 0
m = 0
for RxTermsIngredients201408Row in RxTermsIngredients201408Array[1:]:
    dbInsert = {}
    if(RxTermsIngredients201408Row[0]!=''):
        dbInsert['RXCUI'] = str(RxTermsIngredients201408Row[0])
    if(RxTermsIngredients201408Row[1]!=''):
        dbInsert['INGREDIETN'] = str(RxTermsIngredients201408Row[1])
    if(RxTermsIngredients201408Row[2]!=''):
        dbInsert['ING_RXCUI'] = str(RxTermsIngredients201408Row[2])
    
    RxTerms201408IngredientsCollection.insert(dbInsert)
    print(dbInsert)
#print(db.RxTerms201408.find({RXCUI: "1011841"}))
