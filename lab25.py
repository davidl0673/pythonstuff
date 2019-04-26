class Atm:

    

    def __init__(self):
        self.balance = 0
        self.transactions = []

    # def use_atm(self, amount):
    #     input
    #         if input == 'deposit':
    #             input('enter dollar amount'):
    #                 self.transactions.append(f'user deposited ${amount}')
    #         else:
    #             print('try agian'):
    #                 return
        
    def deposit(self, amount):
        self.balance += amount 
        self.transactions.append(f'user deposited ${amount}')

    def withdrawl( self, amount):
        self.balance -= amount
        self.transactions.append(f'user withdrew ${amount}')

    def check_withdrawl(self, amount):
        return self.balance - amount >= 0
   
    def check_balance(self):
        return self.balance
    
    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)
    

atm = Atm()
atm.deposit(0)
atm.withdrawl(0)
print(atm.balance)
balance = atm.balance
transactions = atm.transactions
while True:
    action = input('would you like to deposit, withdraw, check_balance, history?')
    if action == 'deposit':
        amount = input('enter and amount')
        atm.deposit(int(amount))
        print(f'your balance is {atm.balance}')
    
    elif action == 'withdraw':
        amount = input('how much would you like to withdrawl?')
        atm.balance - int(amount)
        print(f'your balance is {atm.balance}')

    elif action == 'check balance':
        print(f'your balance is { balance}')

    elif action == 'history':
        print(f'your transactions are {transactions}')
    
    
    
    
    else:
        print('try agian')

         

        

    