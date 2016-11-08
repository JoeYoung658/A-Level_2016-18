"""
Joe Young
Employment
"""


class Employee:

    raise_amount = 1.02

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #Affects whole class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    #Does not need access to instance (self) or class (cls) to function
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developper(Employee):
    raise_amount = 1.2


    def __init__(self, first, last, pay, prog_lang):
        #Uses the __init__ from Employee class 
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, Employees=None):
        #Uses the __init__ from Employee class 
        super().__init__(first, last, pay)
        if Employees is None:
            self.Employees = []
        else:
            self.Employees = Employees

    def add_emp(self, emp):
        if emp not in self.Employees:
            self.Employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.Employees:
            self.Employees.remove(emp)
    
    def print_emps(self):
        for emp in self.Employees:
            print("-->", emp.fullname)
    


#Sets the Employees
emp_1 = Employee('Bob', 'Smith', 50000)
emp_2 = Employee('Sam', 'Fred', 60000)

#Shows last name working
print("----------------------------------------------")
print(emp_1.first)
print(Employee.fullname(emp_1))

#Change Class Raise Amounts
print("----------------------------------------------")
Employee.set_raise_amt(1.1)
print("Main {}".format(Employee.raise_amount))
print("Emp 1 {}".format(emp_1.raise_amount))
print("Emp 2 {}".format(emp_2.raise_amount))


#Shows pay rise/Change certain pay raise
print("----------------------------------------------")
print(emp_1.pay)
emp_1.raise_amount = 1.05 #Changed amount to 5%
emp_1.apply_raise()
print(emp_1.pay)

#Shows the use of static methods
#Tells the user if it is a work day though the date given
print("----------------------------------------------")
import datetime
my_date = datetime.date(2016, 11, 8)
if (Employee.is_workday(my_date) == True):
    print("It is a work day")
else:
    print("It is not a work day")

#Sets the Developpers

dev_1 = Developper('Jim', 'Harry', 90000, "Python")
dev_2 = Developper('Simon', 'Perry', 100000, "Java")

#Shows Developper rise/Change certain pay raise
print("----------------------------------------------")
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

#Shows the prog_lang of the Developper, while reusing Employee Code
print("----------------------------------------------")
print("Dev 1 {}".format(dev_1.prog_lang))
print("Dev 2 {}".format(dev_2.prog_lang))



print("----------------------------------------------")
mgr_1 = Manager("Sue", "Smith", 100000000, [dev_1])

print(mgr_1.fullname())


mgr_1.print_emps()