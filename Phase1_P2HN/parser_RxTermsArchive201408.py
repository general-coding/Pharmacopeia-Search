'''
Created on Oct 7, 2014

@author: Puneeth U Bharadwaj
'''

import csv

class RxTermsArchive201408:
    'Parse RxTermsArchive201408 file'
    
    def __init__(self, RXCUI, GENERIC_RXCUI, TTY, FULL_NAME, RXN_DOSE_FORM, FULL_GENERIC_NAME, BRAND_NAME, DISPLAY_NAME, ROUTE, NEW_DOSE_FORM, 
                 STRENGTH, SUPPRESS_FOR, DISPLAY_NAME_SYNONYM, IS_RETIRED, SXDG_RXCUI, SXDG_TTY, SXDG_NAME):
        self.RXCUI = RXCUI
        self.GENERIC_RXCUI = GENERIC_RXCUI
        self.TTY = TTY
        self.FULL_NAME = FULL_NAME
        self.RXN_DOSE_FORM = RXN_DOSE_FORM
        self.FULL_GENERIC_NAME = FULL_GENERIC_NAME
        self.BRAND_NAME = BRAND_NAME
        self.DISPLAY_NAME = DISPLAY_NAME
        self.ROUTE = ROUTE
        self.NEW_DOSE_FORM = NEW_DOSE_FORM
        self.STRENGTH = STRENGTH
        self.SUPPRESS_FOR = SUPPRESS_FOR
        self.DISPLAY_NAME_SYNONYM = DISPLAY_NAME_SYNONYM
        self.IS_RETIRED = IS_RETIRED
        self.SXDG_RXCUI = SXDG_RXCUI
        self.SXDG_TTY = SXDG_TTY
        self.SXDG_NAME = SXDG_NAME        
                
    def display(self):
        print(self.RXCUI+ " " + self.GENERIC_RXCUI+ " " + self.TTY+ " " + self.FULL_NAME+ " " + self.RXN_DOSE_FORM+ " " + self.FULL_GENERIC_NAME+ " " + 
              self.BRAND_NAME+ " " +  self.DISPLAY_NAME+ " " + self.ROUTE+ " " + self.NEW_DOSE_FORM+ " " + self.STRENGTH+ " " + self.SUPPRESS_FOR+ " " + 
              self.DISPLAY_NAME_SYNONYM+ " " + self.IS_RETIRED+ " " + self.SXDG_RXCUI+ " " + self.SXDG_TTY+ " " + self.SXDG_NAME)

rxarchive_obj_list = []
rxarchive_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/RxTermsArchive201408.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='|', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = RxTermsArchive201408(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                    row[10], row[11], row[12], row[13], row[14], row[15], row[16])
                rxarchive_obj_list.append(obj)
                rxarchive_pid_list.append(getattr(obj, 'RXCUI'))
                
mycount = 0

for obj in rxarchive_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()

for pid in rxarchive_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
