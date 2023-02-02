# Comments in Python ---

# Comments are used to explain a block of code or to provide information to the other programmer . These lines does not get executed with the program.

# a). Single-Line Comment -- Used to comment out a single line of code. In python we use "#" symbol for single line comments.
# b). Multi-Line Commetn -- Used to comment out multiple lines at once. In python we use """ """ (Triple colon) symbol for multi line comments.

#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

# Escape Sequence Characters --- 

# To insert characters that cannot be directly used in a string, we use an escape sequence character.

# An escape sequence character is a backslash \ followed by the character you want to insert.

# An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:
print("This doesnt "execute")
print("This will \" execute")
print("This adds a /t tab")

#For more --- https://www.w3schools.com/python/gloss_python_escape_characters.asp