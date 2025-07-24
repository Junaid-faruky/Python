from tkinter import *

def calculate():
    p = float(principal.get())
    r = float(rate.get()) / 1200
    n = int(time.get()) * 12
    emi = p * r * (1 + r)**n / ((1 + r)**n - 1)
    result.set(f"EMI: ₹{emi:.2f}")

root = Tk()
root.title("EMI Calculator")

principal = StringVar()
rate = StringVar()
time = StringVar()
result = StringVar()

Label(root, text="Loan Amount").pack()
Entry(root, textvariable=principal).pack()
Label(root, text="Interest Rate (%)").pack()
Entry(root, textvariable=rate).pack()
Label(root, text="Loan Period (years)").pack()
Entry(root, textvariable=time).pack()
Button(root, text="Calculate", command=calculate).pack()
Label(root, textvariable=result).pack()

root.mainloop()
