#Name:Kayleigh Kennard
#Class: 6th Hour
#Assignment: Sandbox
import random

Health = random.randint(0,10)
gets_hit = random.choice([True, False])
hitting = random.choice([True, False])
full="Max Health"

subject=("player1")
is_walking=random.choice([True, False])
print(subject)
if is_walking==True:
    print("walking", (random.randint(1,10)))
    print("blocks")
    if is_walking==False:
            print("walking", (0))
            print("blocks")

if gets_hit==True:
    print("minus",Health,"HP")
if gets_hit==False:
    print(full)
if hitting==True:
    print("player losses a heart")
if hitting==False:
    print("no change in HP")


