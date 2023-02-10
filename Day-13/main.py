# if-else statements in Python -- 

# Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. 
# If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

# Based on this, the conditional statements are further classified into following types:

#a). if statement -- In statement, the condition inside if block is checked and executed it the condition is true.
num = 10
if(num%2 == 0):
  print("Even number")
  

#b). if-else statement -- similar to if statement but if the if condition fails then the else condition gets checked and executed if true.
age = 19 
if(age>18):
  print("You can drive")
else:
  print("You can't drive")
  

#c). if-elif-else -- To check mutilpe conditions at once we can use if-elif-else statements.
num = 10
if (num < 0):   # False so elif will be executed
    print("Number is negative.")
elif (num == 0):   # False so else will be executed
    print("Number is Zero.")
else:                # True
    print("Number is positive.")


#d). nested if -- We can use if, if-else, elif statements inside other if statements as well.
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")