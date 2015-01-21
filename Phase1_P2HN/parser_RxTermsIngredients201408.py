'''
Created on Oct 7, 2014

@author: Puneeth U Bharadwaj
'''

import csv

class RxTermsIngredients201408:
    'Parse RxTermsIngredients201408 file'
    
    def __init__(self, RXCUI, INGREDIENT, ING_RXCUI):
        self.RXCUI = RXCUI
        self.INGREDIENT = INGREDIENT
        self.ING_RXCUI = ING_RXCUI        
                
    def display(self):
        print(self.RXCUI+ " " + self.GENERIC_RXCUI+ " " + self.TTY)

rxing_obj_list = []
rxing_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/RxTermsIngredients201408.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='|', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = RxTermsIngredients201408(row[0], row[1], row[2])
                rxing_obj_list.append(obj)
                rxing_pid_list.append(getattr(obj, 'RXCUI'))
                
mycount = 0

for obj in rxing_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()

for pid in rxing_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
