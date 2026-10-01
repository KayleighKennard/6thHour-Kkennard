#Name: Kayleigh Kennard
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
Hamilton_dictonary= {
    "year" :[2009,2015, 2016],
    "place":"new york",
    "creator":"Lin"
}
#3. Print the keys of the dictionary from #2.
print(Hamilton_dictonary.keys())
#4. Print the values of the dictionary from #2
print(Hamilton_dictonary.values())
#5. Print one of the three numbers from the list by itself
print(Hamilton_dictonary["year"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
Hamilton_dictonary.update({"reunion":2010})
#7. Print the entire dictionary from #2 with the updated key and value.
print(Hamilton_dictonary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
classpeople= {
    "studentA":{
        "name":"Cody",
        "grade":9,
        "sport":False,
    },
    "studentB":{
        "name":"Bensen",
        "grade":11,
        "sport":False,
    },

    "studentC": {
        "name":"Misa",
        "grade":10,
        "sport":False
    }
}
#9. Print the names of all three classmates on the same line.
print(classpeople["studentA"]["name"],classpeople["studentB"]["name"],classpeople["studentC"]["name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
classpeople.pop("studentA")
print(classpeople)