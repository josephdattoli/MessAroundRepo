#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 03:07:55 2020

@author: joedattoli
"""
import pandas as pd
from scipy.optimize import linprog


#Read in the data pulled from pybaseball
stats = pd.read_csv(r'pwar_08_19.csv')

#For this we only need 2019 data. Also throwing out any rows that contain null values.
stats = stats.loc[stats['year_ID'] == 2019].dropna().reset_index(drop = True)

#Define starters and create aditional column
starters = stats.loc[stats['GS'] >= 15]
stats['starter'] = [True if stats['player_ID'][k] in starters.player_ID.values else False for k in range(len(stats.index))]

#rework dataframe and take only whats needed
stats = stats[['name_common','player_ID','salary','WAR','starter']]

#these are the coefficients of the constraints
roster_size = [-1 for i in range(len(stats.index))]
starter_bool = [0 if stats['starter'][i] == False else 1 for i in range(len(stats.index))]
reliever_bool = [1 if stats['starter'][i] == False else 0 for i in range(len(stats.index))]
salary_list = stats.salary.values

#coefficients of the objective function
war = stats.WAR.values
war = [-1*val for val in war]

#constraint matrix
A = [starter_bool,
     reliever_bool,
     salary_list]

#opens a text file to record the result of each budget
writer = open('pitcher_result_file.txt', 'a')


total_sal=[]
total_war=[]
calc_sal=[]
calc_war=[]
# loops through and runs the programming at multiple budgets
for  i in range(1,20):
    
    ##heading for current budget
    header_string = "\nThe results of the optimization for budget of $" + str(5*i) + " million: \n" 
    writer.write(header_string)
    
    #the inequality vector
    b = [5,8,5000000*i]
    
    #the magic happens here
    result = linprog(war,A,b, bounds = [(0,1) for i in range(len(stats.index))], method = 'revised simplex')
    x = result.x
    
    
    #these lists facilitate the formating of the text file
    starters = []
    starters_str = []
    Swar = []
    Ssal = []
    Rwar = []
    Rsal = []
    relievers = []
    relievers_str =[]
    choosers = []
    choosers_str = []
    Cwar = []
    Csal = []
    proportion_sal = []
    
    ## reads the results and throws the selected into lists
    for k in range(len(x)):
        if x[k] ==1:
           starters.append(stats['name_common'][k]) if stats['starter'][k] == True else relievers.append( stats['name_common'][k])
           Swar.append(stats['WAR'][k]) if stats['starter'][k] == True else Rwar.append( stats['WAR'][k])
           Ssal.append(stats['salary'][k]) if stats['starter'][k] == True else Rsal.append( stats['salary'][k])
        elif (x[k] > 0 and x[k] < 1):
            proportion_sal.append( x[k] * stats['salary'][k])
            choosers.append(stats['name_common'][k])
            Cwar.append(stats['WAR'][k])
            Csal.append(stats['salary'][k])
    calc_war.append(round(result.fun*-1,1))
    calc_sal.append(round(sum(Ssal +Rsal +proportion_sal )/1000000 , 1))
    
    ## another heading       
    sub_head1 = "These are the optimal starters for this budget: \n"
    writer.write(sub_head1)        
    
    ##Everything below is the formatting for the text file
    for s in range(len(starters)):
        starter_str = "SP: " + str(starters[s]) + "   WAR: " + str(Swar[s]) + "   Salary: $" + str(round((Ssal[s]/1000000.0),1)) + "mil \n"
        writer.write(starter_str)
        starters_str.append(starter_str)
        
    sub_head2 = "\n These are the optimal Relievers for this budget: \n"
    writer.write(sub_head2)    
    
    for r in range(len(relievers)):
        reliever_str = "RP: " + str(relievers[r]) + "   WAR: " + str(Rwar[r]) + "   Salary: $" + str(round((Rsal[r]/1000000.0),1)) + "mil \n"
        writer.write(reliever_str)
        relievers_str.append(reliever_str)
        
        
    sub_head3 = "\n Please Choose from list below to complete: \n"
    writer.write(sub_head3)           
    

    for c in range(len(choosers)):
        chooser_str = "Flex: " + str(choosers[c]) + "   WAR: " + str(Cwar[c]) + "   Salary: $" + str(round((Csal[c]/1000000.0),1)) + "mil \n"
        writer.write(chooser_str)
        choosers_str.append(chooser_str)

    total_sal.append(round(sum(Ssal +Rsal)/1000000 , 1))
    total_war.append(round(sum(Swar+Rwar),1))
    final_string = '\n\nWithout Flex...  Total WAR: ' + str(round(sum(Swar+Rwar),1)) + "  Total Salary: $" + str(round(sum(Ssal +Rsal)/1000000 , 1)) + "mil \n"
    writer.write(final_string)
print(total_sal)
print(total_war)

print(calc_sal)
print(calc_war)