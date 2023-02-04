# Loops in Python -- 

# b). While Loop -- while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

count = 5
while (count > 0):
  print(count)
  count = count - 1


# Else with While Loop -- We can even use the else statement with the while loop. Once the condition loops become false, the statements inside the else block gets executed.

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')


# Do-While loop in python --  do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

# Python does not have any do-while loop so to create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.  
  
# The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
  
