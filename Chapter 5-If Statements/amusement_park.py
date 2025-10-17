# The if-elif-else Chain
age = 12

if age < 4:
    print("Your admission cost is $0.")

elif age < 18:
    print("Your admission cost is $5.")

else:
    print("Your admission cost is $10.")

# Here we will insert the prices inside the chain.
age = 12

if age < 4:
    price = 0

elif age < 18:
    price = 5

else:
    price = 10

print("Your admission cost is $" + str(price) + ".")