import csv
import pandas as pd

file1='unitConversion.csv'
file2='brightStars.csv'

d1=[]
d2=[]

with open(file1,'r') as f:
    r=csv.reader(f)
    for i in r:
        d1.append(i)

with open(file2,'r') as f:
    r=csv.reader(f)
    for i in r:
        d2.append(i)

h1=d1[0]
h2=d2[0]
td1=d1[1:]
td2=d1[1:]

h=h1+h2
td=[] 
for i in td1:
    td.append(i)
for j in td2:
    td.append(j)

with open('total_stars.csv','w')as f:
    r=csv.writer(f)
    r.writerow(h)
    r.writerows(td)