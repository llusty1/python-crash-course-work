# Here we will work with a for loop in a list. 
print("For every magician in the list of magicians, print the magicians name. ")
magicians = ["david", "alice", "bowie"] # Define the list
for magician in magicians: # Define a for loop
    print(magician.title()) # Print the results. I added the title() method just to practice using methods.
# Python will repeat lines 3 and 4 until it cycles through all of the names in magicians list.
# Let's display the length of the list for fun:
print("\nWhat is the legth of the list?")
print(len(magicians))

# Now let's create a message using magicians list
magicians = ["david", "alice", "bowie"]
for magician in magicians:
    print(magician.title() + ", that was a great trick. A very excellent trick, like no one has ever seen! ")