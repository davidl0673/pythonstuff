numlist = '4556737586899855'
card = []

for i in numlist:
    card.append(int(i))

check = card.pop()
card.reverse()
 
print(card)

for i in range(len(card)):
    if i % 2 == 0:
        card[i] *= 2

print(card)
for i in range(len(card)):
    if card[i] > 9:
        card[i] -= 9 
print(card)
addedcard = sum(card)

remmainingnum = addedcard % 10

print(remmainingnum)

if remmainingnum == check:
    print('valid')

    