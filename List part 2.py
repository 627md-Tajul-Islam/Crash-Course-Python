subject = ["Tajul","pratasha","Asad","mimi"]
print(len(subject)) #it helps us to define the length.it will not start from the index 0,normal pattern will be followed

subject.append("Momin") # append will add the desired output in the last of the object
print(subject)

subject.insert(2,"Ayan") # we will have to set the index number then we can insert
print(subject)

subject.remove("Momin") # items can be removed too
print(subject)


letters = ["F","E","D","C","B","A"] # it will decorate the numbers from beginning to last in a dictionary order
letters.sort()
print(letters)

letter = ["a","b","c","d","e"] # it will run this from a reverse order,it means
letter.reverse()
print(letter)

numbers = [20,10,30,40,55]
numbers.pop()
numbers.pop() #pop will remove the last element from an object
#numbers.clear() # clear function will clean up the entire function
print(numbers)


name = ["Tajul","Islam"]
name2 = name.copy() # it will copy the entire object and put a copy of that object in another variable
print(name2)


hey = [1,2,3,4,5,6,7,8,8,8]
position = hey.index(7)
print(position) # index function will return the index number of the element

position = hey.count(8)
print(position) # this function help to find how many times the element is in the object











