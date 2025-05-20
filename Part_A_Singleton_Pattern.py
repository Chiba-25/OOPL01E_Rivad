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
