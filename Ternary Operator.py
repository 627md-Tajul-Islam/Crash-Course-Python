num1 = 10
num2 = 20
# Ternay means 3
#Dont do this
if num1>num2:
    print(num1)
else:
    print(num2)

# Do This
print(num1 if num1>num2 else num2)
# Even store in a variable
max = num1 if num1>num2 else num2
print(max)

