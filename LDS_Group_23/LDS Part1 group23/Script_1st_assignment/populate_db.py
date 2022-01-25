import pyodbc 
import csv

##########################
# Connection to database #
##########################

server = 'lds.di.unipi.it' 
database = 'Group_23_DB' 
username = 'Group_23' 
password = 'HLRPFQ70'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

##################
# Inserting data # 
##################
"""

with open('match.csv') as csvfile:
    sql ="INSERT INTO Match(tourney_id,match_id,winner_id,loser_id,score,best_of,round,minutes,w_ace,w_df,w_svpt,w_1stIn,w_1stWon,w_2ndWon,w_SvGms,w_bpSaved,w_bpFaced,l_ace,l_df,l_svpt,l_1stIn,l_1stWon,l_2ndWon,l_SvGms,l_bpSaved,l_bpFaced,winner_rank,winner_rank_points,loser_rank,loser_rank_points) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute(sql, (row['tourney_id'], row['match_num'], row['winner_id'], row['loser_id'], row['score'], row['best_of'], row['round'], row['minutes'], row['w_ace'], row['w_df'], row['w_svpt'], row['w_1stIn'], row['w_1stWon'], row['w_2ndWon'], row['w_SvGms'], row['w_bpSaved'], row['w_bpFaced'], row['l_ace'], row['l_df'], row['l_svpt'], row['l_1stIn'], row['l_1stWon'], row['l_2ndWon'], row['l_SvGms'], row['l_bpSaved'], row['l_bpFaced'], row['winner_rank'], row['winner_rank_points'], row['loser_rank'], row['loser_rank_points']))


with open('tourney.csv') as csvfile:
    sql ="INSERT INTO Tournament(tourney_id, date_id, tourney_name, surface, draw_size, tourney_level, tourney_spectators, tourney_revenue) VALUES(?,?,?,?,?,?,?,?)"
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute(sql, (row['tourney_id'],row['tourney_date'], row['tourney_name'], row['surface'], row['draw_size'],	row['tourney_level'], row['tourney_spectators'], row['tourney_revenue']))
with open('DataCreated\date.csv') as csvfile:
    sql ="INSERT INTO Date(date_id, year, month, day, quarter) VALUES(?,?,?,?,?)"
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute(sql, (row['date_id'], row['year'], row['month'], row['day'], row['quarter']))

"""
#per la tabaella Match abbiamo splittato il csv iniziale in 11 parti da caricare singolarmente. Poichè era necessario tanto tempo per il loading e poi ogni errore portava a dover ricominciare da capo. 
with open('match\match_pro-11.csv') as csvfile:
    sql ="INSERT INTO Match(tourney_id,match_id,winner_id,loser_id,score,best_of,round,minutes,w_ace,w_df,w_svpt,w_1stIn,w_1stWon,w_2ndWon,w_SvGms,w_bpSaved,w_bpFaced,l_ace,l_df,l_svpt,l_1stIn,l_1stWon,l_2ndWon,l_SvGms,l_bpSaved,l_bpFaced,winner_rank,winner_rank_points,loser_rank,loser_rank_points) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute(sql, (row['tourney_id'], row['match_num'], row['winner_id'], row['loser_id'], row['score'], row['best_of'], row['round'], row['minutes'], row['w_ace'], row['w_df'], row['w_svpt'], row['w_1stIn'], row['w_1stWon'], row['w_2ndWon'], row['w_SvGms'], row['w_bpSaved'], row['w_bpFaced'], row['l_ace'], row['l_df'], row['l_svpt'], row['l_1stIn'], row['l_1stWon'], row['l_2ndWon'], row['l_SvGms'], row['l_bpSaved'], row['l_bpFaced'], row['winner_rank'], row['winner_rank_points'], row['loser_rank'], row['loser_rank_points']))
"""
with open('DataCreated\play_pro.csv') as csvfile:
    sql ="INSERT INTO Player(player_id, country_ioc, name, sex, hand, ht, year_of_birth) VALUES(?,?,?,?,?,?,?)"
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute(sql, (row['player_id'], row['country_ioc'], row['name'], row['sex'], row['hand'], row['ht'], row['year_of_birth']))

with open('geo.csv') as csvfile:
    sql ="INSERT INTO Geography(country_ioc, continent, language) VALUES(?,?,?)"
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute(sql, (row['country_ioc'], row['continent'], row['languages']))
"""
cnxn.commit()
cursor.close()
