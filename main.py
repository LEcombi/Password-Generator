import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def show_password():
    try:
        length = int(entry.get())
        password = generate_password(length)
        password_label.config(text=password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))
    messagebox.showinfo("Copied", "Password copied to clipboard.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Dark Mode Style
root.configure(bg="#2E2E2E")
label_font = ("Arial", 12, "bold")
button_font = ("Arial", 10)
password_font = ("Arial", 14, "bold")

# Create and place the widgets
label = tk.Label(root, text="Enter the desired password length:", font=label_font, bg="#2E2E2E", fg="#FFFFFF")
label.pack(pady=10)

entry = tk.Entry(root, font=label_font, bg="#555555", fg="#FFFFFF", insertbackground="#FFFFFF")
entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#2E2E2E")
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate Password", font=button_font, command=show_password, bg="#4CAF50", fg="white")
generate_button.grid(row=0, column=0, padx=10)

copy_button = tk.Button(button_frame, text="Copy Password", font=button_font, command=copy_to_clipboard, bg="#2196F3", fg="white")
copy_button.grid(row=0, column=1, padx=10)

password_label = tk.Label(root, text="", font=password_font, bg="#2E2E2E", fg="#FFFFFF")
password_label.pack(pady=20)

# Run the application
root.mainloop()
