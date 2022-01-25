#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In questo script viene estratta la tabella Match semplicemente selezionando le colonne
"""
import csv

infile = '/home/maryxsempre/Downloads/data2021/tennis.csv'

with open(infile, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     #get fieldnames from DictReader object and store in list
     headers = reader.fieldnames
     head_match = [headers[0]]+headers[6:8]+[headers[14]]+headers[21:47]
     
     with open('match.csv', 'w', newline='') as match:
         
         writer = csv.DictWriter(match, fieldnames=head_match)
         writer.writeheader()
         for line in reader:
             x={k: line[k] for k in head_match}
             x['match_num']=x['match_num']+'-'+x['tourney_id']
             writer.writerow(x)