import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        if text == "":
            messagebox.showwarning("Warning", "Enter text to encrypt")
            return
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypt(text, shift))
    except ValueError:
        messagebox.showerror("Error", "Shift must be a number")

def decrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        if text == "":
            messagebox.showwarning("Warning", "Enter text to decrypt")
            return
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypt(text, shift))
    except ValueError:
        messagebox.showerror("Error", "Shift must be a number")

root = tk.Tk()
root.title("Text Encryption/Decryption")

tk.Label(root, text="Enter Text:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

tk.Label(root, text="Shift:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

tk.Button(root, text="Encrypt", command=encrypt_text, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt_text, bg="red", fg="white").pack(pady=5)

tk.Label(root, text="Output:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

root.mainloop()
