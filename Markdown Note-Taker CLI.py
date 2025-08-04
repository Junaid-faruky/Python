from datetime import datetime
note = input("Enter note: ")
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
with open(f"note_{timestamp}.md", "w") as f:
    f.write(f"# Note taken on {timestamp}\n\n{note}\n")
print("Saved note.")
