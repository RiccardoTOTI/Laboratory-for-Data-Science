#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIn questo script viene creata la tabella Player
"""


import csv
import math
import ast

def read_csv(file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        return csv_rows

#è necessario utilzzare come chiave per la ricerca sia il nome che l'id perchè singolarmente nessuno dei due è unico
infile = '/home/maryxsempre/Downloads/data2021/tennis.csv'
lista=read_csv(infile)
ide=set()
print(len(lista))
newplay=dict()
#i=-1
for elem in lista:
    if ((elem['winner_id'],elem['winner_name']) not in ide) and ((elem['loser_id'],elem['loser_name']) not in ide):
        #i+=1
        ide.add((elem['winner_id'],elem['winner_name']))
        newplay[(elem['winner_id'],elem['winner_name'])]=[elem['winner_name'],elem['winner_hand'],elem['winner_ht'],elem['winner_ioc'],int(elem['tourney_date'][:4])]
        try:
            newplay[(elem['winner_id'],elem['winner_name'])].append(math.floor(ast.literal_eval(elem['winner_age'])))
        except:
            newplay[(elem['winner_id'],elem['winner_name'])].append('')
        #i+=1
        ide.add((elem['loser_id'],elem['loser_name']))
        newplay[(elem['loser_id'],elem['loser_name'])]=[elem['loser_name'],elem['loser_hand'],elem['loser_ht'],elem['loser_ioc'],int(elem['tourney_date'][:4])]
        try:
            newplay[(elem['loser_id'],elem['loser_name'])].append(math.floor(ast.literal_eval(elem['loser_age'])))
        except:
            newplay[(elem['loser_id'],elem['loser_name'])].append('')
    elif (elem['loser_id'],elem['loser_name']) not in ide:
        #i+=1
        ide.add((elem['loser_id'],elem['loser_name']))
        newplay[(elem['loser_id'],elem['loser_name'])]=[elem['loser_name'],elem['loser_hand'],elem['loser_ht'],elem['loser_ioc'],int(elem['tourney_date'][:4])]
        try:
            newplay[(elem['loser_id'],elem['loser_name'])].append(math.floor(ast.literal_eval(elem['loser_age'])))
        except:
            newplay[(elem['loser_id'],elem['loser_name'])].append('')
    elif (elem['winner_id'],elem['winner_name']) not in ide:
        #i+=1
        ide.add((elem['winner_id'],elem['winner_name']))
        newplay[(elem['winner_id'],elem['winner_name'])]=[elem['winner_name'],elem['winner_hand'],elem['winner_ht'],elem['winner_ioc'],int(elem['tourney_date'][:4])]
        try:
            newplay[(elem['winner_id'],elem['winner_name'])].append(math.floor(ast.literal_eval(elem['winner_age'])))
        except:
            newplay[(elem['winner_id'],elem['winner_name'])].append('')
print(len(ide),len(newplay))


#utilizziamo i due file male_players e female_players per assegnare il sex, inoltre notiamo che manca la corrispondenza per 30 tennisti che imputiamo a mano
with open('/home/maryxsempre/Downloads/data2021/male_players.csv',newline='') as malecsv:
    male=set()
    reader_m= csv.DictReader(malecsv)
    for row in reader_m:
         if row['name']+' '+row['surname'] not in male:
             male.add(row['name']+' '+row['surname'])
    #print(len(male),male)                

with open('/home/maryxsempre/Downloads/data2021/female_players.csv',newline='') as femalecsv:
    female=set()
    reader_f= csv.DictReader(femalecsv)
    for row in reader_f:
         if row['name']+' '+row['surname'] not in female:
             female.add(row['name']+' '+row['surname'])
    #print(len(female),female)
for key in newplay:
    if newplay[key][0] in male:
        newplay[key].append('M')
    elif newplay[key][0] in female:
        newplay[key].append('F')
    elif newplay[key][0] in ['Alona Fomina','Zeynep  Sena Sarioglan']:
        newplay[key].append('F')
    else:
        newplay[key].append('M')

players=[]        
for key,item in newplay.items():
    player=dict()
    player['player_id']=key[0]
    player['country_ioc']=item[3]
    player['name']=item[0]
    player['sex']=item[-1]
    player['ht']=item[2]
    player['hand']=item[1]
    try:
        player['year_of_birth']=item[4]-item[5]
    except:
        player['year_of_birth']=''
    players.append(player)
    
#print(players) 

play_head=['player_id','country_ioc','name','sex','ht','hand','year_of_birth']
    
with open('player.csv', 'w', newline='') as play:
    writer = csv.DictWriter(play, fieldnames=play_head)
    writer.writeheader()
    writer.writerows(players)