# 5-6 Stages of Life Exercise
age = 68

if age < 2:
    print("This person is a baby.")
elif age <= 4:  # equivalent to 2 <= age <= 4
    print("This person is a toddler.")
elif age <= 13: # equivalent to 4 < age <= 13
    print("This person is a kid.")
elif age <= 20: # equivalent to 13 < age <= 20
    print("This person is a teenager.")
elif age <= 65: # equivalent to 20 < age <= 65
    print("This person is an adult.")
else:
    print("This person is an elder!")
