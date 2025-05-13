import tkinter as tk
from tkinter import ttk

# Function to create Dashboard UI
def create_dashboard():
    # Main window
    root = tk.Tk()
    root.title("Inventory Management System")
    root.geometry("800x600")

    # Sidebar frame
    sidebar = tk.Frame(root, bg="#2C3E50")
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    # Dashboard title
    dashboard_title = tk.Label(sidebar, text="INVENTORY MANAGEMENT SYSTEM", bg="#2C3E50", fg="white", font=("Arial", 16))
    dashboard_title.pack(pady=20)

    # Sidebar menu items
    menu_items = ["Dashboard", "Products", "Inventory Transactions", "Suppliers", "Reports", "Settings", "Logout"]
    for item in menu_items:
        btn = tk.Button(sidebar, text=item, bg="#34495E", fg="white", width=20, bd=0)
        btn.pack(pady=5)

    # Main content frame
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Dashboard header
    dashboard_header = tk.Label(main_frame, text="Dashboard", bg="white", font=("Arial", 24))
    dashboard_header.pack(pady=20)

    # Info boxes
    info_frame = tk.Frame(main_frame)
    info_frame.pack(pady=10)

    total_products = tk.Label(info_frame, text="Total Products: 200", font=("Arial", 16), bg="white")
    total_low_stock = tk.Label(info_frame, text="Low Stock Items: 15", font=("Arial", 16), bg="white")
    total_suppliers = tk.Label(info_frame, text="Total Suppliers: 25", font=("Arial", 16), bg="white")

    total_products.grid(row=0, column=0, padx=20)
    total_low_stock.grid(row=0, column=1, padx=20)
    total_suppliers.grid(row=0, column=2, padx=20)

    # Recent Transactions table
    recent_transactions_label = tk.Label(main_frame, text="Recent Transactions", bg="white", font=("Arial", 20))
    recent_transactions_label.pack(pady=10)

    # Columns for the table
    columns = ("Date", "Product", "Type", "Quantity", "Performed By")
    transactions_table = ttk.Treeview(main_frame, columns=columns, show='headings')

    # Setting up the columns
    for col in columns:
        transactions_table.heading(col, text=col)

    # Sample Data
    transactions_data = [
        ("04/23/2024", "Tablet", "IN", 20, "Admin"),
        ("04/23/2024", "Monitor", "IN", 5, "Admin"),
        ("04/23/2024", "Printer", "OUT", 8, "Admin"),
        ("04/20/2024", "Chair", "OUT", 15, "Admin"),
        ("04/20/2024", "Laptop", "IN", 10, "Admin"),
    ]

    # Inserting the data
    for transaction in transactions_data:
        transactions_table.insert("", "end", values=transaction)

    transactions_table.pack(pady=10)

    # Run the application
    root.mainloop()

# Call the function to create UI
create_dashboard()
