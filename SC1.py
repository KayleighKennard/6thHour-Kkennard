#Name: Kayleigh Kennard
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.
enemycreatures= {
    "enemyA":{
            "Damage":120,
            "healing factor":True,
            "Health":600,
            "ivisibility pulse":True
    },
    "enemyB":{
            "Damage":50,
            "healing factor":False,
            "invisibility pulse":True
    },
    "enemyC": {
              "Damage":100,
              "healing factor":False,
              "Health":150,
              "invisibility pulse":False
    },
    "enemyD":{
            "Damage":250,
            "healing factor":False,
            "Health":500,
            "invisibility pulse":False
    },
    "enemyE":{
                "Damage":600,
                "healing factor":True,
                "Health":1000,
                "invisibility pulse":True,
    },
        }
print(enemycreatures)

enemycreatures["enemyA"].update({"Damage":int(input("Enter Damage:"))})


enemycreatures["enemyB"].update({"Damage":int(input("Enter Damage:"))})

enemycreatures["enemyC"].update({"Damage":int(input("Enter Damage:"))})

enemycreatures["enemyD"].update({"Damage":int(input("Enter Damage:"))})

enemycreatures["enemyE"].update({"Damage":int(input("Enter Damage:"))})
print(enemycreatures)