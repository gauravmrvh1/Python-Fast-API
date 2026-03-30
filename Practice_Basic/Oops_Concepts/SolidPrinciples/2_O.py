#  Open/Closed Principle (OCP)
# 👉 Code extend karo, modify mat karo

class Discount:
    def calculate(self, type):
        if type == "new":
            return 10
        elif type == "vip":
            return 20
        
d = Discount()
print(d.calculate("new"))


# ########################## Correct Way ###################################################
class DiscountStrategy:
    def apply(self):
        pass


class NewCustomer(DiscountStrategy):
    def apply(self):
        return 10


class VIPCustomer(DiscountStrategy):
    def apply(self):
        return 20
    
# Usage
def calculate_discount(DiscountStrategy: DiscountStrategy):
    return DiscountStrategy.apply()

print(calculate_discount(NewCustomer()))
print(calculate_discount(VIPCustomer()))
