# This exercise is to create a list of at least 3 people you'd like to invite to dinner.
guest = ["Michael Jordan", "Shaquille O'Neal", "Charles Barkley",]
# Now let's create a message to each guest that you'd like to invite.
message1 = "Dear Mr. " + guest[0] + " we humbly invite you to dinner. "
print(message1)
message2 = "Dear Mr. " + guest[1] + " we humbly invite you to dinner. "
print(message2)
message3 = "Dear Mr. " + guest[2] + " we humbly invite you to dinner. " 
print(message3)
# This took me a minute, I will learn if there is a more efficient way of doing this. 
# Someone can't make it to dinner!
print("\nShaquille O'Neal can't make it. Darn")
print("I guess we will have to invite someone else.")
guest.remove("Shaquille O'Neal") # Here we used the remove() method to get rid of the variable by it's value.
guest.append("David Robinson")
message4 = "Dear Mr. " + guest[2] + " we humbly invite you to dinner."
print(message1)
print(message3)
print(message4)
# We have found a bigger table! Time to invite 3 more guests!
guest.insert(0, "Dirk Nowitzki")
guest.insert(2, "Larry Bird")
guest.append("Ron Artest")
print(guest)

# Now let's invite all of the guests we have!
message0 = ("Dear Mr. " + guest[0] + " we humbly invite you to dinner. ")
message2 = ("Dear Mr. " + guest[2] + " we humbly invite you to dinner. ")
message5 = ("Dear Mr. " + guest[5] + " we humbly invite you to dinner. ")
print(message0)
print(message2)
print(message5)