#Name:Kayleigh Kennard
#Class: 6th Hour
#Assignment: HW16
import math
#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a=int(input("Give me a number:"))
b=int(input("Give me a number:"))
c=int(input("Give me a number:"))
#4. Add a and b together, then divide the sum by c. Print the result.
int_sum=(a+b)/c
print(int_sum)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
E=round(int_sum)
if int_sum % 2 == 0:
    print("Even")
else:
    print("Odd")
#6. Create a list of five different random integers between 1 and 10.
z_list=[2,5,7,9,4]
print(z_list)
#7. Print the 4th number in the list.
print(z_list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
z_list.append(1)
print(z_list)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
z_list.sort()
print(z_list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i=1
while i<=100:
    print(i)
    i+=i
#11. Create a list containing the names of five other students in the classroom.
names=["cody","owyn","misa","huxley","nate"]
#12. Create a for loop that individually prints out the names of each student in the list.
for name in names:
    print(names)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
r=1
for r in range(1,100):
    if r%10==0:
        break
#14. Free space. Do something creative. :)
W=random.randint(1,10)
V=random.randint(11,20)
if W%2==0:
    print(W)
if V%2==0:
    print(V)