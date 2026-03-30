class Employee:
    company = "Google"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable


e1 = Employee("Gaurav")
e2 = Employee("Rahul")

print(e1.company)
print(e1.name)
print(e2.name)
