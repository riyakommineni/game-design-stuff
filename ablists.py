#Riya Kommineni 
#learning about lists and functions related to lists
#also going to learn about forloop 

import os 
os.system ('clear')

list1 = ['apple', 'banana', 'cherry', 'mango', 'kiwi', 'orange']
#          0         1         2         3       4         5
#                              -4        -3      -2       -1
print(list1[1]) #print from a specific index
print(list1[-2]) #print from end
print(list1[1:4]) #print between two value; second one is not included in the set
print(list1[:6])  # prints up to a value; does not include #all of these elements can be used in strings
print(list1[5:]) #every after a value, including the value

if 'apple' in list1: #checking if something is in list
    print('yes apple is in the list')


for num in range (10): #creates a loop 9 times
    print(num)

print()

for element in list1: #element=list1(times it runs through the loop)
    print(element)


#add elements to a list
list1.append('pineapple')
print(list1[0:])

#for number in range (2)
list1.append(input('enter a food'))
print(list1[0:])

list1.insert(1, 'pineapple') #adding an element to a specific index insert (index, element you want to add)
print(list1[0:])


for i in range(len(list1)):
    print(list1[i], end = '/' )
print()

list2 = [1, 2, 3, 4, 5]
list2.extend(list1)
print(list2)

#random.choice picks random element on the list
#challenge is y loop
#WRITE PSEDUOCODE AT TOP!!

guess = input('guess a food: \t')
 
