import tkinter as tk
from tkinter import messagebox

def on_button_click():
    name = entry.get()
    messagebox.showinfo("Greeting", f"Hello, {name}!")

root = tk.Tk()
root.title("Simple GUI")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet Me", command=on_button_click)
button.pack()

root.mainloop()
