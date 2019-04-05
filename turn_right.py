# turn_right.py
import random
directions = ['North', 'South', 'East', 'West']
user_direction = random.randint(0, 3)
print(f"You are facing {directions[user_direction]}")
turn_num = int(input("Turn right how many times? >"))
user_direction = user_direction + turn_num
print(f"Now you are facing {directions[user_direction % 4]}")
