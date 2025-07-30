import sqlite3

conn = sqlite3.connect("notes.db")
conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)")
conn.execute("INSERT INTO notes (content) VALUES (?)", ("Hello note",))
conn.commit()
print("Note saved.")
