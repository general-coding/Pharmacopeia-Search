'''
Created on Oct 7, 2014

@author: Puneeth U Bharadwaj
'''

import csv

class INDI13Q4:
    'Parse INDI13Q4 file'
    
    def __init__(self, primaryid, caseid, indi_drug_seq, indi_pt):
        self.primaryid = primaryid 
        self.caseid = caseid 
        self.indi_drug_seq = indi_drug_seq 
        self.indi_pt = indi_pt        
                
    def display(self):
        print(self.primaryid + " " + self.caseid + " " + self.indi_drug_seq + " " + self.indi_pt)

indi_obj_list = []
indi_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/INDI13Q4.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='$', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = INDI13Q4(row[0], row[1], row[2], row[3])
                indi_obj_list.append(obj)
                indi_pid_list.append(getattr(obj, 'PRIMARYID'))
                
mycount = 0

for obj in indi_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()

for pid in indi_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
