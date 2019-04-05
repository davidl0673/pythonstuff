import random 

def pick6():
    numbers = []
    for i in range(6):
        numbers.append(random.randint(1,99))
    return numbers

def matches(winner, ticket):
    count = 0 
    for i in range (len(winner)):
        print(winner[i], ticket[i])
        if winner[i] == ticket[i]:
            count += 1 
    if count == 0:
        return 0
    if count == 1:
        return 4
    if count == 2:
        return 7
    if count == 3:
        return 100
    if count == 4:
        return 50000
    if count == 5:
        return 1000000
    if count == 6:
        return 25000000
    print(matches)


winner = pick6()
ticket = pick6()
won = matches(winner, ticket)

print(won)

def play_pick6():
    money_spent = 0
    winnings = 0 
    for i in range(100000):
        winnings = winnings + won
        money_spent = money_spent + 2 
        print (winnings)
        print (money_spent)
    return

play_pick6()