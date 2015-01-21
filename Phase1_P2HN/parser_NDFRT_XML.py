'''
Created on Oct 17, 2014

@author: Puneeth U Bharadwaj
'''

import xml.etree.ElementTree as ET

class NDFRTXML:
    'Parse NDFRT XML'
    
    def __init__(self, name, code, id, kind):
        self.name = name
        self.code = code
        self.id = id
        self.kind = kind
        
    def display(self):
        print(self.name + '\t' + self.code + '\t' + self.id + '\t' + self.kind)
        
ndfrtxml_obj_list = []    
ndfrtxml_pid_list = []
    
tree = ET.parse('E:/workspace/P2HN/csv_files/NDFRT_Public_2014.07.07_TDE.xml')
root = tree.getroot()
i = 0
print ('Name: \t Code: \t Id:  \t\t Kind: ')
for conceptdef in root.findall('conceptDef'):
        name = conceptdef.find('name').text
        code = conceptdef.find('code').text
        id = conceptdef.find('id').text
        kind = conceptdef.find('kind').text
        obj = NDFRTXML(name, code, id, kind)
        ndfrtxml_obj_list.append(obj)
        ndfrtxml_pid_list.append(getattr(obj, 'id'))
        
mycount=0

for obj in ndfrtxml_obj_list:
    obj.display()
    mycount = mycount + 1
    if mycount > 10:
        mycount = 0
        break
        
print()

for pid in ndfrtxml_pid_list:
    print(pid)
    mycount = mycount + 1
    if mycount > 10:
        break;