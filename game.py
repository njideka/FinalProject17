class Person():
    """All elements of person"""
#Characteristics
    def __init__(self):
        self.status='hungry'
        self.defense=100+lmao['durability']
        self.atk=1+lmao['atk']
        self.xp=300
        self.health=500+self.defense
        self.know=0+lmao['atk']
#Attacking
    def attack(self, some_animal):
        some_animal.health-=self.atk
        print("attacking")
#Defense
    def defend(self, some_animal):
        self.health-=some_animal.atk

class Bear():
    """All elements of bears"""
#Charateristics
    def __init__(self):
        self.health=500
        self.atk=250
        self.xp=300
        self.know=0
#Attacking
    def attack(self, you):
        you.health-=self.atk
#Defense
    def defend(self,you):
        self.health-=you.atk

class Island():
    """Characteristics of the island"""
#characteristics
    def __init__(self):
        self.food=0
        self.animals=200
        self.safety=0
        self.wood=1000
        self.fire=0
#Food
    def food(self, human):
        self.food=200
        print(f"The island's supply of food is at {self.food} right now. Keep that in mind.")

class Juice_Box():
    """About the juice box"""
#Characteristics
    def __init__(self):
        self.health=500
        self.atk=150
        self.xp=300
        self.know=1000
#Attacking
    def attack(self, you):
        you.health-=self.atk
#Defense
    def defend(self,you):
        self.health-=you.atk

class Kangaroo():
    """Everthing about the kangaroo"""
#Characteristics
    def __init__(self):
        self.health=500
        self.atk=300
        self.xp=300
        self.know=1
#Attacking
    def attack(self, you):
        you.health-=self.atk
#Defense
    def defend(self,you):
        self.health-=you.atk
class Ducks():
    """Everthing about ducks"""
#Charateristics
    def __init__(self):
        self.health=750
        self.atk=200
        self.xp=300
        self.know=100
#Attacking
    def attack(self, you):
        you.health-=self.atk
#Defense
    def defend(self,you):
        self.health-=you.atk
#Story bits
print("You are shipwreckred in a deserted island near Australia and you have no clean water, no prepared food,\n and only a tent with only a compass, wrench, your pet chinchilla and a bag of Welch's Fruit Snacks with food poisoning. These are your only items to survive.\n")
lol=input("Pick your poison\n")


#Displays a string based on what you have chose
def choose(lol):
    if lol=="compass":
        print("Did I tell you that it is broken? Well it's broken.\n")
    elif lol=="wrench":
        print("Educated guess\n")
    elif lol=="chinchilla":
        print("Cute\n")
    elif lol=="fruit snacks":
        print("Why?\n")
    else:
        print("You picked fruit snacks, didn't you\n")
print(choose(lol))

#Displays certain stats based on what you've chose
lmao={}
def place(lol):
    """Assigns dictionaries to items"""
    if lol=="compass":
        lmao.update({'qty':1,'atk':100,'know':1000, 'durability':80,'equipped':True})
    elif lol=="wrench":
        lmao.update({'qty':1, 'atk':400,'know':0,'durability':100,'equipped':True})
    elif lol=="chinchilla":
        lmao.update({'qty':1, 'atk':300,'know':0, 'durability':50,'equipped':False})

    elif lol=="fruit snacks":
        lmao.update({'qty':1,'atk':0, 'know':1000, 'durability':80,'equipped':True})
    else:
        lmao.update({'qty':1,'atk':0, 'know':1000, 'durability':80,'equipped':True})
place(lol)
print(f"Your quantity of {lol} is {lmao['qty']}, your attack increased by {lmao['atk']}, your defense increased by {lmao['durability']}, your knowledge increased by {lmao['know']}, and you have this item equipp-\n")

#Objects
bear=Bear()
you=Person()
some_animal=Bear()
island=Island()
juice_box=Juice_Box()
kangaroo=Kangaroo()
ducks=Ducks()

#Story bits
print(f"A koala appeared! It wants your {lol}!\n")
why=input("You have to fight or die. What will you do??????\n")

#For attacking
def fight():
    if why=="fight":
        you.attack(bear)
    else:
        print("The koala is still there\n")
fight()
#Displays health
print(f"The koala's health is at {bear.health}\n")

