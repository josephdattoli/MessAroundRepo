# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 16:39:36 2020

@author: joedattoli
"""
from scipy.optimize import linprog

#### problem one 
#### find the all bases and output maximum


### defaults to minimize problems, therefore we need to switch signs on the coefficients to output a maximum 
z = [-3,-2]

A = [[1,1],
     [1,2]]
b = [[4,6]]


x1_bounds = (0,None)
x2_bounds = (0,None)

maximum = linprog(z,A,b,bounds=[x1_bounds,x2_bounds], method = 'revised simplex')

print('The results of problem one programming.')
print(maximum)
print('Notice that fun = -12 which is the the opposite of the maximum. Therefore, the maximum is 12 at x = [4,0, slack 1 = 0, slack 2 = 2] ')
print("The true maximum is " + str(-1*maximum.fun))
print()
print()









### problem 2
## Show that his has no finite solution
##once againg switched signs to reflict max vs min
z2 = [1,-2,1]

A2 = [[3,1,-4],
     [1,-1,-1],
     [1,-2,6]]

b2 = [4,10,9]



x1_bounds = (0,None)
x2_bounds = (0,None)
x3_bounds = (0,None)

result_2 = linprog(z2,A2,b2,bounds=[x1_bounds,x2_bounds,x3_bounds], method = 'revised simplex')

print('The results of problem two programming.')
print(result_2)
print('Notince that Success == False due to it being unbounded, thus indicating no finite solution ')
print()

### find a particular solution where z>1000
bound = (0,1000)

particular_result_2 = linprog(z2,A2,b2,bounds=[bound,bound,bound], method = 'revised simplex')

print('The results of problem two programming to find a particular solution.')
print(result_2)
print('Note success is now true with a fun of magnitude over 1000 (opposite of what max would be). The particular solution is shown at x ')
print("The true maximum is " + str(-1*particular_result_2.fun))
print()
print()



### problem 3
### solve this maximum problem
z2 = [-22,-35]

A2 = [[.5,.3],
     [.5,.8]]

b2 = [120,160]



x1_bounds = (0,None)
x2_bounds = (0,None)

result_3 = linprog(z2,A2,b2,bounds=[x1_bounds,x2_bounds], method = 'revised simplex')

print('The results of problem three programming.')
print(result_3)
print('Notice that the solution is ' + str(result_3.x))

