# >> Strings in Python --- 

# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

name = "Rohan"
print("Hello, " + name)

# Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

# We can use double quotes in the statement by using more single or double quotes .

print('He said, "I want to eat an apple".')


# >> Multiline Strings -- 

# Multiline string can be created using triple quotes -- 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



# >> Accessing Characters of a String --- 
# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string. 

print(name[0])
print(name[1])


# >> Looping through the string ---

# We can loop through strings using a for loop like this:

for character in name:
    print(character)  # where character is a variable so it could be anything else

for i in a:
  print(i)