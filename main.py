import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import password_generator
import password_manager

def show_password():
    try:
        length = int(entry.get())
        password = password_generator.generate_password(length)
        password_label.config(text=password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))
    messagebox.showinfo("Copied", "Password copied to clipboard.")

def save_password():
    service = simpledialog.askstring("Input", "Enter the service name:")
    password = password_label.cget("text")
    if service and password:
        password_manager.save_password(service, password)
        messagebox.showinfo("Saved", "Password saved successfully.")
    else:
        messagebox.showerror("Error", "Service name or password is missing.")

def retrieve_password():
    service = simpledialog.askstring("Input", "Enter the service name to retrieve:")
    if service:
        password = password_manager.retrieve_password(service)
        if password:
            messagebox.showinfo("Retrieved Password", f"Password for {service}: {password}")
        else:
            messagebox.showerror("Error", "Service not found.")
    else:
        messagebox.showerror("Error", "Service name is missing.")

def unlock_database():
    root_pass = simpledialog.askstring("Input", "Enter root password:", show='*')
    if root_pass:
        entries = password_manager.unlock_database(root_pass)
        if entries:
            entry_list = "\n".join([f"{service}: {password}" for service, password in entries])
            messagebox.showinfo("Database Entries", entry_list)
        else:
            messagebox.showerror("Error", "Invalid root password or no entries found.")
    else:
        messagebox.showerror("Error", "Root password is missing.")

# Create the main window
root = tk.Tk()
root.title("Password Generator and Manager")
root.geometry("400x450")

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

save_button = tk.Button(root, text="Save Password", font=button_font, command=save_password, bg="#FF5722", fg="white")
save_button.pack(pady=10)

retrieve_button = tk.Button(root, text="Retrieve Password", font=button_font, command=retrieve_password, bg="#FFC107", fg="black")
retrieve_button.pack(pady=10)

unlock_button = tk.Button(root, text="Unlock Database", font=button_font, command=unlock_database, bg="#9C27B0", fg="white")
unlock_button.pack(pady=10)

# Run the application
root.mainloop()

# Close the database connection when the application is closed
password_manager.close_connection()
