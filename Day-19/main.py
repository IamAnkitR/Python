# Function Arguments and return statement -- 

# Parameters are what we need(which we decide while defining the function), arguments are what we give(when we call the function).

# There are four types of arguments that we can provide in a function:

# a). Default Arguments -- We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

# b). Keyword Arguments -- We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

# c). Required Arguments -- In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")

# d). Variable length Arguments -- Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

# There are two ways to achieve this:

# 1). Arbitrary Arguments:
# While creating a function, pass a ''*'' before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

# 2). Keyword Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")



# return Statement
# The return statement is used to return the value of the expression back to the calling function. 
# When we return a value from some function we should store it in a variable. 

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

a = name("James", "Buchanan", "Barnes"))

print(a)

