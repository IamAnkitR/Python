# Let's write our first python program

print("Hello World")  #--Hello World
print(10)             #--10
print(20*10)          #--200

# The print() function prints the specified message to the screen, or other standard output device. The message can be a string, or any other object, the object will be converted into a string before written to the screen.

#Syntax-- print(object(s), sep=separator, end=end, file=file, flush=flush)

#a). object(s)---	Any object, and as many as you like. Will be converted to string before printed
#b). sep--- 'separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
#c). end--- 'end'	Optional. Specify what to print at the end. Default is '\n' (line feed)
#d). file---	Optional. An object with a write method. Default is sys.stdout
#e). flush---	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False
