# Bank Version 1
# Single account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

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
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print('Your balance is:', accountBalance)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        try:
            userDepositAmount = int(userDepositAmount)
            if userDepositAmount < 0:
                print('You cannot deposit a negative amount!')
            else:
                userPassword = input('Please enter the password: ')
                if userPassword != accountPassword:
                    print('Incorrect password')
                else:  # OK
                    accountBalance += userDepositAmount
                    print('Your new balance is:', accountBalance)
        except ValueError:
            print('Invalid input. Please enter a valid amount.')
    elif action == 's':  # show
        print('Show:')
        print('       Name:', accountName)
        print('       Balance:', accountBalance)
        print('       Password:', accountPassword)
        print()
    elif action == 'q':
        break
    elif action == 'w':
        print('Withdraw:')
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        try:
            userWithdrawAmount = int(userWithdrawAmount)
            if userWithdrawAmount < 0:
                print('You cannot withdraw a negative amount')
            elif userWithdrawAmount > accountBalance:
                print('You cannot withdraw more than you have in your account')
            else:
                userPassword = input('Please enter the password: ')
                if userPassword != accountPassword:
                    print('Incorrect password for this account')
                else:  # OK
                    accountBalance -= userWithdrawAmount
                    print('Your new balance is:', accountBalance)
        except ValueError:
            print('Invalid input. Please enter a valid amount.')

print('Done')
