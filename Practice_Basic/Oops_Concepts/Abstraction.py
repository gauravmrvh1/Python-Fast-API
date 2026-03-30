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
