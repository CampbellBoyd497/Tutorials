'''
Created on 1 Oct 2017
5. Hangman game (http://en.wikipedia.org/wiki/Hangman_(game)). Hard code a word for the 
user to guess (we will look at reading words from a file soon). The user (i.e. the player) is 
allowed to guess up to 10 letters in the unknown word. Correct guessed letters are displayed 
in their correct position in the word, and unknown letters are represented as “_”. For 
example “J_h_” means “J” and “h” have been guessed correctly, and the 2nd and 4th letters 
are still unknown. You do not need to do a graphical display of man at the gallows, but 
instead just tell the user how many guesses they have correct. You can also display a list of 
the letters that have already been used as guesses so far, so the user does not need to 
remember. (we may ask the computer to play next week). 
@author: campbell
'''
StringToGuess = "banana"

WordToGuess = []
WordSoFar = []
for i in StringToGuess:
    WordToGuess.append(i)
    WordSoFar.append('-')

   
Guesses  = 0 
Limit = 10
Guessed = False


print( "Try to guess the word, entering 1 letter at a time")
print( "You have 10 guesses. The word is " + str(len(WordToGuess)) + " letters long.")

while not Guessed and Guesses < Limit:
    Guess = input("Please enter your guess - one letter only!")
    Guess.lower
    Guesses +=1
    # check Guess type?
    if Guess in WordToGuess:
        for i in range(0,len(WordToGuess)):
            if WordToGuess[i] == Guess:
                WordSoFar[i] = Guess

    print("Your guess: "+ Guess + "  Hidden word so far: " + "".join(WordSoFar) + " Guesses left: " + str(Limit - Guesses))
    if WordToGuess == WordSoFar:
        Guessed = True
        print("Well done!")

if not Guessed:
    print("suck it, loser!")