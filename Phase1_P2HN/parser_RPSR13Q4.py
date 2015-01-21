'''
Created on Oct 7, 2014

@author: Puneeth U Bharadwaj
'''

import csv

class RPSR13Q4:
    'Parse RPSR13Q4 file'
    
    def __init__(self, primaryid, caseid, rpsr_cod):
        self.primaryid = primaryid
        self.caseid = caseid
        self.rpsr_cod = rpsr_cod        
                
    def display(self):
        print(self.primaryid + " " + self.caseid + " " + self.rpsr_cod)

rspr_obj_list = []
rspr_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/RPSR13Q4.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='$', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = RPSR13Q4(row[0], row[1], row[2])
                rspr_obj_list.append(obj)
                rspr_pid_list.append(getattr(obj, 'PRIMARYID'))
                
mycount = 0

for obj in rspr_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()

for pid in rspr_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
