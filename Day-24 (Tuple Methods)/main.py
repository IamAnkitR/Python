# Tuple Methods -- 

# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

# Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

# However, we can directly concatenate two tuples without converting them to list.

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


# As tuple is immutable type of collection of elements it have limited built in methods.They are explained below

# 1). count() Method -- The count() method of Tuple returns the number of times the given element appears in the tuple.
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# 2). index() method -- The Index() method returns the first occurrence of the given element from the tuple.

# Note: This method raises a ValueError if the element is not found in the tuple.

Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)

res = Tuple.index(3, 4, 8 ) # Searches for 3's occurance between index 4 to 7