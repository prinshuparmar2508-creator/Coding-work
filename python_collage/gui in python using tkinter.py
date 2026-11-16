import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("simple gui programme")
root.geometry("400x200")

def greet_user():
    user_name = name_entry.get()
    if user_name:
        result_label.config(text=f"hello,{user_name}! Welcome!")

    else:
        result_label.config(text="Pls enter name")

instruction_Label = ttk.Label(root,text="Enter name",font=("Arial",10))
instruction_Label.pack(pady=10)

name_entry = ttk.Entry(root,font=("Arial",12))
name_entry.pack(pady=5)

submit_button = ttk.Button(root,text="Greet Box",command = greet_user)
submit_button.pack(pady=10)

result_label = ttk.Label(root,text=" ",font = ("Arial",12,"bold"))
result_label.pack(pady=10)

root = tk.mainloop()