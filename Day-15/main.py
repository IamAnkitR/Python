# Loops in Python -- 

# Loops are used to execute a group of statements certain number of times. In python, we have two different types of loops.-- 

# a). For Loop -- For loops can iterate over a sequence of iterable objects(list, tuples, string, sets and dictonaries) in python.

#Example1 : Iterating over a string -- 
name = 'Abhishek'
for i in name:
    print(i, end=", ")

#Example2 : Iterating over a list -- 
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)


# range() function -- 
# What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times? Here, we can use the range() function.

# Syntax -- range(start(optional), end , gap(optional))

for k in range(5):
    print(k)

for k in range(4,9):
    print(k)

for k in range(1, 12, 3):
  print(k)