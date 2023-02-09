# String Slicing & Operations on String ---

# a). Length of a String - We can find the length of a string using len() function.

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")


# b). String Slicing -  The method of dividing a string into different parts is known as string slicing.
#A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.
pie = "ApplePie"
print(pie[:5]) #returns part of string pie from index 0 to index 4
print(pie[1:6]) #returns part of string from index 1 to 5
print(pie[3:]) # returns part of string from 3 to 7(length of string) 
print(pie[6])	#returns character at specified index

# We can also use negative indexing to slice or access the string elements. 

print(pie[-2: -5]) 

#Negative indexing is used if the string is too big and we have to access last of the elements.