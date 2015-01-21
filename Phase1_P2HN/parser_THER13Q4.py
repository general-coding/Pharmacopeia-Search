'''
Created on Oct 7, 2014

@author: Puneeth U Bharadwaj
'''

import csv

class THER13Q4:
    'Parse THER13Q4 file'
    
    def __init__(self, primaryid, caseid, dsg_drug_seq, start_dt, end_dt, dur, dur_cod):
        self.primaryid = primaryid
        self.caseid = caseid
        self.dsg_drug_seq = dsg_drug_seq        
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.dur = dur
        self.dur_cod = dur_cod
                
    def display(self):
        print(self.primaryid + " " + self.caseid + " " + self.dsg_drug_seq + " " + 
              self.start_dt + " " + self.end_dt + " " + self.dur + " " + self.dur_cod)

ther_obj_list = []
ther_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/THER13Q4.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='$', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = THER13Q4(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                ther_obj_list.append(obj)
                ther_pid_list.append(getattr(obj, 'PRIMARYID'))
                
mycount = 0

for obj in ther_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()

for pid in ther_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
