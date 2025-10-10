foods = ("Eggs", "Toast", "Bacon", "Bagels", "Sausage")
print("Food Menu: ")
for food in foods:
    print(food)
drinks =("Coffee", "Tea", "Water")
print("\nDrink Menu: ")
for drink in drinks:
    print(drink)

# Now let's modify the tuple:
print("\nThe original menu is:")
for food in foods:
    print(food)

print("\nThe Menu is now:")
foods =("Eggs", "Sausage", "Toast", "Oatmeal")
for food in foods:
    print(food)