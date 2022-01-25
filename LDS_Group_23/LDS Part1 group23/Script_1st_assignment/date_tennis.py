#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 17:11:50 2021

@author: maryxsempre
"""


import csv

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

lista=[]
for data , ide in date_id.items():
    date=dict()
    date['date_id']=ide
    date['year']=int(data[:4])
    date['month']=int(data[4:6])
    date['day']=int(data[6:])
    if date['month'] in {1,2,3,4}:
        date['quarter']=1
    elif date['month'] in {5,6,7,8}:
        date['quarter']=2
    else:
        date['quarter']=3
    lista.append(date)

#print(lista)
head=['date_id','year','month','day','quarter']
with open('date.csv','w') as file:
         writer = csv.DictWriter(file, fieldnames=head)
         writer.writeheader()    
         writer.writerows(lista)