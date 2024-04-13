# Bank Version 2
# Single account
accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    """Create a new account."""
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    """Display account details."""
    global accountName, accountBalance, accountPassword
    print('       Name:', accountName)
    print('       Balance:', accountBalance)
    print('       Password:', accountPassword)
    print()

def getBalance(password):
    """Get account balance."""
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    """Deposit into account."""
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
    try:
        if accountPassword == password:
            accountBalance += int(amountToDeposit)
            return accountBalance
        return None
    except ValueError:
        raise ValueError('Invalid input. Please enter a valid amount.')


def withdraw(amountToWithdraw, password):
    """Withdraw from account."""
    global accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    if password != accountPassword:
        print('Incorrect password for this account')
        return None
    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None
    accountBalance -= amountToWithdraw
    return accountBalance

newAccount("Joe", 100, 'soup')  # create an account

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()
    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()
    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 'w':
        print('Withdraw:')
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 's':
        print('Show Account Details:')
        show()
    elif action == 'q':
        break

print('Done')
