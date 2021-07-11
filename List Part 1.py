# list is an object,where we can store objects

Skills = ["Html","Css","Javascript","Python","Django"]

print(Skills) # it will print the full object
print(Skills[0])  # we can print the specific index number
print(Skills[2:4]) # we can also print from a specofic value
print(Skills[-1]) # minus means it will start and start form the last digit


print("Python" in Skills) #we can check if it is in our list,if there is it will return true
print("Java" in Skills) #if there is nothing it will return false
print("pyhon" in Skills) #python is a case sensitive language.

print("swift" not in Skills) # it means swift is not in the array,so its true

print(Skills + ["Swift","Java"])
print(Skills * 4)