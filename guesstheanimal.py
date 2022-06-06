#Riya Kommineni 
#Guessing a word in a list 

#pseudocode
# create list, print introduction, put random selection, guess the animal, if guess then:, else then:


import os 
os.system ('clear')

list1 = ['penguin', 'giraffe', 'elephant', 'koala', 'bear', 'flamingo', 'seal', 'panda', 'peacock', 'cow'] #from which the animals are chosen
print('In this game, you will be trying to guess an animal!') #this is the introduction


import random   #this is needed for the random loop
random.choice(list1)  #random loop is now for list1


guess=input('enter an animal name: ') #for player to guess an animal from list

if guess in random.choice(list1) : 
    print('Congratulations you guessed the animal!')
else: 
    print('Sorry you did not guess the animal :(') 
   
#some concerns i have 
#should i print the whole list for the player to know what is available to guess?
#i couldn't figure out the while loop. it would've been useful
#need to figure out how to give option to continue guessing if they lost or to start a new round if they guess correctly (while loop probably)
#this needs to somehow upload to github ugh!