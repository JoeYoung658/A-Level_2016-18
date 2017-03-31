#Joe Young #31/03/2017


class Customer():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def desposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount


Jim = Customer("Jim", 50)

print(Jim.name)
print(Jim.balance)

Jim.desposit(10)
print(Jim.balance)


Jim.withdraw(15)
print(Jim.balance)