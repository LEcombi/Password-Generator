import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import password_generator
import password_manager

# Function to generate and display a password
def show_password():
    try:
        length = int(entry.get())
        password = password_generator.generate_password(length)
        password_label.config(text=password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))
    messagebox.showinfo("Copied", "Password copied to clipboard.")

# Function to save the generated password for a specific service
def save_password():
    service = simpledialog.askstring("Input", "Enter the service name:")
    password = password_label.cget("text")
    if service and password:
        password_manager.save_password(service, password)
        messagebox.showinfo("Saved", "Password saved successfully.")
    else:
        messagebox.showerror("Error", "Service name or password is missing.")

# Function to copy a specific password to the clipboard
def copy_to_clipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard.")

# Function to retrieve and display a password for a specific service
def retrieve_password():
    service = simpledialog.askstring("Input", "Enter the service name to retrieve:")
    if service:
        password = password_manager.retrieve_password(service)
        if password:
            output_window = tk.Toplevel(root)
            output_window.title("Retrieved Password")
            output_window.geometry("400x150")
            output_window.configure(bg="#2E2E2E")
            output_window.iconbitmap("key.ico")

            password_label = tk.Label(output_window, text=f"Password for {service}: {password}", font=password_font, bg="#2E2E2E", fg="#FFFFFF")
            password_label.pack(pady=10)

            copy_button = tk.Button(output_window, text="Copy Password", font=button_font, command=lambda: copy_to_clipboard(password), bg="#2196F3", fg="white")
            copy_button.pack(pady=10)
        else:
            messagebox.showerror("Error", "Service not found.")
    else:
        messagebox.showerror("Error", "Service name is missing.")

# Function to unlock the database using the root password
def unlock_database():
    root_pass = simpledialog.askstring("Input", "Enter root password:", show='*')
    if root_pass:
        entries = password_manager.unlock_database(root_pass)
        if entries:
            show_all_passwords(entries)
        else:
            messagebox.showerror("Error", "Invalid root password or no entries found.")
    else:
        messagebox.showerror("Error", "Root password is missing.")

# Function to display all passwords in the database
def show_all_passwords(entries):
    output_window = tk.Toplevel(root)
    output_window.title("All Passwords")
    output_window.geometry("400x450")
    output_window.configure(bg="#2E2E2E")
    output_window.iconbitmap("key.ico")

    for service, password in entries:
        frame = tk.Frame(output_window, bg="#2E2E2E")
        frame.pack(fill=tk.X, pady=5)

        password_label = tk.Label(frame, text=f"{service}: {password}", font=password_font, bg="#2E2E2E", fg="#FFFFFF", justify=tk.LEFT)
        password_label.pack(side=tk.LEFT, padx=10)

        copy_button = tk.Button(frame, text="Copy", font=button_font, command=lambda p=password: copy_to_clipboard(p), bg="#2196F3", fg="white")
        copy_button.pack(side=tk.RIGHT, padx=10)

# Create the main window
root = tk.Tk()
root.title("Password Generator and Manager")
root.iconbitmap("key.ico")
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