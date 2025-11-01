current_users = ["Rob", "Mary-Elizabeth", "Kathryn", "John",  "Lydia"]
new_users = ["John", "Rob", "Johnny", "Fender", "Gibson"]

for new_user in new_users:
    if new_user in current_users:
        print(new_user + " your username is not available.")
    else:
        print(new_user + " you're good to go.")

# Now we will add the list above and print out the current users:
current_users = ["Rob", "Mary-Elizabeth", "Kathryn", "John", "Lydia"]

print("\nCurrent Users: ")
for user in current_users:
    print(user)