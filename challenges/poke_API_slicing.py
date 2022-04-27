#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    #print the front_default URL for sprites
    image= pokeapi["sprites"]["front_default"]
    print(f"View the image here: {image}")

    #print out the names of all the selected pokemon moves:
    for x in pokeapi['moves']:
        print(' >', x['move']['name'])
    
  

main()
