# Match Case Statements in Python -- 

# If you are aware of any programming language like C , C++ or Java, you must have heard about switch-case statements.
# Switch-case elements are very similar to if-else elements. In python, instead of switch-case we call it match-case statements.

#A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. 
# The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

#The match case consists of three main entities :
# a). The match keyword
# b). One or more case clauses
# c). Expression for each case

# The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

# Example --

x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)