# Let's create a list of dictionaries
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10 }
alien_2 = {"color": "red", "points": 15}
#Now let's nest those dictionaries:
aliens = [alien_0, alien_1, alien_2]
# A little for loop to print the dictionaries:
for alien in aliens:
    print(alien)