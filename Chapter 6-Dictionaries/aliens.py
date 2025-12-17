# Let's create a list of dictionaries
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10 }
alien_2 = {"color": "red", "points": 15}
#Now let's nest those dictionaries in a list:
aliens = [alien_0, alien_1, alien_2]
# A little for loop to print the dictionaries:
for alien in aliens:
    print(alien)

# Now let's create an empty list:
aliens = []

# Make 30 green aliens:
for alient_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append("new_alien")

# Show first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# Let's show how many aliens have been created:
print("Total number of aliens: " + str(len(aliens)))