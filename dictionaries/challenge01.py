#!/usr/bin/env python3

def main():

    pokedex={"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}

    #pokedex=["Pickachu"]= "Electric"
    pokedex["Pikachu"]= "Electric"
    choice= input("Name a Generation 1 starter Pokemon:\n>")

    print(pokedex.get(choice, "Sorry, we don't have any record of that Pokemon!"))
    print(pokedex.keys())
    print(pokedex.values())

main()
