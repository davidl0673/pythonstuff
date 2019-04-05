import random
eyes = [';', ':']
noses  = ['@', 'o']
mouths = [')' , '3', '(']
print(random.choice(eyes) + random.choice(noses) + random.choice(mouths))
length = 
out_string = ''
for num in range(0, length):
    out_string = out_string + random.choice(eyes) + random.choice(noses) + random.choice(mouths)
print(out_string)
