# DnD 5th Edition Character Creator
# Mason Ferucci
# Programming Logic and Design
# Final Project
# 4/19/2019

import cmd
import textwrap
import sys
import os
import time
import random


##### Player Character Setup #####
class playerChar:
    def __init__(self):
        self.playerName = ''
        self.charName = ''
        self.charClass = ''
        self.charRace = ''
        self.hp = 0
        self.str = 0
        self.strMod = 0
        self.dex = 0
        self.dexMod = 0
        self.con = 0
        self.conMod = 0
        self.int = 0
        self.intMod = 0
        self.wis = 0
        self.wisMod = 0
        self.cha = 0
        self.chaMod = 0
        self.ac = 10


myCharacter = playerChar()

### Valid Race Choice Options ###
validRaces = ['aarakocra', 'dragonborn', 'dwarf', 'elf', 'gnome',
              'goliath', 'halfling', 'human', 'tiefling']

### Valid Class Choice Options ###
validClasses = ['barbarian', 'bard', 'cleric', 'druid', 'fighter',
                'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']


##### Main Menu Seclection Options #####
def mainSelection():
    option = input("> ")
    if option.lower() == ("create"):
        launchCreator()
    elif option.lower() == ("random"):
        randomCharGen()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['create', 'random', 'quit']:
        print("Please enter a valid option")
        option = input("> ")
        if option.lower() == ("create"):
            launchCreator()
        elif option.lower() == ("random"):
            randomCharGen()
        elif option.lower() == ("quit"):
            sys.exit()


##### Main Menu #####
def mainMenu():
    os.system('clear')
    print('********************************************')
    print('  Welcome to the DnD 5E Character Creator  ')
    print('********************************************')
    print('                 • Create •                 ')
    print('                 • Random •                 ')
    print('                 •  Quit  •                 ')
    print('********************************************')

    mainSelection()


##### Collect Players Name #####
def nameCollector():
    qPlayerName = "Hello, what's your name?\n"
    for character in qPlayerName:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input("> ")
    myCharacter.playerName = playerName.capitalize()


##### Collect Character Name #####
def charNameCollector():
    qGreet = f"Alright {myCharacter.playerName}, what do you want your characters name to be? \n"
    # Write out question nicely
    for character in qGreet:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    charName = input("> ")
    myCharacter.charName = charName.capitalize()


##### Collect Players Class Choice #####
def classCollector():
    qClass = f"Okay {myCharacter.playerName}, what class do you want your character {myCharacter.charName} to be?\n"
    qClassDef = "(You can be a Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, or Wizard)\n"

   # Write out question nicely
    for character in qClass:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in qClassDef:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    playerClass = input("> ")

    if playerClass.lower() in validClasses:
        myCharacter.charClass = playerClass.lower()
        setClassTemplate()
        print(f"{myCharacter.charName} is now a {playerClass}!\n")
    while playerClass.lower() not in validClasses:
        print("Please enter a valid class")
        playerClass = input("> ")
        if playerClass.lower() in validClasses:
            myCharacter.charClass = playerClass.lower()
            setClassTemplate()
            print(f"{myCharacter.charName} is now a {playerClass}!\n")


##### Collect Players Race Choice #####
def raceCollector():
    qRace = f"Alright, {myCharacter.playerName} your character {myCharacter.charName} is a {myCharacter.charClass}..\n What race do you want them be?\n"
    qRaceDef = "(You can be a Aarakocra, Dragonborn, Dwarf, Elf, Gnome, Goliath, Halfling, Human, or Tiefling)\n"

    # Write out question nicely
    for character in qRace:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in qRaceDef:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    playerRace = input("> ")

    if playerRace.lower() in validRaces:
        myCharacter.charRace = playerRace.lower()
        setRacials()
        print(f"{myCharacter.charName} is now a {playerRace}!\n")
    while playerRace.lower() not in validRaces:
        print("Please enter a valid race")
        playerRace = input("> ")
        if playerRace.lower() in validRaces:
            myCharacter.charRace = playerRace.lower()
            setRacials()
            print(f"{myCharacter.charName} is now a {playerRace}!\n")


