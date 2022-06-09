#Riya Kommineni 
#guess the word in a list (but with 3 different lists this time!)

from ctypes.wintypes import WORD
import os
import random 
import code 


os.system ('clear')
from time import sleep 




list1 = ['penguin', 'giraffe', 'elephant', 'koala', 'bear', 'flamingo', 'seal', 'panda', 'peacock', 'cow']
list2 = ['lily', 'daisy', 'hydrangea', 'lotus', 'daffodil', 'tulip', 'peony', 'violet', 'orchid', 'sunflower']
list3 = ['New York City','Shanghai', 'Buenos Aires', 'Lagos', 'Mumbai', 'Tokyo', 'Seoul', 'Paris', 'Barcelona']
count = 0
Game = True
theWord = ''



def hint():
    global count 
    if count == 0:
        print('hint: these could be considered unconventional animals')

name=input('What is your name? ')
print(name, end=', ')
answer=input("Would you like to play? ")
answer=answer.lower()
if 'n' in answer: 
    Game=False


while Game == True: #Menu
    print('In this game, you can try to guess something from 3 different lists!')
    print('1. animals')
    print('2. flowers')
    print('3. world cities')


 
choice=input('Would you like to play game 1,2, or 3?')
try: 
        choice=int(choice)
        if choice > 1 and choice <= 3: 
         print('select 1,2,or 3')
except: 
         print('sorry')




if (choice == 1):
    theWord=random.choice(list1)
    ifNotGuessed = True 
    count = 0
    while ifNotGuessed == True and count < 5: 
        guess = input('enter an animal game to guess')

    if guess in theWord: 
        print('Congratulations, you guessed the animal!')
        ifNotGuessed = False 
    else:
                print('Sorry that is incorrect; please try again:')
                hint()
    count = count + 1
elif (choice == 2):
        theWord = random.choice(list2)
        ifNotGuessed = True
        count = 0
        while ifNotGuessed == True and count < 5:
            guess = input('enter an animal name to guess:')

            if guess in theWord: #they guessed the word
                print('Congratulations you guessed the animal!')
                ifNotGuessed = False
            else:
                print('Sorry that is incorrect; please try again:')
                hint()
            count = count + 1
elif (choice == 2):
        theWord = random.choice(list2)
        ifNotGuessed = True
        count = 0
        while ifNotGuessed == True and count < 5:
            guess = input('enter a flower name to guess:')

            if guess in theWord: #they guessed the word
                print('Congratulations you guessed the flower!')
                ifNotGuessed = False
            else:
                print('Sorry that is incorrect; please try again:')
                hint()
            count = count + 1 
else:
        theWord = random.choice(list3)
        ifNotGuessed = True
        count = 0
        while ifNotGuessed == True and count < 5:
            guess = input('enter an animal name to guess:')

            if guess in theWord: #they guessed the word
                print('Congratulations you guessed the animal!')
                ifNotGuessed = False
            else:
                print('Sorry that is incorrect; please try again:')
                hint()
            count = count + 1

print('----------------')
answer=input('Do you want to play again?')
answer=answer.lower()
if 'n' in answer:
    Game = False
    print('Thank you for playing, please come again!')
else: 
    Game = True 

    
        
