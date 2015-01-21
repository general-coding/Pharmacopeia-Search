'''
Created on Nov 11, 2014

@author: Puneeth U Bharadwaj
'''
import csv

class DEMO13Q4:
    'Parse DEMO13Q4 file'
    
    def __init__(self, primaryid, caseid, caseversion, i_f_code, event_dt, mfr_dt, init_fda_dt, fda_dt, rept_cod, mfr_num, mfr_sndr, age, age_cod, gndr_cod, e_sub, wt, wt_cod, rept_dt, to_mfr, occp_cod, reporter_country, occr_country):
        self.primaryid = primaryid
        self.caseid = caseid
        self.caseversion = caseversion
        self.i_f_code = i_f_code
        self.event_dt = event_dt
        self.mfr_dt = mfr_dt
        self.init_fda_dt = init_fda_dt
        self.fda_dt = fda_dt
        self.rept_cod = rept_cod
        self.mfr_num = mfr_num
        self.mfr_sndr = mfr_sndr
        self.age = age
        self.age_cod = age_cod
        self.gndr_cod = gndr_cod
        self.e_sub = e_sub
        self.wt = wt
        self.wt_cod = wt_cod
        self.rept_dt = rept_dt
        self.to_mfr = to_mfr
        self.occp_cod = occp_cod
        self.reporter_country = reporter_country
        self.occr_country = occr_country        
                
    def display(self):
        print(self.primaryid + " " + self.caseid + " " + self.caseversion + " " + self.i_f_code + " " + self.event_dt + " " + self.mfr_dt + " " + 
              self.init_fda_dt + " " + self.fda_dt + " " + self.rept_cod + " " + self.mfr_num + " " + self.mfr_sndr + " " + self.age + " " +
              self.age_cod + " " + self.gndr_cod + " " + self.e_sub + " " + self.wt + " " + self.wt_cod + " " + self.rept_dt + " " + 
              self.to_mfr + " " + self.occp_cod + " " + self.reporter_country + " " + self.occr_country)

demo_obj_list = []
demo_pid_list = []
    
with open('E:/workspace/P2HN/csv_files/DEMO13Q4.txt', 'r') as csvfile :
            filereader = csv.reader(csvfile, delimiter='$', quoting=csv.QUOTE_NONE)
            for row in filereader:
                obj = DEMO13Q4(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], 
                               row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21])
                demo_obj_list.append(obj)
                demo_pid_list.append(getattr(obj, 'PRIMARYID'))
                
mycount = 0

for obj in demo_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break

print()

for pid in demo_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;
