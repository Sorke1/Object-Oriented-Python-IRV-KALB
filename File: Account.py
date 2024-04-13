
  # Define a custom exception
class AbortTransaction(Exception): 
    '''Raise this exception to abort a bank transaction.'''
    pass

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            ammount = int(amount)
        except ValueError:
            raise AbortTransaction('must be intiger')
        if ammount<0:
            raise AbortTransaction('Amount must be positive')
        return ammount
    
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            return 'Incorrect password'
        amountToDeposit = self.validateAmount(self, amountToDeposit)
        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            return 'Incorrect password'
        if amountToWithdraw < 0:
            raise AbortTransaction('Amount must be positive')
        if amountToWithdraw > self.balance:
            return 'Insufficient funds'
        self.balance -= amountToWithdraw
        return self.balance

    def get_balance(self, password):
        if password != self.password:
            return 'Incorrect password'
        return self.balance

    def __str__(self):
        return f'Name: {self.name}, Balance: {self.balance}, Password: {self.password}'

# Main program
accounts = []

while True:
    print()
    print('Press f to get the general information')
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    action = input('What do you want to do? ').lower()

    if action == 'f':
        print('Get information')
        user_password = input("Please Enter the password: ")
        for account in accounts:
            if account.password == user_password:
                print(account)
                break
        else:
            print("Your password is incorrect!")

    elif action == 'b':
        print('Get Balance:')
        user_account_number = int(input('Please enter your account number: '))
        user_password = input('Please enter the password: ')
        for account in accounts:
            if account.password == user_password:
                if user_account_number < len(accounts):
                    balance = account.get_balance(user_password)
                    if isinstance(balance, int):
                        print('Your balance is:', balance)
                    else:
                        print(balance)
                    break
                else:
                    print('Invalid account number')
        else:
            print("Your password is incorrect!")

    elif action == 'd':
        print('Deposit:')
        user_account_number = int(input('Please enter your account number: '))
        user_password = input('Please enter the password: ')
        amount_to_deposit = float(input('Please enter the amount to deposit: '))
        for account in accounts:
            if account.password == user_password:
                if user_account_number < len(accounts):
                    result = account.deposit(amount_to_deposit, user_password)
                    if isinstance(result, int):
                        print('Your new balance is:', result)
                    else:
                        print(result)
                    break
                else:
                    print('Invalid account number')
        else:
            print("Your password is incorrect!")

    elif action == 'w':
        print('Withdraw:')
        user_account_number = int(input('Please enter your account number: '))
        user_password = input('Please enter the password: ')
        amount_to_withdraw = float(input('Please enter the amount to withdraw: '))
        for account in accounts:
            if account.password == user_password:
                if user_account_number < len(accounts):
                    result = account.withdraw(amount_to_withdraw, user_password)
                    if isinstance(result, int):
                        print('Your new balance is:', result)
                    else:
                        print(result)
                    break
                else:
                    print('Invalid account number')
        else:
            print("Your password is incorrect!")

    elif action == 'n':
        print('Create a new account:')
        name = input('Enter your name: ')
        balance = float(input('Enter initial balance: '))
        password = input('Enter a password: ')
        accounts.append(Account(name, balance, password))

    elif action == 's':
        print('Show All Accounts:')
        for i, account in enumerate(accounts):
            print('Account', i + 1)
            print(account)

    elif action == 'q':
        break

print('Done')
