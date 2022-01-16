name="Dinesh"
location="London"
print(f"Welcome {name} to {location}")

num_1 = 10
num_2 = 100

print(f"Sum of given numbers {num_1} and {num_2} is {num_1 + num_2}")

#Special data collection type
'''
1. List : Array : collection of types of data
2. Dictionary
3. Tuple
'''

#Loops in Python
'''
1. if...else, nested if else
2. for
3. while
4. try ... except
'''
i=8
#1. if..else
if i < 10:
    print("value is less than 10")
    if i < 6:
        print("value is less than 6")
    elif i < 8:
        print ("value is less than 8 but greater than or equal to 6")
    else:
        print("I'm in else block of line no 26")
else:
    print("I'm in else block of line no 28")


#2 for
'''
for <item> in []:
    line

indentation
'''
print(f"\n example of for loop...")
for number in [1,2,3,4]:
    print(f"number is {number}")
    if (number % 2 == 0):
        print("this number is even")
        print("something.....")
    print("end of for loops iteration")
print(f"this is a number")

print(f"\n below example of while")
#while
i=1
while i<4:
    i = i + 1
    print(i)
print("i'm out of while loop")


print(f"\n below example of try..except...")
a=4.9028
b=9.7867
try:
    print(a+b)
except:
    print(f"given values are {a} and {b}")
