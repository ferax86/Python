# -*- coding: utf-8 

"""
Created on Wed Oct 20 16:21:06 2021

@author: XRFRBL
"""
###Part I


####1. User Defined Functions
#Built in functions 

x = str(5)
print(x)
print(type(x))

def square():
    new_value=4**2
    print(new_value)
    
square()

#Function parameters
def square(value):
    new_value = value ** 2
    print(new_value)

square(4)


#Return values from functions
#using return
def square(value):
    new_value = value ** 2
    return new_value

num=square(4)
print(num)

# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout = word + '!!!'

    # Print shout_word
    print(shout)

# Call shout with the string 'congratulations'
shout("congratulations")




#Docsstrings
def square(value):
    """Return the square of a value."""
    new_value = value ** 2
    return new_value


####Multiple Function parameters

def raise_to_power(value1, value2):
    """Raise value1 to the power of value2."""
    new_value = value1 ** value2
    return new_value


result = raise_to_power(2, 3)
print(result)

##Jump into tuples(it makkes function return multiple values)

even_nums = (2, 4, 6)
print(type(even_nums))

###Unpack tuples 
# i)Unpack a tuple into several variables:
a, b, c = even_nums
print(a)
print(b)
print(c)

#ii)Access tuple elements like you do with lists

print(even_nums[1])
second_num = even_nums[1]
print(second_num)


#Returning multiple values

def raise_both(value1, value2):
    """Raise value1 to the power of value2 and vice versa."""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2) #tuple construction 
    return new_tuple

result = raise_both(2, 3)
print(result)


###Exercises of fine capitolo
##Ex.1
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1=word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2=word2+ '!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout=shout1+shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell= shout('congratulations','you')  

# Print yell
print(yell)

##Ex.2

nums=(3,4,6)
# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums

# Construct even_nums
even_nums = (2, num2, num3)

##Ex.3
# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1=word1 + '!!!' 
    
    # Concatenate word2 with '!!!': shout2
    shout2=word2+ '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words=(shout1,shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1,yell2=shout_all('congratulations','you')
# Print yell1 and yell2
print(yell1)
print(yell2)



##Ex.4
# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry]+=1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry]=1

    # Return the langs_count dictionary
    
    return langs_count
# Call count_entries(): result
result = count_entries(tweets_df,"lang")

# Print the result
print(result)


####2. Scope and User Defined Functions

#Global vs. local scope (1)

def square(value):
    """Returns the square of a number."""
    new_val = value ** 2
    return new_val
square(3)

new_val



#Global vs. local scope (2)

new_val = 10
def square(value):
    """Returns the square of a number."""
    new_val = value ** 2
    return new_val
square(3)
new_val


#Global vs. local scope (3)

new_val = 10
def square(value):
    """Returns the square of a number."""
    new_value2 = new_val ** 2 #If python cannot find the local scope variable , only then it loon in the global scope
    return new_value2
square(3)

new_val = 20
square(3)


#Global vs. local scope (4)
new_val = 10
def square(value):
    """Returns the square of a number."""
    global new_val           #here we want to alter the value of a global variable  within a function call
    new_val = new_val ** 2
    return new_val
square(3)

new_val #we want a new value of this global variable that has been altered inside the function



###Exercise
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team="justice league"
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)


#Here you're going to check out Python's built-in scope, which is really just a built-in module called builtins. 
#However, to query builtins, you'll need to import builtins. After executing import builtins
#execute dir(builtins) to print a list of all the names in the module builtins.

import  builtins as bt
dir(bt)



#Nested Functions

def mod2plus5(x1, x2, x3):
    """Returns the remainder plus 5 of three values."""
    new_x1 = x1 % 2 + 5
    new_x2 = x2 % 2 + 5
    new_x3 = x3 % 2 + 5
    return (new_x1, new_x2, new_x3)


print(mod2plus5(1, 2, 3))


#HERE above we perform tha same operation across tree variables. Not very scalable?
#Here below we create a nested function that do exactly the same but more efficiently 


def mod2plus5_new(x1, x2, x3):
    """Returns the remainder plus 5 of three values."""
    def inner(x):
        """Returns the remainder plus 5 of a value."""
        return x % 2 + 5
    return (inner(x1), inner(x2), inner(x3))


print(mod2plus5_new(1, 2, 3))


#One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or inner function 
#remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing scope is available 
#to the inner function even when the outer function has finished execution.


def raise_val(n):
    """Return the inner function."""
    def inner(x):
        """Raise x to the power of n."""
        raised = x ** n
        return raised
    return inner

square = raise_val(2)
cube = raise_val(3)
print(square(2), cube(4))



#Using non local
def outer():
    """Prints the value of n."""
    n = 1
    def inner():
        nonlocal n
        n = 2
        print(n)
    inner()
    print(n)
outer()


####Exercises

#1.
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))





#2.
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo


# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))


#3
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word=word+word    
    
    # Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word+'!!!'
    
    # Call function shout()
    shout()
    
    # Print echo_word
    print(echo_word)

# Call function echo_shout() with argument 'hello'
print(echo_shout('hello'))


####Default and flexible arguments

#Add a default argument

def power(number, pow=1):
    """Raise number to the power of pow."""
    new_value = number ** pow
    return new_value
power(9, 2)
power(9, 1)
power(9)



#Flexible arguments: *args (1)
def add_all(*args):
    """Sum all values in *args together."""
    # Initialize sum
    sum_all = 0
    # Accumulate the sum
    for num in args:
        sum_all += num
    return sum_all

add_all(1)
add_all(1, 2)
add_all(5, 10, 15, 20)



def print_all(**kwargs):
    """Print out key-value pairs in **kwargs."""
    # Print out the key-value pairs
    for key, value in kwargs.items():
            print(key + ":" + value)
print_all(name="Hugo Bowne-Anderson", employer="DataCamp")

####Exercises
##1.Function with one default argument
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = echo*word1

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey",echo=5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo) 
              
              
##2.Functions with multiple default arguments   
# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey",echo=5,intense=True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey",intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)


##3.Functions with variable-length arguments (*args) 

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge=""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words"
print(one_word)
print(many_words)


##4.Functions with variable-length arguments (*args) 
# What makes **kwargs different is that it allows you to pass a variable number 
# of keyword arguments to functions. Recall from the previous video that, within 
# the function definition, kwargs is a dictionary.      


# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")



###Chapter 3: Lambda Functions

#Some function definitions are simple enough that they can be converted to a lambda 
#function. By doing this, you write less lines of code, which is pretty awesome and will come 
#in handy, especially when you're writing and maintaining big programs.

raise_to_power = lambda x, y: x ** y
raise_to_power(2, 3)


#Exercise Basic lambda Function 
# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1,echo:word1 * echo)

# Call echo_word: result
result = echo_word('hey',5)

# Print result
print(result)



#THis is what would it be with the regular function 
def echo_word1(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words

print(echo_word1('hey',5))

 

# So far, you've used lambda functions to write short, simple functions as well as to redefine functions
# with simple functionality. The best use case for lambda functions, however, are for when you want these
# simple functionalities to be anonymously embedded within larger expressions. What that means is that the
# functionality is not stored in the environment, unlike a function defined with def. To understand this idea better, 
# you will use a lambda function in the context of the map() function.


nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)
print(square_all) #it is a map object 


print(list(square_all)) # so see in the shell we convert the map into a list object


##Exercises Map() and lambda functions

# 1.Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item +'!!!',spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list=list(shout_spells)

# Print the result
print(shout_spells_list)


# 2.Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member:len(member)>6 , fellowship)
result_1=filter(lambda x:x[0:2]=='fr', fellowship)
# Convert result to a list: result_list
result_list=list(result)
result_list_1=list(result_1)
# Print result_list
print(result_list)
print(result_list_1)


#3.

# Import reduce from functools
from functools  import reduce


# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1,item2: item1+ item2,stark)

# Print the result
print(result)


####Introduction to error handling

#Passing an incorrect argument

float(2)
float('2.3')
float('hello')


def sqrt(x):
    """Returns the square root of a number."""
    return x ** (0.5)
sqrt(4)
sqrt('hello')


#Errors and exceptions

def sqrt(x):
    """Returns the square root of a number."""
    try:
        return x ** 0.5
    except:
        print('x must be an int or float')
sqrt(4)
sqrt('hi')


def sqrt_1(x):
    """Returns the square root of a number."""
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')


sqrt_1(4)
sqrt_1('hi')
sqrt_1(-9) #We do not want this result

def sqrt_2(x):
    """Returns the square root of a number."""
    if x < 0:
        raise ValueError('x must be non-negative')
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')

###Exercise 
#1
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word=""
    shout_words=""

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word+'!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")


#2.Error handling by raising an error
# Another way to raise an error is by using raise. In this exercise, you will add a
# raise statement to the shout_echo() function you defined 
# before to raise an error message when the value supplied by the user to the echo 
# argument is less than 0.

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo<0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)


#####Esercizi fine capitolo
##1.
import pandas as pd
sales = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\sales.csv",sep=";")
sales.head(10)

# Define count_entries()
def count_entries(df, col_name='Quantity'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in dataframe
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        print("The DataFrame does not have a '+ col_name +' column.")

# Call count_entries(): result1
result1 = count_entries(sales, 'Quantity')
result2 = count_entries(sales, 'Quantities')
# Print result1
print(result1)


##2.

# Define count_entries()
def count_entries(df, col_name='Quantity'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
        
        # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1=count_entries(sales, col_name='Quantity')
result2=count_entries(sales, col_name='Quantities')
# Print result1
print(result1)
print(result2)



