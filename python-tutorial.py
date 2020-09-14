#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 09 2020
@author: Claire Pontbriand, Data Analysis Specialist for Science

Tutorial - Python Fundamentals for Coders

Today we will
- Understand python syntax, array indexing, loops, conditionals, and functions
- Import and use the Numpy library

"""

# Normally, we will import libraries at the start of a script.
# Don't worry about this right now.
# This is explained more in the libraries section below!
import numpy as np


    
############################ 
#   
# Hello World!
#
############################    


# COMMENTING:
# <- Hashtag denotes a comment that will not execute any commands
x = 6 * 7 + 12
print(x)

# Variables persist between cells once they have been run (executed)
x - 20
    
#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      
#
# QUESTION 1:   Write the message 'Hello World' in the quotes.
#
#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      

message = 'Hello World'
print(message)



############################    
#
# Variables and Assignment
#
############################    

# How can I store data in programs?

#   Equals sign = assigns a value to the variable.

age = 36
first_name = 'Claire'


#  What's in a name?  Variable name conventions:
#
# - Use only letters, digits, and underscores _
# - Start with a letter (typically lower case)
# - Variable names are case sensitive
# - Use meaningful names!


# Python function print prints things as text

print(first_name)
print(first_name,'is',age,'years old.')


# Variables must be created before they are used.

print(last_name)

# What happens if I try to correct my error in the same cell?

last_name='Pontbriand'
print(last_name)

    
#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      
#
# QUESTION 2.  What will happen if I run this code?
#
# ? ? ? ? ? ? ? ? ? ? ? ?      

last_name = Pontbriand
print(last_name)

    
# Variables can be used in calulations.

# What will the output of the python code be?

age = age + 3
print('Age in three years:',age)




############################    
#
# PYTHON INDEXING
#
############################    
# Use an index to get a single character from a string
# - Use square brackets for the position
# - Indices are numbered from 0


atom_name = "helium"
print(atom_name[0])
print(atom_name[1])
print(atom_name[2])
print(atom_name[-1])

    
# Slicing Strings
# Use a slice to get a substring
# - Take a slice with `[start:stop]` but mathematically it gets [start:stop)

#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      
#
# QUESTION 3. What will the output of the following slice be?
#
#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      

print(atom_name[3:5])




#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      
# QUESTION 4.
#
# Swapping Values: a check of understanding
# Given the code below, what is the value of the variable `swap`?
#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      

x    = 1.0
y    = 3.0
swap = x
x    = y
y    = swap 


# Check your guess:

print(swap)


    
############################
#
# Data Types and Conversion 
#
############################
#
# ### Data Types:
# - integers (`int`) represent positive or negative whole numbers like 3 or -512
# - floating point numbers (`float`) represent real numbers like 3.12159 or -2.5 
# - character strings (`str`) are text
#    - written with single or double quotes (matching)
#    - quotations aren't printed when the string is displayed



# Find the type with function type()
print(type(52))
print(type(age))
print(type(first_name))
print(type(3.14))

# notice we are nesting functions.

# Data types control what operations can be performed on a value.


print(5-3)
print('hello'-'h')

# You can use the + and * operators on strings.


print(type(first_name))
full_name = first_name + ' ' + 'Pontbriand'
print(full_name)

# Strings have length (`len()`), but numbers don't.


print(len(full_name))
print(len(3.1415))


# We must convert numbers to strings or vice versa when operating on them.
# Consistency is key!


# print(1+'2')
print(1+int('2'))
print(str(1)+'2')


# We can mix integers and floats freely in operations.

print('half is', 1/2.0)
print('three squared is', 3.0 ** 2)

# Variables only change value when something is assigned to them.
# They are not like spreadsheets where a cell can depend on another 
# and update automatically.


# ### Division Types with numbers
# - // operator performs integer floor division
# - / operator performs floating point division
# - % modulo operator returns the remainder from integer division


print(5//3)
print(5/3)
print(5%3)



# # # # # # # # # # # # # # # #  
#                             #
# Built-in Functions and Help #
#                             #
# # # # # # # # # # # # # # # # 
#
#  How can I use built-in functions?
#  How can I find out what they do?
#  What kind of errors can occur in programs?


#  Use comments to add documentation to programs.
# This sentence isn't executed by python
adjustment = 0.5 # Neither is this - anything after # is ignored
print(adjustment)


#  A FUNCTION may take zero or more arguments
#  A function must always use parentheses
print('before')
print()
print('after')


# Commonly-used built-in functions include max, min, 
#  and round.
print(max(1,2,3))
print(min('a','A','0')) # Python users (0-9,A-Z,a-z) to compare letters
round(3.712)
round(3.71215,2) # second argument specifies number of decimal places

# Use the built-in function help to get help for a function.
help(round)

# Python reports syntax errors
# when it can’t understand the source of a program.
name='Feng  #forgot to close the quotation marks


# Python reports a runtime error 
# when something goes wrong while a program is executing.
age = 53
remaining = 100 - aege  #mispelled age





############################################
#
# FOR LOOPS
# How can I make a program do many things?
#
############################################


# for each thing in this group, do these operations
for number in [2, 3, 5]:
    print(number)

# This for loop is equivalent to:
print(2)
print(3)
print(5)

# for loop vocabulary:
#  - The collection is what the loop is being run on
#  - The body is the operations done for each value in the collection
#  - The loop variable is what changes in each iteration of the loop



# INDENTATION is always meaningful in Python
firstName = "Claire"
    lastName="Pontbriand"
    
#    The loop variable can be called anything.
for kitten in [2, 3, 5]:
    print(kitten)

    
#    The body of a loop can contain many statements
primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed   = p ** 3
    print(p, squared, cubed)

#    Use range to iterate over a sequence of numbers
print('a range is a build in function: range(0,3)')
for number in range(0,3):
    print(number)


#    The Accumulator pattern turns many values into one
#  A common pattern:
#  1. Initialize an accumulator variable to 0, an empty string, or empty list
#  2. Update the variable with values from a collection

# Sum the first 10 integers.
total = 0
for number in range(10):
    total = total + (number + 1)
    print(total)

#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      
#
# QUESTION 5: what happens if we change indention in the code above?
#
#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      





###########################################################
#
# CONDITIONALS
# How can programs do different things for different data?
#
###########################################################

#   Use if statements to control whether or not
#  a block of code is executed

mass = 3.5
if mass > 3.0:
    print(mass, 'is large')

mass = 2.0
if mass > 3.0:
    print(mass, 'is large')


#   Conditionals can be used inside loops
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')


# Use else to execute a block of code with if condition is not met
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 9.0:
        print(m, 'is huge')
    elif m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')


masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')

        
# Use elif (short for else if) to specify additional tests
# Conditions are tested once, in order, so order matters!
#
# QUESTION 4: What will this give us?
grade = 85
if grade >= 70:
    print('grade is C')
elif grade >= 80:
    print('grade is B')
elif grade >= 90:
    print('grade is A')


# We can evolve the values of variables too
velocity = 10.0
for i in range(5): # execute the loop 5 times
    print(i, ':', velocity)
    if velocity > 20.0:
        print('moving too fast')
        velocity = velocity - 5.0
    else:
        print('moving too slow')
        velocity = velocity + 10.0
print('final velocity:', velocity)


#   Compounding relations using and, or, and parentheses
mass     = [ 3.54,  2.07,  9.22,  1.86,  1.71]
velocity = [10.00, 20.00, 30.00, 25.00, 20.00]

i = 0
for i in range(5):
    if mass[i] > 5 and velocity[i] > 20:
        print("Fast heavy object.  Duck!")
    elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
        print("Normal traffic")
    elif mass[i] <= 2 and velocity[i] <= 20:
        print("Slow light object.  Ignore it")
    else:
        print("Whoa!  Something is up with the data.  Check it")

# Make use of parentheses just like in mathematics
# if (mass[i] <= 2 or mass[i] >= 5) and velocity[i] > 20:
# if mass[i] <= 2 or (mass[i] >= 5 and velocity[i] > 20):


#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      
#
# QUESTION 6.  What does this program print?
#
#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      

pressure = 71.9
if pressure > 50.0:
    pressure = 25.0
elif pressure <= 50.0:
    pressure = 0.0
print(pressure)



# # # # # # # # # # # # # # # #  
#                             #
# Libraries                   #
#                             #
# # # # # # # # # # # # # # # # 
#
#  How can I use software that other people have written?
#
#
# Most of the power of a programming language is in its libraries.
# A library is a collection of files (called modules) 
# that contains functions for use by other programs.
# May also contain data values 
# PyPI is the Python Package Index
#
# A program must import a library module before using it.
#
# The NumPy library contains multidimensional array and matrix data structures 
# NumPy can be used to perform a wide variety of math operations on arrays and
# matrices. 
#
# When we use "as", we are naming an alias for the library name
# np is the standard for shortening numpy

import numpy as np


# Have a question about a package?
# Get documentation with the question mark ?
# INSTRUCTIONS:  Ask about a library here:

?np

# Array Creation
# There are several ways to create arrays.
# For example, you can create an array from a regular Python list or 
# tuple using the array function. 
# The type of the resulting array is deduced from the type of the 
# elements in the sequences.

# Example array:
a = np.array([2,3,4])
print(a)
a.dtype  # Type of array


b = np.array([1.2, 3.5, 5.1])
b.dtype

# ? ? ? ? ? ? ? ? ? ? ?
#
# QUESTION 8: What's wrong with this array definition?
#
# ? ? ? ? ? ? ? ? ? ? ?

a = np.array(1,2,3,4)    






#######################################
# 
# # Writing Functions
# 
# - Break programs down into functions to make them easier to understand.
# - Human beings can only keep a few items in working memory at a time.
# - Understand larger/more complicated ideas by understanding and combining pieces.
# - Encapsulate complexity so that we can treat it as a single “thing”.
# - Also enables re-use.
# 
# ######################################
#
# *Define a function using def with a name, parameters, and a block of code.*
#  

def print_greeting():
    print('Hello!')


# Defining a function does not run it.

print_greeting()


# Arguments in call are matched to parameters in definition.

def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19)


# Or, we can name the arguments when we call the function, which allows 
# us to specify them in any order:

print_date(month=3, day=19, year=1871)


# Functions may return a result (a value) to their caller using return.

def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)

a = average([1, 3, 4])
print('average of actual values:', a)


# Remember: every function returns something.
# A function that doesn’t explicitly return a value automatically returns None.

print('average of empty list:', average([]))


result = print_date(1871, 3, 19)
print('result of call is:', result)




# ? ? ? ? ? ? ? ? ? ? ? ? ? 
#
#  Question 9.  What is the error here?
#
# ? ? ? ? ? ? ? ? ? ? ? ? ? 

def another_function
  print("Syntax errors are annoying.")
   print("But at least python tells us about them!")
  print("So they are usually not too hard to fix.")



# ? ? ? ? ? ? ? ? ? ? ? ? ? 
#
#  Question 10.  What does this code return?
#
# ? ? ? ? ? ? ? ? ? ? ? ? ? 


def report(pressure):
    print('pressure is', pressure)

print('calling', report, 22.5)




# ? ? ? ? ? ? ? ? ? ? ? ? ? 
#
#  Question 11. Does order of operations matter?
#
# ? ? ? ? ? ? ? ? ? ? ? ? ? 


fahr_to_celsius(32)

def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))



# ### Add documentation to your functions

# If the first thing in a function is a string that isn’t assigned to 
# a variable, that string is attached to the function as its documentation.  
# This is called a *docstring* and is in triple quotes.
# 


def offset_mean(data, target_mean_value):
    """Return a new array containing the original data
       with its mean offset to match the desired value."""
    return (data - numpy.mean(data)) + target_mean_value



help(offset_mean)

# ? ? ? ? ? ? ? ? ? ? ?
#
# QUESTION 12: PLEASE HELP ME WITH THIS CODE:
#
# ? ? ? ? ? ? ? ? ? ? ?
#    
    
def sort_for_middle(a,b,c):
    '''Return the middle value of three
     Assumes that the values can actually be compared
     Usage: sort_for_middle(a,b,c).  input three values
     '''
    values = [a,b,c]
    values.sort()
    return values[0]

help(sort_for_middle)

sort_for_middle(4,3,2)



# ## Readable Functions

#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      
#
#  Question 12:  Which one of these is more readable - s or std_dev? Why?
#
#? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?      


def s(p):
    a = 0
    for v in p:
        a += v
    m = a / len(p)
    d = 0
    for v in p:
        d += (v - m) * (v - m)
    return numpy.sqrt(d / (len(p) - 1))



def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return numpy.sqrt(sum_squared_devs / (len(sample) - 1))



############################################
# A Little extra PYTHON SYNTAX AND STRUCTURE
# How do we make sense of all these periods?
############################################

# ENDING A STATEMENT

# end-of-line
x = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9

# continuation marker \
x = 1 + 2 + 3 + 4 +\
5 + 6 + 7 + 8 + 9

# continuation with () [] ""
x = (1 + 2 + 3 + 4 +
         5 + 6 + 7 + 8 + 9)

# early end of statement ;
x = 1 + 2 + 3; print(x)

# In a program like excel, we structure our functions like this:
# we have data in x
x = [2, 3, 5]

# We are used to calling an operation on x with f(x)
max(x)

# In python, everything is treated as an object
# We have data in a numpy array x
# we call an operation on x with x.f()
x = np.array([2, 3, 5])
x.max()


##### end of tutorial #####




