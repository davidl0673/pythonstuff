import random 

def pick6():
    numbers = []
    for i in range(6):
        numbers.append(random.randint(1,99))
    return numbers

def matches(winner, ticket):
    count = 0 

    for i in range (len(winner)):
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


ticket = pick6()

def play_pick6():
    winner = pick6()
    money_spent = 0
    winnings = 0 
    for i in range(100000):
        current = pick6()
        winnings = winnings + matches(winner, current)
        money_spent = money_spent + 2 
        roi = (winnings - money_spent) / money_spent
    

    print(f'you won {winnings} \nyou  spent {money_spent}, \nyour roi was {roi}')
play_pick6()