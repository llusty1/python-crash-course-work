# Here is a dictionary a Similar Objects:
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

print("Sarah's favorite language is " + 
      favorite_languages["sarah"].title() + 
      ".\n")


#Here we will loop through the dictionary that's been created:
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")

#Let's put a line break here:
print()

# Looping through all the Key in a Dictionary:
for name in favorite_languages.keys():
    print(name.title())

# Another line break:
print()

# Now let's write a message to each person in the dictionary:
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() +
              " I see your favorite language is " + 
              favorite_languages[name].title() + "!")
        
# Now let's loop through and add a message to a friend who isn't a key in the dictionary:
if "erin" not in favorite_languages.keys():
    print("\nErin, please take our poll!\n") # Notice the line break in this line of code. 

# Looping through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking our poll.")

# Looping through the values in a dictionary:
print("\nThese languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())