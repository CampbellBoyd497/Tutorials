'''
Created on 25 Sep 2017

@author: campbell

Write a program to ask the user for a number. If the input is not a number, inform the user
they made a mistake and did not enter a number and ask them again. When they have
entered a number, tell them if it is small (<10), medium (<20) or large (>20) and also if the
number is even or odd. Is this program specified completely?
'''
from reportlab.lib.validators import isNumber

Number = False
while not Number:
    Entered = input("Please enter a number:")
    if isNumber(Entered):
        Number = True

# Convert integer to float as spec silent
Entered = float(Entered)
        
if (Entered < 10.0):
    print("small")
    Size = "small"
elif Entered < 20.0:
    Size = "medium"
else:
    Size = "large"
    # Note: large assumed to be >= 20    

if Entered  % 2 == 0:
    OddOrEven = "even"
else: 
    OddOrEven = "odd"
    
print ("This number you entered is " + Size + " and is " + OddOrEven + ".")             
    
