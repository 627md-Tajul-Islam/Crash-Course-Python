#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:

#Example
one, two, three = ("Tajul", "sumaiya", "Pratasha")
print(one)
print(two)
print(three)

#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:

#Example
x = y = z = "Tajul islam"
print(x)
print(y)
print(z)


#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

#Example
#Unpack a list:

language = ["JAVASCRIPT", "JAVA", "C"]
x, y, z = language
print(x)
print(y)
print(z)