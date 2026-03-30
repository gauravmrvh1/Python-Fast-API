class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.name)
print(p1.get_age())

p1.set_age(26)
print(p1.name)
print(p1.get_age())





# #############################################################################
# #############################################################################
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
# print(acc.__balance)  # This will cause an error
print(acc.get_balance())