# candy_betting.py
import random
user_pennies = random.randint(200, 300)
user_candy = 0
while True:
    print(f"You have {user_pennies} pennies and {user_candy} candy.")
    user_choice = input("Would you like to (bet) or (cash out) >")
    while user_choice not in ['bet', 'cash out']:
        user_choice = input("Would you like to (bet) or (cash out) >")
    if user_choice == 'cash out':
        break
    bet_amount = int(input("How many quarters would you like to bet >"))
    if user_pennies < bet_amount * 25:
        continue
    if random.randint(0, 1) == 0:
        print("You won!")
        user_candy = user_candy + bet_amount
    else:
        print("You lost!")
        user_pennies = user_pennies - (25 * bet_amount)
print("Cashing out")
user_candy = user_candy + (user_pennies // 25)
user_pennies = user_pennies % 25
print(f"You have {user_candy} candy and {user_pennies} pennies left over.")
