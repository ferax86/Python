# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:19:33 2021

@author: XRFRBL
"""

#####Set up the directory in which the script is located

import os
import pandas as pd 
cwd = os.getcwd()
print(cwd)
Test=pd.read_csv("Test.csv",sep=";" )


###Chapter 1 : Introduction to iterators
#I:
#an iterable is an object that can return an iterator, while an iterator 
#is an object that keeps state and produces the next value when you call next()
##Iterating with a for loop
#over a list
employees = ['Nick', 'Lore', 'Hugo']
for employee in employees:
    print(employee)
    
#over a list
for letter in 'DataCamp':
    print(letter)
    
#over a range object :
    #not all iterables are actual lists. 
    #A couple of examples that we looked at are strings and the use of the range() 
    #.Range() doesn't actually create the list; 
    #instead, it creates a range object with an iterator that produces the 
    #values until it reaches the limit 

for i in range(4): 
    print(i)
    
    
#Iterating over iterables: next()

word = 'Da'
it = iter(word)
next(it)
next(it)
next(it) #her eit stops as we arriveat the end of the iterable 


#Iterating at once with *

word = 'Data'
it = iter(word)
print(*it)
print(*it) # No more values to go through!


#Iterating over dictionaries

pythonistas = {'hugo': 'bowne-anderson', 'francis': 'castro'}
for key, value in pythonistas.items():
    print(key, value)


#Iterating over file connections
file=open(r"\\Wwg00m.rootdom.net\bfs-home\XRFRBL\Personal Doc\Python\0. Python Data Science Toolbox_Part2\file.txt.txt")
it = iter(file)
print(next(it))
print(next(it))


###Exercises
#1.
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print (person)


# Create an iterator for flash: superhero
superhero=iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))


#2.

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

#3.

# Create a range object: values
values = range(10,21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)


#II:Playing with iterators

# Using enumerate()-->returns an enumerate object that produces a sequence of tuples, 
                       #and each of the tuples is an index-value pair.
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers)
print(type(e))
e_list = list(e)
print(e_list)

#enumerate() and unpack
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
for index, value in enumerate(avengers):
    print(index, value)


for index, value in enumerate(avengers, start=10):
    print(index, value)


#Using zip()-->takes any number of iterables and returns a zip object that 
               #is an iterator of tuples. If you wanted to print the values of 
               #a zip object, you can convert it into a list and then print it. 
               #Printing just a zip object will not return the values unless 
               #you unpack it first
               
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']
z = zip(avengers, names)
print(type(z))
z_list = list(z)
print(z_list)

#zip() and unpack

avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']
for z1, z2 in zip(avengers, names):
    print(z1, z2)

#Print zip with *
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']
z = zip(avengers, names)
print(*z)


##Exercises

##1.
# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1,value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2,value2 in enumerate(mutants,start=1):
    print(index2, value2)



#III:Using iterators to load large files into memory

#Iterating over data


import pandas as pd
result = []
for chunk in pd.read_csv(r"\\Wwg00m.rootdom.net\bfs-home\XRFRBL\Personal Doc\Python\0. Python Data Science Toolbox_Part2\Test.csv",sep=";" ,chunksize=10):
     # result=print(chunk['Salary'])
     result.append(sum(chunk['Salary']))
     print(result)
       
total = sum(result)
print(total)


#We can obtain the same result by using also this procedure

total = 0
for chunk in pd.read_csv(r"\\Wwg00m.rootdom.net\bfs-home\XRFRBL\Personal Doc\Python\0. Python Data Science Toolbox_Part2\Test.csv",sep=";" ,chunksize=10):
    total += sum(chunk['Salary'])
    print(total)
print(total)


#Iterate over datata  with a dictionary 
# Initialize an empty dictionary: counts_dict
counts_dict={}
# Iterate over the file chunk by chunk
for chunk in pd.read_csv(r"\\Wwg00m.rootdom.net\bfs-home\XRFRBL\Personal Doc\Python\0. Python Data Science Toolbox_Part2\Test.csv",sep=";" ,chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['Department']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1
print(chunk['Department'])
# Print the populated dictionary
print(counts_dict)

#####We can automate the previous code with a FUNCTION:
    
# Define count_entries()
def count_entries(csv_file,c_size,colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk 
    for chunk in pd.read_csv(csv_file,sep=";" ,chunksize=c_size):
        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries("Test.csv",10,'Department')

# Print result_counts
print(result_counts)





###Chapter 2 : List comprehension

#Paragrapgh 2.1
#Populate a list with a for loop

nums = [12, 8, 21, 3, 16]
new_nums = []
for num in nums:
    new_nums.append(num + 1)
    #print(new_nums) I insert this line of code to understand the logic behind
print(new_nums)


#A list comprehension(same result than befoe but just one line of code rather than do the for loop)

nums = [12, 8, 21, 3, 16]
new_nums = [num + 1 for num in nums]
print(new_nums)



#List comprehension with range()

result = [num for num in range(11)]
print(result)



#Nested loops (1)

pairs_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append(num1, num2)
print(pairs_1)

#do the the same with a list comprehension
pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
print(pairs_2)



##Exercise par 2.1
#1.
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
first_ch_doctor= [doc[0] for doc in  doctor ]
print(first_ch_doctor)

#2. Create list comprehension: squares
squares = [i**2 for i in range(0,10)]
print(squares)


#3.Nested list comprehensions
# Create a 5 x 5 matrix using a list of lists: matrix

col_vector=[ col for col in range(5)]

matrix = [[ col for col in range(5)] for row in range(5)]
print(matrix)
# Print the matrix
for row in matrix:
    print(row)


#Paragrapgh 2.2: Advanced comprehensions

#Conditionals on the iterable
 #We can apply a conditional statement to test the iterator variable by adding an if statement in the optional 
  #predicate expression part after the for statement in the comprehension:
   # [ output expression for iterator variable in iterable if predicate expression ].


[num ** 2 for num in range(10) if num % 2 == 0]

#Conditionals on the output expression
 # Previously we used an if conditional statement in the predicate expression part of a list comprehension to evaluate 
 # an iterator variable. Now we are going to  use an if-else statement on the output expression of the list.
[num ** 2 if num % 2 == 0 else 0 for num in range(10)]

#Dictionary comprehension
  #Comprehensions aren't relegated merely to the world of lists. There are many other objects you can
  #build using comprehensions, such as dictionaries, pervasive objects in Data Science.
pos_neg = {num: -num for num in range(9)}
print(pos_neg)

print(type(pos_neg))

##Exercise par 2.2

#1.Using conditionals in comprehensions (1)
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member)>=7]

# Print the new list
print(new_fellowship)



#2.Using conditionals in comprehensions (2)
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member)>=7 else "" for member in fellowship]

# Print the new list
print(new_fellowship)




#3 .Dict comprehensions
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)




#Paragrapgh 2.3: Introduction to generator expressions


#Generator expressions

[2 * num for num in range(10)] #List comprehension

(2 * num for num in range(10)) # Generator expressions (just change [] with ())


#Printing values from generators (1)

result = (num for num in range(6))
for num in result:
    print(num)

result = (num for num in range(6))
print(list(result))



#Printing values from generators (2)

result = (num for num in range(6))

print(next(result))
print(next(result))
print(next(result)) #Lazy evaluation


#Conditionals in generator expressions

even_nums = (num for num in range(10) if num % 2 == 0)
print(list(even_nums))



#Generator functions

def num_sequence(n):
    """Generate values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1

result = num_sequence(5)
print(type(result))

for item in result:
    print(item)


