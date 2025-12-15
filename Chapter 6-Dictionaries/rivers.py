# Let's create a dictionary of three rivers and then loop them:
rivers = {"Nile": "Egypt",
          "Trinity": "USA",
          "Shinano": "Japan"
          }
print(rivers)
print()
# Now let's list the keys
for key in rivers.keys():
    print(f"River: {key}")
print()
# Now let's list the values:
for value in rivers.values():
    print(f"Country: {value}")
print()
# Now let's write a sentence about each item
for key, value in rivers.items():
    print(f"The {key} runs through {value}.")