##### Sets Class Stats Based On Chosen Class #####
def setClassTemplate():
        ### Class Base Stats ###
    if myCharacter.charClass == 'barbarian':
        myCharacter.hp = 12
        myCharacter.str = 15
        myCharacter.dex = 13
        myCharacter.con = 14
        myCharacter.int = 8
        myCharacter.wis = 10
        myCharacter.cha = 12
    elif myCharacter.charClass == 'bard':
        myCharacter.hp = 8
        myCharacter.str = 8
        myCharacter.dex = 10
        myCharacter.con = 15
        myCharacter.int = 14
        myCharacter.wis = 12
        myCharacter.cha = 13
    elif myCharacter.charClass == 'cleric':
        myCharacter.hp = 8
        myCharacter.str = 10
        myCharacter.dex = 8
        myCharacter.con = 13
        myCharacter.int = 12
        myCharacter.wis = 15
        myCharacter.cha = 14
    elif myCharacter.charClass == 'druid':
        myCharacter.hp = 8
        myCharacter.str = 8
        myCharacter.dex = 14
        myCharacter.con = 12
        myCharacter.int = 10
        myCharacter.wis = 15
        myCharacter.cha = 13
    elif myCharacter.charClass == 'fighter':
        myCharacter.hp = 10
        myCharacter.str = 15
        myCharacter.dex = 12
        myCharacter.con = 14
        myCharacter.int = 8
        myCharacter.wis = 10
        myCharacter.cha = 13
    elif myCharacter.charClass == 'monk':
        myCharacter.hp = 8
        myCharacter.str = 13
        myCharacter.dex = 15
        myCharacter.con = 12
        myCharacter.int = 8
        myCharacter.wis = 14
        myCharacter.cha = 10
    elif myCharacter.charClass == 'paladin':
        myCharacter.hp = 10
        myCharacter.str = 14
        myCharacter.dex = 8
        myCharacter.con = 13
        myCharacter.int = 10
        myCharacter.wis = 12
        myCharacter.cha = 15
    elif myCharacter.charClass == 'ranger':
        myCharacter.hp = 10
        myCharacter.str = 15
        myCharacter.dex = 14
        myCharacter.con = 12
        myCharacter.int = 8
        myCharacter.wis = 10
        myCharacter.cha = 13
    elif myCharacter.charClass == 'rogue':
        myCharacter.hp = 8
        myCharacter.str = 13
        myCharacter.dex = 15
        myCharacter.con = 12
        myCharacter.int = 10
        myCharacter.wis = 8
        myCharacter.cha = 14
    elif myCharacter.charClass == 'sorcerer':
        myCharacter.hp = 6
        myCharacter.str = 8
        myCharacter.dex = 10
        myCharacter.con = 15
        myCharacter.int = 14
        myCharacter.wis = 12
        myCharacter.cha = 13
    elif myCharacter.charClass == 'warlock':
        myCharacter.hp = 8
        myCharacter.str = 8
        myCharacter.dex = 10
        myCharacter.con = 14
        myCharacter.int = 15
        myCharacter.wis = 13
        myCharacter.cha = 12
    elif myCharacter.charClass == 'wizard':
        myCharacter.hp = 6
        myCharacter.str = 8
        myCharacter.dex = 10
        myCharacter.con = 13
        myCharacter.int = 15
        myCharacter.wis = 14
        myCharacter.cha = 12


