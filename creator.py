# DnD 5th Edition Character Creator
# Mason Ferucci
# Programming Logic and design
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
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.pro = 0
        self.walk = 0

    # def addPoint(self, amount):
    #     self.str += amount


myCharacter = playerChar()


def mainSection():
    option = input("> ")
    if option.lower() == ("create"):
        launchCreator()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['create', 'quit']:
        print("Please enter a valid option")
        option = input("> ")
        if option.lower() == ("create"):
            launchCreator()
        elif option.lower() == ("quit"):
            sys.exit()


def mainMenu():
    os.system('clear')
    print('###########################################')
    print('# Welcome to the DnD 5E Charactor Creator #')
    print('###########################################')
    print('                 • Create •                ')
    print('                 •  Quit  •                ')

    mainSection()


def nameCollector():
    ##### Collect Players Name #####
    qPlayerName = "Hello, what's your name?\n"
    for character in qPlayerName:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input("> ")
    myCharacter.playerName = playerName


def classCollector():
        ##### Collect Players Class Choice #####
    qClass = f"Hello {myCharacter.playerName}, what class do you want to be?\n"
    qClassDef = "(You can be a Barbarian, Bard, Cleric, Druid, Figther, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, or Wizard)\n"

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

    # Valid Class choice options
    validClasses = ['barbarian', 'bard', 'cleric', 'druid', 'fighter',
                    'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']
    if playerClass.lower() in validClasses:
        myCharacter.charClass = playerClass.lower()
        print(f"You are now a {playerClass}!\n")
    while playerClass.lower() not in validClasses:
        print("Please enter a valid class")
        playerClass = input("> ")
        if playerClass.lower() in validClasses:
            myCharacter.charClass = playerClass.lower()
            print(f"You are now a {playerClass}!\n")

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


def raceCollector():
    ##### Collect Players Race Choice #####
    qRace = f"Hello {myCharacter.playerName} you want to be {myCharacter.charClass}, what race do you want to be?\n"
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

    # Valid Race choice options
    validRaces = ['aarakocra', 'dragonborn', 'dwarf', 'elf', 'gnome',
                  'goliath', 'halfling', 'human', 'tiefling']
    if playerRace.lower() in validRaces:
        myCharacter.charRace = playerRace.lower()
        print(f"You are now a {playerRace}!\n")
    while playerRace.lower() not in validRaces:
        print("Please enter a valid race")
        playerRace = input("> ")
        if playerRace.lower() in validRaces:
            myCharacter.charRace = playerRace.lower()
            print(f"You are now a {playerRace}!\n")

    ### Race Base Stats ###
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

def charNameCollector():
    ##### Collect Character Name #####
    qGreet = f"So, {myCharacter.playerName} you are a {myCharacter.charRace} {myCharacter.charClass}...\n What do you want your characters name to be? \n"
    for character in qGreet:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    charName = input("> ")
    myCharacter.charName = charName

def hpCalc():
    myCharacter.hp =  myCharacter.hp + (myCharacter.hp + myCharacter.con - 10) / 2


def launchCreator():
    os.system('clear')
    nameCollector()
    classCollector()
    raceCollector()
    charNameCollector()
    hpCalc()

    

    ##### Print Out Character Info #####

    qPrint1 = f"You're ready to go, {myCharacter.playerName}!\n"
    qPrint2 = f"Here is your character, {myCharacter.charName}'s the {myCharacter.charRace} {myCharacter.charClass}'s stats\n"
    for character in qPrint1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in qPrint2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print("#############################")
    print(f"Player Name: {myCharacter.playerName}")
    print(f"Character Name: {myCharacter.charName}")
    print(f"Class: {myCharacter.charClass}")
    print(f"Race: {myCharacter.charRace}")
    print(f"Hit Points: {int(myCharacter.hp)} plus Constitution Modifier")
    print(f"Strength: {myCharacter.str}")
    print(f"Dexterity: {myCharacter.dex}")
    print(f"Constitution: {myCharacter.con}")
    print(f"Intelligence: {myCharacter.int}")
    print(f"Wisdom: {myCharacter.wis}")
    print(f"Charisma: {myCharacter.cha}")
    print("#############################")


mainMenu()
