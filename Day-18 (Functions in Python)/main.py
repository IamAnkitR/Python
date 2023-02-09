# Functions in Python -- 

# A function is a block of code that performs a specific task whenever it is called.
# In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

# There are two types of functions:

# a). Built-in functions -- These functions are defined and pre-coded in python. 
# e.g. - min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
# b). User-defined functions -- We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.
# Syntax --
def function_name(parameters):
  pass
  # Code and Statements


# Calling a function -- We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")



def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass  # The pass statement is used as a placeholder for future code.
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)