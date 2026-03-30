# Liskov Substitution Principle (LSP)
# 👉 Child class parent ko break na kare


############################# ❌ WRONG Example (Payment Gateway Break)############################
class PaymentGateway:
    def pay(self, amount):
        pass

    def refund(self, amount):
        pass

class Paytm(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} via Paytm")

    def refund(self, amount):
        print(f"Refunded {amount} via Paytm")

class CashOnDelivery(PaymentGateway):
    def pay(self, amount):
        print(f"Order placed with COD: {amount}")

    def refund(self, amount):
        raise Exception("Refund not supported")  # ❌ LSP break
############################# ❌ WRONG Example (Payment Gateway Break)############################


# ############################ Correct Way ###################################################
# ✅ Correct Example (Payment Gateway Fix)
# ############################ Correct Way ###################################################
from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Refundable(ABC):
    @abstractmethod
    def refund(self, amount):
        pass

class Paytm(PaymentGateway, Refundable):
    def pay(self, amount):
        print(f"Paid {amount} via Paytm")

    def refund(self, amount):
        print(f"Refunded {amount} via Paytm")

class CashOnDelivery(PaymentGateway):
    def pay(self, amount):
        print(f"Order placed with COD: {amount}")
        
# Usage
def process_payment(payment: PaymentGateway):
    payment.pay(1000)
    
def process_refund(refund: Refundable):
    refund.refund(500)
    
paytm = Paytm()
cod = CashOnDelivery()
process_payment(paytm)  # Works
process_payment(cod)   # Works  
process_refund(paytm)  # Works
# process_refund(cod)   # ❌ LSP break
