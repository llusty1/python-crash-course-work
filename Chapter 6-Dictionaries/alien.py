# Let's start by creating a dictionary
alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

# When you shoot down an Alien it prints the following:
alien_0 = {"color": "green", "points":5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Alien position, but first let's print the dictionary associated with said Alien
alien_0 = {"color": "green", "points":5}
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Let's start with an empty dictionary
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)

# Let's modify a dictionary, below is an example of the changing of the key/value pair.
alien_0 = {"color": "green"}
print("The alien is " + alien_0["color"] + ".")

alien_0["color"] = "yellow"
print("The alien is now " +alien_0["color"] + ".")