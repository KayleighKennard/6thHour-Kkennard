#Name:Kayleigh Kennard
#Class: 6th Hour
#Assignment: HW15

import time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
i=1
for i in range(5,0,-1):
    print(i)

#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
x=1
for x in range(1,30):
    if x%2==0:
        print(x)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
y=1
for y in range(1,30):
    if y%3==0:
        continue
    else:
        print(y)
#4. Create a for loop that prints 5 different animals from a list.
animal=["pig","cow","horse","chicken","cat"]
for animal in animal:
    print(animal)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for word in input("ENTER WORD HERE:")[::-1]:
    print(word)
#6. Create a list containing 10 integers of your choice and print the list.
integer_list = [1,2,3,4,5,6,7,8,9,15]
print(integer_list)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for even_number in integer_list:
    if even_number%2==0:
        evenNumbers += 1
    else:
        oddNumbers += 1
print(evenNumbers)
print(oddNumbers)

#9. Create a variable that asks the user for an integer and an empty integer variable.
H=int(input("ENTER INTEGER HERE:"))
L=1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for V in range(1,H+1):
    L*=V
print(L)
