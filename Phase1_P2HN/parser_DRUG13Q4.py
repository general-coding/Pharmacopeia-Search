'''
Created on Oct 7, 2014

@author: Puneeth U Bharadwaj
'''

import csv

class DRUG13Q4:
    'Parse DRUG13Q4 file'
    
    def __init__(self, primaryid, caseid, drug_seq, role_cod, drugname, val_vbm, route, dose_vbm, cum_dose_chr, cum_dose_unit, dechal, rechal, lot_num, exp_dt, nda_num, dose_amt, dose_unit, dose_form, dose_freq):
        self.primaryid = primaryid 
        self.caseid = caseid 
        self.drug_seq = drug_seq 
        self.role_cod = role_cod 
        self.drugname = drugname 
        self.val_vbm = val_vbm 
        self.route = route 
        self.dose_vbm = dose_vbm 
        self.cum_dose_chr = cum_dose_chr 
        self.cum_dose_unit = cum_dose_unit 
        self.dechal = dechal 
        self.rechal = rechal 
        self.lot_num = lot_num 
        self.exp_dt = exp_dt 
        self.nda_num = nda_num 
        self.dose_amt = dose_amt 
        self.dose_unit = dose_unit 
        self.dose_form = dose_form 
        self.dose_freq = dose_freq        
                
    def display(self):
        print(self.primaryid + " " + self.caseid + " " + self.drug_seq + " " + self.role_cod + " " + self.drugname + " " + self.val_vbm + " " + 
              self.route + " " + self.dose_vbm + " " + self.cum_dose_chr + " " + self.cum_dose_unit + " " + self.dechal + " " + self.rechal + " " + 
              self.lot_num + " " + self.exp_dt + " " + self.nda_num + " " + self.dose_amt + " " + self.dose_unit + " " + self.dose_form + " " + 
              self.dose_freq)

drug_obj_list = []
drug_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/DRUG13Q4.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='$', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = DRUG13Q4(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                               row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18])
                drug_obj_list.append(obj)
                drug_pid_list.append(getattr(obj, 'PRIMARYID'))
                
mycount = 0

for obj in drug_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()

for pid in drug_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