#If statment about fighting again
if why=="fight":
    l=input("He's not dead, fight him again\n")
else:
    l=input("Do you want to fight or not? Your life is on the line right now\n")

#Prints based on parameters
def survive():
    if l=="fight" and lol=="compass":
        for bear.health in range(1,5):
            you.attack(bear)
        bear.attack(you)
        print("The koala's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="thirsty"
        lmao['durability']+0.0000000001
        print("You have gained bear hide and meat!\n")
        print("Your durability increased by 0.0000000001\n")
    elif l=="fight" and lol=="fruit snacks":
        for bear.health in range(1,500):
            you.attack(bear)
        bear.attack(you)
        print("The koala's health is FINALLY at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="thirsty"
        lmao['durability']+0.0000000001
        print("You have gained bear hide and meat!\n")
        print("Your durability increased by 0.0000000001\n")
    elif l=="fight":
        you.attack(bear)
        bear.attack(you)
        print("The koala's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="thirsty"
        lmao['durability']+0.0000000001
        print("You have gained bear hide and meat!\n")
        print("Your durability increased by 0.0000000001\n")
    else:
        print("The koala went away")
survive()

#Saving
save=input("Do you want to save?\n")
def save_file():
    """Saves based on responses"""
    if save=="yes":
        print("There is nothing wrong with wearing animal hides. Day 1 complete\n")
    else:
        print("You are shipwreckred in a deserted island near Australia and you have no clean water, no prepared food, \n and only a tent with only a compass, wrench, your pet chinchilla and a bag of Welch's Fruit Snacks with food poisoning. These are your only items to survive.\n")
        print(lol)

print(save_file())


#Story bits
print(f"You wake up to see a lake up ahead, and you are {you.status}\n")
lake=input("What will you do?\n")

#Prints something based on responses
def swim():
    if lake=="drink" or "eat":
        print("There is a juice box ahead! It doesn't want you to have a healthy diet!\n")
    else:
        print("The lake is not poisonous. Just find food right now\n")
swim()

why1=input("You have to fight or die right now. What will you do??????\n")

#Attacks based on responses
def fight1():
    if why1=="fight":
        you.attack(juice_box)
    else:
        print("The juice box is still there\n")
#Prints health
print(f"The juice box's health is at {juice_box.health}\n")
#If statement about attacking again
if why1=="fight":
    l1=input("It's not dead, fight it again\n")
else:
    l1=input("Do you want to fight or not? Your life is on the line right now\n")
#You fight the juice box based on parameters
def survive1():
    """You fight the juice box based on your previous responses"""
    if l1=="fight" and lol=="compass" and lake=="thirsty":
        for juice_box.health in range(1,5):
            you.attack(juice_box)
        juice_box.attack(you)
        print("The juice box's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="hungry"
        lmao['know']+20
        lmao['atk']+20
        print("You have gained orange juice!\n")
        print("Your attack and knowledge increased by 20\n")
    elif l1=="fight" and lol=="fruit snacks" and lake=="thirsty":
        for juice_box.health in range(1,500):
            you.attack(bear)
        juice_box.attack(you)
        print("The juice box's health is FINALLY at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="hungry"
        lmao['know']+20
        lmao['atk']+20
        print("You have gained orange juice!\n")
        print("Your attack and knowledge increased by 20\n")
    elif l1=="fight" and lol=="compass" and lake=="hungry":
        for juice_box.health in range(1,5):
            you.attack(juice_box)
        juice_box.attack(you)
        print("The juice box's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="thirsty"
        lmao['know']+20
        lmao['atk']+20
        print("You have gained orange juice!\n")
        print("Your attack and knowledge increased by 20\n")
    elif l1=="fight" and lol=="fruit snacks" and lake=="hungry":
        for juice_box.health in range(1,500):
            you.attack(juice_box)
        juice_box.attack(you)
        print("The juice box's health is FINALLY at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="thristy"
        lmao['know']+20
        lmao['atk']+20
        print("You have gained orange juice!\n")
        print("Your attack and knowledge increased by 20\n")
    elif l1=="fight" and lake=="hungry":
        you.attack(juice_box)
        juice_box.attack(you)
        print("The juice box's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="thirsty"
        lmao['know']+20
        lmao['atk']+20
        print("You have gained orange juice!\n")
        print("Your attack and knowledge increased by 20\n")
    elif l1=="fight" and lake=="thirsty":
        you.attack(juice_box)
        juice_box.attack(you)
        print("The juice box's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="hungry"
        lmao['know']+20
        lmao['atk']+20
        print("You have gained orange juice!\n")
        print("Your attack and knowledge increased by 20\n")
    else:
        print("The juice box got swept away by the tide\n")
survive1()

#Save file
save1=input("Do you want to save?\n")
def save_file1():
    """Makes you able to save"""
    if save1=="yes":
        print("The night was rough for you, but you got your OJ. Day 2 complete\n")
    else:
        print("You are shipwreckred in a deserted island near Australia and you have no clean water, no prepared food, \n and only a tent with only a compass, wrench, your pet chinchilla and a bag of Welch's Fruit Snacks with food poisoning. These are your only items to survive.\n")
        print("This is just for show move on")


#Story bits
print(f"You wake up from your tent to see multiple log cabins in the distance. You see a trail made of cans of Mountain Dew and Doritos but the same trail leads to a rabies filled kangaroo. Remember you are still {you.status}.\n")
why2=input("Make your decision or die. or the kangaroo would do it for you.\n")


#Attacks kangaroo
def fight2():
    if why2=="fight":
        you.attack(kangaroo)
    else:
        print("The kangaroo is still there\n")
print(f"The kangaroo's health is at {kangaroo.health}\n")
#Enables you to fight again
if why2=="fight":
    l2=input("She's not dead, fight her again\n")
else:
    l2=input("Do you want to fight or not? Your life is REALLY on the line right now\n")

#You fight the kangarooo based on parameters
def survive2():
    """Fights kangaroo based on previous responses"""
    if l2=="fight" and lol=="compass" and you.status=="thirsty":
        for kangaroo.health in range(1,5):
            you.attack(kangaroo)
        kangaroo.attack(you)
        print("The kangaroo's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="hungry"
        lmao['know']+50
        lmao['atk']+50
        lmao['durability']+50
        print("You have gained Mountain Dew!\n")
        print("You have gained Doritos!\n")
        print("Your attack, knowledge, and durability increased by 50\n")
    elif l2=="fight" and lol=="fruit snacks" and you.status=="thirsty":
        for kangaroo.health in range(1,5):
            you.attack(kangaroo)
        kangaroo.attack(you)
        print("The kangaroo's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="hungry"
        lmao['know']+50
        lmao['atk']+50
        lmao['durability']+50
        print("You have gained Mountain Dew!\n")
        print("You have gained Doritos!\n")
        print("Your attack, knowledge, and durability increased by 50\n")
    elif l2=="fight" and lol=="compass" and you.status=="hungry":
        for kangaroo.health in range(1,5):
            you.attack(kangaroo)
        kangaroo.attack(you)
        print("The kangaroo's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="thristy"
        lmao['know']+50
        lmao['atk']+50
        lmao['durability']+50
        print("You have gained Mountain Dew!\n")
        print("You have gained Doritos!\n")
        print("Your attack, knowledge, and durability increased by 50\n")
    elif l2=="fight" and lol=="fruit snacks" and you.status=="hungry":
        for kangaroo.health in range(1,5):
            you.attack(kangaroo)
        kangaroo.attack(you)
        print("The kangaroo's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="thirsty"
        lmao['know']+50
        lmao['atk']+50
        lmao['durability']+50
        print("You have gained Mountain Dew!\n")
        print("You have gained Doritos!\n")
        print("Your attack, knowledge, and durability increased by 50\n")
    elif l2=="fight" and you.status=="hungry":
        you.attack(kangaroo)
        kangaroo.attack(you)
        print("The kangaroo's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="hungry"
        lmao['know']+50
        lmao['atk']+50
        lmao['durability']+50
        print("You have gained Mountain Dew!\n")
        print("You have gained Doritos!\n")
        print("Your attack, knowledge, and durability increased by 50\n")
    elif l2=="fight" and you.status=="thirsty":
        you.attack(kangaroo)
        kangaroo.attack(you)
        print("The kangaroo's health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="hungry"
        lmao['know']+50
        lmao['atk']+50
        lmao['durability']+50
        print("You have gained Mountain Dew!\n")
        print("You have gained Doritos!\n")
        print("Your attack, knowledge, and durability increased by 50\n")
    else:
        print("The kangaroo died because it has rabies\n")
survive2()


#Saves
save2=input("Do you want to save?\n")
def save_file2():
    if save2=="yes":
        print("The night was rough for you, but you got your OJ. Day 2 complete\n")
    else:
        print("You are shipwreckred in a deserted island near Australia and you have no clean water, no prepared food, \n and only a tent with only a compass, wrench, your pet chinchilla and a bag of Welch's Fruit Snacks with food poisoning. These are your only items to survive.\n")
        print("This is just for show move on")

#Story bit
print("After you have came out of the cabin, you found a telephone so you can call your family to pick you up. But it doesn't work. Unfortunately, you need the most pwerful tool, duck tape. ...Don't look at me that way, I know all, including how to spell. So you need ducks to kill to craft it. Luckily there are ducks in that marsh in front of you")


why3=input("Just fight or die.\n")
#Function that attacks the ducks
def fight3():
    if why3=="fight":
        you.attack(ducks)
    else:
        print("The ducks are still there\n")
print(f"The ducks' health is at {ducks.health}\n")
#If statements that make you able to attack again or pass through areas
if why3=="fight":
    l3=input("They're not dead, fight them again\n")
else:
    l3=input("Do you want to fight or not? You'll wait 5-10 business days\n")

#Takes responses and interprets them differently based on them
def survive3():
    if l3=="fight" and lol=="compass":
        for ducks.health in range(1,5):
            you.attack(ducks)
        ducks.attack(you)
        print("The ducks'combined health is at 0\n")
        lmao['know']+9000
        print(f"Your health is {you.health}\n")
        you.status="fine"
        print("You have gained duck tape!\n")
        print("Your knowledge increased by 9000\n")
    elif l3=="fight" and lol=="fruit snacks":
        for ducks.health in range(1,500):
            you.attack(ducks)
        ducks.attack(you)
        print("The ducks'combined health is FINALLY at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="fine"
        lmao['know']+9000
        print("You have gained duck tape!\n")
        print("Your knowledge increased by 9000\n")
    elif l3=="fight":
        you.attack(ducks)
        ducks.attack(you)
        print("The ducks' health is at 0\n")
        print(f"Your health is {you.health}\n")
        you.status="fine"
        lmao['know']+9000
        print("You have gained duck tape\n")
        print("Your knowledge increased by 9000\n")
    else:
        print("The ducks went away\n")
island.animals=197
#Story bits
print(f"Now you have fixed the telephone,you can contact your folks at home. But until they can give you a lift, you are being held as a hero by the Australian government.So when you step into the airplane, the flight attendant asks you a few questions to verify if it is you. One of those questions is how many animals did you kill today. There were 200 animals when you got shipwrecked and {island.animals} currently.\n")
#If statements about how many animals you have killed
dead=input("How many animals have you killed today? \n")
def end(dead):
    if dead=="1":
        print("You're smart, Day 4 complete\n")
        print("Thanks for playing :-)\n")

    elif dead=="2":
        print("Wrong answer GAME OVER\n")
        print("You are shipwreckred in a deserted island near Australia and you have no clean water, no prepared food, \n and only a tent with only a compass, wrench, your pet chinchilla and a bag of Welch's Fruit Snacks with food poisoning. These are your only items to survive.\n")
        print("JK Thanks for playing :-)\n")


    elif dead=="3":
        print("Wrong answer GAME OVER\n")
        print("You are shipwreckred in a deserted island near Australia and you have no clean water, no prepared food, \n and only a tent with only a compass, wrench, your pet chinchilla and a bag of Welch's Fruit Snacks with food poisoning. These are your only items to survive.\n")
        print("JK Thanks for playing :-)\n")


    elif dead=="4":
        print("Wrong answer GAME OVER\n")
        print("You are shipwreckred in a deserted island near Australia and you have no clean water, no prepared food, \n and only a tent with only a compass, wrench, your pet chinchilla and a bag of Welch's Fruit Snacks with food poisoning. These are your only items to survive.\n")
        print("JK Thanks for playing :-)\n")
end(dead)