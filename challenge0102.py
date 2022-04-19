#!/usr/bin/env python3

icecream= ["indentation", "spaces"]

tlgstudents= ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]

icecream.append(4)

# Include an input asking for a number between 0 and 17
choice= input("Choose a number between 0 and 17: ")

# change the string to an integer
choice= int(choice)

# Use this number to identify one of the students from the tlgstudents list!
name= tlgstudents[choice]
num= icecream[2] # returns 4
spaces= icecream[1] # return "spaces"

# <student_name> always uses <4> <spaces> to indent.
print(f"{name} always uses {num} {spaces} to indent.")


student_name= tlgstudents[choice]

print(student_name + "always uses " + icecream[3] + icecream[1] + "to indent".)

