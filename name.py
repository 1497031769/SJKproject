#! /usr/bin/env python

import _pickle as pk
import csv
import numpy as np

f = open('./pdb25-6767-train.release.contactFeatures.pkl','rb')
raw = pk.load(f,encoding='bytes')
#f.close()

line = []
lines = []

for i in range(6367):
	line = []
	line.append(str(raw[i][b'name'])[2:-2])
	line.append('http://www1.rcsb.org/structure/'+str(raw[i][b'name'])[2:-2])
#	line.append(str(raw[i][b'sequence'])[2:-1])
#	line.append(len(str(raw[i][b'sequence'])[2:-1]))
	lines.append(line)

f = open('ids.csv','w',newline='')
headline = ['id','PDB link','sequence','seqlen']
writer = csv.writer(f)
writer.writerow(headline)
writer.writerows(lines)
f.close()

