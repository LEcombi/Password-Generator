import tkinter as tk
from tkinter import messagebox

def copy_to_clipboard(root, password):
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard.")

def show_all_passwords(root, entries):
    output_window = tk.Toplevel(root)
    output_window.title("All Passwords")
    output_window.geometry("400x450")
    output_window.configure(bg="#2E2E2E")
    output_window.iconbitmap("key.ico")

    label_font = ("Arial", 12, "bold")
    button_font = ("Arial", 10)
    password_font = ("Arial", 14, "bold")

    for service, password in entries:
        frame = tk.Frame(output_window, bg="#2E2E2E")
        frame.pack(fill=tk.X, pady=5)

        password_label = tk.Label(frame, text=f"{service}: {password}", font=password_font, bg="#2E2E2E", fg="#FFFFFF", justify=tk.LEFT)
        password_label.pack(side=tk.LEFT, padx=10)

        copy_button = tk.Button(frame, text="Copy", font=button_font, command=lambda p=password: copy_to_clipboard(root, p), bg="#2196F3", fg="white")
        copy_button.pack(side=tk.RIGHT, padx=10)