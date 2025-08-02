import sqlite3
import sys

conn = sqlite3.connect("todo.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, done INTEGER)")

def add(task):
    c.execute("INSERT INTO tasks (task, done) VALUES (?,0)", (task,))
    conn.commit()

def list_tasks():
    for row in c.execute("SELECT id, task, done FROM tasks"):
        status = "✔" if row[2] else "✗"
        print(f"{row[0]}. [{status}] {row[1]}")

def complete(task_id):
    c.execute("UPDATE tasks SET done=1 WHERE id=?", (task_id,))
    conn.commit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: add/list/complete <args>")
    elif sys.argv[1] == "add":
        add(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "complete":
        complete(int(sys.argv[2]))
