marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

char_name= input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n>")

#save the answer to a variable
character_answer = input("Sorry, which character again?")

#display answer 
print("You chose " + character_answer)

char_stat= input("What statistic do you want to know about? (real name, powers, archenemy)")

print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")
