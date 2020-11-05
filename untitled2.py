#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:24:03 2020

@author: joedattoli
"""

import pybaseball as pb
import pandas as pd
import sklearn.linear_model as sklm
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

sexy_coprimes = pd.read_csv(r"/Users/joedattoli/Documents/GitHub/MessAroundRepo/salarydata", index_col = 'Unnamed: 0')


first_year = sexy_coprimes.loc[sexy_coprimes['year'] == 1]

second_year = sexy_coprimes.loc[sexy_coprimes['year'] == 2]


third_year = sexy_coprimes.loc[sexy_coprimes['year'] == 3]
x = third_year['trail_career_war']
y = third_year['salary']
x3 = third_year['trail_career_war'].values.reshape(-1,1)
y3 = third_year['salary'].values.reshape(-1,1)


third_reg = sklm.LinearRegression().fit(x3,y3)
third_coef_ = third_reg.coef_
third_intercept_ = third_reg.intercept_
line_x = np.linspace(max(x),max(y), num=100)

line_y = third_coef_ * line_x + third_intercept_


sb.scatterplot(x=x, y=y)
plt.plot(line_x,line_y)
plt.show()

fourth_year = sexy_coprimes.loc[sexy_coprimes['year'] == 4]
x = fourth_year['trail_career_war']
y = fourth_year['salary']
x4 = fourth_year['trail_career_war'].values.reshape(-1,1)
y4 = fourth_year['salary'].values.reshape(-1,1)

fourth_reg = sklm.LinearRegression().fit(x4,y4)
fourth_coef_ = fourth_reg.coef_
fourth_intercept_ = fourth_reg.intercept_

line_x = np.reshape(line_x,(1,100))
line_y = fourth_coef_ * line_x + fourth_intercept_

sb.scatterplot(x=x, y=y)
plt.plot(line_x,line_y)
plt.show()

fifth_year = sexy_coprimes.loc[sexy_coprimes['year'] == 5]
x = fifth_year['trail_career_war']
y = fifth_year['salary']
x5 = fifth_year['trail_career_war'].values.reshape(-1,1)
y5 = fifth_year['salary'].values.reshape(-1,1)

fifth_reg = sklm.LinearRegression().fit(x5,y5)
fifth_coef_ = fifth_reg.coef_
fifth_intercept_ = fifth_reg.intercept_


line_y = fifth_coef_ * line_x + fifth_intercept_

sb.scatterplot(x=x, y=y)
plt.plot(line_x,line_y)
plt.show()