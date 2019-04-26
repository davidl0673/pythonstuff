card_dict = {'a':1,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 , '10':10 ,'j':10, 'q':10, 'k':10}

card1 = input('pick a card a,1,2,3,4,5,6,7,8,9,10,q,k,a:')
card2 = input('pick another card')
card3 = input('pick one last card')

def card_calulate():
    cardtotal = (card_dict[card1] + card_dict[card2] + card_dict[card3])
    if cardtotal == 21:
        print('blackjack!!')
     elif cardtotal <= 17:
        print('hit!')
    elif cardtotal >= 17 and cardtotal <= 21:
        print('stay')
    return

card_calulate()


#generate a both possible li