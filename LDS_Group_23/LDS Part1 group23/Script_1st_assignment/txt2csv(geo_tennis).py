#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questo script è dedicato sia alla trasformazione in csv di countryInfo.txt e poi alla creazione della tabella Geography
"""


import csv

with open('/home/maryxsempre/Downloads/countryInfo.txt', 'r') as in_file:
    header = in_file.readlines()[50:51]
    head_stripped = (line.strip() for line in header)
    head_line = (line.split('\t') for line in head_stripped if line)
    in_file.seek(0) #ho bisogno di resettare il pointer sul file prima di usare readlines di nuovo
    lines1 = in_file.readlines()[51:]
    stripped = (line.strip() for line in lines1)
    lines = (line.split('\t') for line in stripped if line)
    with open('countryInfo.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        for row in head_line:
            writer.writerow(row)
        writer.writerows(lines)

#una volta trasformato posso usare il csv per estrarre le lingue, sia per iso, che per paese
with open('countryInfo.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     newcoun=dict()
     for row in reader:
         newcoun[row['ISO3']]=row['Languages']
         
with open('countryInfo.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     ndcoun=dict()
     for row in reader:
         ndcoun[row['Country']]=row['Languages']
#print(newcoun)


verogeo=dict()     
with open('/home/maryxsempre/Downloads/data2021/countries.csv', 'r') as geocsv:
    reader = csv.DictReader(geocsv)
    for line in reader:
        verogeo[line['country_code']]=[line['continent'],line['country_name']]
        try:
            verogeo[line['country_code']].append(newcoun[line['country_code']])
        except:
            verogeo[line['country_code']].append('')
            
            
for key in verogeo:
    if verogeo[key][-1]=='':
        del verogeo[key][-1]
        try:
            verogeo[key].append(ndcoun[verogeo[key][1]])
        except:
            verogeo[key].append('')

   
#a questo punto sistemo la lista di dizionari per la scrittura
geo_head=['country_ioc','continent','languages']
geos=[]        
for key,item in verogeo.items():
    geoer=dict()
    geoer['country_ioc']=key
    geoer['continent']=item[0]
    geoer['languages']=item[-1]
    geos.append(geoer)

with open('geography.csv','w') as file:
         writer = csv.DictWriter(file, fieldnames=geo_head)
         writer.writeheader()    
         writer.writerows(geos)
