#Name: Kayleigh Kennard
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library
import random


#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
d10=random.randint(1,10)
d20=random.randint(1,10)
d30=random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(d10,d20,d30)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
d10=d10+2
d20=d20-4
d30=d30*1.5
#6. Print each result from #5 on the same line.
print(d10,d20,d30)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
Bland_List=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
Bland_List.sort()
print(Bland_List)

#9. Add together the highest three numbers in the list from #7 and print the result.
Bland_list_sum=Bland_List[1]+Bland_List[2]+Bland_List[3]
print(Bland_list_sum)
#10. Create a list with 5 names of other students in this class and print the list.
Burr_List=["Cody","Tucker","Brody","Huxley","Matthew"]
print(Burr_List)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(Burr_List)
print(Burr_List)
#12. Print a random choice from the list of names from #10.
Burr_List_choice=random.choice(Burr_List)
print(Burr_List_choice)