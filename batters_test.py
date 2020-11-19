#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 02:56:44 2020

@author: joedattoli
"""
import pybaseball as pb
import pandas as pd


batters = pb.bwar_bat()
batters = batters.loc[batters['year_ID'] == 2019].loc[batters['PA'] >= 50].loc[batters['pitcher'] == 'N']

batters = batters.fillna(0)
batters = batters[['name_common', 'mlb_ID', 'player_ID','stint_ID','salary','WAR']]
bnames = [str(i) for i in batters.name_common.unique()]
batters['key_fgid'] = [0 for i in range(len(batters.index))]
batters_summed = pd.DataFrame(columns = batters.columns)
for name in bnames:
    small_frame = batters.loc[batters['name_common'] == name].reset_index(drop=True)
    temp_dict = pd.DataFrame(columns = small_frame.columns)
    if len(small_frame['stint_ID']) > 1:
        batter_ids = pb.playerid_reverse_lookup([small_frame['player_ID'].values[0]], key_type='bbref')
        temp_dict['key_fgid'] = batter_ids.key_fangraphs.values[0]
        temp_dict['name_common'] = name
        temp_dict['mlb_ID'] = small_frame['mlb_ID'].values[0]
        temp_dict['player_ID'] = small_frame['player_ID'].values[0]
        if sum(small_frame['salary']) >= 100000:
            temp_dict['salary'] = sum(small_frame['salary'])
        elif sum(small_frame['WAR'])>=0:
            temp_dict['salary'] =  500000*sum(small_frame['WAR'])+555000
        else:
            temp_dict['salary'] = 555000
        temp_dict['WAR'] = sum(small_frame['WAR'])
        batters_summed = batters_summed.append(temp_dict, ignore_index = True)
    else:
        batter_ids = pb.playerid_reverse_lookup([small_frame['player_ID'].values[0]], key_type='bbref')
        small_frame.loc[0,'key_fgid'] = batter_ids.key_fangraphs.values[0]
        if sum(small_frame['salary']) == 0:
            if sum(small_frame['WAR']) >=0:
                small_frame.loc[0,'salary'] = 500000*sum(small_frame['WAR'])+555000
            else:
                small_frame.loc[0,'salary'] = 555000
        batters_summed = batters_summed.append(small_frame, ignore_index = True)
        
    
batters_summed.to_csv(r'/Users/joedattoli/Desktop/CSVFILES/batter_salaries.csv', index = False)

    

