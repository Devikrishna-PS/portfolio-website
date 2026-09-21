import sqlite3

conn = sqlite3.connect("portfolio.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()
cursor.execute("SELECT * FROM messages")

messages = cursor.fetchall()

print("\n----- Contact Messages -----\n")

if len(messages) == 0:
    print("No messages found.")
else:
    for message in messages:
        print(f"ID      : {message['id']}")
        print(f"Name    : {message['name']}")
        print(f"Email   : {message['email']}")
        print(f"Subject : {message['subject']}")
        print(f"Message : {message['message']}")
        print("-" * 35)

conn.close()