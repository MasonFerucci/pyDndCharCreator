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

    def addPoint(self, amount):
        self.str += amount


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


def launchCreator():
    os.system('clear')

    ##### Collect Players Name #####
    qPlayerName = "Hello, what's your name?\n"
    for character in qPlayerName:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input("> ")
    myCharacter.playerName = playerName

    ##### Collect Players Class Choice #####
    qClass = f"Hello {playerName}, what class do you want to be?\n"
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
        myCharacter.charClass = playerClass
        print(f"You are now a {playerClass}!\n")
    while playerClass.lower() not in validClasses:
        playerClass = input("> ")
        if playerClass.lower() in validClasses:
            myCharacter.charClass = playerClass
            print(f"You are now a {playerClass}!\n")

    ### Class Base Stats ###
    if myCharacter.charClass == 'barbarian':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'bard':
        myCharacter.hp = 0
        myCharacter.str = 50
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 22
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'cleric':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'druid':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'fighter':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'monk':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'paladin':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'ranger':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'rogue':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'sorcerer':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'warlock':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0
    elif myCharacter.charClass == 'wizard':
        myCharacter.hp = 0
        myCharacter.str = 0
        myCharacter.dex = 0
        myCharacter.con = 0
        myCharacter.int = 0
        myCharacter.wis = 0
        myCharacter.cha = 0
        myCharacter.pro = 0
        myCharacter.walk = 0

    ##### Collect Players Race Choice #####
    qRace = f"Hello {playerName} the {playerClass}, what race do you want to be?\n"
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
        myCharacter.charRace = playerRace
        print(f"You are now a {playerRace}!\n")
    while playerRace.lower() not in validRaces:
        playerRace = input("> ")
        if playerRace.lower() in validRaces:
            myCharacter.charRace = playerRace
            print(f"You are now a {playerRace}!\n")

    ### Race Base Stats ###
    if myCharacter.charRace == 'aarakocra':
        myCharacter.dex = +2
        myCharacter.wis = +1
    elif myCharacter.charRace == 'dragonborn':
        myCharacter.str = +2
        myCharacter.cha = +1
    elif myCharacter.charRace == 'dwarf':
        myCharacter.con = +2
    elif myCharacter.charRace == 'elf':
        myCharacter.dex = +2
    elif myCharacter.charRace == 'gnome':
        myCharacter.int = +2
    elif myCharacter.charRace == 'goliath':
        myCharacter.str = +2
        myCharacter.con = +1
    elif myCharacter.charRace == 'halfling':
        myCharacter.dex = +2
    elif myCharacter.charRace == 'human':
        myCharacter.str = myCharacter.str + 1
        myCharacter.dex = +1
        myCharacter.con += 1
        myCharacter.int = +1
        myCharacter.wis = +1
        myCharacter.cha = +1
    elif myCharacter.charRace == 'tiefling':
        myCharacter.int = +1
        myCharacter.cha = +2

    ##### Collect Character Name #####
    qGreet = f"So, {playerName} the {playerRace} {playerClass}...\n There is one more thing.\n What do you want your characters name to be? \n"
    for character in qGreet:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    charName = input("> ")
    myCharacter.charName = charName

    ##### Print Out Character Info #####

    qPrint1 = f"You're ready to go, {playerName}!\n"
    qPrint2 = f"Here is your character, {charName}'s the {playerRace} {playerClass}'s stats\n"
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
    print(f"Hit Points: {myCharacter.hp}")
    print(f"Strength: {myCharacter.str}")
    print(f"Dexterity: {myCharacter.dex}")
    print(f"Constitution: {myCharacter.con}")
    print(f"Intelligence: {myCharacter.int}")
    print(f"Wisdom: {myCharacter.wis}")
    print(f"Charisma: {myCharacter.cha}")
    print("#############################")


mainMenu()
