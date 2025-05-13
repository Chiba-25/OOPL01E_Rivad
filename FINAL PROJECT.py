# === Personal Finance Tracker ===
# This script allows users to track income, expenses, set category budgets,
# and generate monthly financial reports.

# --- Base Transaction Class ---
class Transaction:
    def __init__(self, amount, category, date):
        self.amount = amount  # Amount of the transaction
        self.category = category  # Category name or income source
        self.date = date  # Date of the transaction

    def display(self):
        # Returns a string summary of the transaction
        return f"{self.date}: {self.category} - ${self.amount:.2f}"


# --- Expense Class (inherits from Transaction) ---
class Expense(Transaction):
    def display(self):
        return f"Expense -> {super().display()}"


# --- Income Class (inherits from Transaction) ---
class Income(Transaction):
    def display(self):
        return f"Income -> {super().display()}"


# --- Category Class (handles budget tracking) ---
class Category:
    def __init__(self, name, budget_limit=0):
        self.name = name  # Category name (e.g., Food, Rent)
        self.budget_limit = budget_limit  # Optional spending limit
        self.total_spent = 0  # Running total of expenses in this category

    def set_budget(self, limit):
        self.budget_limit = limit  # Update the budget limit

    def add_expense(self, amount):
        self.total_spent += amount  # Update spending total
        # Warn if spending exceeds budget
        if self.budget_limit > 0 and self.total_spent > self.budget_limit:
            print(f"⚠ WARNING: You have exceeded your budget for '{self.name}'!")

    def display_budget_status(self):
        # Return formatted string of the category's budget status
        return f"{self.name}: Budget Limit = ${self.budget_limit:.2f}, Spent = ${self.total_spent:.2f}"


# --- FinanceManager Class (main logic of the app) ---
class FinanceManager:
    def __init__(self):
        self.transactions = []  # List of all income and expense records
        self.categories = {}  # Dictionary of category name -> Category object

    def add_category(self, name, budget_limit=0):
        self.categories[name] = Category(name, budget_limit)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

        if isinstance(transaction, Expense):
            # Update budget for the category if it exists
            if transaction.category in self.categories:
                self.categories[transaction.category].add_expense(transaction.amount)

            # Check if total expenses exceed income
            total_income = sum(t.amount for t in self.transactions if isinstance(t, Income))
            total_expenses = sum(t.amount for t in self.transactions if isinstance(t, Expense))

            if total_expenses > total_income:
                print("⚠ WARNING: You have insufficient balance! Expenses exceed income.")

    def generate_report(self):
        # Calculate summary values
        total_income = sum(t.amount for t in self.transactions if isinstance(t, Income))
        total_expenses = sum(t.amount for t in self.transactions if isinstance(t, Expense))
        balance = total_income - total_expenses

        # Print financial summary
        print("\n===== Monthly Summary Report =====")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")
        print("\nBudget Status:")
        for category in self.categories.values():
            print(category.display_budget_status())

    def list_transactions(self):
        print("\n===== Transactions =====")
        for t in self.transactions:
            print(t.display())


# --- Main interactive user interface ---
def main():
    fm = FinanceManager()

    while True:
        # Display menu
        print("\n==== Personal Finance Tracker ====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget for a Category")
        print("4. View Transactions")
        print("5. View Monthly Summary Report")
        print("6. Exit")

        choice = input("Choose an option: ")

        # Handle menu selection
        if choice == "1":
            amount = float(input("Enter income amount: "))
            category = input("Enter income source (e.g., Salary, Freelance): ")
            date = input("Enter date (YYYY-MM-DD): ")
            fm.add_transaction(Income(amount, category, date))

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date = input("Enter date (YYYY-MM-DD): ")

            if category not in fm.categories:
                print("Category not found. Add a budget first!")
            else:
                fm.add_transaction(Expense(amount, category, date))

        elif choice == "3":
            category = input("Enter category name: ")
            budget = float(input(f"Set budget for {category}: "))
            fm.add_category(category, budget)

        elif choice == "4":
            fm.list_transactions()

        elif choice == "5":
            fm.generate_report()

        elif choice == "6":
            print("Exiting program. Have a nice day!")
            break

        else:
            print("Invalid choice. Please try again.")


# Entry point of the program
if __name__ == "__main__":
    main()
