ones = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', }
teens = {10:'ten', 11:'eleven',12:'twelve',  14:'fourteen',15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',19:'nineteen'}
tens = {2:'twenty',3:'thirty', 4:'fourty', 5:'fifty',6:'sixty',7:'seventy',7:'seventy',7:'seventy',8:'eighty',9:'ninety'}


 

def numbers_words(number):
    tens_digit = number // 10
    ones_digit = number % 10
    hundreds = number // 100 
            
    if number < 10:
        print(ones[number])
    elif number >= 10 and number < 20:
        print(teens[number]) 
    elif number >=20 and number < 100:
        print(tens[tens_digit] + ones[ones_digit])
    elif number >=100 and number <1000: 
        print(ones[hundreds] + ' hundred' +
        

numbers_words(639)

