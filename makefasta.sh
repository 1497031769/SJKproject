#! /bin/bash
function makefasta(){
for file in `ls`
do
 python pdb2fasta.py $file >> result.fasta
done
}
makefasta
