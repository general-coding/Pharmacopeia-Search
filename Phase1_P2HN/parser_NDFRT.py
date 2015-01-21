'''
Created on Oct 7, 2014

@author: Puneeth U Bharadwaj
'''

import csv

class NDFRT:
    'Parse NDFRT file'
    
    def __init__(self, name, nid):
        self.name = name
        self.nid = nid        
                
    def display(self):
        print(self.name + "-" + self.nid)

ndfrt_obj_list = []
ndfrt_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/NDFRT_Public_2014.07.07_NUI.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = NDFRT(row[0], row[1])
                ndfrt_obj_list.append(obj)
                ndfrt_pid_list.append(getattr(obj, 'NAME'))
                
mycount = 0

for obj in ndfrt_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()

for pid in ndfrt_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
