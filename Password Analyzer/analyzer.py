import tkinter as tk
from tkinter import messagebox
import re

def check_password():
    password = entry.get().strip()
    strength = 0

    strength += min(len(password)//4, 4)

    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    if re.search(r"\s", password):
        strength -= 1

    if strength >= 6:
        msg = "Very Strong Password"
    elif strength >= 4:
        msg = "Moderate Password"
    else:
        msg = "Weak Password"

    messagebox.showinfo("Password Strength", msg)

root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("500x150")

tk.Label(root, text="Enter Password:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)

root.mainloop()
