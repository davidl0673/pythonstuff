import random
baby_sounds = ['ba' , 'ma' , 'da']

length = 10
out_string = ' '
for num in range (0, length):
    out_string = out_string + random.choice(baby_sounds)
print(out_string)
