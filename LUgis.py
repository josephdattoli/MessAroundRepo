# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:52:26 2020

@author: joedattoli
"""
import pybaseball as pb
import pandas as pd



full_stats_19 = pb.pitching_stats(2019, qual = 10) 
full_stats_20 = pb.pitching_stats(2020, qual = 10) 

## Select only certain players: Relievers, defined as 30 IP in relief for 2019 and 15P for 2020 Going off of the GOAT of lefty specialists Randy Choate's usuall IP 

selected_19 = full_stats_19.loc[(full_stats_19['Relief-IP'] >=30) & ((full_stats_19['Relief-IP']>=full_stats_19['Start-IP']) | (pd.isnull(full_stats_19['Start-IP'])))]
selected_20 = full_stats_20.loc[(full_stats_20['Relief-IP'] >=15) & ((full_stats_20['Relief-IP']>=full_stats_20['Start-IP']) | (pd.isnull(full_stats_20['Start-IP'])))]

final_names = selected_20['Name']

selected_edited_19 = selected_19.loc[selected_19['Name'].isin(final_names)]

interested_names = []
 
for i in range(len(selected_edited_19['Name'].index)):
    row_19 = selected_edited_19.iloc[[i]].reset_index(drop = True)
    name =str(row_19.iloc[0]['Name'])
    row_20 = selected_20.loc[selected_20['Name'] == name].reset_index(drop = True)
    if(( row_20.iloc[0]['WPA'] * 2.7) > (row_19.iloc[0]['WPA'] )):
        interested_names.append(name)