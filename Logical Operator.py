# Logical Operator {and + or + not}
# and means each conditions must be fulfilled
# or means if 1/3 is fulfilled it will be executed

'''
num1 = 200
num2 = 100
num3 = 80

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
     print(num2)
else :
    print(num3)
'''

# Vowel = a,e,i,o,u

chr = "g"
if chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u':
    print("Vowel")
else:
    print("Consonant")