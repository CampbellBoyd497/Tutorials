'''
Created on 1 Oct 2017
2. Imagine a string which contains a mathematical expression with brackets. For example 
“(1+2*(3+4))”. Clearly the brackets must balance. For now ignore all the symbols other than 
“(” and “)”. For example “(())” and “()()” are balanced but “)()(“ and “)))” are not. 
@author: campbell
'''

TestStr = ")(1+2*(3+4)"
Left = 0
Right = 0
Balanced = True
for i in TestStr:
    if i == "(":
        Left +=1
    elif i == ")": 
        Right +=1
    if Right > Left:
        Balanced = False
    
if Balanced == False or (Left != Right):
    print("TestStr is not balanced")
else:    
    print("TestStr is balanced")