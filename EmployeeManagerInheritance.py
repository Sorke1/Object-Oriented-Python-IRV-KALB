# Define the Employee class, which we will use as a base
class Employee():
    def __init__(self, name, title, ratePerHour=None):
        self.__name = name
        self.title = title
        if ratePerHour is not None:
            self.ratePerHour = float(ratePerHour)
        else:
            self.ratePerHour = None

    def getName(self):
        return self.__name

    def getTitle(self):
        return self.title

    def payPerYear(self):
        if self.ratePerHour is not None:
            # 52 weeks * 5 days a week * 8 hours per day
            pay = 52 * 5 * 8 * self.ratePerHour
            print( 'Employee of the year bonus added')

            return pay
        else:
            return "Rate per hour not specified"
# Define a Manager subclass that inherits from Employee
class Manager(Employee):
    def __init__(self, name, title, salary, reportsList=None):
        self.salary = float(salary)
        if reportsList is None:
            reportsList = []
        self.reportsList = reportsList
        super().__init__(name, title) #  Employee.__init__(self, name, title)

    def getReports(self):
        return self.reportsList

    def payPerYear(self, giveBonus=False):
        pay = self.salary
        if giveBonus:
            pay += 0.10 * self.salary  # add a bonus of 10%
            print( 'Manager of the year bonus added')
        return pay

# Create Employee and Manager objects
oEmployee1 = Employee('Joe Schmoe', 'Pizza Maker', 16)
oEmployee2 = Employee('Chris Smith', 'Cashier', 14)
oManager = Manager('Sue Jones', 'Pizza Restaurant Manager', 55000, [oEmployee1, oEmployee2])

# Print details of Employee objects
print('Employee name:', oEmployee1.getName())
print('Employee salary: ${:,.2f}'.format(oEmployee1.payPerYear()))
print('Employee name:', oEmployee2.getName())
print('Employee salary: ${:,.2f}'.format(oEmployee2.payPerYear()))
print()

# Print details of Manager object
managerName = oManager.getName()
print('Manager name:', managerName)
# Give the manager a bonus and print updated salary
print('Manager salary: ${:,.2f}'.format(oManager.payPerYear(giveBonus=True)))
print(managerName, '(' + oManager.getTitle() + ')', 'direct reports:')
reportsList = oManager.getReports()
for oEmployee in reportsList:
    print('   ', oEmployee.getName(), '(' + oEmployee.getTitle() + ')')
