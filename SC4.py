#Name:Kayleigh Kenanrd
#Class: 6th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

x=int(input("How many users?"))
Y=0
for i in range(1,x):
    R=int(input("any number 1 to 5"))
    while R>5 or R<1:
        R = int(input("invalid rating. Try again"))
    else:
        Y+=R
average=Y/(x-1)
print(average)
