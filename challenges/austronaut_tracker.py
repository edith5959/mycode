#!/usr/bin/python3

import requests

URL= "http://api.open-notify.org/astros.json"

#This dictionary only has 3 keys

def main():
    # requests.get() requests info from the URL
    # .json() method transforms that data into a Pythonic dictionary!
    sliceme= requests.get(URL).json()

    print(sliceme)
    print(type(sliceme))

#print People in Space:
   # for x in sliceme[int('number')]:
       # print(f"People in space: " + {x}) 

    print(sliceme["people"]) #This will give you thepeople
    input()
    print(sliceme["people"][0]) 
    input()
    print(sliceme["people"][0]["name"])

    for every_dict in sliceme["people"]:
        print(every_dict["name"] "is on the " + every_dict["craft"])

main()


#print People in Space:  7

#print Raja Chari is on the ISS
#print Tom Marshburn is on the ISS
#print Kayla Barron is on the ISS
#print Matthias Maurer is on the ISS
#print Oleg Artemyev is on the ISS
#print Denis Matveev is on the ISS
#print Sergey Korsakov is on the ISS
