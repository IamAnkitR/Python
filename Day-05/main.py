# Variables in Python

# Variables are containers that  holds data. Creating a variable is like creating a placeholder in memory and assigning it some value. 

a = 10  
name = "Ankit" 
d = None 
lie = False 


# Datatypes in Python 

# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.

#In python, we can print the type of any operator using type function:

a = 1
print(type(a))   # --- <class 'int'>
b = "1"
print(type(b))   # --- <class 'str'>

# Python has following buitl-in datatypes --- 

#a). Numeric data: int, float, complex
int = 3
float =  7.349
complex = complex(8, 2)

print(int,float,complex)
#b). Text data: str
str = "Hello World!!!"
print(str)
#c). Sequenced data: list, tuple

# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

#d). Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)