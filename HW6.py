#Name:Kayleigh Kennard
#Class: 6th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
List_Hamil=[1,6,4,3,8,9,12,34,68]
#2. Sort the list from highest to lowest.
List_Hamil.sort(reverse=True)
#3. Create an empty list.
Empty_list=[]
#4. Remove the median number from the first list and add it to the second list.
Alex=List_Hamil.pop(4)
Empty_list.append(Alex)
#5. Remove the first number from the first list and add it to the second list.
Aaron=List_Hamil.pop(0)
Empty_list.append(Aaron)
#6. Print both lists.
print(List_Hamil)
print(Empty_list)
#7. Add the two numbers in the second list together and print the result.
Jefferson=Empty_list[0]+Empty_list[1]
print(Jefferson)
#8. Add the sum from #7 to the first list.
List_Hamil.append(Jefferson)
#9. Sort the first list from lowest to highest and print it.
List_Hamil.sort()
print(List_Hamil)