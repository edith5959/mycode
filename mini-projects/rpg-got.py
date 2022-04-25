#!/usr/bin/python3
"""Edith5959 | Alta3 Research
    Creating a simple Role Playing Game """

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game of finding dragonglass 
    to defeat the White Walkers
    ===================================
    Find the dragonglass before the 
    White Walkers find you. Be advised-
    DO NOT GO PAST THE WALL!!!!
    ==================================
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print('You are in ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
      print('You see ' + rooms[currentRoom]['item'])
    if "item_two" in rooms[currentRoom]:
      print('You see ' + rooms[currentRoom]['item_two'])
    print("---------------------------")


#an inventory you start with
inventory = ["slingshot","Valyrian Steel","sunflower seeds"]

#a dictionary linking a room to other rooms
rooms = {

            'Winterfell' : {
                'south' : 'Highgarden',
                'east'  : 'Kings Landing',
                'north' : 'The Wall',
                'item'  : 'direwolves',
                'item_two' : 'figs',
                },

            'Highgarden' : {
                  'north' : 'Winterfell',
                  'item'  : 'golden roses',
                  'item_two' : 'peaches',
                  },
            'Kings Landing' : {
                  'west' : 'Winterfell',
                  'item' : 'iron throne',
                  },
            'Casterly Rock' : {
                'east' : 'Winterfell',
                'item'  : 'tyrion',
                },
            'The Wall' : {
                'south': 'Winterfell',
                'north': 'The First of the First Men',
                'item' : 'dragonglass',
                },
            'The First of the First Men' : {
                'south': 'The Wall',
                'item' : 'White Walkers',
                }
            }
#start thi player in Winterfell
currentRoom = 'Winterfell'

showInstructions()

#loop forever
while True:
    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>')

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

        # two ifs here... I think this is the same as that warmup we had the other day

        elif "item_two" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item_two']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' acquired')
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
