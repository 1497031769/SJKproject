#! /usr/bin/python
import sys
import csv
import os
from Bio.PDB.PDBParser import PDBParser
p=PDBParser(PERMISSIVE=1)



f = open('./ids.csv','r')
read_lines = csv.reader(f)


line = []
lines = []
for i in read_lines:
#p=PDBParser(PERMISSIVE=1)
	if(i[0]=='id'):
		continue
	if(not os.path.exists('./proteindb/'+i[0]+'.pdb')):
		print('Pay attention %s not exist'%i[0])
		continue
	s=p.get_structure(i[0],'./proteindb/'+i[0]+'.pdb')
	author=s.header['author']
	s_ref=s.header['structure_reference']
	j_ref=s.header['journal_reference']
	line = []
	line.append(i[0])
	line.append(str(author))
	line.append(str(s_ref))
	line.append(str(j_ref))
	lines.append(line)

f.close()
f = open('./ref.csv','w',newline='')
head_line = ['id','author','structure reference','journal reference']
writer = csv.writer(f)
writer.writerow(head_line) 
writer.writerows(lines)
f.close()



'''
print(author)
print(s_ref)
print(j_ref)
'''
