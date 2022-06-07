#Riya Kommineni 
#guess the word in a list (but with 3 different lists this time!)

from ctypes.wintypes import WORD
import os
import random 


os.system ('clear')
from time import sleep 




list1 = ['penguin', 'giraffe', 'elephant', 'koala', 'bear', 'flamingo', 'seal', 'panda', 'peacock', 'cow']
count=0
Game=True
theWord= ''



def hint():
    global count 
    if count == 0:
        print('hint: these could be considered unconventional animals')

guess= input('enter an animal name to guess:')
if guess in theWord: 
    print('Congratulations you guessed the animal!')
else: 
    print('Sorry that is incorrect; please try again:')

if (count) == 1: 
    print('hint: these are my favorite animals')
else:
    print('keep going')

while Game: 
    print('In this game, you can try to guess something from 3 different lists!')
    print('1. animals')
    print('2. flowers')
    print('3. world cities')

theWord=random.choice(list1)
name=input('What is your name? ')
print(name, end=', ')
answer=input("Would you like to play? ")
answer=answer.lower()
if 'n' in answer: 
    Game=False 
    break
    

while True: 
    choice=input('Would you like to play game 1,2, or 3?')
    try: 
        choice=int(choice)
        if choice>0 and choice<4: 
            break
        else: 
            print('select 1,2,or 3')
    except: 
        print('sorry')

os.system('clear')

check=True 
while check and count <5: 
    guess=input('enter your guess here:')
    print()
    if guess == theWord: 
        print('Congrats you got the word!')
        check=False
    else: 
            hint()
    count+=1
os.system('clear')
print('----------------')
answer=input('Do you want to play again?')
if 'n' or 'N' in answer:
    Game=False
    print('Thank you for playing, please come again!')
