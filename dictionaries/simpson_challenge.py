#!/usr/bin/env/ python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

#We want to print: My eyes! The goggles do nothing!


chall_eyes= challenge[2][1]
chall_goggles= challenge[2][0]
chall_nothing= challenge[3]

print(f"My {chall_eyes}! The {chall_goggles} do {chall_nothing}!")


trial_eyes= trial[2]["goggles"]
trial_goggles= trial[2]["eyes"]
trial_nothing= trial[3]


print(f"My {trial_eyes}! The {trial_goggles} do {trial_nothing}!")

night_eyes= nightmare[0]["user"]["name"]["first"]
night_goggles= nightmare[0]["kumquat"]
night_nothing= nightmare[0]["d"]

print(f"My {night_eyes}! The {night_goggles} do {night_nothing}!")
