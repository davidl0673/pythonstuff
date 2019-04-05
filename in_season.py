# in_season.py
import random
food_list = ['jam', 'toast']
ingredient_list = ['strawberries', 'avacado']
user_food = input("What food would you like to make, {food_list[0]} or {food_list[1]}? >").lower()
while user_food not in food_list:
    user_food = input("What food would you like to make, {food_list[0]} or {food_list[1]}? >").lower()
in_season = random.choice(ingredient_list)
print(f"{in_season.capitalize()} are in season.")
if in_season == 'strawberries':
    if user_food == 'jam':
        print("Time to make jam!")
    if user_food == 'toast':
        print("Can't make avacado toast!")
else:
    if user_food == 'jam':
        print("No berries right now!")
    if user_food == 'toast':
        print("Avacado toast, yum! :)")
