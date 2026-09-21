import sqlite3

# Connect to SQLite database (creates portfolio.db if it doesn't exist)
conn = sqlite3.connect("portfolio.db")

cursor = conn.cursor()

# ---------------- PROJECTS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    technologies TEXT NOT NULL,
    github TEXT,
    demo TEXT,
    image TEXT
)
""")

# ---------------- CERTIFICATES TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS certificates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    pdf TEXT
)
""")

# ---------------- CONTACT MESSAGES TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and tables created successfully!")