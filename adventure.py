## Task 1: Code Correction

# Buggy

#place = input("Choose a place: forest or cave? ")

#if place = "forest":
 #   action = input("climb a tree or cross a river?")
 #   if action = "climb a tree":
  #      print("You found a bird's nest!")
  #  else action = "cross a river":
 #       print("You found a boat!")
#   elif place = "cave":
 #   print("You find a hidden treasure!")

# Corrected
    
place = input("Choose a place: forest or cave? ")

if place == "forest": # Fix comparison operators
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": # Elif should be here
        print("You found a boat!")
else: # Else should be here / removed unnecessary comparison
    print("You find a hidden treasure!")

### Task 2 Setting the Scene

#  Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch"
#  or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest": 
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": 
        print("You found a boat!")
elif place == "cave": 
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Good idea, this cave is very dark, and now you can see.")
    elif action == "proceed in the dark":
        print("You might want to reconsider, as you'll probably need a torch!")
    else:
        print("You must choose between the torch and the dark!")
else:
    pass

# Task 3: Default Path

#If the user makes an invalid choice at any point, incorporate a pass statement to handle it.
#  HINT: How can an else statement be of use here?

place = input("Choose a place: forest or cave? ")

if place == "forest": 
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": 
        print("You found a boat!")
    else:
        pass
elif place == "cave": 
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Good idea, this cave is very dark, and now you can see.")
    elif action == "proceed in the dark":
        print("You might want to reconsider, as you'll probably need a torch!")
    else:
        pass
else:
    pass