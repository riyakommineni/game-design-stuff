#Riya Kommineni
#Integers and Float Assignment 

from math import remainder
import os
os.system ('clear')

number=float (input('enter a number'))
x=number


num_1= (x % 2)
 

if (num_1 == 1): 
    print('odd')

if (num_1 == 0):
    print('even')

num_2= (x % 3)

if (num_2 != 0): 
    print('not a multiple of 3') 

if (num_2 == 0):
    print('multiple of 3')

num_3= (x % 5)

if (num_3 != 0):
    print('not a multiple of 5')

if (num_3 == 0):
    print('multiple of 5')