#Name: Kayleigh Kennard
#Class: 6th Hour
#Assignment: HW10

import random
#1. Print "Hello World!"
print("Hello World")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
a=random.randint(1,10)
b=random.randint(1,10)
c=random.randint(1,10)
#3. Print A, B, and C on the same line.
print(a,b,c)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if a>b:
    print("A is greater than B")
elif a<b:
    print("A is less than B")
elif a==b:
    print("A is equal to B")
#5.Make an if statement that prints if variable B is between 3 and 7, or not.
if b < 7 and b > 3:
    print("b is between 7 and 3")
else:
    print("B is not between 7 and 3")
#6. Make an if statement that prints if variable C is even or odd.
    if c % 2 == 0:
        print(f"{c} is even")

#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
D=3+random.randint(1,20)
print(D)
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
if D < a+b+c:
    print(f"{D} is greater than {a+b+c}")
