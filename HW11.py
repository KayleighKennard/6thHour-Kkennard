#Name:
#Class: 6th Hour
#Assignment: HW11
import random



#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
V_List=[
    random.randint(1,100),
    random.randint(1,100),
    random.randint(1,100)
]
#3. Print the list.
print(V_List)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if V_List[0]>V_List[1] and V_List[0]>V_List[2]:
    num=V_List[0]
    print(V_List[0],"is the biggest number")
elif V_List[1]>V_List[0] and V_List[1]>V_List[2]:
    num=V_List[1]
    print(V_List[1],"is the biggest number")
elif V_List[2]>V_List[0] and V_List[2]>V_List[1]:
    num=V_List[2]
    print(V_List[2],"is the biggest number")
#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num % 2 == 0:
    print(V_List[0],"is the even number")
elif num % 3 == 0:
    print(V_List[1],"is the odd number")
elif num %2==0 and num % 3 == 0:
    print(V_List[0],"can divide by 2 and 3")


