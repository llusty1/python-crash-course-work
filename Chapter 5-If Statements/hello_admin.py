# Hello Admin Exercise
user_names = ["Admin", "Agness", "Agatha", "Germaine", "Jacq"]

for user in user_names:
    if user == "Admin":
        print("Hello " + user + ", would you like a status report?\n")
    else: 
        print("Hello, " + user + " thank you for logging in.")

# Now we will ad to our code an empty list:
user_names = []

for user in user_names:
    print("Hello, " + user + ", would you like a status report? ")
else:
    print("\nWe've got to find some users!")
