#! /usr/bin/ python
import pymysql 
import csv

conn=pymysql.connect(host='175.24.189.23',user='root',passwd='qq19980214qq',db='MMPDB',port=3306,charset='utf8')
cur=conn.cursor()
with open('/root/Project/ref.csv','r',newline='',encoding='utf-8') as csvfile:
    next(csvfile)  #跳过第一行
    reader=csv.reader(csvfile,delimiter=',')
    lines = set()
    for row in reader:
        eachline = str(row[0])+'#'+str(row[1])
        lines.add(eachline)
    for i in lines:
        values=i.split('#')[:2]
        #print(values)
        sql='INSERT INTO Protein VALUES (%s,%s)'
        cur.execute(sql,values)
        conn.commit()
    
print("done!")
cur.close()
conn.close()
