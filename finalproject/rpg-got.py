#!/usr/bin/python3
"""Edith5959 | Alta3 Research | TLG NDE Cohort
    Game of Thrones Role Playing Game """

# Install imports required
import os   #import os to clear screen
import sys  #import system.exit function

def showInstructions():
    """Show the game instructions when called"""
    #print menu 
    print('''
====================================================================
====================================================================
                  Game of Thrones: Find the Dragonglass 
====================================================================
====================================================================
        Find the DRAGONGLASS  before the White Walkers find you.
                 Be advised- DO NOT GO PAST THE WALL!!!!
====================================================================
====================================================================
    ''')

def showStatus():
    print('''
=====================================================================
Use these commands:
  go [direction: south, east, west, or north]
  get [item]
  use [item]
  talk [person]
=====================================================================
    ''')
    
    """determine the current status of the player"""
    #print the player's current status
    #print('---------------------------')
    print(f"{rooms[currentRoom]['desc']} \n")

    #print the current inventory
    print('This is in your inventory :\n ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
      print('You see ' + rooms[currentRoom]['item'])
    if "item_two" in rooms[currentRoom]:
      print('You see ' + rooms[currentRoom]['item_two'])
    if "person" in rooms[currentRoom]:
        print('You see ' + rooms[currentRoom]['person']['name'])
    print("----------------------------------------------------------------------")


#an inventory you start with
inventory = ["slingshot","Valyrian Steel","sunflower seeds"]

#a dictionary for rooms, movement 
rooms = {
 
            'Winterfell':{
                'desc'  : 'You are in WINTERFELL, the stronghold of the Kings in the North.\n When Aegon the Conqueror invaded Westeros, King Torrhen Stark bent\n the knee when he saw the strength the Targaryens\' commanded, and \n the Starks were retained as the Warden of the North and ruling \n Lords of the North.',
                'south' : 'Highgarden',
                'east'  : 'Kings Landing',
                'west'  : 'Casterly Rock',
                'north' : 'The Wall',
                'item'  : 'direwolves',
                'item_two' : 'figs',
                'person': {'name': 'Bran',
                    'dialogue': 'Bran: "An endless night. He wants to erase this world,\n and I am its memory. Find the dragonglass."'},
                },
            
            'Highgarden' : {
                  'desc'  : 'HIGHGARDEN, the seat of House Tyrell, the regional capital of the \n Reach, and the heart of chivalry in the Seven Kingdoms.\n It lies on the Mander where the ocean road meets the rose road.',
                  'north' : 'Winterfell',
                  'item_two' : 'peaches',
                  },
            'Kings Landing' : {
                  'desc' : 'KINGS LANDING, named after King Baelor Targaryen, is the site of \n the Iron Throne and the Red Keep. \n It is here Daenerys releases her fury.',
                  'west' : 'Winterfell',
                  'person': {'name': 'Robert Baratheon',
                      'dialogue': '"Robert: I swear to you, I was never so alive as when I was winning this throne,\n or so dead as now that I\'ve won it.'
                             },
                  'item' : 'iron throne',

                  },
            'Casterly Rock' : {
                'desc'  : 'CASTERLY ROCK, the seat of House Lannister and the capital of the \n westerlands. It is here that the Unsullied army of House Targaryen with \n the assistance of Tyrion that victory is proclaimed.', 
                'east'  : 'Winterfell',
                'person': {'name':'Tyrion',
                            'dialogue':'We’ve had vicious kings and we’ve had idiot kings,\n but I don’t know if we’ve ever been cursed with a vicious idiot boy king!'},
                'item_two'  : 'grapes',
                },
            'The Wall' : {
                'desc' : 'The WALL, what separates all men from the Night King,\n warded with magic to prevent the dead from crossing over.',
                'south': 'Winterfell',
                'north': 'The First of the First Men',
                'item' : 'dragonglass',
                },
            'The First of the First Men' : {
                'south': 'The Wall',
                'item' : 'White Walkers',
                }
            }
#start this player in Winterfell
currentRoom = 'Winterfell'

os.system("clear")

showInstructions()

#Game loop

while True:
    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    move = ''
    while move == '':  
        move = input('>')

    os.system("clear")
    # split allows an items to have a space on them
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no place to go that way
        else:
            print('You can\'t go that way!')

    #if they type 'use' first
    if move[0] == 'use':
        if move[1] in inventory or ("item_two" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item_two"]):
            if move[1] in ["peaches","figs", "grapes", "sunflower seeds"]:
                print(f"\nYou ate the {move[1]}! How delicious!!")
                #delete the item from the room
                del rooms[currentRoom]['item_two']
            else: # if it's not in your inventory
                print(f"You don't have {move[1]}!")
        elif move[1] in inventory or ("item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]):
            if move[1] in ["direwolves"]:
                print(f"You are now walking with the direwolves!!")
                del rooms[currentRoom]['item']
            else: 
                print(f"You don't have {move[1]}!")
    
    #if they type 'talk' first
    if move[0] == 'talk':
        if "person" in rooms[currentRoom] and move[1].title() in rooms[currentRoom]['person']['name']:
                print(rooms[currentRoom]['person']['dialogue'])
                
    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' acquired!')
            #delete the item from the room
            del rooms[currentRoom]['item']

        elif "item_two" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item_two']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' acquired!')
            #delete item from the room
            del rooms[currentRoom]['item_two']

        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

## Define how a player can win
    if currentRoom == 'The Wall' and 'dragonglass' in inventory:
      print('You have reached The Wall and have found the dragonglass... YOU WIN!')
      break

    ## If a player enters a room with a white walker
    elif 'item' in rooms[currentRoom] and 'White Walkers' in rooms[currentRoom]['item']:
      print('The White Walkers have found you... GAME OVER!')
      break
