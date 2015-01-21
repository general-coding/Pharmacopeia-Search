'''
Created on Oct 7, 2014

@author: Puneeth U Bharadwaj
'''

import csv

class REAC13Q4:
    'Parse RPSR13Q4 file'
    
    def __init__(self, primaryid, caseid, pt):
        self.primaryid = primaryid
        self.caseid = caseid
        self.pt = pt        
                
    def display(self):
        print(self.primaryid + " " + self.caseid + " " + self.pt)

reac_obj_list = []
reac_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/REAC13Q4.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='$', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = REAC13Q4(row[0], row[1], row[2])
                reac_obj_list.append(obj)
                reac_pid_list.append(getattr(obj, 'PRIMARYID'))
                
mycount = 0

for obj in reac_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()

for pid in reac_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
