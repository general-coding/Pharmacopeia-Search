'''
Created on Oct 7, 2014

@author: Puneeth U Bharadwaj
'''

import csv

class OUTC13Q4:
    'Parse OUTC13Q4 file'
    
    def __init__(self, primaryid, caseid, outc_cod):
        self.primaryid = primaryid
        self.caseid = caseid
        self.outc_cod = outc_cod
                
    def display(self):
        print(self.primaryid + " " + self.caseid + " " + self.outc_cod)

outc_obj_list = []
outc_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/OUTC13Q4.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='$', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = OUTC13Q4(row[0], row[1], row[2])
                outc_obj_list.append(obj)
                outc_pid_list.append(getattr(obj, 'PRIMARYID'))
                
mycount = 0

for obj in outc_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()
outc_pid_list
for pid in outc_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
