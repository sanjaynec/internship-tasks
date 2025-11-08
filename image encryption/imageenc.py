from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
def encrypt_image():
    try:
        key_value = int(key.get("1.0", "end-1c")) % 256
        src = filedialog.askopenfile(mode='rb', filetypes=[('JPEG file', '*.jpeg'), ('PNG file', '*.png')])
        if src is None:
            return
        
        img_name = src.name
        src.close()
        
        with open(img_name, 'rb') as f1:
            image = bytearray(f1.read())
        
        for i, val in enumerate(image):
            image[i] = ((val^key_value)-1) %256
        
        with open(img_name, 'wb') as f1:
            f1.write(image)

        messagebox.showinfo("Success", "Image encrypted successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Unable to open or process image.\n{e}")



def decrypt_image():
      try:
        key_value = int(key.get("1.0", "end-1c")) % 256
        src = filedialog.askopenfile(mode='rb', filetypes=[('JPEG file', '*.jpeg'), ('PNG file', '*.png')])
        if src is None:
            return
        
        img_name = src.name
        src.close()
        
        with open(img_name, 'rb') as f1:
            image = bytearray(f1.read())
        
        for i, val in enumerate(image):
            image[i] = ((val + 1) ^ key_value) % 256
        
        with open(img_name, 'wb') as f1:
            f1.write(image)

        messagebox.showinfo("Success", "Image decrypted successfully!")

      except Exception as e:
        messagebox.showerror("Error", f"Unable to open or process image.\n{e}")


windows = Tk()
windows.title("IMAGE ENCRYPT & DECRYPT")
windows.geometry("600x600")
windows.config(bg="#535353")


frame = Frame(windows, bg="#ffffff", highlightbackground="gray", relief="solid", bd=2)
frame.pack(padx=10, pady=10,expand=True)
Label(frame, text=" IMAGE ENCRYPTION", font=("Times New Roman", 24, "bold"),fg="#212121").pack(side="top")
Label(frame, text="ENTER A KEY TO ENCRYPT & DECRYPT A IMAGE", font=("Times New Roman", 16),fg="#212121").pack(pady=(15,5))


key = Text(frame, height=5, width=20, font=("Times New Roman", 14),bd=2, relief="groove")
key.pack(padx=50,pady=50,side="top",expand=True)


encrypt_button = Button(frame,text="ENCRYPT",command=encrypt_image,bg="red",font=("Times New Roman", 14, "bold"),bd=2,relief="ridge")
encrypt_button.pack(side="left", expand=True, padx=5, pady=20)



decrypt_button=Button(frame,text="DECRYPT",command=decrypt_image,bg="blue",font=("Times New Roman", 14, "bold"),bd=2,relief="ridge")
decrypt_button.pack(side="right", expand=True, padx=5, pady=20)

windows.mainloop()