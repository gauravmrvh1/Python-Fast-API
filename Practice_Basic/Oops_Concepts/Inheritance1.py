class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Gaurav", "Marvaha")
x.printname()


# #############################################################################
# Inheritance:
# #############################################################################
 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Marwah")
x.printname()


# #############################################################################
# Use the super() function to add the __init__() function to the child class:
# #############################################################################

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    # self.firstname = fname
    # self.lastname = lname
    self.graduationyear = 2019
    
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Gaurav", "Olsen")
x.printname()
print(x.graduationyear)
x.welcome()



# #############################################################################
# #############################################################################
class Animal:
  def speak(self):
    print("Animal speaks")

class Dog(Animal):
  def bark(self):
    print("Dog barks")

d = Dog()
d.speak() # inherited
d.bark()
# #############################################################################
# #############################################################################