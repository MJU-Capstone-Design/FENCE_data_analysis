import csv
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import seaborn as sns  
goo = ['중구', '종로구', '마포구', '영등포구', '용산구', '금천구', '강남구', '구로']

f = open('./addr_10001.csv', 'r', encoding='utf-8')
w = open('./output1.csv', 'w', encoding='utf-8')
rdr = csv.reader(f)
wr = csv.writer(w)

for line in rdr:
    for g in goo:
        if g in line[2]:
            wr.writerow(line)
f.close()
w.close()

f = open('./nolatlnt_1.csv', 'r', encoding='utf-8')
w = open('./output2.csv', 'w', encoding='utf-8')
rdr = csv.reader(f)
wr = csv.writer(w)

for line in rdr:
    for g in goo:
        if g in line[2]:
            wr.writerow(line)
f.close()
w.close()

f = open('./nolatlnt_2.csv', 'r', encoding='utf-8')
w = open('./output3.csv', 'w', encoding='utf-8')
rdr = csv.reader(f)
wr = csv.writer(w)

for line in rdr:
    for g in goo:
        if g in line[2]:
            wr.writerow(line)
f.close()
w.close()

f = open('./nolatlnt2.csv', 'r', encoding='utf-8')
w = open('./output4.csv', 'w', encoding='utf-8')
rdr = csv.reader(f)
wr = csv.writer(w)

for line in rdr:
    for g in goo:
        if g in line[2]:
            wr.writerow(line)
f.close()
w.close()

f = open('./nolatlnt3.csv', 'r', encoding='utf-8')
w = open('./output5.csv', 'w', encoding='utf-8')
rdr = csv.reader(f)
wr = csv.writer(w)

for line in rdr:
    for g in goo:
        if g in line[2]:
            wr.writerow(line)
f.close()
w.close()
f = open('./perfect_data.csv', 'r', encoding='utf-8')
w = open('./output6.csv', 'w', encoding='utf-8')
rdr = csv.reader(f)
wr = csv.writer(w)

for line in rdr:
    for g in goo:
        if g in line[2]:
            wr.writerow(line)
f.close()
w.close()

f = open('./perfect_street.csv', 'r', encoding='utf-8')
w = open('./output7.csv', 'w', encoding='utf-8')
rdr = csv.reader(f)
wr = csv.writer(w)

for line in rdr:
    for g in goo:
        if g in line[2]:
            wr.writerow(line)
f.close()
w.close()