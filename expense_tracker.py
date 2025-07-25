import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

FILE = "expenses.csv"

# Initialize file if not exists
if not os.path.exists(FILE):
    with open(FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    date = datetime.today().strftime('%Y-%m-%d')
    category = input("Category (e.g., Food, Travel, Bills): ")
    amount = float(input("Amount spent: ₹"))
    desc = input("Description: ")
    with open(FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, desc])
    print("Expense recorded!")

def show_summary():
    df = pd.read_csv(FILE)
    print("\nLast 5 Entries:")
    print(df.tail())
    print("\nTotal Spent: ₹", df["Amount"].sum())

def plot_expenses():
    df = pd.read_csv(FILE)
    df.groupby("Category")["Amount"].sum().plot(kind="bar", color="skyblue")
    plt.title("Total Spent by Category")
    plt.ylabel("Amount (₹)")
    plt.xlabel("Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\n1. Add Expense\n2. Show Summary\n3. Plot Expenses\n4. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            plot_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    menu()
