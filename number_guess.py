import random
print(' hello what is your name?')
name = input()
print (' well ,'+ name + 'i am thinking of a number between one and 20')
secretnumber = random.randint(1, 20)

for guessestaken in range (1,7):
    print('take a guess.')
    guess = int(input())

    if guess < secretnumber:
        print ('your guess is to low')
    elif  guess > secretnumber:
        print('your guess is too high')
    else:
        break

if guess == secretnumber:
    print(' good job,'+ name +' ! you gussed my number in ' + str(guessestaken) + 'guesses!')
print ('nope, the number i was thinking of was ' + str( secretnumber))

 # DEBUG:
