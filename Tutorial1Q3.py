'''
Created on 25 Sep 2017

@author: campbell
Write code to simulate The Birthday Problem
(http://en.wikipedia.org/wiki/Birthday_problem). Think about what numbers you need to
generate, and how you will store them (dictionary, tuple, or list).
list will be used to store results with n-1 = index of list.
Assumed to display probabilty for n=1 to 366
'''
from math import pow

results = []

for number in range(1,366):
    if number == 1:
        term = (1.0 / 365.0) * 365.0
    else:
        term = term * (1.0 / 365.0) * (365.0 - float(number - 1.0))
    prob = 1.0 - term       
    print(number,"{:.2%}".format(prob))
#    secondTerm = secondTerm * (365.0 - float(number)) 