accountNamesList = []
accountBalancesList = []
accountPasswordsList = []
accountInfo = []
info = {}


def newAccount(name, balance, password):
  # ... rest of the function
    global accountNamesList, accountBalancesList, accountPasswordsList, accountInfo
    
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)
    info = {'name': name, 'balance': balance, 'password': password}
    accountInfo.append(info)

def getInformation(password):
  global accountInfo
  for acc in accountInfo:
    if acc['password'] == str(password):  # Convert user input to string
      print("Name is {} and balance is {}".format(acc['name'], acc['balance']))
      break
    else:
      print("Your password is incorrect!")



def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if accountNumber < len(accountNamesList):
        print('Account', accountNumber)
        print('       Name:', accountNamesList[accountNumber])
        print('       Balance:', accountBalancesList[accountNumber])
        print('       Password:', accountPasswordsList[accountNumber])
        print()
    else:
        print('Invalid account number')


def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if accountNumber < len(accountPasswordsList) and password == accountPasswordsList[accountNumber]:
        return accountBalancesList[accountNumber]
    print('Incorrect account number or password')
    return None


def deposit(accountNumber, amountToDeposit, password):
    global accountBalancesList, accountPasswordsList
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
    if accountNumber < len(accountPasswordsList) and password == accountPasswordsList[accountNumber]:
        accountBalancesList[accountNumber] += amountToDeposit
        return accountBalancesList[accountNumber]
    print('Incorrect account number or password')
    return None


def withdraw(accountNumber, amountToWithdraw, password):
    global accountBalancesList, accountPasswordsList
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount!')
        return None
    if accountNumber < len(accountPasswordsList) and password == accountPasswordsList[accountNumber]:
        if accountBalancesList[accountNumber] >= amountToWithdraw:
            accountBalancesList[accountNumber] -= amountToWithdraw
            return accountBalancesList[accountNumber]
        print('Insufficient funds')
        return None
    print('Incorrect account number or password')
    return None


# Create two sample accounts
print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345, 'nuts')

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
    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()
    if action == 'f':
        print('Get information')
        userPassword = input("Please Enter the password: ")
        getInformation(userPassword)
    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 'd':
        print('Deposit:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        amountToDeposit = float(input('Please enter the amount to deposit: '))
        newBalance = deposit(userAccountNumber, amountToDeposit, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        amountToWithdraw = float(input('Please enter the amount to withdraw: '))
        newBalance = withdraw(userAccountNumber, amountToWithdraw, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 's':
        print('Show All Accounts:')
        for i in range(len(accountNamesList)):
            show(i)
    elif action == 'q':
        break

print('Done')
