

# 👉 Concept
# Protect data using private variables
# Access via methods

# #############################################################################
# #############################################################################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())
# #############################################################################
# #############################################################################




# #############################################################################
# #############################################################################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age)  # This will cause an error
# #############################################################################
# #############################################################################



# #############################################################################
# #############################################################################
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
# #############################################################################
# #############################################################################



# #############################################################################
# #############################################################################
class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Gaurav Marvaha")
print(student.name)
student.set_grade(-1)
print(student.get_grade())
print(student.get_status())
# #############################################################################
# #############################################################################