#!/usr/bin/env python3
import requests
import wget

# props to Shawn for the solution!

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

def main():
    choice= input("Enter a movie title:\n>")

    full_url= URL + choice

    movies= requests.get(full_url).json()

    count = 0
    for x in movies['Search']:
        if x['Type'] == 'movie':
            print(f"{x['Title']} was released in {x['Year']}")

            if count == 0:
                poster_url = x['Poster']
                wget.download(poster_url, "/home/student/static/")
                print(f"Downloaded first movie poster for {x}.")
                count += 1

main()
