'''
Created on 25 Sep 2017

@author: campbell
Here is a game. Player one thinks of a target number between 0 and 100, and player two
attempts to find the number with a series of guesses. Player one can make one of three
statements, depending on the relationship between the guesses number and the target
number, either, “too high”, “too low”, or “correct”. The program prints out the number of
attempts it took the user to find the target number.
ADDITION: target number required to be integer
'''
from types import *

def GetNumber(Low,High,InputMessage):
    Number = False
    while not Number:
        Entered = int(input(InputMessage))
        
        if isinstance(Entered,int):
            Number = True

        if Number and (Entered not in range(Low,High)):
            Number = False

    return Entered
        
PlayerOne = GetNumber(0,100,"Please enter a number between 0 and 100 inclusive:")

PlayerTwo = 101 # force while loop to execute at least once

guesses = 0
while PlayerOne != PlayerTwo:
    PlayerTwo = GetNumber(0,100,"Please enter your guess, between 0 and 100 inclusive:")
    guesses +=1
    if PlayerTwo < PlayerOne:
        print("\ntoo low\n")
    elif PlayerTwo > PlayerOne:
        print("\ntoo high\n") 
        
print("\ncorrect. You had " + str(guesses) + " guess(es).\n")
   
    