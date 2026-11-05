#Name:Kayleigh Kennard
#Class: 6th Hour
#Assignment: SC3

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
X=0
while X<100:
    X=X+1
    if X%3==0:
        print("Fizz")
    if X%5==0:
        print("Buzz")
    if X%15==0:
        print("FizzBuzz")
    else:
        print(X)
