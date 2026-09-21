import sqlite3

conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM certificates")

conn.commit()
conn.close()

print("Old certificates deleted successfully!")