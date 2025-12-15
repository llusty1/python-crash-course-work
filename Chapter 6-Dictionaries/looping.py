# Here we will create dictionaries to learn how to loop through them
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value.title())