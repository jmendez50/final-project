#Juan M Mendez
#Wheel of Fortune Final Project.

import random
import os

name = ''
print("What's your name?")
name = input()
#This part is just for show to make the game look like something
print('Welcome contestent ' + name, 'to Wheel of Fortune!')
print("        @@@@#@@@@")
print("     @@@    |    @@@")
print("    @       |       @")
print("   @ \  700 | 600  / @")
print("  @    \    |    /    @")
print(" @ 400   \ #|# /   100 @")
print("# ---------|+|--------- #")
print(" @ 800   / #|# \   200 @")
print("  @    /    |    \    @")
print("   @ /  500 | 300  \ @")
print("    @       |       @")
print("     @@@    |    @@@")
print("        @@@@#@@@@")

print('Alright lets get started!')

words = open ('words.py').read().splitlines()
word = random.choice(words)
#print(word) #remove the # before print to see the random word.
spin = ['100','200','300','400','500','600','700','800','Bust']
cash = random.choice(spin)
used = []

while True:
    guess = input()
    guess = guess.lower()
    print('Ok '+ name, 'guess a letter. a-z')
    if len(guess) != 1:
        print('Pick one letter at a time.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Letters only please.')
    elif guess in used:
        print('You already used that.')
    else:
        print('You guessed '+ guess)

if guess in word:
    print('Good'+ guess, ' that was in the word.')
if guess not in word:
    print('Sorry'+ guess,'is not in the word.')
