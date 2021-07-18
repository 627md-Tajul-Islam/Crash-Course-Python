"""
Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""
"""
In Python, defining the function works as follows. def is the keyword for defining a function. The function name is followed by parameter(s) in (). The colon : signals the start of the function body, which is marked by indentation. Inside the function body, the return statement determines the value to be returned
"""

x = "One"
def function():
    print("ALLAH is " + x)
function()

"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
"""

#Example
#Create a variable inside a function, with the same name as the global variable

y = "awesome"

def myfunc():
    y = "fantastic"
    print("Python is " + y)

myfunc()

print("Python is " + y)

"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside
that function.

To create a global variable inside a function, you can use the global keyword.
"""

#Example
#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global a
    a = "fantastic"

myfunc()

print("Python is " + a)
