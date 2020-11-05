
"""
Created on Thu Oct 29 09:37:02 2020

@author: joedattoli
"""

import pybaseball as pb
import pandas as pd

def get_full_frame(bwar):
    player_id = list(bwar['player_ID'].unique())

    listoframes = []
    for player in player_id:
        player_frame = bwar.loc[bwar['player_ID'] == player]
        name = list(player_frame['name_common'].unique())[0]
        years = list(player_frame['year_ID'].unique())
        war_list =[0]
        if (len(years)>=6):
            for year in years[:7]:
                year_frame = player_frame.loc[player_frame['year_ID']==year]
                games_sum = sum(year_frame['G'].values)
                war_sum = sum(year_frame['WAR'].values)
                war_list_sum = (war_list[-1] + war_sum)
                war_list.append(war_list_sum)
                salary = list(year_frame['salary'].loc[pd.notnull(year_frame['salary'])])
                row = pd.DataFrame({'name_common': name,'player_ID':player,'year_ID':year,
                                    'G': games_sum,'salary':salary,'WAR':war_list[-2]})
                listoframes.append(row)
        else:
            continue
    bwar_maybe = pd.concat(listoframes, ignore_index = True)
    return bwar_maybe


def differences(frame):
    player_id =  list(frame['player_ID'].unique())
    list_frame = []
    for player in player_id:
        player_frame = frame.loc[frame['player_ID'] == player]
        name = list(player_frame['name_common'].unique())[0]
        years = list(player_frame['year_ID'].unique())
        years.sort()
        will_cont = True
        for i in range(1,len(years)):
            year_i = player_frame.loc[player_frame['year_ID'] == years[i]]
            year_i_min1 = player_frame.loc[player_frame['year_ID'] == years[i-1]]
            g = sum(year_i_min1['G'].values)
            if ((g >= 80) & (will_cont != False) ):
                war = sum(year_i_min1['WAR'].values)
                salary = sum(year_i['salary'].values)
                temp = pd.DataFrame({'name_common': name, 'year': i , 'trail_career_war' : war , 'salary': salary}, index = [0] )
                list_frame.append(temp)
            else:
                will_cont = False
                continue
            
    daemon = pd.concat(list_frame,ignore_index = True)
    return daemon
    
bwar_bat = pb.bwar_bat()
bwar_pitch = pb.bwar_pitch()
players = pb.people()
players_current = players.loc[players['debut']> '2000-01-01']
current_players_list = list(players_current['playerID'])


#pitching_stats = pybaseball.pitching_stats(2012,2020)
#batting_stats = pybaseball.batting_stats(2012,2020)

#pitching_stats.to_csv(r"/Users/joedattoli/Documents/GitHub/MessAroundRepo/pitching_stats_12_20")
#batting_stats.to_csv(r"/Users/joedattoli/Documents/GitHub/MessAroundRepo/batting_stats_12_20")



bwar_bat_need = bwar_bat[['name_common','player_ID','year_ID','pitcher','G','salary','WAR']]
bwar_bat_need = bwar_bat_need.loc[bwar_bat_need['pitcher'] == "N"]
bwar_bat_need = bwar_bat_need[['name_common','player_ID','year_ID','G','salary','WAR']]
bwar_pitch_need = bwar_pitch[['name_common','player_ID','year_ID','G','salary','WAR']]
bwar_all = pd.DataFrame(columns = ['name_common','player_ID','year_ID','G','salary','WAR'])
bwar_all = pd.concat([bwar_bat_need,bwar_pitch_need], ignore_index=True)
bwar_all = bwar_all.loc[bwar_all["year_ID"] >=2000 ]
bwar_all = bwar_all.loc[bwar_all['player_ID'].isin(current_players_list)]

sexy_primes = get_full_frame(bwar_all)
sexy_coprimes = differences(sexy_primes)
sexy_coprimes.to_csv(r"/Users/joedattoli/Documents/GitHub/MessAroundRepo/salarydata")