# >> String Methods -- 

# Python provides a set of built-in methods that we can use to alter and modify the strings.

# a). upper() : The upper() method converts a string to upper case.
str1 = "AbcDEfghIJ"
print(str1.upper())    # -- ABCDEFGHIJ

# b). lower() : The lower() method converts a string to lower case.
str1 = "AbcDEfghIJ"
print(str1.lower())   # -- abcdefghij

# c). strip() : The strip() method removes any white spaces before and after the string.
str2 = " Silver Spoon "
print(str2.strip)    # --Silver Spoon

# d). rstrip() : the rstrip() removes any trailing characters. Example:
str3 = "Hello !!!"
print(str3.rstrip("!"))   # -- Hello

# e). replace() : The replace() method replaces all occurences of a string with another string. Example:
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))  #-- Silver Moon

# f). split() : The split() method splits the given string at the specified instance and returns the separated strings as list items.
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".

# Output -- ['Silver', 'Spoon']

# g). capitalize() : The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. 
# The string has no effect if the first character is already uppercase.

str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)      # -- Hello
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)      # -- Hello world


# h). center() : The center() method aligns the string to the center as per the parameters given by the user.
str1 = "Welcome to the Console!!!"
print(str1.center(50))

# We can also provide padding character. It will fill the rest of the fill characters provided by the user.
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))

# i). count() : The count() method returns the number of times the given value has occurred within the given string.

str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)    # -- 4

#j). endswith() : The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))  # --True

#k). index() : The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))   # -- 13
print(str1.index("Daniel"))   # - ValueError: substring not found

# l). find() : The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))   # -- 10

# As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))  # -1

# m). isalnum() : The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str1 = "WelcomeToTheConsole"
print(str1.isalnum())    # -- True

# n). isalpha() :The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
str1 = "Welcome"
str2 = "Welcome1"
print(str1.isalpha())  # -- True
print(str2.isalpha())  # -- False

# o). islower() : The islower() method returns True if all the characters in the string are lower case, else it returns False.
str1 = "hello world"
print(str1.islower())   # -- True

# p). isprintable() : The isprintable() method returns True if all the values within the given string are printable, if not, then return False. Means there is no escape sequence character.
str1 = "We wish you a Merry Christmas"
print(str1.isprintable()) # -- True


# For More- https://www.w3schools.com/python/python_ref_string.asp