import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard with Sales Orders Feature")
        self.geometry("900x600")
        self.configure(bg="#d3e6de")
        self.font_family = "Times New Roman"

        # Sample sales orders data
        self.sales_orders = [
            {"id": 101, "customer": "John Doe", "date": "2024-04-01", "status": "Pending"},
            {"id": 102, "customer": "Jane Smith", "date": "2024-04-03", "status": "Shipped"},
            {"id": 103, "customer": "Acme Corp", "date": "2024-04-05", "status": "Delivered"},
        ]

        self.create_widgets()

    def create_widgets(self):
        # Sidebar frame
        self.sidebar = tk.Frame(self, bg="#db2777", width=200)
        self.sidebar.pack(side="left", fill="y")

        # Sidebar buttons
        self.nav_buttons = {}
        nav_items = [
            ("Dashboard", "stock"),
            ("Inventory", "orders"),
            ("Suppliers", "suppliers"),
            ("Sales orders", "sales"),
            ("Purchase orders", "purchase"),
        ]

        for text, tab in nav_items:
            btn = tk.Button(
                self.sidebar, text=text, font=(self.font_family, 10),
                fg="white", bg="#db2777" if tab == "sales" else "#ec4899",
                activebackground="#be185d", relief="flat",
                command=lambda t=tab: self.show_tab(t),
                anchor="w", padx=10, pady=8,
            )
            btn.pack(fill="x", pady=2)
            self.nav_buttons[tab] = btn

        # Main content frame
        self.main_content = tk.Frame(self, bg="white")
        self.main_content.pack(side="right", fill="both", expand=True)

        # Welcome label
        self.welcome_label = tk.Label(
            self.main_content, text="Welcome back, James!",
            font=(self.font_family, 16, "bold"), bg="white",
            anchor="w", padx=20, pady=10,
        )
        self.welcome_label.pack(fill="x")

        # Tabs container
        self.tabs_container = tk.Frame(self.main_content, bg="white")
        self.tabs_container.pack(fill="both", expand=True, padx=20, pady=10)

        # Create tab frames
        self.tabs = {
            "stock": self.create_tab_placeholder("Stock inventory content goes here."),
            "orders": self.create_tab_placeholder("Orders content goes here."),
            "suppliers": self.create_tab_placeholder("Suppliers content goes here."),
            "purchase": self.create_tab_placeholder("Purchase orders content goes here."),
            "sales": self.create_sales_tab(),
        }

        # Show default tab
        self.show_tab("sales")

    def create_tab_placeholder(self, text):
        frame = tk.Frame(self.tabs_container, bg="white")
        tk.Label(frame, text=text, font=(self.font_family, 12), bg="white").pack()
        return frame

    def show_tab(self, tab):
        for t in self.tabs.values():
            t.pack_forget()
        self.tabs[tab].pack(fill="both", expand=True)
        for key, btn in self.nav_buttons.items():
            btn.configure(bg="#db2777" if key == tab else "#ec4899")

    def create_sales_tab(self):
        frame = tk.Frame(self.tabs_container, bg="white")

        # Add New Sales Order button
        add_btn = tk.Button(
            frame, text="Add New Sales Order", font=(self.font_family, 12),
            bg="#db2777", fg="white", activebackground="#be185d",
            command=self.add_sales_order, padx=10, pady=6,
        )
        add_btn.pack(anchor="w", pady=(0, 10))

        # Sales orders Treeview
        columns = ("id", "customer", "date", "status")
        self.sales_tree = ttk.Treeview(frame, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.sales_tree.heading(col, text=col.title())
        self.sales_tree.column("id", width=80, anchor="center")
        self.sales_tree.column("customer", width=150)
        self.sales_tree.column("date", width=100, anchor="center")
        self.sales_tree.column("status", width=100, anchor="center")
        self.sales_tree.pack(fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.sales_tree.yview)
        self.sales_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Populate table
        self.refresh_sales_orders()

        # Bind double-click to edit
        self.sales_tree.bind("<Double-1>", self.on_sales_order_double_click)

        # Delete button
        del_btn = tk.Button(
            frame, text="Delete Selected Order", font=(self.font_family, 12),
            bg="#ef4444", fg="white", activebackground="#b91c1c",
            command=self.delete_selected_order, padx=10, pady=6,
        )
        del_btn.pack(anchor="w", pady=10)

        return frame

    def refresh_sales_orders(self):
        """Refreshes the sales order list in the tree view."""
        # Clear current items in Treeview
        for item in self.sales_tree.get_children():
            self.sales_tree.delete(item)

        # Insert new data
        for order in self.sales_orders:
            self.sales_tree.insert("", "end", values=(order["id"], order["customer"], order["date"], order["status"]))

    def add_sales_order(self):
        """Adds a new sales order via dialog."""
        customer = simpledialog.askstring("New Order", "Enter Customer Name:")
        if customer:
            new_id = max(order["id"] for order in self.sales_orders) + 1
            self.sales_orders.append({"id": new_id, "customer": customer, "date": "2024-04-10", "status": "Pending"})
            self.refresh_sales_orders()

    def delete_selected_order(self):
        """Deletes a selected sales order."""
        selected_item = self.sales_tree.selection()
        if selected_item:
            values = self.sales_tree.item(selected_item, "values")
            order_id = int(values[0])
            self.sales_orders = [order for order in self.sales_orders if order["id"] != order_id]
            self.refresh_sales_orders()

    def on_sales_order_double_click(self, event):
        """Edits sales order status on double-click."""
        selected_item = self.sales_tree.selection()
        if selected_item:
            values = self.sales_tree.item(selected_item, "values")
            new_status = simpledialog.askstring("Edit Order", "Enter new status:", initialvalue=values[3])
            if new_status:
                for order in self.sales_orders:
                    if order["id"] == int(values[0]):
                        order["status"] = new_status
                self.refresh_sales_orders()

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
