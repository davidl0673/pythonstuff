import random
pattern_list = ['##', '%%', '~~', '||', '//', '\\\\', '&&', '$$']
length = 20
out_string = ''
for num in range ( 0 , length):
    out_string = out_string + random.choice(pattern_list) *5
    out_string = out_string + '\n'
print(out_string)
