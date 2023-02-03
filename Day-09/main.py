
# >> Taking UserInput in Python-- 

# input() funtion is used to take a input from user in python. It gives us a return value as string/character so to store it we need to pass that into a variable.
name = input()
print("Hello, ", name)

# We can also diaplay a text message while taking input by inserting a string inside the input function.
name = input("Enter your name ")
print("Hey there! ",name)

# Note -- Because input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

variable=int(input("Enter an integer")) # input function will take it as an string and due to typecasting it'll be converted into int.
variable=float(input("Enter a float")) # input function will take it as an string and due to typecasting it'll be converted into float.

# It can also be done this way --

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x  + y)

print(int(x) + int(y))
