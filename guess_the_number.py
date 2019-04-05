import random
guess = random.randint(1,10)
while  True:
    user_guess = input('guess a number between 1 and 10!')
    (f"{(guess)} == {user_guess}")
    if int(user_guess) == guess:
        print('you guessed correct!')
        break
    else:
        print('try again')
