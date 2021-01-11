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
        #print(type(row[2]))
        '''
        for j in row[2]:
            struct=str(j)+','
        '''
        eachline = str(row[0])+'@'+str(row[2])+'@'+str(row[3])
        lines.add(eachline)
    for i in lines:
        values=i.split('@')
        #print(len(values));
        #print(values)
        sql='INSERT INTO Reference VALUES (%s,%s,%s)'
        cur.execute(sql,values)
        conn.commit()
    
print("done!")
cur.close()
conn.close()

