#Part A: Singleton Pattern
from datetime import datetime

class Logger:
    _instance = None  # Stores the single instance of the Logger class
    _log = []  # Shared log list across all instances

    def __new__(cls):
        #Ensures only one instance of Logger is created.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        #Adds a log entry with a timestamp.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._log.append(f"[{timestamp}] {message}")

    def show_logs(self):
        #Returns the list of log entries.
        return self._log

# Demo
logger1 = Logger()  # First instance
logger2 = Logger()  # Second instance (same as logger1)

# Logging messages using both instances
logger1.log("First log entry.")
logger2.log("Second log entry.")

# Displaying the shared log
print(logger1.show_logs())

# Verifying that logger1 and logger2 are the same instance
print(f"logger1 is logger2: {logger1 is logger2}")

#Part B: Factory Method Pattern
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

#Part C Builder Pattern
class Computer:
    #Represents a computer with configurable hardware components.
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def specs(self):
        #Returns the computer's specifications as a dictionary.
        return vars(self)

class ComputerBuilder:
    #Builder class to construct a Computer instance step-by-step.
    def __init__(self):
        self.reset()  # Initialize with a fresh Computer object

    def reset(self):
        #Resets the builder to start a new configuration.
        self.computer = Computer()
        return self

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        #Returns the configured Computer instance and resets the builder for reuse.
        built_computer = self.computer
        self.reset()  # Reset for the next build
        return built_computer

# Demo
builder = ComputerBuilder()

# Building a gaming PC
gaming_pc = builder.set_cpu("AMD Ryzen™ 9 9950X3D").set_ram("64GB").set_storage("8TB SSD").set_gpu("RTX 5090").build()
print("Gaming PC specs:", gaming_pc.specs())

# Reusing the builder to create a budget PC
budget_pc = builder.set_cpu("Intel Core i7 10700").set_ram("16GB").set_storage("512GB SSD").set_gpu("RTX 3060").build()
print("Budget PC specs:", budget_pc.specs())
