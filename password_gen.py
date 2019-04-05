import random
alphebet = 'abcdefghijklmnopqrstuvwxyz'
pw_length = 8
my_pw = ''

for num in range ( 0, pw_length):
    my_pw = my_pw + random.choice(alphebet)
print(my_pw)