##### Race Base Stats, adds stats to character stats #####
def setRacials():
    if myCharacter.charRace == 'aarakocra':
        myCharacter.dex += 2
        myCharacter.wis += 1
    elif myCharacter.charRace == 'dragonborn':
        myCharacter.str += 2
        myCharacter.cha += 1
    elif myCharacter.charRace == 'dwarf':
        myCharacter.con += 2
    elif myCharacter.charRace == 'elf':
        myCharacter.dex += 2
    elif myCharacter.charRace == 'gnome':
        myCharacter.int += 2
    elif myCharacter.charRace == 'goliath':
        myCharacter.str += 2
        myCharacter.con += 1
    elif myCharacter.charRace == 'halfling':
        myCharacter.dex += 2
    elif myCharacter.charRace == 'human':
        myCharacter.str += 1
        myCharacter.dex += 1
        myCharacter.con += 1
        myCharacter.int += 1
        myCharacter.wis += 1
        myCharacter.cha += 1
    elif myCharacter.charRace == 'tiefling':
        myCharacter.int += 1
        myCharacter.cha += 2


##### Calculate Modifiers for each stat #####
def modCalc():
    ### Takes the stat and subtracts 10, then divides by 2 to get the modifier ###
    myCharacter.strMod = (myCharacter.str - 10) / 2
    myCharacter.dexMod = (myCharacter.dex - 10) / 2
    myCharacter.conMod = (myCharacter.con - 10) / 2
    myCharacter.intMod = (myCharacter.int - 10) / 2
    myCharacter.wisMod = (myCharacter.wis - 10) / 2
    myCharacter.chaMod = (myCharacter.cha - 10) / 2


##### Calculate Hit Points(HP) #####
def hpCalc():
    ### Takes the base HP and adds it to the constitution modifier ###
    myCharacter.hp = myCharacter.hp + myCharacter.conMod


##### Calculate Armor Class(AC) #####
def acCalc():
    ### Takes the base AC and adds it to the dexterity modifier ###
    myCharacter.ac = myCharacter.ac + myCharacter.dexMod


##### Print Out Character Info #####
def printChar():
    qPrint1 = f"You're ready to go, {myCharacter.playerName}!\n"
    qPrint2 = f"Here is your character, {myCharacter.charName} the {myCharacter.charRace} {myCharacter.charClass}'s stats\n"
    for character in qPrint1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in qPrint2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print("###########################################")
    print(f"Player Name: {myCharacter.playerName.capitalize()}")
    print(f"Character Name: {myCharacter.charName.capitalize()}")
    print(f"Class: {myCharacter.charClass.capitalize()}")
    print(f"Race: {myCharacter.charRace.capitalize()}")
    print(f"Hit Points: {int(myCharacter.hp)}")
    print(f"Armor Class: {int(myCharacter.ac)}")
    print(
        f"Strength: {myCharacter.str} with a modifier of {int(myCharacter.strMod)}")
    print(
        f"Dexterity: {myCharacter.dex} with a modifier of {int(myCharacter.dexMod)}")
    print(
        f"Constitution: {myCharacter.con} with a modifier of {int(myCharacter.conMod)}")
    print(
        f"Intelligence: {myCharacter.int} with a modifier of {int(myCharacter.intMod)}")
    print(
        f"Wisdom: {myCharacter.wis} with a modifier of {int(myCharacter.wisMod)}")
    print(
        f"Charisma: {myCharacter.cha} with a modifier of {int(myCharacter.chaMod)}")
    print("###########################################")


##### Selects a random race and class #####
def randChar():
    myCharacter.charRace = random.choice(validRaces)
    myCharacter.charClass = random.choice(validClasses)


##### Runs Random Character Generator #####
def randomCharGen():
    os.system('clear')
    nameCollector()
    charNameCollector()
    randChar()
    setClassTemplate()
    setRacials()
    modCalc()
    hpCalc()
    acCalc()
    printChar()


##### Runs Character Creator #####
def launchCreator():
    os.system('clear')
    nameCollector()
    charNameCollector()
    classCollector()
    raceCollector()
    modCalc()
    hpCalc()
    acCalc()
    printChar()


mainMenu()
