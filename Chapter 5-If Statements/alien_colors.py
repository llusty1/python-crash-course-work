# Alien colors exercise
alien_colors = ["green", "yellow", "red"]
if "green" in alien_colors:
    print("You have earned 5 points!")
elif "blue" in alien_colors:
    print("You have earned 10 point!")
elif "yellow" in alien_colors: # Even though yellow is in the list it doesn't work becaues elif rules.
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