# 11. SQLite database
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE user(id, name)")
cur.execute("INSERT INTO user VALUES(1,'Alice')")
print(cur.execute("SELECT * FROM user").fetchall())
