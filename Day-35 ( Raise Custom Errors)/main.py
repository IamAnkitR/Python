# Raising Custom Errors in Python --- 


# Sometimes we may need to create our own custom exceptions that serve our purpose. We use custo In python, we can raise custom errors by using the raise keyword.


salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")



# Defining Custom Exceptions ---  In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

# Syntax -- 
'''
class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...
'''

# This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.

# Example -- 
a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")