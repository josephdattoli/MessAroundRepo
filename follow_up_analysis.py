# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:08:30 2020

@author: joedattoli
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

salaries = [3.7, 8.6, 11.6, 15.4, 20.1, 18.2, 30.5, 28.0, 43.8, 43.8, 43.8, 56.7, 56.7, 56.7, 56.7, 56.7, 84.7, 84.7, 84.7]
wars     = [23.8, 42.5, 42.5, 43.8, 45.5, 38.3, 43.3, 46.1, 51.5, 51.5, 51.5, 52.4, 52.4, 52.4, 52.4, 52.4, 59.8, 59.8, 59.8]
budget   = [str(5*i) for i in range(1,len(wars)+1)]

salaries_add = [0,1.4,0.6,0.6,4.3,(0.6 + 4.3 + 3.1),(0.6 + 0.6 ), (9.3 + 3.1), 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6,  0.6, 0,0,0]
wars_add     = [0,2.57,4.54,4.57,5.94,(4.84 +5.94 + 2.96), (5.71 + 4.84),(7.51 + 2.96), 5.71, 5.71, 5.71, 5.72, 5.72, 5.72, 5.72,5.72,0,0,0 ]

salaries_post = [salaries[i] + salaries_add[i] for i in range(len(salaries))]
wars_post     = [wars[i] + wars_add[i]  for i in range(len(wars))]

calc_salaries=[5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 84.7, 84.7, 84.7]
calc_wars=[35.6, 45.0, 48.1, 49.9, 51.6, 53.3, 54.9, 56.4, 57.2, 57.6, 57.9, 58.3, 58.6, 58.9, 59.2, 59.5, 59.8, 59.8, 59.8]

sns.lineplot(x=salaries , y = wars , label= "Computer")
sns.lineplot(x=salaries_post , y = wars_post , label= "After Choice")
sns.lineplot(x=calc_salaries , y = calc_wars , label= "Via Proportion")


plt.title(label = "Wars and Salaries based on Budgets Using LP")
plt.xlabel('Salary/Budget')
plt.ylabel('WAR')

plt.legend()
plt.show()

data = [salaries,
        salaries_add,
        salaries_post,
        wars,
        wars_add,
        wars_post]

df = pd.DataFrame({'BudgetLevel': budget, 'LP_Salaries': salaries, 'Sal_Chosen': salaries_add, 'Combined Salaries':salaries_post,
                   'LP_WAR': wars, 'War_Chosen': wars_add, 'Combined WAR': wars_post })
df1 = pd.DataFrame({'BudgetLevel': budget, 'LP_Salaries_1': salaries, 'Combined Salaries':salaries_post,'Full Salaries': calc_salaries,
                   'LP_WAR_1': wars, 'Combined WAR': wars_post, 'Full_War': calc_wars })
