import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Component Demo")
root.geometry("350x200")

def show_message():
    user_text = entry_feild.get()
    messagebox.showinfo("Getting",f"hello, {user_text}")

label = tk.Label(root,text = "Enter your name:")
entry_feild = tk.Entry(root)
submit_btn = tk.Button(root,text = "submit",command = show_message)

label.pack(pady = 5)
entry_feild.pack(pady = 5)
submit_btn.pack(pady = 10)

root.mainloop()
