# Alien colors exercise #1
alien_colors = ["green", "yellow", "red"]
if "green" in alien_colors:
    print("You have earned 5 points!")
elif "blue" in alien_colors:
    print("You have earned 10 point!")
elif "yellow" in alien_colors: # Even though yellow is in the list it doesn't run because the first if statement passed the conditional so the loop stopped running
    print("Yellow is mellow.")

print("Lil' Flip says game over.")

# Here we will correct the above code and make it work properly
alien_colors = ["green", "yellow", "red"]
if "green" in alien_colors:
    print("\nYou have earned 5 points!")
if "blue" in alien_colors:
    print("You have earned 10 points!")
if "yellow" in alien_colors: # If statement works in this loop where elif fails. 
    print("Yellow is mello.")

print("Lil' Flip says game over.")

# Alien colors exercise #2
alien_colors = ["green","yellow", "red"]
if "green" in alien_colors:
    print("\nYou have earned 5 points!")
else:
    print("\nYou have earned 10 points!")

alien_colors = ["green", "blue", "red"]
if "green" in alien_colors:
    print("\nYou have earned 5 points Green!")
if "blue" in alien_colors:
    print("You have earned 10 points Blue!")
if "red" in alien_colors:
    print("You have earned 20 points Red!")

# Alien colors exercise #3
alien_colors = ["green", "blue", "red"]
if "green" in alien_colors:
    print("\nYou have earned 5 points Green!")
if "blue" in alien_colors:
    print("You have earned 10 points Blue!")
if "red" in alien_colors:
    print("You have earned 15 points Red!")

alien_colors = ["green", "blue", "red"]
if "green" in alien_colors:
    print("\nYou have earned 5 points Green!")
elif "blue" in alien_colors:
    print("You have earned 15 points Blue!")
elif "red" in alien_colors:
    print("You have earned 15 points Red!")
else:
    print("You have zero points!")

color = "green"
if "green" in color:
    print("\nYou have earned 5 points Green!")
if "blue" in color:
    print("\nYou have earned 10 points Blue!")
if "red" in color:
    print("\nYou have earned 15 points Red!")

color = "blue"
if "green" in color:
    print("You have earned 5 points Green!")
if "blue" in color:
    print("You have earned 10 points Blue!")
if "red" in color:
    print("You have earned 15 points Red!")

color = "red"
if "red" in color:
    print("You have earned 5 points Green!")
if "blue" in color:
    print("You have earned 10 points Blue!")
if "red" in color:
    print("You have earned 15 points Red!")
print("Thanks for playing!")