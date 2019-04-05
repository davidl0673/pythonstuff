#fav blah blah
import os
favorite_colors = []
while True:
    user_color = input(" give me one of your favorite colors or type 'stop': ")
    if user_color.lower() == 'stop':
        break
    favorite_colors.append(user_color.lower())

os.system('clear')

favorite_colors = ['blue', 'red']
color_guesses = []
while len(color_guesses ) < len(favorite_colors ):
    one_more_guess = input(f"guess one of my {len(favorite_colors)} favorite colors")
    color_guesses.append(one_more_guess.lower())
favorite_colors.sort()
color_guesses.sort()
print(favorite_colors)
print(color_guesses)
if favorite_colors == color_guesses:
    print("correct")
else:
    print("nice try!")
