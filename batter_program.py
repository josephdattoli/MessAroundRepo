#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 04:23:56 2020

@author: joedattoli
"""

import pybaseball as pb
import pandas as pd



batting_stats = pd.read_csv('/Users/joedattoli/Desktop/CSVFILES/batter_salaries.csv')

statsC  = pb.batting_stats(2019,2019,position = 'C',  qual = 60)
stats1B = pb.batting_stats(2019,2019,position = '1B', qual = 100)
stats2B = pb.batting_stats(2019,2019,position = '2B', qual = 100)
statsSS = pb.batting_stats(2019,2019,position = 'SS', qual = 100)
stats3B = pb.batting_stats(2019,2019,position = '3B', qual = 100)
statsLF = pb.batting_stats(2019,2019,position = 'LF', qual = 100)
statsCF = pb.batting_stats(2019,2019,position = 'CF', qual = 100)
statsRF = pb.batting_stats(2019,2019,position = 'RF', qual = 100)
statsDH = pb.batting_stats(2019,2019,position = 'DH', qual = 100)

stats = statsC.copy()
stats = stats.append([stats1B,stats2B,statsSS,stats3B,statsLF,statsCF,statsRF,statsDH], ignore_index = True)
stats = stats.drop_duplicates().reset_index(drop = True)
stats_names = stats["Name"].unique().tolist()
stats_names = [str(i) for i in stats_names]


stats['C']  = [1 if stats['Name'][i] in statsC.Name.values  else 0 for i in range(len(stats.index)) ]
stats['B1'] = [1 if stats['Name'][i] in stats1B.Name.values else 0 for i in range(len(stats.index)) ]
stats['B2'] = [1 if stats['Name'][i] in stats2B.Name.values else 0 for i in range(len(stats.index)) ]
stats['SS'] = [1 if stats['Name'][i] in statsSS.Name.values else 0 for i in range(len(stats.index)) ]
stats['B3'] = [1 if stats['Name'][i] in stats3B.Name.values else 0 for i in range(len(stats.index)) ]
stats['LF'] = [1 if stats['Name'][i] in statsLF.Name.values else 0 for i in range(len(stats.index)) ]
stats['CF'] = [1 if stats['Name'][i] in statsCF.Name.values else 0 for i in range(len(stats.index)) ]
stats['RF'] = [1 if stats['Name'][i] in statsRF.Name.values else 0 for i in range(len(stats.index)) ]
stats['DH'] = [1 if stats['Name'][i] in statsDH.Name.values else 0 for i in range(len(stats.index)) ]

stats1 = stats[['IDfg','Name','C','B1','B2','SS','B3','LF','CF','RF','DH']]

full_frame = pd.merge(left=stats1,right=batting_stats,how = 'outer', left_on = 'IDfg' , right_on = 'key_fgid')
full_frame = full_frame.dropna().reset_index(drop = True)

full_frame.to_csv('/Users/joedattoli/Desktop/CSVFILES/full_batter_frame.csv', index = False)

