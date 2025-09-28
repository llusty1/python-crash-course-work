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
# It seems that there can only be two guests I can invite to dinner
print("I can only invite two guests to dinner.")
print(guest)
popped_guest1 = guest.pop()
print(popped_guest1)
popped_guest2 = guest.pop()
print(popped_guest2)   
popped_guest3 = guest.pop(0)
print(popped_guest3)
popped_guest4 = guest.pop(1)
print(popped_guest4)
print(guest)
print(message1)
print(message3)
del(guest[0]) # Here we del the guest at position 0
del(guest[0]) # After that the guest onlky guest that's left occupies position 0. So we delete this guest to give us an empty list. 
print(guest) # Here is proof that the listis empty. 