from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Push sent: {message}")


# Usage
def notify_user(notification: Notification):
    notification.send("Order Placed Successfully")

notify_user(EmailNotification())
notify_user(SMSNotification())
notify_user(PushNotification())






# Abstract class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete class
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


# Usage
p1 = CreditCardPayment()
p1.pay(1000)

p2 = UpiPayment()
p2.pay(500)