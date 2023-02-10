# Dictionary Methods

# Dictionary uses several built-in methods for manipulation.They are listed below


# 1. update() -- The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

#Removing items from dictionary: There are a few methods that we can use to remove items from dictionary.

# 2. clear() -- The clear() method removes all the items from the list.

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

# 3. pop() -- The pop() method removes the key-value pair whose key is passed as a parameter.

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

# 4. popitem(): The popitem() method removes the last key-value pair from the dictionary.

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

# 5. del: we can also use the del keyword to remove a dictionary item.

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

# 6. If key is not provided, then the del keyword will delete the dictionary entirely.

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
# print(info)