# Recursion in Python -- Calling the same function inside that function is Recursion. These types of construct are termed as recursive functions.

# Most common example of recursion is factorial of a number. 

'''
factorial(7) = 7*6*5*4*3*2*1
         or
factorial(7) = 7*factorial(6)
factorial(6) = 6*factorial(5) ... and so on
'''


#We can code it like this

def factorial(n):
  if(n==0 or n==1): # this is the termination condition for the function
    return 1
  else:
    return n*factorial(n-1) # the function will keep calling itself till n becomes 2

print(factorial(5))



# Fibonacci Sequence --

def fibb(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:  
    return fibb(n-1) + fibb(n-2)  

fibb(6)
  
  

 
    
