# Docstring in Python --- 

# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
# These are used to explain the working of the function , class, modules etc.



# Example 1:
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)



# Example 2: 

def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
  
    return num1 + num2
    



# docstring are not like comments, the Python interpreter does not ignore them. We can print the docstring using thr "doc" attribute. 
  #   print(add.__doc__)    --use this line before return statement to read docstring. 
   






# PEP 8 --- Python Enhancement Proposal

# PEP 8 is a document that provides guidelines and best practices on how to write Python code. 
# It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.
#  A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.




# The Zen of Python --- An easter egg in python 
 
import this   # describes the basic priciples of python in a form of poem