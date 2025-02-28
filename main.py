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

# Create and place the widgets
label = tk.Label(root, text="Enter the desired password length:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Generate Password", command=show_password)
button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack(pady=5)

copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
root.mainloop()
