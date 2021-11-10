# -*- coding: utf-8 -*-

#Comment 
"""
a=6 
print (a)
"""

# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)


 ####1.Intro to Python

# Variable type

Height = 200
type (Height)
#%%  


savings=100
growth_multiplier=1.1
result=savings*(growth_multiplier**7)
print(result)
#%%
desc="compound interest"  #String type
profitable=True  #Boolean Type
#%%

doubledesc=desc+desc 
print(doubledesc)

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")


# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float=float(pi_string)

#Different data type--> different behaviour
'ab'+'cd'
2+3   


#######2. Lists
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas=[hall,kit,liv,bed,bath]

# Print areas
print(areas)

# Adapt list areas
areas = ["hallway",hall,"kitchen",kit, "living room", liv, "bedroom",bed, "bathroom", bath]
# Print areas
print(areas)

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

# Subsetting Lists

fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89] #Python uses 0 index
fam
fam[3]
fam[-1] # Find last element of a list
fam[-2]
fam[3:5] # the 5 element is excluded(very important)
fam[:4]
fam[5:]

#Sum of different lists element
liz_emma=fam[1]+fam[3]
liz_emma

#Subsetting lists of lists

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]


###Manipulating Lists

#Changing Lists Elements
fam[7]=1.86
fam
fam[0:2] = ["lisa", 1.74]
fam
#Adding elements
fam + ["me", 1.79]
fam_ext = fam + ["me", 1.79]
#Deleting Elements
del(fam[2])
fam
#Behind the scenes(Case1)

x=["a","b","c"]
x
y=x
y[1]="z"
y
x

#Behind the scenes(Case2)
x1=["a","b","c"]
x1
y1=list(x1)
y1[1]="z"
y1
x1


#######3.Functions
#3.1 Introduction
fam = [1.73,1.68,1.71,1.89] 
fam
max(fam)
len(fam)
tallest = max(fam) 
tallest
round(1.68, 1)
round(1.68)
help(round) # Open up documentation
var2 = True
out2=int(var2) #Data type conversion(boolean to integer)
help(sorted)

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full=first+second
full_sorted=sorted(full,reverse=True) # Sort in Descending order
print(full_sorted)

##3.2 Methods

#List Methods
fam = ["liz", 1.73, "emma", 1.68,"mom", 1.71, "dad", 1.89]
fam.index("mom") # "Call method index() on fam"
fam.count(1.73)  #Number of times 1.73 occurs in the fam list

#String Methods
sister ="liz"
sister.capitalize()
sister.replace("z", "sa")

# Exercise
place = "poolhouse"
place_up=place.upper()
print(place)
print(place_up)
print(place.count('o'))
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas.index(20)
areas.count(9.5)
areas.append(24.5)
areas.append(15.45)
print(areas)
areas.reverse()
print(areas)

##3.3 Packages
import numpy as np
np.array([1, 2, 3])
dir()

from numpy import array #Here we import only the array package in numpy
array([1, 2, 3])

# Exercise
# Definition of radius
r = 0.43
# Import the math package
import math as math
# Calculate C
C = 2*math.pi*r
# Calculate A
A = math.pi*r*r
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))



#######4.Numpy

#Numpy Introduction
height = [1.73, 1.68, 1.71, 1.89, 1.79]
height
type(height)

weight = [65.4, 59.2, 63.6, 88.4, 68.7]
weight

weight / height ** 2 #Error as we cannot perform operation on list-->Solution wth Numpy

import numpy as np
np_height = np.array(height)
type(np_height)
print(np_height)

np_height.mean()
np_height.max()
len(np_height)

np_weight = np.array(weight)
np_weight
bmi = np_weight / (np_height ** 2)
bmi

#Numpy: remarks
np.array([1.0, "is", True]) #Error as Numpy arrays can contain only one type

python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])
python_list + python_list
numpy_array + numpy_array                 #Different data type : different behaviour
np.array([True, 1, 2]) + np.array([3, 4, False])
#Numpy Subsetting

bmi
type(bmi)
bmi[1]
bmi > 23
bmi[bmi > 23]
x = ["a", "b", "c"]
x[1]
np_x = np.array(x)
np_x[1]


#Numpy : 2D Numpy Arrays

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
type(np_height)
type(np_weight)

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],[65.4, 59.2, 63.6, 88.4, 68.7]])
np_2d
np_2d.shape # 2 rows, 5 columns shape is an attribute not a method


np.array([[1.73, 1.68, 1.71, 1.89, 1.79],[65.4, 59.2, 63.6, 88.4, "68.7"]]) #we have one string so all float will be convert to string to be homogeneous (coerced)

np_2d[0]   # select the first row 
np_2d[0][2] # Select third element of the first row
np_2d[0,2] # Alternative 
np_2d[:,1:3] #select all rows but only second and third column
np_2d[1,:] # Select all columns but only the second row


#Exercise 

baseball = [
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball=np.array(baseball)
print(type(np_baseball))
np_baseball.shape
print(np_baseball.shape)


# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]
# numpy
np_x = np.array(x)
np_x[:,0]
np_mat = np.array([[1, 2], [3, 4], [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat


#Numpy : Basic Statistics
# Generate data : "np.random.normal"
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
len(height)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight)) # it is the cbind in R

#Descriptive statistics
media=np.mean(np_city[:,0])
mediana=np.median(np_city[:,0])
correlazione=np.corrcoef(np_city[:,0], np_city[:,1])
correlazione
deviazonestandard=np.std(np_city[:,0])
print("Standard Deviation: " + str(deviazonestandard))
np.sort(np_city[:,0])
np.sum(np_city[:,0])








