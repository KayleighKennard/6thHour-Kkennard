#Name: Kayleigh Kennard
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
Hamil_List=["Alexander Hamilton","Aaron Burr","Thomas Jefferson","James Madison","George Washington"]
#2. Append a new name onto the Name List.
Hamil_List.append("Charles Lee")
print(Hamil_List)
#3. Print out the 4th name on the list.
print(Hamil_List[3])
#4. Create a list with 4 different integers in it.
Int_List=[7,55,2,3,90]
print(Int_List)
#5. Insert a new integer into the 2nd spot and print the new list.
Int_List.insert(1,2)
print(Int_List)
#6. Sort the list from lowest to highest and print the sorted list.
Int_List.sort()
print(Int_List)
#7. Add the 1st three numbers on the sorted list together and print the sum.
Int_List_sum=Int_List[0]+Int_List[1]+Int_List[2]
print(Int_List_sum)
#8. Create a list with two strings, two variables, and two boolean values.
List_Confusion=["My","Shot",2,5,True,False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(List_Confusion[int(input("give me a number"))])