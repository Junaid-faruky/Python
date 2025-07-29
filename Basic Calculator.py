import tkinter as tk

def calculate():
    result = eval(entry.get())
    label_result.config(text=f"Result: {result}")

win = tk.Tk()
win.title("Calculator")

entry = tk.Entry(win)
entry.pack()

btn = tk.Button(win, text="Calculate", command=calculate)
btn.pack()

label_result = tk.Label(win, text="Result:")
label_result.pack()

win.mainloop()
