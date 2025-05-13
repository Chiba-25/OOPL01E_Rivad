# personal_finance_tracker.py

class Transaction:
    """Base class for transactions"""
    def __init__(self, amount, category, description):
        self._amount = amount  # Encapsulation with private attribute
        self._category = category
        self._description = description

    def display(self):
        return f"Transaction: {self._description} | Amount: {self._amount} | Category: {self._category}"

    def edit(self, amount, category, description):
        self._amount = amount
        self._category = category
        self._description = description

class Expense(Transaction):  # Inheritance
    """Represents an expense transaction"""
    def __init__(self, amount, category, description):
        super().__init__(-abs(amount), category, description)  # Expenses are negative

    def display(self):  # Polymorphism
        return f"Expense - {self._description}: {self._amount} ({self._category})"

class Income(Transaction):  # Inheritance
    """Represents an income transaction"""
    def __init__(self, amount, category, description):
        super().__init__(abs(amount), category, description)  # Income is positive

    def display(self):  # Polymorphism
        return f"Income - {self._description}: {self._amount} ({self._category})"

transactions = []  # Stores all transactions

def add_transaction(transaction):
    """Adds a transaction to the list"""
    transactions.append(transaction)

def edit_transaction(index):
    """Edits an existing transaction"""
    if 0 <= index < len(transactions):
        amount = float(input("Enter new amount: "))
        category = input("Enter new category: ")
        description = input("Enter new description: ")
        transactions[index].edit(amount, category, description)
        print("Transaction updated!")
    else:
        print("Invalid transaction index.")

def delete_transaction(index):
    """Deletes a transaction"""
    if 0 <= index < len(transactions):
        transactions.pop(index)
        print("Transaction deleted!")
    else:
        print("Invalid transaction index.")

def generate_summary():
    """Generates a simple financial summary"""
    total_income = sum(t._amount for t in transactions if isinstance(t, Income))
    total_expense = sum(t._amount for t in transactions if isinstance(t, Expense))
    balance = total_income + total_expense

    return f"\n--- Monthly Summary ---\nTotal Income: {total_income}\nTotal Expenses: {total_expense}\nBalance: {balance}\n"

# Console-based menu system
def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Transactions")
        print("4. Edit Transaction")
        print("5. Delete Transaction")
        print("6. View Summary Report")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_transaction(Expense(amount, category, description))
            print("Expense added!")

        elif choice == '2':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_transaction(Income(amount, category, description))
            print("Income added!")

        elif choice == '3':
            if transactions:
                print("\n--- Transactions ---")
                for i, t in enumerate(transactions):
                    print(f"{i}. {t.display()}")
            else:
                print("No transactions recorded.")

        elif choice == '4':
            index = int(input("Enter transaction index to edit: "))
            edit_transaction(index)

        elif choice == '5':
            index = int(input("Enter transaction index to delete: "))
            delete_transaction(index)

        elif choice == '6':
            print(generate_summary())

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
