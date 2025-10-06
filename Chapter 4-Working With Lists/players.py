# Here we will create a list of players and then slice the list using their index position.
players = ["Agnes", "Agatha", "Jermaine", "Jack", "Biz" ] # Just having a friend couldn't be no crime
print(players[0:4]) # Cause I've got friends and that's a fact like:
print(players[1:4])
print(players[:4])
print(players)
print(players[2:])
print(players[-3:])
# Now let's print out the first three players using a for loop. 
print("\nHere are the first three players on my team:")
for player in players[:3]: # Instead of looping through the entire list Python loops through only the first three names.
    print(player.title())