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