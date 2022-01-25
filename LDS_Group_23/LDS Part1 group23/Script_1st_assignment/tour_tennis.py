#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In questo script viene estratta la tabella Torunament 
"""

import csv


#in questa prima parte viene genrata una chiave fittizia
infile = '/home/maryxsempre/Downloads/data2021/tennis.csv'
with open(infile, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     
     date_id=dict()
     i= -1
     for row in reader:
         if row['tourney_date'] not in date_id:
             i+=1
             date_id[row['tourney_date']]=i
     #print(date_id)
    
with open(infile, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     #get fieldnames from DictReader object and store in list
     headers = reader.fieldnames
     head_tour = headers[0:6]+headers[47:49]
     
     with open('tour.csv', 'w', newline='') as tour:
         
         writer = csv.DictWriter(tour, fieldnames=head_tour)
         writer.writeheader()
         for line in reader:
             x={k: line[k] for k in head_tour}
             x['tourney_date']=date_id[x['tourney_date']]
             writer.writerow(x)

#dopo aver estratto le righe interessate rimouoviamo i duolicati generati dall'estrazione
with open('tour.csv','r') as file:
    reader = csv.DictReader(file)
    newrows=[]
    ide=[]
    for row in reader:
        if row['tourney_id'] not in ide:
            ide.append(row['tourney_id'])
            newrows.append(row)


with open('tournament.csv','w') as file:
         writer = csv.DictWriter(file, fieldnames=head_tour)
         writer.writeheader()    
         writer.writerows(newrows)





