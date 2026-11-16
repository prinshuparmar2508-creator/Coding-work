import tkinter as tk
def show_selection():
    selected_option = choice_var.get()
    label_result.config(text=f"you selected:{selected_option}")

root = tk.Tk()
root.title("radio button example")
root.geometry("300x200")

choice_var = tk.StringVar(value = " option1")
rb1 = tk.Radiobutton(root, text = "option1", variable = choice_var, value="option 1", command = show_selection)
rb2 = tk.Radiobutton(root, text = "option2", variable = choice_var, value="option 2", command = show_selection)
rb3 = tk.Radiobutton(root, text = "option3", variable = choice_var, value="option 3", command = show_selection)

label_result = tk.Label(root, text = "you selected option 1", font = ("arial",12))
label_result.pack(pady = 20)

root.mainloop()

