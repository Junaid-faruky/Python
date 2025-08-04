import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, done INTEGER)')
def add(task): c.execute('INSERT INTO tasks (task, done) VALUES (?,0)', (task,)); conn.commit()
def list_tasks():
    for row in c.execute('SELECT id, task, done FROM tasks'):
        status = "✓" if row[2] else " "
        print(f"[{status}] {row[0]}: {row[1]}")
def complete(task_id): c.execute('UPDATE tasks SET done=1 WHERE id=?',(task_id,)); conn.commit()

# Example usage
add("Finish assignment")
list_tasks()
complete(1)
list_tasks()
