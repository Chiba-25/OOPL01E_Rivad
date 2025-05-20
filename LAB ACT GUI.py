import customtkinter as ctk
from tkinter import messagebox

# Configure appearance mode
ctk.set_appearance_mode("dark")  # You can change to "light" or "system"
ctk.set_default_color_theme("blue")  # Other options: "green", "dark-blue"

def submit_form():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    gender = gender_var.get()
    course = combo_course.get()

    if not first_name or not last_name or not email or not gender or not course:
        messagebox.showwarning("Warning", "All fields must be filled out")
    else:
        messagebox.showinfo("Submitted Information", f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nGender: {gender}\nCourse: {course}")

def clear_form():
    entry_first_name.delete(0, ctk.END)
    entry_last_name.delete(0, ctk.END)
    entry_email.delete(0, ctk.END)
    gender_var.set("")
    combo_course.set("")

# Create the main window
app = ctk.CTk()
app.title("User Information Form")
app.geometry("400x400")

# Create and place the labels and entry fields
ctk.CTkLabel(app, text="First Name:").pack(pady=5)
entry_first_name = ctk.CTkEntry(app, width=250)
entry_first_name.pack(pady=5)

ctk.CTkLabel(app, text="Last Name:").pack(pady=5)
entry_last_name = ctk.CTkEntry(app, width=250)
entry_last_name.pack(pady=5)

ctk.CTkLabel(app, text="Email Address:").pack(pady=5)
entry_email = ctk.CTkEntry(app, width=250)
entry_email.pack(pady=5)

# Gender Selection
ctk.CTkLabel(app, text="Gender:").pack(pady=5)
gender_var = ctk.StringVar()
frame_gender = ctk.CTkFrame(app)
frame_gender.pack()
ctk.CTkRadioButton(frame_gender, text="Male", variable=gender_var, value="Male").pack(side="left", padx=10)
ctk.CTkRadioButton(frame_gender, text="Female", variable=gender_var, value="Female").pack(side="left", padx=10)
ctk.CTkRadioButton(frame_gender, text="Prefer not to say", variable=gender_var, value="Prefer not to say").pack(side="left", padx=10)

# Course Selection
ctk.CTkLabel(app, text="Course:").pack(pady=5)
combo_course = ctk.CTkComboBox(app, values=["BSCS", "BSIT", "BSIS", "BSEMC"])
combo_course.pack(pady=5)

# Buttons
frame_buttons = ctk.CTkFrame(app)
frame_buttons.pack(pady=10)
ctk.CTkButton(frame_buttons, text="Submit", command=submit_form, fg_color="green").pack(side="left", padx=10)
ctk.CTkButton(frame_buttons, text="Clear", command=clear_form, fg_color="red").pack(side="left", padx=10)

# Run the application
app.mainloop()
