#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)
#The first line should collect and store input from the user. Ask the user for the 'vendor name' associated with the device. Use any variable name you would like.
#Use a second line of code to print the input you just collected from the user.

#collect string input from the user

user_input_vendor = input("Please enter your vendor name associated with your device.:")
print("You told me your device name is:", user_input_vendor)

main()

