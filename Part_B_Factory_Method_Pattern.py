from abc import ABC, abstractmethod

class Notification(ABC):
    #Abstract base class defining a notification.
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    #Concrete class for email notification.
    def send(self):
        return "Sending Email Notification"

class SMSNotification(Notification):
    #Concrete class for SMS notification.
    def send(self):
        return "Sending SMS Notification"

class PushNotification(Notification):
    #Concrete class for push notification.
    def send(self):
        return "Sending Push Notification"

class NotificationFactory:
    #Factory class to create notification instances based on type.
    @staticmethod
    def create_notification(type_):
        type_ = type_.lower()
        if type_ == "email":
            return EmailNotification()
        elif type_ == "sms":
            return SMSNotification()
        elif type_ == "push":
            return PushNotification()
        else:
            raise ValueError("Unsupported notification type")

# Demo
notif_type = input("Enter notification type (Email/SMS/Push): ")
notification = NotificationFactory.create_notification(notif_type)
print(notification.send())
