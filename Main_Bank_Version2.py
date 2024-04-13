from Account import *

accountList = []
oAccount = Account('Joe', 100, 'JoesPassword')
accountList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account('Mary', 12345, 'MarysPassword') 
accountsList.append(oAccount)
print("Mary's account number is 1")

accountList[0].show
accountList[1].show
print

print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')
accountsList[1].deposit(100, 'MarysPassword')

accountsList[0].show()
accountsList[1].show()
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)