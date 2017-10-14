'''
3. In last week’s lab we wrote a program which generated a number between 0 and 100, and 
asked the user (i.e. player) to guess, while given feedback “too high”, “too low” and 
“correct”. We are going to now let the computer play itself with 3 different ways. 
a. Firstly, random guessing and ignoring the feedback (just by generating a random 
number in the range 0-100). 
b. Secondly, by bisecting the known range (picking a number midway between the 
lowest and highest numbers it could be based on previous guesses). 
c. Thirdly, by enumeration (guessing 1, 2, 3 until it guesses correctly). 
In each case what do you think the average number of guesses is (just run your program a 
few times to get an idea – I am not expecting a mathematical analysis). Can you think of any 
other strategies what might work? 
@author: campbell
'''
import random

# set initial number

ComputerPick = random.randrange(0, 101, 1) 

# method a 
a = 0 # number of guesses
ComputerRight = False
while ComputerRight == False:
    ComputerGuess = random.randrange(0, 101, 1) 
    a += 1
    if ComputerGuess == ComputerPick:
        ComputerRight = True
print(a)

# method b
b = 0 # number of guesses
ComputerRight = False
Low = 0
High = 100

ComputerRight = False
while ComputerRight == False:
    ComputerGuess = (Low + High)/ 2
    b +=1
    if ComputerGuess < ComputerPick:
        Low = ComputerGuess
    elif ComputerGuess > ComputerPick:
        High = ComputerGuess  
    if ComputerGuess == ComputerPick:
        ComputerRight = True
print(b)


# method c 
c = 0 # number of guesses
ComputerRight = False
ComputerGuess = 0
while ComputerRight == False:
    if ComputerGuess == ComputerPick:
        ComputerRight = True
    else:
        ComputerGuess +=1
print(ComputerGuess)

