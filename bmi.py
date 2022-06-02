#Riya Kommineni
#Calculate BMI 

import os
os.system ('clear')

weight=float (input('your weight in pounds: ')) 
a=weight*703
height=float(input("your height in inches: "))
b=height*height
x=a/b
print (x) #BMI in terminal 

if (x<18.5):
    print("you are underweight")

if (x>25):
    print("you are overweight")

if (x > 18.6 and x < 24.9): 
    print ("you are at a healthy weight")