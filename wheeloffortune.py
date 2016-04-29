#Juan M Mendez
#Wheel of Fortune Final Project.

import random
import os

name = ''
words = open ('words.py').read().splitlines()
word = random.choice(words)
spin = ['100','200','300','400','500','600','700','800','Bust']
cash = random.choice(spin)
right = ' '
wrong = ' '
done = False
#print(word) #remove the # before print to see the random word.
print("What's your name?")
name = input()
print('Welcome contestent ' + name, 'to Wheel of Fortune!')
print("        @@@@#@@@@")
print("     @@@    |    @@@")
print("    @       |       @")
print("   @ \  700 | 600  / @")
print("  @    \    |    /    @")
print("# ---------|+|--------- #")
print(" @ 800   / #|# \   200 @")
print("  @    /    |    \    @")
print("   @ /  500 | 300  \ @")
print("    @       |       @")
print("     @@@    |    @@@")
print("        @@@@#@@@@")
def game(wrong, right, word):
    print('You have used: ', end = ' ')
    for letter in wrong:
        print(letter, end = ' ')
    print()
    blank = '#' * len(word)    
    for let in range(len(word)):
        if word[let] == ' ':
            blank = blank[let] + word[let] + blank[let+1:]
        if word[let] in right:
            blank = blank[let] + word[let] + blank[let+1:]
    for letter in blank:
        print(letter, end = '')
    print()
def play(used):
    while True:
        print('Your word is:')
        print('Cash is:')
        print('Ok '+ name, 'guess a letter. a-z')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Pick one letter at a time.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Letters only please.')
        elif guess in used:
            print('You already used that.')
        else:
            return guess
while True:
    game(wrong, right, word)
    guess = play(wrong + right)
    if guess in word:
        right = right + guess
        print("That's Right! Good one!")
        finished = True
        for x in range(len(word)):
            if word[x] not in right:
                finished = False
                break
        if finished:
            print('You on your way to winning the brand prize ' + name, 'You won $'+ cash,)
            done = True
    else:
         wrong = wrong + guess
         print('Beep Beep Beep. Im sorry thats not right', cash)
         print()
    if done:
        if start():
            wrong = ''
            right = ''
            done = False
        else:
            break
