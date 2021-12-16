import time
import random
class Creature:
    name = None
    age = None
    energy = None
    dead = False
#############
##   core  ##
#############
    def __init__(self, name, hp, energy,type):
        self.name = name
        self.hp = hp
        self.energy = energy
        self.type = type

    def intro(self):
        if not self.dead:
            print(f"Oh ho! You have no choice, but to get past me! \n My name is {self.name} and I will be the last peron you'll ever see! ")
        else:
            print(f"""{self.name} has been killed by {hero.name}""")
    
    def kill(self, creature):
        if creature.dead == False:
            randomroll = random.randint(0, 1)
            if randomroll == 0:
                creature.hp -= 45
                if creature.hp <= 0:
                    creature.dead = True
                print(f"{enemy1.name} has decided to be a champ and took full damage.")
            else:
                creature.hp -= 10
                if creature.hp <= 0:
                    creature.dead =  True
                print(f"{enemy1.name} has dodged \n he took only 10 damage.")

    #Creatures:
hero = Creature("Bob",100, 150, "human")
enemy1 = Creature("Pablo", 100, 150, "E_human")
enemy2 = Creature("Michael", 115, 150, "E_human")
    #Actions :)
print("An enemy has appeared before you!\n ")
enemy1.intro()
while True:
    choice1 = int(input("""
    1. Try to kill your enemy.
    2. Check your enemies health.
    3.Go somewhere else.
    Choose your action: """))
    if choice1 == 1:
        hero.kill(enemy1)
        time.sleep(1)
        print(f"{enemy1.name} has {enemy1.hp} health left.")
    elif choice1 == 2:
        time.sleep(0.3)
        print(f"{enemy1.name} has {enemy1.hp} health left.")
        if enemy1.hp <= 0:
            print(f"Your enemy is dead already.")
        else:
            print(f"Keep fighting him champ! :D")
    elif choice1 ==3:
        break
choice2 = int(input("""

You stumble upon a city.
1. Go to the city.
2. Exit the game (No saves here fella ;)
What do you do? : """))
    







