# if we put a nested statement it means it will have to execute all of the conditions to make it executed
'''
if 7>10:
    if 7>5:
        print("Hello")
else:
    print("Out")
'''

# Largest Number

num1 = 80
num2 = 90
num3 = 40

if num1 > num2:
    if num1 > num3:
        print(num1)

if num2 > num1:
    if num2 > num3:
        print(num2)

if num3 > num1:
    if num3 > num2:
        print(num3)


