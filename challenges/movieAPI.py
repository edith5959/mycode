#!/usr/bin/env python3
import requests

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

def main():
    choice= input("Enter a movie title:\n>")

    full_url= URL + choice

    movies= requests.get(full_url).json()
    # this slicing is accurate!! but not necessary
    #title= movies["Search"][str('0')]
    
    #print out the movie names
    for x in movies["Search"]:
        print('>', x["Title"])
        #print(x)

    # the only issue is that you're missing a slice-- watch this
    # movies dict has three keys: Search, totalResults, and Response
    # you have to go through one of those keys FIRST before going after titles

    # x on line 19 is now equal to a movie dictionary-- what's left is to slice x further so you just return the value of "Title"
    # ha, like you already did :)


if __name__ == "__main__":
    main()



