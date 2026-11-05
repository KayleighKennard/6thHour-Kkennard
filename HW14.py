#Name:Kayleigh Kennard
#Class: 6th Hour
#Assignment: HW14
import random

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i=5
while i>=0:
    print(i)
    i-=1
else:
    print("Hello World!")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
num=1
while num <= 30:
    if num % 2 == 0:
        print(num)
    num+=1
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
num2=0
while num2<=30:
    num2+=1
    if num2 % 3 == 0:
        continue
    print(num2)


#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
k=random.randint(1,6)
while k==1:
    print(k)
    if k==1:
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
N=int(input("enter number 0"))
while N !=0:
    N = int(input("enter number 0"))
