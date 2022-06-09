#Riya Kommineni 
#Guess the Number 
#File Project 
#pseudocode in journal


import os 
import random 
import code 
import datetime
from ctypes.wintypes import WORD 


os.system ('clear')
 
Game = True 
theNum = ''
#Menu



 
 
print('|GUESS THE NUMBER!')
print('|1. Instructions')
print('|2. Level 1: 1-25')
print('|3. Level 2: 1-50')
print('|4. Level 3: 1-100')
print('|5. Print score')
print('|6. Exit')

name=input('What is your name? ')
print(name, end=', ')
answer=input("Would you like to play? ")
 

choice=input('What number would you like to go to?')
try: 
        choice=int(choice)
        if choice > 6: 
         print('select something from the selection above:')
except: 
         print('sorry')


if choice == 1:
    with open ('instructions.txt', 'r') as f: #instructions tab
     f_contents = f.read()
     print(f_contents)
    

def selectNum(choice):
    global level 




if (choice == 2):
     theNum = 'random.randint(1,25)'
     level = 25
     ifNotGuessed = True 
     count = 0
     while ifNotGuessed == True and count < 5: 
        guess = input('Guess a number from 1 to 25:')
        
        if guess in theNum: 
           print('Congratulations, you guessed the number!')
           ifNotGuessed = False 
        else:
             print('Sorry that is incorrect; please try again:')
             
        count = count + 1



if (choice == 3):
     theNum = 'random.randint(1,50)'
     level = 50
     ifNotGuessed = True 
     count = 0
     while ifNotGuessed == True and count < 5: 
        guess2 = input('Guess a number from 1 to 50:')
        
        if guess2 in theNum: 
           print('Congratulations, you guessed the number!')
           ifNotGuessed = False 
        else:
             print('Sorry that is incorrect; please try again:')
             
        count = count + 1


if (choice == 4):
     theNum = 'random.randint(1,100)'
     level = 100
     ifNotGuessed = True 
     count = 0
     while ifNotGuessed == True and count < 5: 
        guess3 = input('Guess a number from 1 to 100:')
        
        if guess3 in theNum: 
           print('Congratulations, you guessed the number!')
           ifNotGuessed = False 
        else:
             print('Sorry that is incorrect; please try again:')
             
        count = count + 1

if choice == 5:
 date=datetime.datetime.now()
 print(date)
 print(date.strftime("%m-%d-%Y"))

name="Riya"
sce=320
scrLine=str(sce)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
myFile = open("scre.txt", 'w')
myFile.write(scrLine)
myFile.close()
name="Daisy"
sce=319
scrLine=str(sce)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
myFile = open("scre.txt", 'a')
myFile.write(scrLine)
myFile.close()
myFile = open("scre.txt", 'r')
stuff=myFile.readlines()
stuff.sort(reverse=True)
myFile.close()
for line in stuff:
    print(line)


if choice == 6: 
    print('----------------')
answer=input('Do you want to play again?')
answer=answer.lower()
if 'n' in answer:
    Game = False
    print('Thank you for playing, please come again!')
else: 
    Game = True 
