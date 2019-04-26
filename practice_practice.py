ones = {1 : "One", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine"}
outliers = {10 : "Ten", 11 : "Eleven", 12 : "Twelve", 13 : "Thirteen", 14 : "Fourteen", 15 : "Fifteen", 16 : "Sixteen", 17 : "Seventeen", 18 : "Eighteen", 19 : "Nineteen"}
tens = {2 : "Twenty", 3 : "Thirty", 4 : "Forty", 5 : "Fifty", 6 : "Sixty", 7 : "Seventy", 8 : "Eighty", 9 : "Ninety"}

def conversion():
    #Get input from user
    number = input("Please type a number between 1 and 999 ")
    #find out what kind of pain this number is going to be
    #If it is between 20 and 99 use this loop
    if int(number) >= 100 and int(number) <= 999:
        hundreds_digit = int(number)//100
        tens_digit = (int(number)//10)%10
        ones_digit = int(number)%10
        if tens_digit == 1:
            nightmare = str(tens_digit) + str(ones_digit)
            print(f"{ones[hundreds_digit]}-hundred {outliers[int(nightmare)]}") 
        elif ones_digit != 0:
            print(f"{ones[hundreds_digit]}-hundred {tens[tens_digit]}-{ones[ones_digit]}")
        else:
            print(f"{ones[hundreds_digit]}-hundred {tens[tens_digit]}")  
    elif int(number) >= 20 and int(number) <= 99:
        tens_digit = int(number)//10
        ones_digit = int(number)%10
        #Check to see if it a multiple of 10
        if ones_digit > 0:
            print(f"{tens[tens_digit]}-{ones[ones_digit]}")
        else:
            print(f"{tens[tens_digit]}")
    #Check if it is an off one with a special name
    elif int(number) >= 10 and int(number) <= 19:
        print(f"{outliers[int(number)]}") 
    #Check if it is a single digit
    elif int(number) <= 9:
        print(f"{ones[int(number)]}")
    #Must be out of bounds, return an error
    else:
        print(f"Sorry {number} is not a valid choice.")

conversion()