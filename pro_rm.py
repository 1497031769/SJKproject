#! /usr/bin/python
import _pickle as pk
import numpy as np
import os

f = open('./pdb25-6767-train.release.contactFeatures.pkl','rb')
raw = pk.load(f,encoding='bytes')
f.close()
  
# create a list to save the id
ids=[]
for i in raw:
	ids.append(i[b'name']+'.pdb')

#from .pkl get the

for j in ids:
	result = os.system('mv ./proteindb/%s ./pdbs'%i)
	 
