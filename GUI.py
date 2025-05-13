import customtkinter as ctk
import sqlite3

# Initialize main window
root = ctk.CTk()
root.geometry("1000x600")
root.title("Inventory Management System")

# SQL Database Setup
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        category TEXT, 
        quantity INTEGER, 
        price REAL, 
        reorder_level INTEGER
    )
""")
conn.commit()

# Sidebar frame
sidebar = ctk.CTkFrame(root, width=200, corner_radius=0, fg_color="#1E1E1E")
sidebar.pack(side="left", fill="y")

# Define button navigation
buttons = ["Dashboard", "Products", "Inventory Transactions", "Suppliers", "Reports", "Settings"]
screen_frames = {}

# Function to switch screens with animation
def switch_screen(screen_name):
    for frame in screen_frames.values():
        frame.place_forget()

    screen_frames[screen_name].place(relx=1, y=0, relwidth=1, relheight=1)
    screen_frames[screen_name].animate_slide()

class AnimatedScreen(ctk.CTkFrame):
    def __init__(self, parent, bg_color):
        super().__init__(parent, fg_color=bg_color)
        self.place(x=1000, y=0, relwidth=1, relheight=1)  # Start off-screen

    def animate_slide(self):
        for i in range(1000, 0, -20):  # Sliding animation
            self.place(x=i, y=0, relwidth=1, relheight=1)
            root.update_idletasks()

# Create screen frames
for name in buttons:
    screen_frames[name] = AnimatedScreen(root, bg_color="white")

# Sidebar Buttons with Navigation
for btn_text in buttons:
    ctk.CTkButton(sidebar, text=btn_text, fg_color="#007acc", hover_color="#005f99", command=lambda x=btn_text: switch_screen(x)).pack(fill="x", pady=8)

# Sample Product Table in "Products" screen
tree = ctk.CTkFrame(screen_frames["Products"], fg_color="white")
tree.pack(expand=True, fill="both", padx=20, pady=10)

# Run application
root.mainloop()
