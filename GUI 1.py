import tkinter as tk
from tkinter import ttk
import sqlite3

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()
        self.create_table()

        self.create_dashboard_widgets()
        self.populate_dashboard_data()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                product_name TEXT NOT NULL,
                type TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                performed_by TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def create_dashboard_widgets(self):
        # --- Dashboard Title ---
        title_label = ttk.Label(self.root, text="Dashboard", font=("TkDefaultFont", 16, "bold"))
        title_label.pack(pady=10, padx=10, anchor="w")

        # --- Information Boxes Frame ---
        info_frame = ttk.Frame(self.root)
        info_frame.pack(pady=10, padx=10, fill="x")

        # Total Products
        self.total_products_label = ttk.LabelFrame(info_frame, text="Total Products")
        self.total_products_label.pack(side="left", padx=5, fill="x", expand=True)
        self.total_products_value = ttk.Label(self.total_products_label, text="0", font=("TkDefaultFont", 14))
        self.total_products_value.pack(padx=10, pady=10)

        # Low Stock Items
        self.low_stock_label = ttk.LabelFrame(info_frame, text="Low Stock Items")
        self.low_stock_label.pack(side="left", padx=5, fill="x", expand=True)
        self.low_stock_value = ttk.Label(self.low_stock_label, text="0", font=("TkDefaultFont", 14))
        self.low_stock_value.pack(padx=10, pady=10)

        # Total Suppliers
        self.total_suppliers_label = ttk.LabelFrame(info_frame, text="Total Suppliers")
        self.total_suppliers_label.pack(side="left", padx=5, fill="x", expand=True)
        self.total_suppliers_value = ttk.Label(self.total_suppliers_label, text="0", font=("TkDefaultFont", 14))
        self.total_suppliers_value.pack(padx=10, pady=10)

        # --- Recent Transactions Frame ---
        transactions_frame = ttk.LabelFrame(self.root, text="Recent Transactions")
        transactions_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.transactions_tree = ttk.Treeview(transactions_frame, columns=("Date", "Product", "Type", "Quantity", "Performed By"), show="headings")
        self.transactions_tree.heading("Date", text="Date")
        self.transactions_tree.heading("Product", text="Product")
        self.transactions_tree.heading("Type", text="Type")
        self.transactions_tree.heading("Quantity", text="Quantity")
        self.transactions_tree.heading("Performed By", text="Performed By")
        self.transactions_tree.pack(fill="both", expand=True)

    def populate_dashboard_data(self):
        # Total Products
        self.cursor.execute("SELECT COUNT(*) FROM items")
        total_products = self.cursor.fetchone()[0]
        self.total_products_value.config(text=total_products)

        # Low Stock Items (you'll need to define what "low stock" means)
        # For example, let's say items with quantity less than 10 are low stock
        self.cursor.execute("SELECT COUNT(*) FROM items WHERE quantity < 10")
        low_stock_count = self.cursor.fetchone()[0]
        self.low_stock_value.config(text=low_stock_count)

        # Total Suppliers
        self.cursor.execute("SELECT COUNT(*) FROM suppliers")
        total_suppliers = self.cursor.fetchone()[0]
        self.total_suppliers_value.config(text=total_suppliers)

        # Recent Transactions (let's fetch the last 5 transactions)
        for item in self.transactions_tree.get_children():
            self.transactions_tree.delete(item)
        self.cursor.execute("SELECT date, product_name, type, quantity, performed_by FROM transactions ORDER BY id DESC LIMIT 5")
        transactions = self.cursor.fetchall()
        for row in transactions:
            self.transactions_tree.insert("", "end", values=row)

    # --- Placeholder functions for other sections (you'll need to implement these) ---
    def show_products(self):
        # Logic to display the products view
        pass

    def show_inventory_transactions(self):
        # Logic to display inventory transactions
        pass

    def show_suppliers(self):
        # Logic to display suppliers
        pass

    def show_reports(self):
        # Logic to display reports
        pass

    def show_settings(self):
        # Logic for settings
        pass

    def logout(self):
        # Logic for logout
        self.root.destroy()

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()

    # --- Style Configuration for ttk Buttons ---
    style = ttk.Style()
    style.configure("Sidebar.TButton", padding=(10, 8), anchor="w") # (padx, pady)

    # --- Sidebar Frame ---
    sidebar_frame = ttk.Frame(root, width=150, relief="solid", borderwidth=1)
    sidebar_frame.pack(side="left", fill="y")

    app = InventoryApp(root) # Initialize the main content

    # --- Sidebar Buttons ---
    dashboard_button = ttk.Button(sidebar_frame, text="Dashboard", command=lambda: app.create_dashboard_widgets(), style="Sidebar.TButton")
    dashboard_button.pack(fill="x", pady=2)

    products_button = ttk.Button(sidebar_frame, text="Products", command=app.show_products, style="Sidebar.TButton")
    products_button.pack(fill="x", pady=2)

    transactions_button = ttk.Button(sidebar_frame, text="Inventory Transactions", command=app.show_inventory_transactions, style="Sidebar.TButton")
    transactions_button.pack(fill="x", pady=2)

    suppliers_button = ttk.Button(sidebar_frame, text="Suppliers", command=app.show_suppliers, style="Sidebar.TButton")
    suppliers_button.pack(fill="x", pady=2)

    reports_button = ttk.Button(sidebar_frame, text="Reports", command=app.show_reports, style="Sidebar.TButton")
    reports_button.pack(fill="x", pady=2)

    settings_button = ttk.Button(sidebar_frame, text="Settings", command=app.show_settings, style="Sidebar.TButton")
    settings_button.pack(fill="x", pady=2)

    logout_button = ttk.Button(sidebar_frame, text="Logout", command=app.logout, style="Sidebar.TButton")
    logout_button.pack(fill="x", pady=2, side="bottom")

    root.mainloop()
